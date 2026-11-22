#!/usr/bin/env python3
"""Analyze a small Linux SSH authentication log for basic SOC triage signals.

This is a learning tool for synthetic or authorized log data. It does not block
IPs, change accounts, or perform any response action.
"""
from __future__ import annotations

import argparse
import re
from collections import Counter, defaultdict
from pathlib import Path

FAILED_RE = re.compile(
    r"sshd\[\d+\]: Failed password for (?:invalid user )?(?P<user>\S+) "
    r"from (?P<ip>(?:\d{1,3}\.){3}\d{1,3})"
)
ACCEPTED_RE = re.compile(
    r"sshd\[\d+\]: Accepted (?:password|publickey) for (?P<user>\S+) "
    r"from (?P<ip>(?:\d{1,3}\.){3}\d{1,3})"
)


def analyze_lines(lines: list[str], threshold: int = 5) -> tuple[Counter, dict, list]:
    """Return failed-login counts, successful sources, and normalized findings."""
    failures: Counter = Counter()
    failed_users: dict[str, set[str]] = defaultdict(set)
    successful: list[dict[str, str]] = []

    for line in lines:
        failed = FAILED_RE.search(line)
        if failed:
            ip = failed.group("ip")
            failures[ip] += 1
            failed_users[ip].add(failed.group("user"))
            continue

        accepted = ACCEPTED_RE.search(line)
        if accepted:
            successful.append(
                {"ip": accepted.group("ip"), "user": accepted.group("user")}
            )

    findings = []
    for ip, count in sorted(failures.items()):
        if count >= threshold:
            findings.append({
                "type": "repeated_failed_ssh_logins",
                "source_ip": ip,
                "failed_attempts": count,
                "users_targeted": sorted(failed_users[ip]),
                "threshold": threshold,
                "severity": "medium",
            })

    failed_sources = set(failures)
    for event in successful:
        if event["ip"] in failed_sources:
            findings.append({
                "type": "successful_ssh_login_after_failures",
                "source_ip": event["ip"],
                "account": event["user"],
                "failed_attempts_before_success": failures[event["ip"]],
                "severity": "high",
            })

    return failures, dict(failed_users), findings


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Triage repeated SSH authentication failures in an auth.log file."
    )
    parser.add_argument(
        "--log", type=Path, default=Path("sample_auth.log"),
        help="Path to an authorized Linux auth.log file (default: sample_auth.log)",
    )
    parser.add_argument(
        "--threshold", type=int, default=5,
        help="Failed attempts per source IP needed to raise an alert (default: 5)",
    )
    args = parser.parse_args()

    if args.threshold < 1:
        parser.error("--threshold must be at least 1")
    if not args.log.is_file():
        parser.error(f"log file not found: {args.log}")

    lines = args.log.read_text(encoding="utf-8", errors="replace").splitlines()
    failures, _, findings = analyze_lines(lines, args.threshold)

    print("SOC LAB | SSH AUTHENTICATION TRIAGE")
    print(f"Log file: {args.log}")
    print(f"Lines reviewed: {len(lines)}")
    print(f"Source IPs with failed logins: {len(failures)}")
    print(f"Findings: {len(findings)}")

    if not findings:
        print("No findings met the configured detection conditions.")
    for number, finding in enumerate(findings, start=1):
        print(f"\n[{number}] {finding['severity'].upper()} | {finding['type']}")
        print(f"    Source IP: {finding['source_ip']}")
        if finding["type"] == "repeated_failed_ssh_logins":
            print(f"    Failed attempts: {finding['failed_attempts']}")
            print(f"    Targeted accounts: {', '.join(finding['users_targeted'])}")
            print(f"    Detection threshold: {finding['threshold']}")
        else:
            print(f"    Account: {finding['account']}")
            print(
                "    Failed attempts from this source before success: "
                f"{finding['failed_attempts_before_success']}"
            )

    print("\nAnalyst note: validate the source, account owner, and event context")
    print("before deciding whether escalation or containment is appropriate.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
