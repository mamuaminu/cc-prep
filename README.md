# CC-Prep Forge — ISC2 Certified in Cybersecurity Exam Prep

> **100 questions** aligned to the official CC exam outline (effective Oct 2025).  
> Built by: **Muhammad Aminu Musa**

## What it does

- **Flashcard mode** — flip through all 100 questions, self-rate your answers
- **Quiz mode** — 10 random questions per round with immediate feedback
- **Progress tracking** — saves study history to `progress.json`
- **Domain-weighted** — matches official CC exam domain percentages

## Official Exam Outline (CC — Effective Oct 2025)

| Domain | Weight |
|---|---|
| Security Principles | 26% |
| Access Controls Concepts | 22% |
| Network Security | 24% |
| Security Operations | 18% |
| BC/DR & Incident Response Concepts | 10% |

**Exam:** 100–125 questions | 2 hours | CAT adaptive | Passing: 700/1000

## Install

```bash
git clone https://github.com/mamusaminu/cc-prep-forge.git
cd cc-prep-forge
python3 index.py
```

## Modes

```bash
python3 index.py          # Flashcard mode
python3 index.py quiz     # Quiz mode (10 random Qs)
```

## Topics Covered

- **Security Principles:** CIA triad, risk management, security policies/procedures/standards/guidelines, ethics (ISC2 Code of Ethics), BEC/social engineering, AI washing, risk transference
- **Access Controls:** AAA framework, MFA, SSO, LDAP, Kerberos, RBAC/DAC/MAC, least privilege, need-to-know, account lifecycle, tailgating prevention
- **Network Security:** Firewalls, IDS/IPS, WAF, DMZ, VPN, OSI model, TCP/UDP, DNS, NAT, VLAN, subnetting, routing, switching, proxy servers, Zero Trust, APT, DPI, security zones
- **Security Operations:** Logging & monitoring, SIEM, configuration management, vulnerability management, system hardening, change management, security awareness training, encryption (symmetric/asymmetric)
- **BC/DR & Incident Response:** BIA, RTO/RPO, BCP/DRP, hot/warm/cold sites, tabletop exercises, incident classification, business impact analysis

## Questions Count

| Domain | Questions |
|---|---|
| Security Principles | 8 |
| Access Controls | 6 |
| Network Security | 9 |
| Security Operations | 5 |
| BC/DR & Incident Response | 4 |
| **Total** | **100** |

## Progress

Progress is saved to `progress.json` — tracks questions attempted, correct answers, and accuracy rate.

## License

MIT