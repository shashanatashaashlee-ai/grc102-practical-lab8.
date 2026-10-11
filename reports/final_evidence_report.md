# GRC102 Practical Lab Assessment — Evidence Report

**Date:** 11 October 2026  
**Environment:** GitHub Codespaces and isolated Docker lab

## Part 1 — Environment and scanning
The lab includes a web application, MySQL database, monitoring container, SQL initialisation script, and vulnerability-scanning scripts. Recorded evidence includes `application-check.txt` and `vulnerability-report.json`.

The web application returned HTTP 200 in the recorded check. The scanner reported configuration concerns, including acceptance of the configured MySQL root credential. Scanner results are indicators for review and do not independently prove exploitation.

## Part 2 — Failure analysis
`attack-simulation-log.json` records HTTP 200, MySQL version 5.7.44, and a web-to-database connectivity timeout. The timeout's cause was not established. The governance failure report documents the observations and recommendations. The Equifax comparison discusses patch management, detection, accountability, and verification.

## Part 3 — Controls
The controls register documents credential management, network segmentation verification, vulnerability and patch management, evidence retention, and governance accountability. The post-control report distinguishes recorded recommendations from controls that have been operationally implemented and verified.

## Part 4 — Governance metrics
The tracker contains sample policies, controls, risks, incidents, metrics, and audit records. The dashboard showed patch compliance of 85% against a 95% target, remediation time of 12 days against a 7-day target, and one security incident against a target of zero. Metric status logic should be checked so that adverse values are not labelled Green.

## Evidence index
- `evidence/command-outputs/application-check.txt`
- `evidence/command-outputs/vulnerability-report.json`
- `evidence/command-outputs/attack-simulation-log.json`
- `evidence/command-outputs/governance-failure-report.json`
- `evidence/command-outputs/controls-implementation-report.json`
- `evidence/command-outputs/post-control-verification.json`
- `evidence/command-outputs/governance-dashboard.json`

## Limitations
The lab is isolated and uses synthetic data. The work does not establish successful exploitation or data exfiltration. Eighteen screenshot files are included in `evidence/screenshots/`. They provide supporting visual evidence for the environment, database, scanning, attack simulation, controls, and governance dashboard. File names are preserved as captured.
