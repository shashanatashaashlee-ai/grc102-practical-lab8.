import subprocess
from datetime import datetime, timezone
from pathlib import Path

target = "http://127.0.0.1:8080/"
evidence_dir = Path("../evidence/command-outputs")
evidence_dir.mkdir(parents=True, exist_ok=True)

result = subprocess.run(
    [
        "docker", "exec", "web_server", "curl", "-sS",
        "-o", "/tmp/struts_page.html",
        "-w", "%{http_code}",
        "--max-time", "10", target
    ],
    capture_output=True, text=True
)

status = result.stdout.strip()
report = [
    "ICDFA GRC102 Practical Lab 8",
    "Struts2 Application Availability Check",
    f"Timestamp UTC: {datetime.now(timezone.utc).isoformat()}",
    f"Target: {target} (checked inside web_server container)",
    f"HTTP status: {status or 'No response'}",
    f"Command exit code: {result.returncode}",
    f"Error: {result.stderr.strip() or 'None'}",
    "Assessment: Availability check only; vulnerability not confirmed."
]

output = "\n".join(report) + "\n"
print(output)
(evidence_dir / "application-check.txt").write_text(output)
