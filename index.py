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
    # Additional questions — Network Security & more
    {
        "id": 41, "domain": "Network Security", "weight": "16%",
        "q": "What is the primary function of a Router?",
        "options": [
            "A) Broadcast data to all connected devices",
            "B) Forward data packets between different networks based on IP addresses",
            "C) Filter traffic within the same subnet",
            "D) Assign IP addresses to clients"
        ],
        "answer": 1, "explanation": "Routers forward packets between different networks based on IP address routing tables. Switches forward within a LAN; hubs broadcast."
    },
    {
        "id": 42, "domain": "Network Security", "weight": "16%",
        "q": "What is the difference between a Layer 2 Switch and a Layer 3 Switch?",
        "options": [
            "A) Layer 2 switches only support Wi-Fi",
            "B) Layer 2 switches use MAC addresses; Layer 3 switches can route based on IP addresses (like a router)",
            "C) They are identical",
            "D) Layer 3 switches are slower"
        ],
        "answer": 1, "explanation": "Layer 2 = MAC address switching (same network). Layer 3 = can route between subnets using IP addresses. Layer 3 switches combine switch + router functions."
    },
    {
        "id": 43, "domain": "Network Security", "weight": "16%",
        "q": "What does NAT (Network Address Translation) do?",
        "options": [
            "A) Translates domain names to IP addresses",
            "B) Maps private IP addresses to a public IP address to allow internet access while hiding internal IPs",
            "C) Blocks all inbound traffic",
            "D) Encrypts network traffic"
        ],
        "answer": 1, "explanation": "NAT maps private internal IPs to a single (or few) public IP(s) for internet access. Also provides a layer of security by hiding internal network topology."
    },
    {
        "id": 44, "domain": "Network Security", "weight": "16%",
        "q": "What is a VLAN and why is it used?",
        "options": [
            "A) A type of virus",
            "B) Virtual LAN — logically separates devices on the same physical network without requiring separate infrastructure",
            "C) A backup storage method",
            "D) A WAN connection protocol"
        ],
        "answer": 1, "explanation": "VLAN = Virtual LAN. Groups devices logically by function or department, not physical location. Improves performance and security by isolating broadcast domains."
    },
    {
        "id": 45, "domain": "Network Security", "weight": "16%",
        "q": "What port does DNS use?",
        "options": [
            "A) 25",
            "B) 53",
            "C) 443",
            "D) 110"
        ],
        "answer": 1, "explanation": "DNS uses port 53 (both TCP and UDP). DHCP = 67/68. HTTP = 80. HTTPS = 443. FTP = 21."
    },
    {
        "id": 46, "domain": "Network Security", "weight": "16%",
        "q": "What is the OSI layer for the Transport layer?",
        "options": [
            "A) Layer 1",
            "B) Layer 2",
            "C) Layer 4",
            "D) Layer 7"
        ],
        "answer": 2, "explanation": "Layer 4 = Transport. Responsible for end-to-end communication, reliability, flow control, and segmentation/desegmentation. TCP & UDP operate here."
    },
    {
        "id": 47, "domain": "Network Security", "weight": "16%",
        "q": "What is the main difference between TCP and UDP?",
        "options": [
            "A) TCP is faster than UDP",
            "B) TCP is connection-oriented with error checking; UDP is connectionless and faster but without guarantees",
            "C) They are the same",
            "D) UDP is used for web browsing, TCP for video streaming"
        ],
        "answer": 1, "explanation": "TCP = connection-oriented, reliable, ordered delivery, error correction. UDP = connectionless, no guarantee of delivery, lower overhead. TCP for web/email; UDP for video/DNS."
    },
    {
        "id": 48, "domain": "Network Security", "weight": "16%",
        "q": "What is an Intrusion Prevention System (IPS)?",
        "options": [
            "A) A type of antivirus",
            "B) Actively blocks and prevents detected attacks in addition to monitoring and alerting",
            "C) A backup system",
            "D) A firewall that only logs traffic"
        ],
        "answer": 1, "explanation": "IPS = actively blocks malicious traffic after detecting it (inline). IDS = passive monitoring and alerting only. IPS can stop threats in real-time."
    },
    {
        "id": 49, "domain": "Network Security", "weight": "16%",
        "q": "What is the OSI layer that Encrypted Traffic operates at?",
        "options": [
            "A) Layer 1",
            "B) Layer 3",
            "C) Layer 6",
            "D) TLS/SSL operates at Layer 5-6 but encryption can span multiple layers"
        ],
        "answer": 3, "explanation": "TLS/SSL encrypts data at the Presentation layer (Layer 6). However, TLS tunnels can carry any application-layer traffic. Know which layer your encryption lives at."
    },
    {
        "id": 50, "domain": "Network Security", "weight": "16%",
        "q": "What is a 'Zero Trust' security model?",
        "options": [
            "A) Trust all internal traffic by default",
            "B) Never trust any user or device by default — always verify, regardless of location (inside or outside the network perimeter)",
            "C) Only trust devices on the local network",
            "D) Disable all firewalls"
        ],
        "answer": 1, "explanation": "Zero Trust = 'never trust, always verify.' Every user, device, and connection must be authenticated and authorized before accessing resources, regardless of network location."
    },
    {
        "id": 51, "domain": "Network Security", "weight": "16%",
        "q": "What does a proxy server provide?",
        "options": [
            "A) Direct connection to the internet",
            "B) Acts as an intermediary — caches content, filters requests, hides client IPs, and can enforce security policies",
            "C) Increases network bandwidth",
            "D) Automatically encrypts all traffic"
        ],
        "answer": 1, "explanation": "Proxy server = intermediary between clients and the internet. Can cache files (faster access), filter content, hide internal IPs, log user activity, and enforce security policies."
    },
    {
        "id": 52, "domain": "Network Security", "weight": "16%",
        "q": "What is the difference between a hub and a switch?",
        "options": [
            "A) Same thing",
            "B) Hub broadcasts to all ports; Switch sends data only to the intended destination device based on MAC address",
            "C) Switch is slower than hub",
            "D) Hub is more secure"
        ],
        "answer": 1, "explanation": "Hub = broadcasts all data to every device (shared media, no intelligence). Switch = learns MAC addresses and forwards data only to the correct port (reduced collisions, better security)."
    },
    {
        "id": 53, "domain": "Network Security", "weight": "16%",
        "q": "What type of attack floods a network with traffic to make it unavailable?",
        "options": [
            "A) Phishing",
            "B) DDoS — Distributed Denial of Service",
            "C) SQL Injection",
            "D) Social Engineering"
        ],
        "answer": 1, "explanation": "DDoS = Distributed Denial of Service. Multiple compromised systems (botnet) flood a target with traffic to overwhelm it and make services unavailable."
    },
    {
        "id": 54, "domain": "Network Security", "weight": "16%",
        "q": "What is the main security concern with public Wi-Fi networks?",
        "options": [
            "A) They are always encrypted",
            "B) Traffic can be intercepted by nearby attackers (man-in-the-middle); use VPN to protect",
            "C) They are faster than wired networks",
            "D) They are only available in coffee shops"
        ],
        "answer": 1, "explanation": "Public Wi-Fi is typically unencrypted. Attackers on the same network can intercept traffic (packet sniffing/MITM). Always use a VPN on public Wi-Fi to encrypt your traffic."
    },
    {
        "id": 55, "domain": "Network Security", "weight": "16%",
        "q": "What is the OSI layer for the Application layer?",
        "options": [
            "A) Layer 1",
            "B) Layer 3",
            "C) Layer 7",
            "D) Layer 5"
        ],
        "answer": 2, "explanation": "Layer 7 = Application layer (OSI). This is where user-facing applications like HTTP, FTP, SMTP, DNS operate. Note: 'Application' here is not the end-user app itself but the network protocol."
    },
    {
        "id": 56, "domain": "Network Security", "weight": "16%",
        "q": "What does an SIEM tool integrate with to provide security monitoring?",
        "options": [
            "A) Firewalls only",
            "B) Log sources across the environment — servers, firewalls, endpoints, applications",
            "C) Only cloud services",
            "D) HR systems"
        ],
        "answer": 1, "explanation": "SIEM aggregates and correlates logs from many sources (network devices, servers, endpoints, cloud). This gives security teams centralized visibility and the ability to detect threats across the entire infrastructure."
    },
    {
        "id": 57, "domain": "Cloud Security", "weight": "10%",
        "q": "What does 'IaaS' stand for?",
        "options": [
            "A) Internet as a Service",
            "B) Infrastructure as a Service — provides virtualized computing resources over the internet",
            "C) Internal as a Service",
            "D) Integrated Application System"
        ],
        "answer": 1, "explanation": "IaaS = Infrastructure as a Service. Cloud provider offers virtual machines, storage, networking. Examples: AWS EC2, Azure VMs, Google Compute Engine. Customer manages OS and apps."
    },
    {
        "id": 58, "domain": "Cloud Security", "weight": "10%",
        "q": "In a SaaS model, who is responsible for data encryption?",
        "options": [
            "A) The customer only",
            "B) The cloud provider handles encryption by default; customer is responsible for access control and data management",
            "C) Neither",
            "D) The government"
        ],
        "answer": 1, "explanation": "In SaaS (Software as a Service), the provider handles underlying infrastructure and encryption. Customer is responsible for their own data (access controls, sharing, classification). Shared responsibility model."
    },
    {
        "id": 59, "domain": "Cloud Security", "weight": "10%",
        "q": "What is a 'Security Group' in cloud computing?",
        "options": [
            "A) A team of security analysts",
            "B) A virtual firewall that controls inbound/outbound traffic to cloud resources",
            "C) A data encryption standard",
            "D) A type of VPN"
        ],
        "answer": 1, "explanation": "Security Groups = virtual firewalls in cloud (AWS, Azure). They act as stateful packet filters controlling what traffic can enter or leave a group of instances. Default deny, you open what you need."
    },
    {
        "id": 60, "domain": "Cloud Security", "weight": "10%",
        "q": "What does 'Serverless' architecture (FaaS) mean?",
        "options": [
            "A) There are no servers involved",
            "B) Code runs in ephemeral containers managed by the cloud provider — you only pay for execution time",
            "C) Servers are removed from the network",
            "D) The application runs without any code"
        ],
        "answer": 1, "explanation": "Serverless (Function as a Service) doesn't mean no servers — it means the cloud provider manages the infrastructure. You write functions that run on demand. AWS Lambda, Azure Functions. Cost = only when code runs."
    },
    {
        "id": 61, "domain": "Cryptography", "weight": "10%",
        "q": "What is the difference between hashing and encryption?",
        "options": [
            "A) Same thing",
            "B) Hashing is one-way (can't be reversed); encryption is reversible with a key",
            "C) Hashing is reversible",
            "D) Encryption is one-way"
        ],
        "answer": 1, "explanation": "Hashing = one-way function, no key, produces fixed-length digest. Used for password storage. Encryption = reversible with key, used for confidentiality. Hash can't be reversed; encryption can."
    },
    {
        "id": 62, "domain": "Cryptography", "weight": "10%",
        "q": "What does 'Data at Rest' mean?",
        "options": [
            "A) Data being sent over a network",
            "B) Data stored on disk, databases, backups — not actively moving",
            "C) Data in RAM",
            "D) Data being processed by a CPU"
        ],
        "answer": 1, "explanation": "Data at Rest = stored data (HDD, SSD, tape, database). Vulnerable to physical theft or unauthorized access. Protected by encryption at rest, access controls, and database security."
    },
    {
        "id": 63, "domain": "Cryptography", "weight": "10%",
        "q": "What is a 'Digital Certificate' (SSL/TLS certificate)?",
        "options": [
            "A) A software license key",
            "B) A file that proves identity of a website using asymmetric cryptography, signed by a trusted Certificate Authority (CA)",
            "C) A type of antivirus",
            "D) An email address"
        ],
        "answer": 1, "explanation": "Digital certificate = binds a public key to an identity, signed by a trusted CA (like DigiCert, Let's Encrypt). Enables HTTPS by proving the server's identity. Browsers verify via the CA's root certificates."
    },
    {
        "id": 64, "domain": "Cryptography", "weight": "10%",
        "q": "What is the main use of a 'Digital Signature'?",
        "options": [
            "A) To encrypt all email",
            "B) To prove authenticity and integrity of a message/document — sender is who they claim, content wasn't altered",
            "C) To speed up network connections",
            "D) To replace passwords"
        ],
        "answer": 1, "explanation": "Digital signature = proves sender authenticity and document integrity. Created with sender's private key, verified with their public key. Provides non-repudiation — sender can't deny signing."
    },
    {
        "id": 65, "domain": "Governance, Risk & Compliance", "weight": "17%",
        "q": "What does 'Regulation' mean in cybersecurity governance?",
        "options": [
            "A) A suggestion",
            "B) A law or rule imposed by a governing body that organizations must legally follow",
            "C) A technical control",
            "D) Optional compliance"
        ],
        "answer": 1, "explanation": "Regulations = mandatory laws/rules (government or industry bodies). Examples: GDPR, HIPAA, PCI DSS, SOX. Non-compliance can result in fines and legal action."
    },
    {
        "id": 66, "domain": "Governance, Risk & Compliance", "weight": "17%",
        "q": "What is the difference between a 'Policy' and a 'Procedure'?",
        "options": [
            "A) Same thing",
            "B) Policy = high-level rule/goal set by management; Procedure = detailed step-by-step instructions to implement the policy",
            "C) Policy is for technical staff; Procedure is for management",
            "D) Procedure is optional"
        ],
        "answer": 1, "explanation": "Policy = what you must do (the rule). Procedure = how you do it (step-by-step). Policy is 'all employees must use strong passwords.' Procedure is the specific steps to create and manage passwords."
    },
    {
        "id": 67, "domain": "Governance, Risk & Compliance", "weight": "17%",
        "q": "What is the purpose of a Security Audit?",
        "options": [
            "A) To test software",
            "B) Independent review to evaluate if security controls, policies, and procedures are in place and effective",
            "C) To install new firewalls",
            "D) To hire security staff"
        ],
        "answer": 1, "explanation": "Security audit = systematic evaluation of an organization's security posture. Checks compliance with regulations, effectiveness of controls, identifies gaps. Can be internal or external."
    },
    {
        "id": 68, "domain": "Security Operations", "weight": "20%",
        "q": "What does 'Change Management' ensure in security operations?",
        "options": [
            "A) That no changes are ever made",
            "B) That changes to systems/networks are documented, reviewed, tested, and approved before implementation to reduce risk",
            "C) That changes happen instantly",
            "D) That only management can make changes"
        ],
        "answer": 1, "explanation": "Change management = controlled process for requesting, reviewing, approving, and implementing changes. Prevents unintended disruptions and security gaps from uncontrolled changes to infrastructure."
    },
    {
        "id": 69, "domain": "Security Operations", "weight": "20%",
        "q": "What is the principle of 'Least Privilege' in security operations?",
        "options": [
            "A) Give users maximum access by default",
            "B) Users and processes should have only the minimum access rights needed to perform their job function",
            "C) Admins should always have full access",
            "D) Passwords should never expire"
        ],
        "answer": 1, "explanation": "Least Privilege = only grant the minimum access needed. Reduces attack surface and damage from compromised accounts. Review access rights regularly and revoke when no longer needed."
    },
    {
        "id": 70, "domain": "Security Operations", "weight": "20%",
        "q": "What is the purpose of a 'Security Information and Event Management' (SIEM)?",
        "options": [
            "A) To block all network traffic",
            "B) To aggregate, normalize, correlate, and analyze log data from multiple sources for real-time monitoring and threat detection",
            "C) To send emails to users",
            "D) To replace antivirus software"
        ],
        "answer": 1, "explanation": "SIEM provides centralized log collection and analysis. Helps detect threats in real-time by correlating events across firewalls, servers, endpoints, and applications. Also used for compliance reporting."
    },
    {
        "id": 71, "domain": "Security Operations", "weight": "20%",
        "q": "What is 'Vulnerability Management'?",
        "options": [
            "A) Ignoring known vulnerabilities",
            "B) Continuous process of identifying, classifying, prioritizing, and remediating security vulnerabilities in systems and software",
            "C) Only scanning once a year",
            "D) Deleting vulnerable software"
        ],
        "answer": 1, "explanation": "Vulnerability management = ongoing cycle: scan → identify → assess severity → prioritize → remediate → verify. Not a one-time activity. Critical for reducing the attack surface proactively."
    },
    {
        "id": 72, "domain": "Security Operations", "weight": "20%",
        "q": "What does 'Hardening' a system mean?",
        "options": [
            "A) Making it physically stronger",
            "B) Configuring a system securely by removing unnecessary services, disabling weak protocols, applying patches, and tightening configurations to reduce attack surface",
            "C) Making the system run faster",
            "D) Adding more software"
        ],
        "answer": 1, "explanation": "System hardening = removing attack surface by disabling unnecessary services/ports, applying patches, enforcing strong configs, removing default accounts, enabling auditing. CIS Benchmarks are common hardening guides."
    },
    {
        "id": 73, "domain": "Access Controls", "weight": "17%",
        "q": "What is 'Single Sign-On' (SSO)?",
        "options": [
            "A) Using one password for all accounts",
            "B) Authentication mechanism where one login grants access to multiple related systems without re-entering credentials",
            "C) Logging in from a single device",
            "D) A type of encryption"
        ],
        "answer": 1, "explanation": "SSO = one authentication event grants access to multiple applications/systems. Improves UX and reduces password fatigue. Risk: if one account is compromised, multiple systems are exposed."
    },
    {
        "id": 74, "domain": "Access Controls", "weight": "17%",
        "q": "What does 'Federated Identity' mean?",
        "options": [
            "A) Using the same password everywhere",
            "B) Sharing identity across separate organizations/trusted partners using a shared authentication protocol (SAML, OAuth)",
            "C) Creating multiple local accounts",
            "D) Storing passwords in a database"
        ],
        "answer": 1, "explanation": "Federated identity = users can access systems of different organizations with one set of credentials. Uses trust relationships and protocols like SAML or OAuth. Example: login with Google on a third-party app."
    },
    {
        "id": 75, "domain": "Access Controls", "weight": "17%",
        "q": "What is the access control concept of 'Need-to-Know'?",
        "options": [
            "A) Everyone needs to know everything",
            "B) Users should only be granted access to data/resources necessary to perform their assigned tasks",
            "C) All managers need to know all passwords",
            "D) Access is granted by default"
        ],
        "answer": 1, "explanation": "Need-to-Know = restricts access to only the information required for a specific job function. Even if someone has clearance, they still only get access to what they need for their role. Complements Least Privilege."
    },
    {
        "id": 76, "domain": "Access Controls", "weight": "17%",
        "q": "What is 'Account Lifecycle Management'?",
        "options": [
            "A) Only creating accounts",
            "B) Managing user accounts from creation through modification, suspension, and termination throughout their existence",
            "C) Deleting all accounts annually",
            "D) Giving everyone admin rights"
        ],
        "answer": 1, "explanation": "Account lifecycle = managing accounts from onboarding to role changes to offboarding. Includes provisioning, deprovisioning (timely removal of access when roles change or employment ends), and regular access reviews."
    },
    {
        "id": 77, "domain": "Business Continuity & Disaster Recovery", "weight": "15%",
        "q": "What is the difference between 'Hot Backup' and 'Cold Backup' sites?",
        "options": [
            "A) Temperature-based",
            "B) Hot site = fully operational with real-time data replication, instant failover; Cold site = shell with infrastructure only, takes days to activate",
            "C) Cold backup is better",
            "D) They are the same"
        ],
        "answer": 1, "explanation": "Hot backup = fully equipped, real-time sync, ready to take over immediately (high cost). Cold backup = just space and basic infrastructure, needs time to become operational (lower cost). Warm site = middle ground."
    },
    {
        "id": 78, "domain": "Business Continuity & Disaster Recovery", "weight": "15%",
        "q": "What is a 'Tabletop Exercise' in BC/DR?",
        "options": [
            "A) Moving physical tablets around",
            "B) A simulation where response team walks through a disaster scenario on paper to test plans without real-world impact",
            "C) A type of backup",
            "D) Replacing actual DR drills"
        ],
        "answer": 1, "explanation": "Tabletop exercise = theoretical walkthrough of an incident scenario. Team discusses their response, identifies gaps in plans, improves coordination. Low cost, no disruption. Complement with functional exercises."
    },
    # ═══════════════════════════════════════════════════════
    # NEW QUESTIONS 79-100 — aligned to CC 2025 exam outline
    # ═══════════════════════════════════════════════════════
    {
        "id": 79, "domain": "Security Principles", "weight": "26%",
        "q": "An employee receives an email from the CEO asking to urgently wire money to a new vendor. This is an example of what type of attack?",
        "options": [
            "A) Malware infection",
            "B) Business Email Compromise (BEC) / CEO fraud",
            "C) SQL Injection",
            "D) DDoS attack"
        ],
        "answer": 1, "explanation": "BEC = attacker impersonates an executive to trick employees into transferring money or sensitive data. Very costly attack. Verify unusual requests via secondary channel."
    },
    {
        "id": 80, "domain": "Security Principles", "weight": "26%",
        "q": "What is the difference between a policy, a standard, a procedure, and a guideline?",
        "options": [
            "A) They are all the same thing",
            "B) Policy = high-level mandatory rule; Standard = specific quantitative requirement; Procedure = step-by-step instructions; Guideline = recommended best practice (non-mandatory)",
            "C) Policy is optional, guideline is mandatory",
            "D) Procedure is written by the CEO, policy by IT staff"
        ],
        "answer": 1, "explanation": "Policy = what you must do (mandatory, management-level). Standard = quantitative benchmark (e.g., password must be 12 chars). Procedure = detailed steps to accomplish a task. Guideline = flexible recommendation. Know the difference for the exam."
    },
    {
        "id": 81, "domain": "Security Principles", "weight": "26%",
        "q": "Which type of attack uses voice calls to trick someone into revealing sensitive information?",
        "options": [
            "A) Phishing",
            "B) Vishing (Voice Phishing)",
            "C) Smishing (SMS Phishing)",
            "D) Whaling"
        ],
        "answer": 1, "explanation": "Vishing = voice-based phishing (phone call). Smishing = SMS phishing. Phishing = generic email-based. Whaling = phishing targeting high-profile executives (CEO/CFO)."
    },
    {
        "id": 82, "domain": "Security Principles", "weight": "26%",
        "q": "What is 'Risk Transference' in risk management?",
        "options": [
            "A) Moving risk to another department",
            "B) Shifting the financial impact of a risk to another party (e.g., buying cyber insurance or outsourcing to a vendor)",
            "C) Ignoring the risk",
            "D) Accepting the risk"
        ],
        "answer": 1, "explanation": "Risk transference = moving the cost of a risk to a third party. Cyber insurance is the most common example. Risk acceptance = accepting the risk as is. Risk avoidance = not doing the risky activity."
    },
    {
        "id": 83, "domain": "Security Principles", "weight": "26%",
        "q": "What is 'AI washing' in cybersecurity?",
        "options": [
            "A) Using AI to wash data",
            "B) Overstating or falsely claiming a product uses AI capabilities for marketing purposes",
            "C) Training AI models on washing machines",
            "D) Using AI to bypass security controls"
        ],
        "answer": 1, "explanation": "AI washing = false or exaggerated AI claims by vendors. In CC 2025 outline, AI concepts are integrated across all domains. Security pros must evaluate AI security claims critically."
    },
    {
        "id": 84, "domain": "Security Principles", "weight": "26%",
        "q": "Which ISC2 Code of Ethics canon states 'Protect society, the common good, necessary public trust and confidence in the profession'?",
        "options": [
            "A) Act honorably, honestly, justly, responsibly, and legally",
            "B) Protect society, the common good, necessary public trust and confidence, and the profession",
            "C) Provide diligent and competent service to principals",
            "D) Advance and protect the profession"
        ],
        "answer": 1, "explanation": "The four ISC2 Code of Ethics canons: 1) Protect society/commongood/public trust (the 'why' of cybersecurity). 2) Act honorably/justly/responsibly. 3) Provide diligent service to principals. 4) Advance and protect the profession."
    },
    {
        "id": 85, "domain": "Access Controls", "weight": "22%",
        "q": "What is the correct order of the AAA framework?",
        "options": [
            "A) Authentication, Authorization, Accountability",
            "B) Authorization, Authentication, Accountability",
            "C) Accountability, Authentication, Authorization",
            "D) Authentication, Accountability, Authorization"
        ],
        "answer": 0, "explanation": "AAA = Authentication (who are you?) → Authorization (what can you do?) → Accountability (logging actions to prove it). Each builds on the previous."
    },
    {
        "id": 86, "domain": "Access Controls", "weight": "22%",
        "q": "What is 'Kerberos' used for in network authentication?",
        "options": [
            "A) Encrypting files at rest",
            "B) A ticket-based authentication protocol that uses symmetric cryptography to authenticate users without transmitting passwords over the network",
            "C) Firewall rule management",
            "D) Domain name resolution"
        ],
        "answer": 1, "explanation": "Kerberos = ticket-based authentication protocol (Windows Active Directory). Uses symmetric cryptography, avoids sending plaintext passwords. Tickets expire and are time-limited. KDC (Key Distribution Center) issues tickets."
    },
    {
        "id": 87, "domain": "Access Controls", "weight": "22%",
        "q": "What does RBAC (Role-Based Access Control) use to determine access rights?",
        "options": [
            "A) User's personal identity",
            "B) The job function/role assigned to a user within the organization",
            "C) The time of day",
            "D) The IP address of the user's device"
        ],
        "answer": 1, "explanation": "RBAC = access rights based on organizational roles (e.g., 'Accountant', 'HR Manager'). Permissions are assigned to roles, not individuals. Reduces administrative overhead vs. Discretionary Access Control (DAC)."
    },
    {
        "id": 88, "domain": "Access Controls", "weight": "22%",
        "q": "What is 'Multi-Factor Authentication' (MFA)?",
        "options": [
            "A) Using two different passwords",
            "B) Requiring two or more different types of verification factors (something you know, have, and/or are)",
            "C) Logging in from two different devices",
            "D) Two people approving the same action"
        ],
        "answer": 1, "explanation": "MFA requires 2+ factor types: Something you KNOW (password), Something you HAVE (token/smartphone), Something you ARE (biometric). Two passwords = not MFA. Authenticator apps and hardware tokens are common 'have' factors."
    },
    {
        "id": 89, "domain": "Access Controls", "weight": "22%",
        "q": "What is 'Least Privilege' also known as?",
        "options": [
            "A) Maximum privilege",
            "B) Need-to-Know / Need-to-Know principle",
            "C) Open access policy",
            "D) Default allow"
        ],
        "answer": 1, "explanation": "Least Privilege = users get only the minimum access needed. Closely related to Need-to-Know (restrict access to only what is required for a specific task/function). Both are fundamental access control principles."
    },
    {
        "id": 90, "domain": "Access Controls", "weight": "22%",
        "q": "What does 'Accountability' mean in access control?",
        "options": [
            "A) Users can access anything they want",
            "B) Users are responsible for their actions — logging and auditing enable traceability back to the individual",
            "C) The system automatically blocks unauthorized access",
            "D) All users share one account"
        ],
        "answer": 1, "explanation": "Accountability = ability to trace actions back to a specific person. Achieved through logs, audit trails, unique user IDs. Even with proper authorization, organizations need accountability to detect misuse. This is the final step in the AAA framework."
    },
    {
        "id": 91, "domain": "Network Security", "weight": "24%",
        "q": "What is an 'Advanced Persistent Threat' (APT)?",
        "options": [
            "A) A simple virus that spreads quickly",
            "B) A long-term, stealthy attack where an intruder maintains access to a network to steal data over an extended period",
            "C) A type of DDoS attack",
            "D) A phishing email"
        ],
        "answer": 1, "explanation": "APT = sophisticated, long-duration attack by well-funded threat actors (nation-states, criminal groups). Goal: maintain foothold, exfiltrate data slowly. Hard to detect because they use legitimate credentials and blend with normal traffic."
    },
    {
        "id": 92, "domain": "Network Security", "weight": "24%",
        "q": "What does a 'mantrap' (or mantrap portal) prevent in physical security?",
        "options": [
            "A) Unauthorized tailgating — a person follows an authorized person into a secured area without credentials",
            "B) DDoS attacks",
            "C) SQL injection",
            "D) Phishing attacks"
        ],
        "answer": 0, "explanation": "Mantrap = small space between two doors. One door closes before the next opens. Prevents tailgating/piggybacking (unauthorized person following authorized person in). Combined with badge readers and anti-tailgating measures."
    },
    {
        "id": 93, "domain": "Network Security", "weight": "24%",
        "q": "What is 'Deep Packet Inspection' (DPI)?",
        "options": [
            "A) Inspecting only packet headers",
            "B) Examining the full payload content of network packets to detect threats, protocols, or data within traffic",
            "C) Blocking all packets from a specific IP",
            "D) A type of firewall that only looks at the destination IP"
        ],
        "answer": 1, "explanation": "DPI = examines data payload (not just headers) of packets. Can detect application-layer threats, malware, data exfiltration. Used in advanced firewalls and IDS/IPS. Standard firewalls only check headers."
    },
    {
        "id": 94, "domain": "Network Security", "weight": "24%",
        "q": "What port does SSH use by default?",
        "options": [
            "A) 21",
            "B) 23",
            "C) 22",
            "D) 25"
        ],
        "answer": 2, "explanation": "SSH = port 22 (secure remote access, replaces Telnet port 23). FTP = 21. SMTP = 25. HTTPS = 443. HTTP = 80. Remember secure versions typically use +1 or +443 offset from insecure versions."
    },
    {
        "id": 95, "domain": "Network Security", "weight": "24%",
        "q": "What is a 'Security Zone' in network architecture?",
        "options": [
            "A) A physical fence",
            "B) A logical grouping of network devices and resources that share similar security requirements and trust levels",
            "C) A single server",
            "D) A type of encryption"
        ],
        "answer": 1, "explanation": "Security zones = logical divisions of a network with common security policies (e.g., internal zone, DMZ, guest zone). Devices in the same zone have similar trust levels. Zones are separated by firewalls. Zero Trust uses micro-segmentation for finer control."
    },
    {
        "id": 96, "domain": "Security Operations", "weight": "18%",
        "q": "What is 'Log Correlation' in security monitoring?",
        "options": [
            "A) Looking at a single log at a time",
            "B) Combining and analyzing events from multiple log sources to identify patterns that indicate an attack",
            "C) Deleting logs to save space",
            "D) Only storing logs from firewalls"
        ],
        "answer": 1, "explanation": "Log correlation = combining events from multiple sources (firewalls, servers, endpoints, apps) to build a complete picture of an attack. SIEM tools automate this. A single failed login might be normal; 50 failed logins across 10 systems in 2 minutes = suspicious."
    },
    {
        "id": 97, "domain": "Security Operations", "weight": "18%",
        "q": "What is the purpose of 'Security Awareness Training'?",
        "options": [
            "A) To meet compliance requirements only",
            "B) To educate employees about threats (phishing, social engineering) and their role in protecting the organization",
            "C) To test employees and punish failures",
            "D) Only required for IT staff"
        ],
        "answer": 1, "explanation": "Security awareness training = regular education for ALL employees (not just IT). Covers phishing, social engineering, password hygiene, data handling, incident reporting. Reduces risk from human error (still the #1 cause of breaches). Should include simulated phishing tests."
    },
    {
        "id": 98, "domain": "Security Operations", "weight": "18%",
        "q": "What does 'Configuration Management' ensure in security operations?",
        "options": [
            "A) That systems are always running",
            "B) That systems are configured according to approved security baselines and changes are documented and controlled",
            "C) That software is always up to date",
            "D) That passwords are changed weekly"
        ],
        "answer": 1, "explanation": "Configuration management = tracking and controlling system configurations over time. Ensures systems stay in a known, secure state. Changes must be documented, tested, and approved. Drift from baseline = risk. Tools like SCCM, Puppet, Ansible automate this."
    },
    {
        "id": 99, "domain": "Security Operations", "weight": "18%",
        "q": "What is the difference between a 'Symmetric' and 'Asymmetric' encryption algorithm?",
        "options": [
            "A) They are the same",
            "B) Symmetric uses one key for both encrypt/decrypt (faster); Asymmetric uses a key pair (public/private) — slower but enables digital signatures and key exchange",
            "C) Asymmetric is faster",
            "D) Symmetric is only used for hashing"
        ],
        "answer": 1, "explanation": "Symmetric = one secret key for both parties (AES, DES). Fast, but key exchange is hard. Asymmetric = key pair (RSA, ECC). Slower, but solves key distribution problem. Hybrid: asymmetric to exchange symmetric session key, then symmetric for bulk data."
    },
    {
        "id": 100, "domain": "Business Continuity & Disaster Recovery", "weight": "10%",
        "q": "What is the difference between a Business Continuity Plan (BCP) and a Disaster Recovery Plan (DRP)?",
        "options": [
            "A) They are the same",
            "B) BCP = keeping business operations running during a disruption (people, processes); DRP = restoring IT systems and infrastructure after a disaster",
            "C) DRP is more comprehensive",
            "D) BCP only covers physical assets"
        ],
        "answer": 1, "explanation": "BCP = overarching plan to keep the business running (all business functions, not just IT). DRP = focused on recovering IT systems, data, and infrastructure after a disaster. BCP is strategic; DRP is tactical/technical. Both should be tested regularly."
    }
]

DOMAINS = {
    "Security Principles":          {"weight": "26%", "count": 8},
    "Access Controls":             {"weight": "22%", "count": 6},
    "Network Security":             {"weight": "24%", "count": 9},
    "Security Operations":          {"weight": "18%", "count": 5},
    "Business Continuity & DR":    {"weight": "10%", "count": 4},
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
║              Exam Domain Outline (Effective Oct 2025)        ║
╠══════════════════════════════════════════════════════════════╣
║ Domain 1: Security Principles                    — 26%       ║
║ Domain 2: Access Controls Concepts              — 22%       ║
║ Domain 3: Network Security                      — 24%       ║
║ Domain 4: Security Operations                    — 18%       ║
║ Domain 5: BC/DR & Incident Response Concepts    — 10%       ║
╠══════════════════════════════════════════════════════════════╣
║ Total: 100 questions | 2 hours | Passing: 700/1000 (CAT)   ║
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