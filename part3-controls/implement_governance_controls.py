#!/usr/bin/env python3
import json
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "evidence" / "command-outputs"
OUT.mkdir(parents=True, exist_ok=True)

controls = [
    {
        "id": "CTRL-01",
        "name": "Privileged credential management",
        "risk": "Weak or default database credentials",
        "implementation": "Document credential risk; require strong unique secrets, restrict root access, and avoid storing passwords in scripts.",
        "verification": "Configuration review required; this script does not change the live database password.",
        "status": "RECOMMENDATION_RECORDED"
    },
    {
        "id": "CTRL-02",
        "name": "Network segmentation verification",
        "risk": "Unapproved application-to-database communication",
        "implementation": "Keep services on the designated internal lab network and document expected communication paths.",
        "verification": "Network is configured as internal; web-to-database connectivity test timed out and requires investigation.",
        "status": "PARTIALLY_VERIFIED"
    },
    {
        "id": "CTRL-03",
        "name": "Vulnerability and patch management",
        "risk": "Outdated application components",
        "implementation": "Inventory application versions, assess vendor advisories, apply supported security updates, and verify remediation.",
        "verification": "Image inventory and patch validation should be completed; this script does not patch the application.",
        "status": "REMEDIATION_REQUIRED"
    },
    {
        "id": "CTRL-04",
        "name": "Logging and incident evidence",
        "risk": "Insufficient evidence for incident investigation",
        "implementation": "Retain timestamped test results and review application, database, and security logs.",
        "verification": "Simulation JSON log exists and records the observed results.",
        "status": "EVIDENCE_RECORDED"
    },
    {
        "id": "CTRL-05",
        "name": "Governance accountability",
        "risk": "Unowned or overdue corrective actions",
        "implementation": "Assign an owner, priority, due date, and evidence-based closure test to each finding.",
        "verification": "Actions are documented below; operational ownership must be assigned by the organisation.",
        "status": "RECOMMENDATION_RECORDED"
    }
]

report = {
    "title": "GRC102 Part 3 - Governance Controls Implementation",
    "generated_utc": datetime.now(timezone.utc).isoformat(),
    "scope": "Control register and verification evidence for the isolated training lab.",
    "important_note": "This script records control implementations and verification requirements. It does not change live credentials, patch software, or claim unverified controls are effective.",
    "controls": controls
}

json_path = OUT / "controls-implementation-report.json"
json_path.write_text(json.dumps(report, indent=2), encoding="utf-8")

verification = {
    "title": "Post-Control Verification",
    "generated_utc": datetime.now(timezone.utc).isoformat(),
    "checks": [
        {
            "control_id": c["id"],
            "control": c["name"],
            "status": c["status"],
            "verification_evidence": c["verification"]
        } for c in controls
    ],
    "conclusion": "The control register was generated successfully. Controls requiring operational changes remain open until those changes are implemented and independently verified."
}
verify_path = OUT / "post-control-verification.json"
verify_path.write_text(json.dumps(verification, indent=2), encoding="utf-8")

md_path = ROOT / "part3-controls" / "controls_report.md"
md_path.write_text("""# Part 3: Governance Controls Report

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
""", encoding="utf-8")

print("Controls implementation report:", json_path)
print("Post-control verification:", verify_path)
print("Controls narrative:", md_path)
print("Controls recorded:", len(controls))
print("Review the status of each control; recommendations are not proof of remediation.")
