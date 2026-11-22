# SOC Alert Triage Lab — SSH Authentication Logs

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![Focus](https://img.shields.io/badge/Focus-SOC%20Alert%20Triage-0A66C2)
![Data](https://img.shields.io/badge/Data-Synthetic%20Lab%20Logs-64748b)

## Project overview

This beginner-friendly SOC lab analyzes a **synthetic Linux SSH authentication log** and raises two simple detection findings:

1. Repeated failed SSH authentication attempts from one source IP.
2. A successful SSH login from a source IP that also generated failed attempts in the supplied log.

The project demonstrates a basic analyst workflow: review telemetry, apply a transparent detection threshold, inspect the alert context, and document the next validation steps. It is a local Python exercise, **not a production SIEM or a claim of real incident response experience**.

## Repository contents

- `analyze_auth.py` — command-line log parser and detection logic.
- `sample_auth.log` — synthetic sample events using documentation-only IP ranges.
- `tests/test_analyze_auth.py` — unit tests for the detection conditions.

## Run the lab

Requires Python 3.10+; no third-party packages are needed.

```bash
cd 11-soc-alert-triage
python analyze_auth.py
```

Use a different authorized log file or adjust the threshold:

```bash
python analyze_auth.py --log /var/log/auth.log --threshold 5
```

Only analyze logs you are authorized to access. The script is read-only: it does not block IP addresses, disable accounts, or modify the host.

## Expected sample findings

The bundled synthetic log contains six failed attempts from `198.51.100.23`, followed by a successful SSH login from the same source. Running the script with the default threshold of five should produce:

- A **medium** repeated-failure finding for that source.
- A **high-priority investigation finding** for the successful login after failures.

These are lab classifications for practice, not a confirmed compromise. The successful event may have a legitimate explanation and must be validated.

## Detection logic

| Detection | Logic | Analyst interpretation |
|---|---|---|
| Repeated failed SSH logins | Failed attempts from one source IP meet or exceed the configured threshold | Possible password guessing; inspect time range, targeted accounts, and source reputation |
| Successful login after failures | A source IP has at least one failed event and a later accepted event in the supplied log | Validate the account owner, authentication method, host, and whether the activity was expected |

The repeated-failure threshold defaults to five. This starter version counts failures across the entire input file; it does **not** implement a rolling time window, deduplication, geolocation, or allow-list logic.

## Analyst triage checklist

1. **Validate the event:** confirm the host, timestamp, source IP, username, and authentication result.
2. **Scope the activity:** check whether other accounts or hosts show activity from the same source.
3. **Correlate:** compare SSH events with endpoint, VPN, firewall, and identity-provider logs where available.
4. **Assess impact:** determine whether the accepted login was expected and whether the account performed unusual actions.
5. **Escalate appropriately:** follow the organization's incident-response process; do not automatically block an address based only on this script.
6. **Document:** record evidence, time range, decisions, and unresolved questions.

## MITRE ATT&CK context

- [T1110 — Brute Force](https://attack.mitre.org/techniques/T1110/)
- [T1110.001 — Password Guessing](https://attack.mitre.org/techniques/T1110/001/)
- [T1078 — Valid Accounts](https://attack.mitre.org/techniques/T1078/) may be relevant if an accepted login is confirmed unauthorized.

Technique mapping is contextual. A failed-login pattern alone does not prove an adversary or a successful compromise.

## Test the detection logic

```bash
python -m unittest discover -s tests -v
```

## Limitations and next improvements

- Parse additional SSH log formats and timezone-aware timestamps.
- Group events into configurable time windows instead of whole-file totals.
- Add structured JSON/CSV output for case management.
- Add Wazuh ingestion and rule testing after the local detections are understood.
- Add analyst-written incident notes with supporting evidence.

## Evidence and reproducibility

All included events are synthetic. The addresses `198.51.100.0/24` and `203.0.113.0/24` are reserved for documentation examples. No real user or production system is represented.
