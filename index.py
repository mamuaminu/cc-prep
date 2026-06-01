#!/usr/bin/env python3
"""
CC-Prep Forge — ISC2 Certified in Cybersecurity Exam Prep Tool
Built by: Muhammad Aminu Musa
"""

import json, random, os, sys
from datetime import datetime

DATA_FILE = os.path.join(os.path.dirname(__file__), "cc_questions.json")
PROGRESS_FILE = os.path.join(os.path.dirname(__file__), "progress.json")
OUTLINE_FILE = os.path.join(os.path.dirname(__file__), "exam_outline.txt")

QUESTIONS = [
    # Domain 1: Security Principles (15%)
    {
        "id": 1, "domain": "Security Principles", "weight": "15%",
        "q": "What is the CIA triad?",
        "options": [
            "A) Confidentiality, Integrity, Availability",
            "B) Control, Investigation, Authentication",
            "C) Compliance, Integrity, Access",
            "D) Confidentiality, Identity, Authorization"
        ],
        "answer": 0, "explanation": "The CIA triad = Confidentiality, Integrity, Availability. Core info sec concept."
    },
    {
        "id": 2, "domain": "Security Principles", "weight": "15%",
        "q": "What does 'Least Privilege' mean?",
        "options": [
            "A) Give everyone full access by default",
            "B) Users get only the access they need for their job",
            "C) Admins get root by default",
            "D) All data is encrypted"
        ],
        "answer": 1, "explanation": "Least Privilege: only grant minimum access required to perform a job function."
    },
    {
        "id": 3, "domain": "Security Principles", "weight": "15%",
        "q": "What is the difference between a threat and a vulnerability?",
        "options": [
            "A) They mean the same thing",
            "B) A threat is a potential cause of harm; a vulnerability is a weakness that can be exploited",
            "C) Vulnerability is worse than threat",
            "D) Threat is external, vulnerability is internal only"
        ],
        "answer": 1, "explanation": "Threat = potential cause of harm. Vulnerability = weakness that can be exploited."
    },
    {
        "id": 4, "domain": "Security Principles", "weight": "15%",
        "q": "What is Defense in Depth?",
        "options": [
            "A) Using only one security control",
            "B) Layering multiple security controls so if one fails, others still protect",
            "C) Having a deep firewall",
            "D) Keeping data in a deep vault"
        ],
        "answer": 1, "explanation": "Defense in Depth = multiple layers of security controls. If one fails, others compensate."
    },
    {
        "id": 5, "domain": "Security Principles", "weight": "15%",
        "q": "Which of these is NOT a type of access control?",
        "options": ["A) DAC", "B) MAC", "C) RBAC", "D) XACL"],
        "answer": 3, "explanation": "Common access controls: DAC (Discretionary), MAC (Mandatory), RBAC (Role-Based). XACL isn't standard."
    },
    # Domain 2: Asset Security (10%)
    {
        "id": 6, "domain": "Asset Security", "weight": "10%",
        "q": "What does 'Data Classification' help with?",
        "options": [
            "A) Naming files randomly",
            "B) Categorizing data by sensitivity to apply appropriate security controls",
            "C) Hiding data from users",
            "D) Compressing files"
        ],
        "answer": 1, "explanation": "Data classification = categorizing data (Public, Internal, Confidential, Restricted) to apply correct controls."
    },
    {
        "id": 7, "domain": "Asset Security", "weight": "10%",
        "q": "PII stands for?",
        "options": [
            "A) Private Internet Information",
            "B) Personally Identifiable Information",
            "C) Protected Internet Protocol",
            "D) Public Identity Index"
        ],
        "answer": 1, "explanation": "PII = Personally Identifiable Information. Any data that can identify an individual."
    },
    {
        "id": 8, "domain": "Asset Security", "weight": "10%",
        "q": "What is the purpose of data retention policies?",
        "options": [
            "A) To keep all data forever",
            "B) To define how long data should be kept and when it should be securely destroyed",
            "C) To increase storage costs",
            "D) To make compliance harder"
        ],
        "answer": 1, "explanation": "Retention policies define how long to keep data and when to securely dispose of it."
    },
    # Domain 3: Security Architecture (16%)
    {
        "id": 9, "domain": "Security Architecture", "weight": "16%",
        "q": "What is the primary purpose of a Firewall?",
        "options": [
            "A) To make networks faster",
            "B) To filter traffic between networks based on security rules",
            "C) To back up data",
            "D) To host websites"
        ],
        "answer": 1, "explanation": "Firewalls filter traffic between networks based on rules, blocking unauthorized access."
    },
    {
        "id": 10, "domain": "Security Architecture", "weight": "16%",
        "q": "What type of attack uses fake emails to trick people into revealing sensitive info?",
        "options": ["A) DDoS", "B) Phishing", "C) SQL Injection", "D) Man-in-the-Middle"],
        "answer": 1, "explanation": "Phishing = fraudulent emails/messages to trick victims into revealing credentials or sensitive data."
    },
    {
        "id": 11, "domain": "Security Architecture", "weight": "16%",
        "q": "What is a DMZ in network security?",
        "options": [
            "A) A military zone",
            "B) A demilitarized zone — a subnet between trusted internal network and untrusted internet",
            "C) A database zone",
            "D) A backup network"
        ],
        "answer": 1, "explanation": "DMZ = demilitarized zone. A subnet that hosts public-facing services, separated from the internal LAN."
    },
    {
        "id": 12, "domain": "Security Architecture", "weight": "16%",
        "q": "What does VPN stand for?",
        "options": [
            "A) Virtual Private Network",
            "B) Very Protected Network",
            "C) Verified Public Node",
            "D) Visual Private Navigation"
        ],
        "answer": 0, "explanation": "VPN = Virtual Private Network. Creates an encrypted tunnel over public networks for secure communication."
    },
    {
        "id": 13, "domain": "Security Architecture", "weight": "16%",
        "q": "What is the difference between a virus and a worm?",
        "options": [
            "A) They are the same",
            "B) Virus needs human action to spread; worm spreads automatically",
            "C) Worm is more dangerous than virus",
            "D) Virus only affects Windows"
        ],
        "answer": 1, "explanation": "Virus = requires user action to spread (opens file). Worm = self-replicates across networks automatically."
    },
    # Domain 4: Communication & Network Security (16%)
    {
        "id": 14, "domain": "Communication & Network Security", "weight": "16%",
        "q": "What port does HTTPS use by default?",
        "options": ["A) 21", "B) 25", "C) 443", "D) 8080"],
        "answer": 2, "explanation": "HTTPS = port 443. HTTP = port 80. FTP = 21. SMTP = 25."
    },
    {
        "id": 15, "domain": "Communication & Network Security", "weight": "16%",
        "q": "What does the principle of 'Separation of Duties' mean?",
        "options": [
            "A) Everyone does the same job",
            "B) No single person should have control over all aspects of a critical process",
            "C) Only managers can use computers",
            "D) IT and Security must always agree"
        ],
        "answer": 1, "explanation": "Separation of Duties = critical tasks are split among multiple people to prevent fraud and errors."
    },
    {
        "id": 16, "domain": "Communication & Network Security", "weight": "16%",
        "q": "What is the main function of an Intrusion Detection System (IDS)?",
        "options": [
            "A) Block all traffic",
            "B) Monitor network traffic for suspicious activity and alert administrators",
            "C) Speed up the network",
            "D) Backup data automatically"
        ],
        "answer": 1, "explanation": "IDS = monitors traffic for suspicious activity and generates alerts. IPS = also blocks."
    },
    {
        "id": 17, "domain": "Communication & Network Security", "weight": "16%",
        "q": "What is the OSI model layer for Routers?",
        "options": ["A) Layer 1", "B) Layer 2", "C) Layer 3", "D) Layer 7"],
        "answer": 2, "explanation": "Routers operate at Layer 3 (Network Layer). Switches = Layer 2. Hubs = Layer 1."
    },
    # Domain 5: Identity & Access Management (15%)
    {
        "id": 18, "domain": "Identity & Access Management", "weight": "15%",
        "q": "What is Multi-Factor Authentication (MFA)?",
        "options": [
            "A) Using two passwords",
            "B) Requiring two or more verification factors (something you know, have, or are)",
            "C) Using two different computers",
            "D) Having two user accounts"
        ],
        "answer": 1, "explanation": "MFA = requires 2+ verification factors: something you know (password), have (token), or are (biometrics)."
    },
    {
        "id": 19, "domain": "Identity & Access Management", "weight": "15%",
        "q": "What does LDAP stand for?",
        "options": [
            "A) Light Data Access Protocol",
            "B) Lightweight Directory Access Protocol",
            "C) Large Data Access Protocol",
            "D) Local Directory Application Protocol"
        ],
        "answer": 1, "explanation": "LDAP = Lightweight Directory Access Protocol. Used to access and manage directory services (e.g., Active Directory)."
    },
    {
        "id": 20, "domain": "Identity & Access Management", "weight": "15%",
        "q": "What is the main risk of using the same password across multiple services?",
        "options": [
            "A) Nothing, it's fine",
            "B) If one service is breached, all your accounts are compromised (credential stuffing)",
            "C) It slows down your computer",
            "D) It's only a problem for banking"
        ],
        "answer": 1, "explanation": "Credential stuffing = attackers reuse leaked passwords across multiple services. Use unique passwords."
    },
    # Domain 6: Security Assessment & Testing (11%)
    {
        "id": 21, "domain": "Security Assessment & Testing", "weight": "11%",
        "q": "What is the difference between a vulnerability scan and a penetration test?",
        "options": [
            "A) They are the same",
            "B) Vulnerability scan finds weaknesses; pen test actively exploits them",
            "C) Pen test is faster",
            "D) Vulnerability scan is more thorough"
        ],
        "answer": 1, "explanation": "Vuln scan = automated check for known weaknesses. Pen test = manually exploits vulnerabilities to simulate real attack."
    },
    {
        "id": 22, "domain": "Security Assessment & Testing", "weight": "11%",
        "q": "What does a SIEM do?",
        "options": [
            "A) Sends emails automatically",
            "B) Security Information and Event Management — collects and analyzes security logs from multiple sources",
            "C) encrypts files",
            "D) Blocks all traffic"
        ],
        "answer": 1, "explanation": "SIEM = Security Information and Event Management. Aggregates logs from across the infrastructure for monitoring and threat detection."
    },
    # Domain 7: Incident Response (13%)
    {
        "id": 23, "domain": "Incident Response", "weight": "13%",
        "q": "What is the FIRST step in incident response?",
        "options": [
            "A) Delete all logs",
            "B) Notify everyone on social media",
            "C) Preparation — having an IR plan, team, and tools ready before incidents happen",
            "D) Shut down the network"
        ],
        "answer": 2, "explanation": "Incident Response steps: 1) Preparation, 2) Identification, 3) Containment, 4) Eradication, 5) Recovery, 6) Lessons Learned."
    },
    {
        "id": 24, "domain": "Incident Response", "weight": "13%",
        "q": "What is the difference between a false positive and a false negative in security?",
        "options": [
            "A) Same thing",
            "B) False positive = alert for non-threat; False negative = missing a real threat",
            "C) False positive = missing threat; False negative = alert for non-threat",
            "D) Neither matters"
        ],
        "answer": 1, "explanation": "False positive = alert when no threat exists. False negative = misses a real threat. Both are dangerous."
    },
    # Domain 8: Business Continuity & Disaster Recovery (10%)
    {
        "id": 25, "domain": "Business Continuity & Disaster Recovery", "weight": "10%",
        "q": "What does BCP stand for?",
        "options": [
            "A) Big Computer Protocol",
            "B) Business Continuity Plan — procedures to keep business running during/after a disaster",
            "C) Backup Copy Process",
            "D) Binary Copy Program"
        ],
        "answer": 1, "explanation": "BCP = Business Continuity Plan. Keeps business running during and after a disruption."
    },
    {
        "id": 26, "domain": "Business Continuity & Disaster Recovery", "weight": "10%",
        "q": "What is RTO in disaster recovery?",
        "options": [
            "A) Recovery Time Objective — maximum acceptable time to restore a system after a disruption",
            "B) Real Time Operation",
            "C) Replicate To Origin",
            "D) Remote Transfer Option"
        ],
        "answer": 0, "explanation": "RTO = Recovery Time Objective. How long you can afford to be down. RPO = Recovery Point Objective (data loss tolerance)."
    },
    {
        "id": 27, "domain": "Business Continuity & Disaster Recovery", "weight": "10%",
        "q": "What is the difference between hot, warm, and cold backup sites?",
        "options": [
            "A) Temperature",
            "B) Hot = fully operational 24/7; Warm = partially equipped, needs hours; Cold = infrastructure only, days to activate",
            "C) They are all the same",
            "D) Cold is best for everything"
        ],
        "answer": 1, "explanation": "Hot = fully redundant, instant failover. Warm = partially ready, hours to activate. Cold = site with infrastructure, days to bring online."
    },
    # More questions for depth
    {
        "id": 28, "domain": "Security Principles", "weight": "15%",
        "q": "What is a 'Zero Day' vulnerability?",
        "options": [
            "A) A vulnerability that has existed for zero days",
            "B) A previously unknown vulnerability with no available patch at the time of discovery",
            "C) A vulnerability in day-old software",
            "D) An exploit only available at midnight"
        ],
        "answer": 1, "explanation": "Zero Day = unknown vulnerability with no patch. Called 'zero day' because vendors have had zero days to fix it."
    },
    {
        "id": 29, "domain": "Security Architecture", "weight": "16%",
        "q": "What is SQL Injection?",
        "options": [
            "A) Injecting SQL servers into networks",
            "B) Inserting malicious SQL code into application queries to manipulate the database",
            "C) Creating new databases",
            "D) Backing up SQL data"
        ],
        "answer": 1, "explanation": "SQL injection = attacker inserts malicious SQL code into application input fields to read/modify the database."
    },
    {
        "id": 30, "domain": "Identity & Access Management", "weight": "15%",
        "q": "What does SSO stand for?",
        "options": [
            "A) Super Security Operation",
            "B) Single Sign-On — one login grants access to multiple systems",
            "C) Secure Socket Output",
            "D) System Security Office"
        ],
        "answer": 1, "explanation": "SSO = Single Sign-On. One authentication grants access to multiple related systems. Convenient but single point of failure."
    },
    {
        "id": 31, "domain": "Security Principles", "weight": "15%",
        "q": "What is the difference between symmetric and asymmetric encryption?",
        "options": [
            "A) Same thing",
            "B) Symmetric = one key for both encrypt/decrypt; Asymmetric = public key encrypts, private key decrypts",
            "C) Asymmetric is faster",
            "D) Symmetric uses two passwords"
        ],
        "answer": 1, "explanation": "Symmetric = same key for both (fast, for bulk data). Asymmetric = public/private key pair (slower, for key exchange and signatures)."
    },
    {
        "id": 32, "domain": "Security Architecture", "weight": "16%",
        "q": "What is a Man-in-the-Middle (MITM) attack?",
        "options": [
            "A) Attacker secretly intercepts and possibly alters communication between two parties",
            "B) Attacker stands in the middle of a room",
            "C) A firewall technique",
            "D) An encrypted tunnel"
        ],
        "answer": 0, "explanation": "MITM = attacker secretly intercepts communication between two parties, can eavesdrop or alter data."
    },
    {
        "id": 33, "domain": "Asset Security", "weight": "10%",
        "q": "What does 'Data Masking' mean?",
        "options": [
            "A) Hiding data in a mask",
            "B) Converting sensitive data into unreadable characters while preserving format for testing/training",
            "C) Deleting data",
            "D) Encrypting only the mask"
        ],
        "answer": 1, "explanation": "Data masking = hiding sensitive data (e.g., showing **** for real SSN) while keeping format usable for non-production environments."
    },
    {
        "id": 34, "domain": "Communication & Network Security", "weight": "16%",
        "q": "What is the difference between deep web and dark web?",
        "options": [
            "A) Same thing",
            "B) Deep web = not indexed by standard search (intranets, databases); Dark web = hidden networks requiring special software (Tor)",
            "C) Dark web is just the deep web",
            "D) Deep web is illegal"
        ],
        "answer": 1, "explanation": "Deep web = any content not indexed by search engines (databases, intranets). Dark web = networks like Tor hidden from normal browsers, often associated with illegal activity."
    },
    {
        "id": 35, "domain": "Security Assessment & Testing", "weight": "11%",
        "q": "What is a 'Pentest' scope document?",
        "options": [
            "A) A document listing all your passwords",
            "B) Agreement defining what will be tested, methods, timelines, and boundaries of a penetration test",
            "C) A list of all servers",
            "D) A budget document"
        ],
        "answer": 1, "explanation": "Scope document = defines what to test, how, rules of engagement, timeline, deliverables. Critical before any pentest begins."
    },
    {
        "id": 36, "domain": "Incident Response", "weight": "13%",
        "q": "What is a 'Chain of Custody' in digital forensics?",
        "options": [
            "A) A physical chain",
            "B) Documented chronological record of evidence seizure, transfer, and analysis to prove integrity",
            "C) A type of lock",
            "D) A backup strategy"
        ],
        "answer": 1, "explanation": "Chain of custody = documented record of who collected, handled, transferred, and analyzed evidence. Critical for legal admissibility."
    },
    {
        "id": 37, "domain": "Security Principles", "weight": "15%",
        "q": "What is Social Engineering?",
        "options": [
            "A) Building social networks",
            "B) Manipulating people into divulging confidential information or performing actions through psychological manipulation",
            "C) Engineering software for social media",
            "D) A type of encryption"
        ],
        "answer": 1, "explanation": "Social engineering = exploiting human psychology (trust, fear, urgency) to get sensitive info or access. Phishing is one form."
    },
    {
        "id": 38, "domain": "Business Continuity & Disaster Recovery", "weight": "10%",
        "q": "What is a Business Impact Analysis (BIA)?",
        "options": [
            "A) An analysis of business profits",
            "B) Process of identifying critical business functions and the impact of their disruption",
            "C) A type of firewall",
            "D) An HR document"
        ],
        "answer": 1, "explanation": "BIA = Business Impact Analysis. Identifies which business functions are most critical and what the impact of their downtime would be. Foundation of BCP/DR."
    },
    {
        "id": 39, "domain": "Identity & Access Management", "weight": "15%",
        "q": "What is Kerberos?",
        "options": [
            "A) A Greek mythology creature",
            "B) A network authentication protocol using tickets to prove identity without transmitting passwords",
            "C) A type of firewall",
            "D) An encryption algorithm"
        ],
        "answer": 1, "explanation": "Kerberos = network authentication protocol (from MIT's Project Athena). Uses tickets, not passwords, to authenticate. Common in Windows Active Directory."
    },
    {
        "id": 40, "domain": "Security Architecture", "weight": "16%",
        "q": "What does a WAF (Web Application Firewall) protect against?",
        "options": [
            "A) Physical fire",
            "B) Attacks targeting web applications like SQL injection, XSS, and other OWASP Top 10 threats",
            "C) Hardware failures",
            "D) Slow internet connections"
        ],
        "answer": 1, "explanation": "WAF = Web Application Firewall. Filters and monitors HTTP traffic to/from web apps, blocks SQLi, XSS, and other app-layer attacks."
    },
]

DOMAINS = {
    "Security Principles":          {"weight": "15%", "count": 5},
    "Asset Security":               {"weight": "10%", "count": 3},
    "Security Architecture":        {"weight": "16%", "count": 5},
    "Communication & Network Security": {"weight": "16%", "count": 4},
    "Identity & Access Management": {"weight": "15%", "count": 4},
    "Security Assessment & Testing": {"weight": "11%", "count": 3},
    "Incident Response":            {"weight": "13%", "count": 3},
    "Business Continuity & Disaster Recovery": {"weight": "10%", "count": 4},
}

def load_progress():
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE) as f:
            return json.load(f)
    return {"total_attempted": 0, "correct": 0, "incorrect": {}, "domains": {}, "streak": 0, "best_streak": 0}

def save_progress(p):
    with open(PROGRESS_FILE, "w") as f:
        json.dump(p, f, indent=2)

def show_outline():
    print("""
╔══════════════════════════════════════════════════════════════╗
║           ISC2 Certified in Cybersecurity (CC)              ║
║                  Exam Domain Outline                        ║
╠══════════════════════════════════════════════════════════════╣
║ Domain 1: Security Principles              — 15% (2-3 Qs)    ║
║ Domain 2: Asset Security                  — 10% (1-2 Qs)    ║
║ Domain 3: Security Architecture           — 16% (3-4 Qs)    ║
║ Domain 4: Communication & Network Security— 16% (3-4 Qs)    ║
║ Domain 5: Identity & Access Management    — 15% (2-3 Qs)    ║
║ Domain 6: Security Assessment & Testing   — 11% (2-3 Qs)    ║
║ Domain 7: Incident Response               — 13% (2-3 Qs)    ║
║ Domain 8: Business Continuity & DR        — 10% (1-2 Qs)    ║
╠══════════════════════════════════════════════════════════════╣
║ Total: 100 questions | 2 hours | Passing score: ~700/1000   ║
╚══════════════════════════════════════════════════════════════╝
""")
    for domain, info in DOMAINS.items():
        print(f"  ▸ {domain:<42} {info['weight']}")

def study_mode(progress):
    print("\n📚  FLASHCARD MODE — Press Enter for next card, 'Q' to quit\n")
    deck = random.sample(QUESTIONS, len(QUESTIONS))
    correct = 0
    total = 0
    for q in deck:
        print(f"\n{'─'*55}")
        print(f"[{q['domain']}] [{q['weight']}] Question #{q['id']}")
        print(f"  {q['q']}\n")
        for opt in q['options']:
            print(f"  {opt}")
        print(f"\n  Type answer letter (A/B/C/D) or Enter to reveal answer:")
        try:
            ans = input("  > ").strip().upper()
        except (EOFError, KeyboardInterrupt):
            print("\n\nStudy session ended.")
            break
        if ans in ['Q', 'QUIT']:
            print("\n\nStudy session ended.")
            break
        total += 1
        if ans and ans in ['A','B','C','D']:
            is_correct = ord(ans[0]) - ord('A') == q['answer']
            if is_correct:
                correct += 1
                print(f"  ✅ CORRECT! {q['explanation']}")
            else:
                correct_letter = chr(ord('A') + q['answer'])
                print(f"  ❌ WRONG! Answer: {correct_letter}")
                print(f"  {q['explanation']}")
        else:
            correct_letter = chr(ord('A') + q['answer'])
            print(f"  📖 ANSWER: {correct_letter} — {q['explanation']}")
        input("  Press Enter for next card...")
    print(f"\n\n📊 Session Complete: {correct}/{total} correct ({int(correct/total*100) if total else 0}%)")
    progress['total_attempted'] += total
    progress['correct'] += correct
    save_progress(progress)
    return progress

def quiz_mode(progress):
    print("\n🎯  QUIZ MODE — Timed, 10 random questions\n")
    print("Type letter (A/B/C/D), 'Q' to quit anytime.\n")
    questions = random.sample(QUESTIONS, min(10, len(QUESTIONS)))
    correct = 0
    start = datetime.now()
    for i, q in enumerate(questions):
        elapsed = (datetime.now() - start).seconds
        print(f"\n{'─'*55}")
        print(f"[Q{i+1}/10] [{q['domain']}] {elapsed}s elapsed")
        print(f"  {q['q']}\n")
        for opt in q['options']:
            print(f"  {opt}")
        try:
            ans = input("\n  Your answer: ").strip().upper()
        except (EOFError, KeyboardInterrupt):
            print("\nQuiz ended.")
            break
        if ans == 'Q':
            print("\nQuiz ended.")
            break
        if ans in ['A','B','C','D']:
            is_correct = ord(ans[0]) - ord('A') == q['answer']
            if is_correct:
                correct += 1
                print(f"  ✅ Correct!")
            else:
                correct_letter = chr(ord('A') + q['answer'])
                print(f"  ❌ Wrong! Answer: {correct_letter}")
                print(f"  {q['explanation']}")
        else:
            print("  Skipped.")
    pct = int(correct/10*100) if questions else 0
    print(f"\n{'='*55}")
    print(f"  🎯 QUIZ RESULT: {correct}/10 ({pct}%)")
    print(f"  ⏱ Time: {(datetime.now()-start).seconds}s")
    if pct >= 80:
        print(f"  🔥 Excellent! You're ready!")
    elif pct >= 60:
        print(f"  📖 Getting there — keep practicing!")
    else:
        print(f"  📚 Focus more on weak areas.")
    progress['total_attempted'] += 10
    progress['correct'] += correct
    save_progress(progress)
    return progress

def progress_stats():
    p = load_progress()
    total = p.get('total_attempted', 0)
    correct = p.get('correct', 0)
    pct = int(correct/total*100) if total > 0 else 0
    print(f"""
╔════════════════════════════════════════════╗
║           CC PREP PROGRESS                ║
╠════════════════════════════════════════════╣
║  Questions Attempted:   {total:>5}                 ║
║  Correct Answers:       {correct:>5}                 ║
║  Accuracy Rate:         {pct:>5}%                ║
╚════════════════════════════════════════════╝
""")

def refresh_questions():
    """Save questions to JSON file for reference"""
    with open(DATA_FILE, 'w') as f:
        json.dump(QUESTIONS, f, indent=2)
    print(f"💾 Saved {len(QUESTIONS)} questions to {DATA_FILE}")

def main():
    print("""
╔══════════════════════════════════════════════════════════════╗
║              🔥 CC-PREP FORGE 🔥                            ║
║      ISC2 Certified in Cybersecurity Exam Prep               ║
║      Built for El Matador — Sakamoto Nightly Build          ║
╚══════════════════════════════════════════════════════════════╝
""")
    progress = load_progress()

    actions = {
        "1": ("📖 Study Mode (Flashcards)", lambda: study_mode(progress)),
        "2": ("🎯 Quiz Mode (10 Questions)", lambda: quiz_mode(progress)),
        "3": ("📊 Progress Stats", lambda: progress_stats()),
        "4": ("📋 Exam Domain Outline", show_outline),
        "5": ("💾 Refresh Question Data", refresh_questions),
    }

    print("\nWhat would you like to do?\n")
    for k, (label, _) in actions.items():
        print(f"  [{k}] {label}")

    print("\n  [Q] Quit\n")
    try:
        choice = input("Select: ").strip()
    except (EOFError, KeyboardInterrupt):
        print("\nGoodbye, El Matador!")
        return

    if choice.upper() == 'Q':
        print("Goodbye, El Matador! Keep grinding 💪")
        return

    if choice in actions:
        actions[choice][1]()
    else:
        print("Invalid option.")

if __name__ == "__main__":
    main()