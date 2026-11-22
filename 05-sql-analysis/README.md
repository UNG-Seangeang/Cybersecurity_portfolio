# SQL Analysis for Security Monitoring — Learning Module

## Purpose
Practice using SQL to filter and investigate structured security-event data. Example use cases include failed logins, account activity, privileged access, and event timelines.

## Suggested workflow
1. Create a small local database from synthetic authentication events.
2. Define a clear schema and document each field.
3. Query failed attempts by account, source IP, and time range.
4. Compare failures with successful authentication events.
5. Explain what the query can and cannot establish.

## Example query
The following query assumes a table named `authentication_events` with columns `event_type`, `source_ip`, and `username`:

```sql
SELECT source_ip, username, COUNT(*) AS failed_attempts
FROM authentication_events
WHERE event_type = 'failed_login'
GROUP BY source_ip, username
HAVING COUNT(*) >= 5
ORDER BY failed_attempts DESC;
```

## Evidence to add
- Database schema and synthetic dataset.
- Queries with comments.
- Query output and analyst interpretation.
- Limitations, including time-window and false-positive considerations.

## Current evidence status
This is a learning guide. The example query is illustrative; it is not evidence that a real dataset has been analyzed.
