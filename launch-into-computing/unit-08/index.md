---
layout: default
---

# Unit 8: Cybersecurity Threat Assessment and Mitigation Plan

## Project Overview

This project presents a cybersecurity threat assessment for a hypothetical enterprise operating public EV charging stations with integrated payment-card terminals.

The assessment examines how physical tampering, malicious software and unauthorised remote access could compromise payment information. It also proposes security measures and considers GDPR, ISO/IEC 27001 and PCI DSS requirements.

The scenario is hypothetical and does not describe the systems, vulnerabilities or security controls of a real organisation.

## Scenario

Drivers use payment terminals installed on public EV charging stations. These terminals communicate with payment services and supporting backend systems.

An attacker may attempt to steal payment-card information by:

- Physically modifying the payment terminal.
- Installing malicious software.
- Compromising a remote administration account.
- Exploiting weak network separation or outdated software.

The main concern is that stolen card and personal information could be reused in later fraudulent transactions or social-engineering attacks.

## Threat Assessment

| Threat | Vulnerability | Potential impact |
|---|---|---|
| Terminal tampering | Insufficient physical inspections and missing tamper alerts | Card information may be captured |
| Payment-terminal malware | Unpatched software and insecure maintenance access | Transaction data may be stolen |
| Unauthorised remote access | Weak authentication and excessive privileges | Settings or software may be modified |
| Data breach | Excessive data storage and weak protection | Personal and payment information may be exposed |

## Mitigation Plan

### Physical Security

Terminals should have tamper-evident seals and automated tamper detection. Regular inspections should be documented and compared with authorised maintenance records.

### Authentication and Access Control

Remote administration should require phishing-resistant multi-factor authentication. Named administrator accounts, role-based access control and least privilege should restrict access.

### Network and Endpoint Security

Firewalls and network segmentation should separate payment terminals from charger-management and corporate networks. Secure boot, digitally signed software, security updates and endpoint monitoring should protect terminal software.

### Data Protection

TLS 1.3 should protect data in transit. AES-256 may protect sensitive stored data. Payment tokenisation should reduce the need to retain reusable card numbers.

Encryption should support authentication and access control rather than being treated as a complete solution.

## Compliance and Ethical Considerations

The assessment considers:

- **GDPR:** Protection, minimisation and appropriate handling of personal data.
- **ISO/IEC 27001:** Risk-based information security management and continual improvement.
- **PCI DSS:** Technical and operational requirements for protecting payment-card data.

The operator should communicate data breaches honestly, collect only necessary information and avoid placing responsibility solely on customers.

## Project File

The complete report is available here:

[Read the Security Threat Assessment](security-threat-assessment.md)

## Skills Applied

- Threat and vulnerability identification
- Risk-based security planning
- Network segmentation and access control
- Encryption and payment tokenisation
- GDPR, ISO/IEC 27001 and PCI DSS evaluation
- Ethical and legal risk analysis

## References

- European Union (2016) *General Data Protection Regulation*.
- ISO (2022) *ISO/IEC 27001 Information Security Management Systems*.
- NIST (2023) *Cybersecurity Framework Profile for Electric Vehicle Extreme Fast Charging Infrastructure*.
- PCI Security Standards Council (2024) *Payment Card Industry Data Security Standard*.