# Part 3: Governance Controls Report

## Scope
This report documents recommended controls and the evidence available from the isolated training lab. Generating this report does not itself change the running services.

## Controls
| ID | Control | Risk addressed | Status |
|---|---|---|---|
| CTRL-01 | Privileged credential management | Weak/default database credentials | Recommendation recorded |
| CTRL-02 | Network segmentation verification | Unapproved service communication | Partially verified |
| CTRL-03 | Vulnerability and patch management | Outdated application components | Remediation required |
| CTRL-04 | Logging and incident evidence | Insufficient investigation evidence | Evidence recorded |
| CTRL-05 | Governance accountability | Unowned corrective actions | Recommendation recorded |

## Post-control verification
The lab network is configured as internal. The application returned HTTP 200 and the configured MySQL root credential was accepted. The web-to-database connectivity check timed out, so its cause remains undetermined. The results do not establish that every control is effective.

## Required follow-up
1. Replace weak/default credentials through an approved, tested change process.
2. Investigate the connectivity timeout and test intended network paths.
3. Inventory the application version, assess applicable advisories, and patch supported components.
4. Review logs and retain dated evidence of tests and remediation.
5. Assign accountable owners and due dates; close actions only after verification.
