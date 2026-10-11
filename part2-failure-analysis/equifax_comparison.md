# Equifax Breach Comparison and Governance Lessons

## Purpose and scope
This comparison uses the Equifax 2017 breach as a governance case study and compares its widely reported control failures with observations from this isolated training lab. The lab checks are limited: they do not prove exploitation, unauthorised access to customer records, or data exfiltration.

## Equifax case study
The 2017 Equifax breach involved exploitation of a vulnerability in Apache Struts (CVE-2017-5638). Public investigations identified weaknesses in vulnerability and patch management, asset visibility, detection, and organisational oversight. The incident illustrates that publishing a patch or having a security policy is not sufficient unless organisations identify affected assets, apply fixes promptly, verify remediation, and escalate unresolved risks.

## Comparison with the lab
| Governance area | Lab observation | Lesson from Equifax |
|---|---|---|
| Vulnerability and patch management | The lab uses an older Struts image; this alone does not prove a specific vulnerability. | Maintain an asset inventory, confirm affected versions, prioritise patches, and verify fixes. |
| Privileged access | The configured MySQL root credential was accepted. | Remove weak/default credentials, limit administrator access, and protect secrets. |
| Network controls | Web-to-database TCP test timed out; cause remains undetermined. | Define expected communication paths and test segmentation rather than assuming it works. |
| Monitoring and evidence | HTTP response and database checks were logged to JSON. | Centralise logs, alert on suspicious events, retain evidence, and rehearse incident response. |
| Accountability | The lab findings need documented owners and remediation. | Assign control owners, deadlines, escalation routes, and independent verification. |

## Recommendations
1. Maintain an accurate inventory of internet-facing applications and dependencies.
2. Establish risk-based patching deadlines and record evidence of successful remediation.
3. Enforce strong unique credentials, least privilege, and controlled administrative access.
4. Test network segmentation and document approved application-to-database flows.
5. Monitor application and database logs, establish alerting, and exercise incident response.
6. Track risks and corrective actions to closure, with accountable owners and management reporting.

## Lessons learned
The lab demonstrates why governance must be measurable: a running application does not by itself demonstrate that it is secure. A database accepting a configured root credential is a concrete access-control concern, while a connectivity timeout requires investigation rather than assumptions. Equifax reinforces the importance of effective vulnerability management, asset visibility, detection, and accountability. Organisations should combine technical controls with clear ownership, deadlines, verification, and regular reporting.

## References
- U.S. House of Representatives, Committee on Oversight and Government Reform (2018), *The Equifax Data Breach*.
- National Institute of Standards and Technology (NIST), *Cybersecurity Framework 2.0* (2024).
- NIST, *SP 800-61 Rev. 2: Computer Security Incident Handling Guide* (2012).
- National Vulnerability Database, CVE-2017-5638, Apache Struts vulnerability record.
