# Governance Tracker User Guide

## Purpose
The tracker stores governance policies, controls, risks, incidents, audits, and performance metrics for the practical lab.

## Run the dashboard
From the repository root:
```bash
python3 part4-governance-metrics/governance_tracker.py --dashboard
```

Run from the tracker directory if relative file paths require it:
```bash
cd part4-governance-metrics
python3 governance_tracker.py --dashboard
```

## Data and evidence
- `part4-governance-metrics/governance_data.json` contains the tracker data.
- `evidence/command-outputs/governance-dashboard.json` contains saved dashboard evidence.
- Keep backups before editing data.
- Do not run the initializer repeatedly; it may add duplicate sample records.
- Verify that metric status logic reflects whether higher or lower values are desirable.

## Operational cautions
This is a training tracker, not a production governance platform. Validate inputs, protect sensitive information, and independently verify controls before reporting them as effective.
