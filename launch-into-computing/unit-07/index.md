---
layout: default
---

# Unit 7: Security Risk Assessment

## Project Overview

This unit presents a security risk assessment for a hypothetical cloud-based EV charging remote management system.

The system allows authorised support staff to monitor charging stations, review diagnostic information and perform selected remote maintenance activities. Because the platform connects staff accounts, endpoints, backend services and charging infrastructure, it may be exposed to several cybersecurity risks.

The scenario is hypothetical and does not describe the infrastructure, vulnerabilities or security controls of a real organisation.

## Assessment Objectives

The assessment aims to:

- Identify relevant cybersecurity threats and vulnerabilities.
- Explain how these weaknesses could affect data and service availability.
- Recommend proportionate security controls.
- Apply guidance from recognised NIST publications.

## Identified Risks

The report examines three main risk areas:

| Threat | Related vulnerability | Possible impact |
|---|---|---|
| Phishing and credential theft | Password-only authentication and excessive privileges | Unauthorised access to management functions |
| Malware on support endpoints | Delayed updates and unrestricted software installation | Stolen session data or disrupted maintenance |
| Data breach and unauthorised changes | Weak access controls and cloud misconfiguration | Exposed records or interrupted charging services |

## Recommended Security Measures

### Multi-Factor Authentication

Phishing-resistant multi-factor authentication should be required for privileged remote access. A stolen password would then be insufficient for account access.

### Endpoint Protection

Managed updates, endpoint detection, restricted software installation and tested incident-response procedures can reduce malware risk.

### Access Control and Encryption

Role-based access control and least privilege should limit what each account can do. Sensitive data should be encrypted during storage and transmission, while important administrative actions should be logged.

## Files

- [Security Risk Assessment in Markdown](security-risk-assessment.md)
- [Security Risk Assessment Word Document](Security-Risk-Assessment.docx)

## Learning Outcomes

This activity developed my understanding of:

- Threat and vulnerability identification.
- The relationship between risks and security controls.
- Multi-factor authentication and least privilege.
- Endpoint security and data encryption.
- Security risk reporting using recognised guidance.

## References

The report applies guidance from:

- NIST IR 8473: Cybersecurity Framework Profile for Electric Vehicle Extreme Fast Charging Infrastructure.
- NIST Cybersecurity Framework 2.0.
- NIST SP 800-63B: Authentication and Authenticator Management.