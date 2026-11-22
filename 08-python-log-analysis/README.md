# Python Log Analysis — Learning Module

## Purpose
Use Python to parse security logs, normalize selected fields, summarize activity, and identify events that deserve analyst review.

## Suggested project workflow
1. Select a synthetic or authorized log source.
2. Document its format and fields.
3. Parse records defensively and handle malformed lines.
4. Create simple, explainable detection conditions.
5. Test normal and suspicious examples.
6. Report findings with evidence, limitations, and next steps.

## Minimum deliverables
- Python script with command-line usage.
- Small synthetic sample log.
- Unit tests for expected and edge-case behavior.
- Example output.
- Short explanation of false positives and detection limitations.

## Current evidence status
This module is a project guide. A working SSH authentication log triage implementation is available in [11-soc-alert-triage](../11-soc-alert-triage/). This folder will be expanded with a separate general-purpose log parsing exercise.
