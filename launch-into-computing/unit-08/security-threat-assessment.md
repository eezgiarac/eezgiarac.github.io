# Cybersecurity Risk Assessment of Payment Card Fraud at Public EV Charging Stations

## Scenario Overview

This report assesses a hypothetical enterprise operating public electric vehicle charging stations with integrated card payment terminals. Drivers can pay without creating an account, making charging convenient but exposing the terminals to physical and digital attacks. The assessment focuses on payment-card data theft, terminal malware and unauthorised remote access. NIST IR 8473 treats charging stations, cloud services and supporting networks as connected parts of the EV charging ecosystem (NIST, 2023).

## Threats and Vulnerabilities

The first threat is physical terminal tampering. An attacker could attach a false reader or replace part of a terminal to capture card data. Poor inspection procedures and the absence of tamper alerts would allow the modification to remain unnoticed.

A second threat is payment-terminal malware. Unpatched software, insecure maintenance ports or weak application controls could allow malicious code to collect transaction data. PCI DSS applies to organisations that store, process or transmit payment account data, including systems that may affect its security (PCI SSC, 2024).

The third threat is unauthorised remote access. Shared administrator accounts, weak passwords and excessive privileges could allow an attacker to change terminal settings or install malicious software. The most serious consequence may extend beyond one fraudulent payment. Stolen card and personal information could be reused in later transactions, phishing attempts or identity fraud.

## Mitigation Plan

Terminals should use tamper-evident seals, automated tamper detection and documented physical inspections. Alerts should be investigated against maintenance records rather than treated as proof of an attack. This distinction reduces false accusations while supporting early intervention.

Network segmentation and firewalls should separate payment terminals from charger-management and corporate networks. Remote administration should require phishing-resistant multi-factor authentication, named accounts and least privilege. Secure boot, digitally signed software, patch management and endpoint monitoring would reduce the likelihood of unauthorised code running on terminals.

Payment data should be minimised through tokenisation, so reusable card numbers are not retained unnecessarily. TLS 1.3 should protect data in transit, while AES-256 may protect stored sensitive information. Encryption keys must be managed separately from encrypted data. Encryption cannot prevent physical tampering or misuse through an authorised account, so it must operate alongside authentication, monitoring and access control.

## Legal and Ethical Considerations

GDPR requires appropriate technical and organisational security measures. If personal data is compromised, the organisation must assess the risk and follow applicable breach-notification duties (European Union, 2016). PCI DSS provides more specific payment-security requirements, while ISO/IEC 27001 supports continuing risk assessment and improvement of an information security management system (ISO, 2022).

These sources serve different purposes. NIST is specific to connected EV infrastructure but provides less payment-card detail. PCI DSS is therefore more useful for terminal and card-data controls, while ISO/IEC 27001 provides the broader management structure. Ethically, the operator should minimise collected data, communicate incidents honestly and avoid placing responsibility solely on customers.

## Conclusion

The proposed controls combine physical security, access management, network protection and encryption. Regular testing and incident exercises are required because compliance alone does not confirm that the controls remain effective.

## References

European Union (2016) *Regulation (EU) 2016/679 General Data Protection Regulation*. Available at: https://eur-lex.europa.eu/eli/reg/2016/679/oj (Accessed: 25 September 2026).

ISO (2022) *ISO/IEC 27001 Information Security Management Systems*. Available at: https://www.iso.org/standard/27001 (Accessed: 25 September 2026).

NIST (2023) *Cybersecurity Framework Profile for Electric Vehicle Extreme Fast Charging Infrastructure*, NIST IR 8473. Available at: https://doi.org/10.6028/NIST.IR.8473 (Accessed: 25 September 2026).

PCI Security Standards Council (2024) *Payment Card Industry Data Security Standard*. Available at: https://www.pcisecuritystandards.org/standards/pci-dss/ (Accessed: 25 September 2026).