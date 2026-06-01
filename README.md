# CC-Prep Forge — ISC2 Certified in Cybersecurity Exam Prep

> Flashcard + quiz CLI tool for the ISC2 Certified in Cybersecurity (CC) exam.  
> Built by: **Muhammad Aminu Musa**

## What it does

- **Flashcard mode** — flip through CC exam questions, self-rate your answers
- **Quiz mode** — multiple-choice rounds with immediate feedback
- **Progress tracking** — saves your study history
- **Domain-weighted questions** — matches the official CC exam outline
- **78 questions** covering all CC exam domains and beyond

## Exam Domains

| Domain | Weight |
|---|---|
| Security Principles | 15% |
| Access Controls | 17% |
| Security Operations | 20% |
| Governance, Risk & Compliance | 17% |
| Business Continuity & Disaster Recovery | 15% |
| Network Security | 16% |
| Cloud Security | 10% |
| Cryptography | 10% |

## Install

```bash
git clone https://github.com/mamusaminu/cc-prep-forge.git
cd cc-prep-forge
python3 index.py
```

## Modes

### Flashcard Mode
```bash
python3 index.py
# Shows a question → you answer → press Enter to reveal → rate yourself
```

### Quiz Mode
```bash
python3 index.py quiz
# Multiple choice, 10 questions per round, domain-weighted selection
```

### Study by Domain
```bash
python3 index.py study "Network Security"
```

## Progress

Progress is saved to `progress.json` in the same directory.

## Topics Covered

- CIA Triad, Least Privilege, Defense in Depth, Zero Trust
- Firewalls, IDS/IPS, WAF, DMZ, VPN
- OSI Model, TCP/UDP, DNS, NAT, VLAN, Routing
- Authentication (MFA, SSO, LDAP, Kerberos, Federated Identity)
- Encryption (Symmetric/Asymmetric, Hashing, Digital Certificates, Digital Signatures)
- Cloud (IaaS, SaaS, PaaS, Security Groups, Serverless)
- Incident Response, BIA, RTO/RPO, BCP/DR Plans
- SIEM, Vulnerability Management, System Hardening, Change Management
- Governance: Policy vs Procedure, Regulations, Security Audits