#!/usr/bin/env python3
import json
from pathlib import Path
from datetime import datetime, timezone

root = Path(__file__).resolve().parent.parent
log_path = root / "evidence/command-outputs/attack-simulation-log.json"
out_path = root / "evidence/command-outputs/governance-failure-report.json"

if not log_path.exists():
    raise SystemExit("Simulation log not found: " + str(log_path))

log = json.loads(log_path.read_text(encoding="utf-8"))
findings = []

for result in log.get("results", []):
    name = result.get("check", "Unnamed check")
    output = result.get("output", "")
    error = result.get("error", "")
    code = result.get("return_code")

    if name == "Web application response":
        findings.append({
            "area": "Application availability",
            "observation": output or error,
            "status": "PASS" if code == 0 and "200" in output else "REVIEW",
            "governance_implication": "Availability checks should be monitored and recorded."
        })
    elif name == "Database accepts configured root password":
        findings.append({
            "area": "Privileged access and credentials",
            "observation": output or error,
            "status": "RISK" if code == 0 else "REVIEW",
            "governance_implication": "The lab accepts its configured root credential. Replace default or weak credentials, restrict privileged access, and manage secrets securely."
        })
    elif name == "Database connectivity from web container":
        findings.append({
            "area": "Network connectivity",
            "observation": output or error,
            "status": "REVIEW",
            "governance_implication": "The TCP test timed out. The cause is undetermined; validate firewall rules, service reachability, and segmentation before drawing conclusions."
        })

report = {
    "report_title": "GRC102 Part 2 Governance Failure Analysis",
    "generated_utc": datetime.now(timezone.utc).isoformat(),
    "evidence_source": str(log_path.relative_to(root)),
    "scope": "Isolated lab only; no exploitation or data extraction performed.",
    "findings": findings,
    "overall_conclusion": (
        "The lab demonstrates a successful HTTP availability check and acceptance "
        "of the configured MySQL root credential. Database connectivity from the "
        "web container timed out and requires further investigation. These checks "
        "do not establish that an exploit or data breach occurred."
    ),
    "recommended_actions": [
        "Replace weak or default privileged credentials and use a secret-management process.",
        "Apply least privilege and restrict administrative database access.",
        "Investigate the database connectivity timeout and verify intended segmentation.",
        "Patch and inventory software, monitor logs, and test controls regularly.",
        "Assign control owners, remediation deadlines, and evidence-based closure checks."
    ]
}
out_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
print("Governance failure report saved:", out_path)
print(json.dumps(report, indent=2))
