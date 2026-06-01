# CC-Prep Forge — ISC2 Certified in Cybersecurity Exam Prep

> Flashcard + quiz CLI tool for the ISC2 Certified in Cybersecurity (CC) exam.

## What it does

- **Flashcard mode** — flip through CC exam questions, self-rate your answers
- **Quiz mode** — multiple-choice rounds with immediate feedback
- **Progress tracking** — saves your study history
- **Domain-weighted questions** — matches the official CC exam outline

## Exam Domains

| Domain | Weight |
|--------|--------|
| Security Principles | 15% |
| Access Controls | 17% |
| Security Operations | 20% |
| Governance, Risk, and Compliance | 17% |
| Incident, Business Continuity, and Disaster Recovery | 15% |
| Network Security | 16% |

## Install

```bash
git clone https://github.com/mamuaminu/cc-prep-forge.git
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
python3 index.py study "Access Controls"
```

## Progress

Progress is saved to `progress.json` in the same directory.

## Files



---

