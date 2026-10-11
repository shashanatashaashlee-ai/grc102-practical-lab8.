
#!/usr/bin/env python3
import argparse
import datetime
import json
import os


class GovernanceTracker:
    def __init__(self, data_file="governance_data.json"):
        self.data_file = data_file
        self.load_data()

    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, "r", encoding="utf-8") as file:
                self.data = json.load(file)
        else:
            self.data = {
                "policies": [],
                "controls": [],
                "risks": [],
                "incidents": [],
                "metrics": [],
                "audits": []
            }

    def save_data(self):
        with open(self.data_file, "w", encoding="utf-8") as file:
            json.dump(self.data, file, indent=2)

    def _add(self, category, prefix, fields):
        record = {
            "id": f"{prefix}-{len(self.data[category]) + 1:03d}",
            **fields
        }
        self.data[category].append(record)
        self.save_data()
        return record["id"]

    def add_policy(self, name, description, owner, approval_date, review_date):
        return self._add("policies", "POL", {
            "name": name, "description": description, "owner": owner,
            "approval_date": approval_date, "review_date": review_date,
            "status": "Active"
        })

    def add_control(self, name, description, policy_id, owner, implementation_date):
        return self._add("controls", "CTL", {
            "name": name, "description": description, "policy_id": policy_id,
            "owner": owner, "implementation_date": implementation_date,
            "status": "Implemented"
        })

    def calculate_risk_level(self, likelihood, impact):
        matrix = {
            "High": {"High": "Critical", "Medium": "High", "Low": "Medium"},
            "Medium": {"High": "High", "Medium": "Medium", "Low": "Low"},
            "Low": {"High": "Medium", "Medium": "Low", "Low": "Very Low"}
        }
        return matrix.get(likelihood, {}).get(impact, "Unknown")

    def add_risk(self, name, description, likelihood, impact, owner, mitigation_plan):
        return self._add("risks", "RISK", {
            "name": name, "description": description,
            "likelihood": likelihood, "impact": impact,
            "risk_level": self.calculate_risk_level(likelihood, impact),
            "owner": owner, "mitigation_plan": mitigation_plan, "status": "Open"
        })

    def add_incident(self, name, description, date, severity,
                     affected_systems, root_cause, resolution):
        return self._add("incidents", "INC", {
            "name": name, "description": description, "date": date,
            "severity": severity, "affected_systems": affected_systems,
            "root_cause": root_cause, "resolution": resolution, "status": "Closed"
        })

    def add_metric(self, name, description, target, actual, period, trend):
        return self._add("metrics", "MET", {
            "name": name, "description": description, "target": target,
            "actual": actual, "period": period, "trend": trend, "status": "Active"
        })

    def add_audit(self, name, description, date, auditor, findings, recommendations):
        return self._add("audits", "AUD", {
            "name": name, "description": description, "date": date,
            "auditor": auditor, "findings": findings,
            "recommendations": recommendations, "status": "Completed"
        })

    def list_policies(self):
        return self.data["policies"]

    def list_controls(self):
        return self.data["controls"]

    def list_risks(self):
        return self.data["risks"]

    def list_incidents(self):
        return self.data["incidents"]

    def list_metrics(self):
        return self.data["metrics"]

    def list_audits(self):
        return self.data["audits"]

    def generate_dashboard(self):
        risks = self.data["risks"]
        incidents = self.data["incidents"]
        metrics = self.data["metrics"]

        return {
            "generated_date": datetime.datetime.now().isoformat(),
            "summary": {
                key: len(self.data[key])
                for key in ["policies", "controls", "risks", "incidents", "metrics", "audits"]
            },
            "risk_summary": {
                level.lower().replace(" ", "_"): sum(
                    1 for risk in risks if risk["risk_level"] == level
                )
                for level in ["Critical", "High", "Medium", "Low", "Very Low"]
            },
            "incident_summary": {
                level.lower(): sum(1 for incident in incidents if incident["severity"] == level)
                for level in ["Critical", "High", "Medium", "Low"]
            },
            "metrics_summary": [
                {
                    "name": metric["name"],
                    "target": metric["target"],
                    "actual": metric["actual"],
                    "status": "Green" if metric["actual"] >= metric["target"] else "Red"
                }
                for metric in metrics
            ]
        }


def main():
    parser = argparse.ArgumentParser(description="Security Governance Tracker")
    actions = {
        "add_policy": "add-policy",
        "add_control": "add-control",
        "add_risk": "add-risk",
        "add_incident": "add-incident",
        "add_metric": "add-metric",
        "add_audit": "add-audit",
        "list_policies": "list-policies",
        "list_controls": "list-controls",
        "list_risks": "list-risks",
        "list_incidents": "list-incidents",
        "list_metrics": "list-metrics",
        "list_audits": "list-audits",
        "dashboard": "dashboard"
    }

    for argument, option in actions.items():
        parser.add_argument(
            f"--{option}", action="store_true", help=option.replace("-", " ").title()
        )

    args = parser.parse_args()
    tracker = GovernanceTracker()

    if args.add_policy:
        values = [input(prompt) for prompt in [
            "Policy Name: ", "Description: ", "Owner: ",
            "Approval Date (YYYY-MM-DD): ", "Review Date (YYYY-MM-DD): "
        ]]
        print("Policy added with ID:", tracker.add_policy(*values))

    elif args.add_control:
        values = [input(prompt) for prompt in [
            "Control Name: ", "Description: ", "Policy ID: ",
            "Owner: ", "Implementation Date (YYYY-MM-DD): "
        ]]
        print("Control added with ID:", tracker.add_control(*values))

    elif args.add_risk:
        values = [input(prompt) for prompt in [
            "Risk Name: ", "Description: ", "Likelihood (High/Medium/Low): ",
            "Impact (High/Medium/Low): ", "Owner: ", "Mitigation Plan: "
        ]]
        print("Risk added with ID:", tracker.add_risk(*values))

    elif args.add_incident:
        values = [input(prompt) for prompt in [
            "Incident Name: ", "Description: ", "Date (YYYY-MM-DD): ",
            "Severity (Critical/High/Medium/Low): ", "Affected Systems: ",
            "Root Cause: ", "Resolution: "
        ]]
        print("Incident added with ID:", tracker.add_incident(*values))

    elif args.add_metric:
        name = input("Metric Name: ")
        description = input("Description: ")
        target = float(input("Target Value: "))
        actual = float(input("Actual Value: "))
        period = input("Period: ")
        trend = input("Trend (Improving/Stable/Declining): ")
        print("Metric added with ID:", tracker.add_metric(
            name, description, target, actual, period, trend
        ))

    elif args.add_audit:
        values = [input(prompt) for prompt in [
            "Audit Name: ", "Description: ", "Date (YYYY-MM-DD): ",
            "Auditor: ", "Findings: ", "Recommendations: "
        ]]
        print("Audit added with ID:", tracker.add_audit(*values))

    elif args.dashboard:
        print(json.dumps(tracker.generate_dashboard(), indent=2))
    else:
        list_options = {
            "list_policies": tracker.list_policies,
            "list_controls": tracker.list_controls,
            "list_risks": tracker.list_risks,
            "list_incidents": tracker.list_incidents,
            "list_metrics": tracker.list_metrics,
            "list_audits": tracker.list_audits
        }
        for option, function in list_options.items():
            if getattr(args, option):
                print(json.dumps(function(), indent=2))
                break
        else:
            parser.print_help()


if __name__ == "__main__":
    main()