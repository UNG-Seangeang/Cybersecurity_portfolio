# 🛡️ UNG Seangeang (Eang) — Cybersecurity Portfolio

![Cybersecurity](https://img.shields.io/badge/Focus-Cybersecurity%20%26%20Network%20Defense-0A66C2?style=for-the-badge)
![Linux](https://img.shields.io/badge/Linux-Kali%20%7C%20Ubuntu%20%7C%20Bash-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![Python](https://img.shields.io/badge/Python-Security%20Automation%20%26%20NLP-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Education](https://img.shields.io/badge/B.S.%20Cybersecurity-AUPP%20(Year%203)-2EA44F?style=for-the-badge)

Welcome to my technical cybersecurity portfolio. I am a third-year **B.S. in Cybersecurity** student at the **American University of Phnom Penh (AUPP)** and a STEM/Robotics educator, focusing on defensive security operations, network vulnerability assessment, and security automation for the **banking and fintech** sectors in Cambodia.

---

## 📂 Portfolio Directory Index

| # | Module / Folder | Core Focus & Deliverables | Key Tools & Frameworks |
| :--- | :--- | :--- | :--- |
| **01** | [`01-professional-statement`](./01-professional-statement/) | Cybersecurity career philosophy, ethical commitment, and banking/fintech security focus | Professional Identity, Ethics |
| **02** | [`02-security-audit`](./02-security-audit/) | Internal security control audit and compliance posture evaluation | NIST CSF, CIS Controls, PoLP |
| **03** | [`03-network-analysis`](./03-network-analysis/) | Packet inspection, network traffic analysis, and anomaly investigation | Wireshark, `tcpdump`, `dsniff`, TCP/IP |
| **04** | [`04-linux-permissions`](./04-linux-permissions/) | File system authorization audit and automated Bash remediation script (`remediate_permissions.sh`) | Linux CLI, `ls -la`, `chmod`, `stat`, Bash |
| **05** | [`05-sql-analysis`](./05-sql-analysis/) | Querying security databases to audit login attempts, user privileges, and endpoint filters | SQL, MariaDB/MySQL, Log Filtering |
| **06** | [`06-vulnerability-assessment`](./06-vulnerability-assessment/) | Active network reconnaissance, OWASP Juice Shop evaluation, and risk remediation report | Nmap, OWASP Top 10, VirtualBox, Kali |
| **07** | [`07-incident-response`](./07-incident-response/) | Incident handler's journal, alert triage, containment, and recovery documentation | NIST Incident Response Lifecycle, SIEM |
| **08** | [`08-python-log-analysis`](./08-python-log-analysis/) | Python scripts for parsing authentication logs and automating IP allow/deny lists | Python, Regex, File I/O Automation |
| **09** | [`09-resume`](./09-resume/) | Updated curriculum vitae highlighting cybersecurity coursework, labs, and STEM teaching | CV / Resume |
| **10** | [`10-certificate`](./10-certificate/) | Verified industry certificates and academic credentials | Google Cybersecurity, Cisco, Great Learning |

---

## 🔧 Technical Skills Summary

* **Operating Systems & Virtualization:** Kali Linux, Ubuntu/Debian, Windows 11, Oracle VirtualBox, VMware
* **Network & Vulnerability Assessment:** Nmap, OWASP Juice Shop, Wireshark, Shodan, `dsniff`, Firewall Rule Configuration
* **Scripting & Development:** Bash, Python, SQL, Java, HTML5/CSS3/JS, Google Apps Script
* **Applied AI & Security Engineering:** Biometric Anti-Spoofing (`MobileFaceNet` + `AntiSpoofNet`), Khmer NLP Sentiment Analysis (`scikit-learn`, NLTK, CRF)

---

## 🚀 Quick Start: Linux Permissions Remediation Demo (`04-linux-permissions`)

You can test my automated Linux file permissions hardening script directly in any Linux terminal or GitHub Codespace:

```bash
git clone [https://github.com/UNG-Seangeang/Cybersecurity_portfolio.git](https://github.com/UNG-Seangeang/Cybersecurity_portfolio.git)
cd Cybersecurity_portfolio/04-linux-permissions
chmod +x remediate_permissions.sh
./remediate_permissions.sh --setup-demo
