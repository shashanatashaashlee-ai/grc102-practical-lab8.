# Executive Board Report: GRC102 Practical Lab

**Date:** 11 October 2026  
**Scope:** Isolated training environment

## Executive summary
The lab produced evidence of application availability, acceptance of the configured MySQL root credential, and a database connectivity timeout requiring investigation. These results demonstrate why technical controls must be supported by governance, monitoring, and accountable remediation.

## Key findings
- Application returned HTTP 200 during the recorded test.
- MySQL accepted the configured root credential. This is a privileged-access risk.
- The web-to-database connectivity test timed out. The cause is not confirmed.
- The network is configured as an internal Docker network.
- The lab uses an older Struts image; the specific vulnerability status must be independently verified.

## Recommended board actions
1. Require strong credential management and least-privilege access.
2. Require a documented patch-management process and evidence of remediation.
3. Validate network segmentation and approved service communication.
4. Assign owners and deadlines to all open findings.
5. Require periodic metrics reporting and independent control verification.

## Limitations
This was a limited training exercise. It did not establish successful exploitation or data exfiltration. The results are not a full production security assessment.
