import unittest

from analyze_auth import analyze_lines


class AnalyzeAuthTests(unittest.TestCase):
    def test_repeated_failures_raise_threshold_finding(self):
        lines = [
            "Nov 22 09:00:00 host sshd[1]: Failed password for invalid user admin from 198.51.100.23 port 50000 ssh2",
            "Nov 22 09:00:01 host sshd[2]: Failed password for root from 198.51.100.23 port 50001 ssh2",
        ]
        failures, users, findings = analyze_lines(lines, threshold=2)
        self.assertEqual(failures["198.51.100.23"], 2)
        self.assertEqual(users["198.51.100.23"], {"admin", "root"})
        self.assertEqual(findings[0]["type"], "repeated_failed_ssh_logins")

    def test_success_after_failure_creates_separate_finding(self):
        lines = [
            "Nov 22 09:00:00 host sshd[1]: Failed password for eang from 198.51.100.23 port 50000 ssh2",
            "Nov 22 09:01:00 host sshd[2]: Accepted password for eang from 198.51.100.23 port 50001 ssh2",
        ]
        _, _, findings = analyze_lines(lines, threshold=5)
        self.assertEqual(len(findings), 1)
        self.assertEqual(findings[0]["type"], "successful_ssh_login_after_failures")
        self.assertEqual(findings[0]["severity"], "high")

    def test_below_threshold_without_success_has_no_finding(self):
        lines = [
            "Nov 22 09:00:00 host sshd[1]: Failed password for eang from 198.51.100.23 port 50000 ssh2",
        ]
        _, _, findings = analyze_lines(lines, threshold=5)
        self.assertEqual(findings, [])


if __name__ == "__main__":
    unittest.main()
