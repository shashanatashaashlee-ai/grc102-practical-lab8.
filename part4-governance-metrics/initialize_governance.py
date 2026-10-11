
#!/usr/bin/env python3

from governance_tracker import GovernanceTracker


def initialize_governance_data():
    tracker = GovernanceTracker()

    # Policies
    patch_policy_id = tracker.add_policy(
        "Patch Management Policy",
        "Policy governing the timely application of security patches",
        "CISO",
        "2023-01-15",
        "2024-01-15"
    )

    vuln_policy_id = tracker.add_policy(
        "Vulnerability Management Policy",
        "Policy governing identification and remediation of vulnerabilities",
        "Security Director",
        "2023-02-10",
        "2024-02-10"
    )

    incident_policy_id = tracker.add_policy(
        "Incident Response Policy",
        "Policy governing responses to security incidents",
        "CISO",
        "2023-03-05",
        "2024-03-05"
    )

    # Controls
    tracker.add_control(
        "Patch Management Process",
        "Process for identifying, testing and applying security patches",
        patch_policy_id,
        "IT Manager",
        "2023-01-20"
    )

    tracker.add_control(
        "Vulnerability Scanning",
        "Regular scanning for security vulnerabilities",
        vuln_policy_id,
        "Security Engineer",
        "2023-02-15"
    )

    tracker.add_control(
        "Incident Response Team",
        "Team responsible for responding to security incidents",
        incident_policy_id,
        "Security Director",
        "2023-03-10"
    )

    # Risks
    tracker.add_risk(
        "Unpatched Vulnerabilities",
        "Risk of exploitation due to unpatched vulnerabilities",
        "High",
        "High",
        "Security Engineer",
        "Implement an automated patch management system"
    )

    tracker.add_risk(
        "Insufficient Network Segmentation",
        "Risk of lateral movement due to insufficient segmentation",
        "Medium",
        "High",
        "Network Engineer",
        "Implement network segmentation using least privilege"
    )

    tracker.add_risk(
        "Weak Authentication",
        "Risk of unauthorised access due to weak authentication",
        "Medium",
        "Medium",
        "Identity Manager",
        "Implement multi-factor authentication"
    )

    # Incident
    tracker.add_incident(
        "Web Server Compromise",
        "Simulated compromise involving an unpatched Struts vulnerability",
        "2023-04-15",
        "High",
        "Web Server",
        "Unpatched Struts vulnerability (CVE-2017-5638)",
        "Simulated remediation and restoration"
    )

    # Metrics
    tracker.add_metric(
        "Patch Compliance",
        "Percentage of systems with all critical patches applied",
        95.0,
        85.0,
        "May 2023",
        "Improving"
    )

    tracker.add_metric(
        "Vulnerability Remediation Time",
        "Average time to remediate critical vulnerabilities in days",
        7.0,
        12.0,
        "May 2023",
        "Declining"
    )

    tracker.add_metric(
        "Security Incidents",
        "Number of security incidents during the reporting period",
        0.0,
        1.0,
        "May 2023",
        "Stable"
    )

    # Audit
    tracker.add_audit(
        "Annual Security Audit",
        "Comprehensive review of security controls",
        "2023-05-01",
        "External Auditor",
        "Findings related to patch management and network segmentation",
        "Improve patch management and implement network segmentation"
    )

    print("Governance tracker initialized with sample data.")
    print("Policies: 3 | Controls: 3 | Risks: 3")
    print("Incidents: 1 | Metrics: 3 | Audits: 1")


if __name__ == "__main__":
    initialize_governance_data()
