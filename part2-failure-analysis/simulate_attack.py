#!/usr/bin/env python3
import datetime
import json
import subprocess
from pathlib import Path

def run_check(name, command):
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=12
        )
        return {
            "check": name,
            "timestamp_utc": datetime.datetime.now(
                datetime.timezone.utc
            ).isoformat(),
            "return_code": result.returncode,
            "output": result.stdout.strip(),
            "error": result.stderr.strip()
        }
    except Exception as exc:
        return {
            "check": name,
            "timestamp_utc": datetime.datetime.now(
                datetime.timezone.utc
            ).isoformat(),
            "error": str(exc)
        }

def main():
    print("ICDFA GRC102 Part 2 - Authorised Lab Simulation")
    print("Scope: isolated lab containers only")
    print("No real data will be accessed or exfiltrated.")

    results = [
        run_check(
            "Web application response",
            ["docker", "exec", "web_server", "curl", "-sS",
             "-o", "/dev/null", "-w", "HTTP %{http_code}",
             "--max-time", "8", "http://127.0.0.1:8080/"]
        ),
        run_check(
            "Database accepts configured root password",
            ["docker", "exec", "database_server", "mysql",
             "-uroot", "-ppassword", "-N", "-e", "SELECT VERSION()"]
        ),
        run_check(
            "Database connectivity from web container",
            ["docker", "exec", "web_server", "curl", "-sS",
             "--connect-timeout", "5", "--max-time", "7",
             "http://database_server:3306"]
        )
    ]

    output_dir = Path("../evidence/command-outputs")
    output_dir.mkdir(parents=True, exist_ok=True)
    log_file = output_dir / "attack-simulation-log.json"

    report = {
        "timestamp_utc": datetime.datetime.now(
            datetime.timezone.utc
        ).isoformat(),
        "scope": "Authorised isolated ICDFA lab containers",
        "note": (
            "Configuration and connectivity checks only. "
            "This script does not exploit the application or extract data."
        ),
        "results": results
    }

    log_file.write_text(json.dumps(report, indent=2), encoding="utf-8")

    for item in results:
        print(f"\n{item['check']}")
        print("Output:", item.get("output", ""))
        if item.get("error"):
            print("Error:", item["error"])
        print("Return code:", item.get("return_code", "not available"))

    print(f"\nSimulation log saved to: {log_file}")

if __name__ == "__main__":
    main()
