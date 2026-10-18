# 🛡️ UNG Seangeang (Eang) — Cybersecurity Portfolio

![Cybersecurity](https://img.shields.io/badge/Focus-Cybersecurity%20%26%20Network%20Defense-0A66C2?style=for-the-badge)
![Linux](https://img.shields.io/badge/Linux-Kali%20%7C%20Ubuntu%20%7C%20Bash-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![Python](https://img.shields.io/badge/Python-Security%20Automation%20%26%20NLP-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/B.S.%20Cybersecurity-AUPP%20(Year%203)-2EA44F?style=for-the-badge)

Welcome to my technical cybersecurity portfolio. I am a third-year **B.S. in Cybersecurity** student at the **American University of Phnom Penh (AUPP)** and a STEM/Robotics educator, focused on defensive security operations, network vulnerability assessment, and security automation for the **banking and fintech** sectors.

This repository houses hands-on security labs, automated remediation scripts, vulnerability assessments, and governance reports demonstrating practical defensive engineering.

---

## 🔧 Technical Skills & Tooling

| Domain | Tools, Technologies & Frameworks |
| :--- | :--- |
| **Operating Systems & Virtualization** | Kali Linux, Ubuntu/Debian, Windows 11, Oracle VirtualBox, VMware |
| **Network & Vulnerability Assessment** | Nmap, Shodan, OWASP Juice Shop, Wireshark, `dsniff`, TCP/IP Analysis |
| **Scripting & Programming** | Bash Scripting, Python, SQL, Java, JavaScript / Google Apps Script |
| **Security Frameworks & Governance** | Principle of Least Privilege (PoLP), NIST CSF, OWASP Top 10, Access Control (RBAC/DAC) |
| **Data, Cloud & Applied AI** | Cloud Computing Architecture, NLP (`scikit-learn`, NLTK, CRF), Biometric Anti-Spoofing |

---

## 📂 Featured Security Projects & Lab Artifacts

### 1. Linux File System Auditing & Automated Hardening
* **Directory:** [`./01-linux-and-bash-security/file-permissions-audit/`](./01-linux-and-bash-security/file-permissions-audit/)
* **Overview:** Conducted a least-privilege permission audit on a multi-user Linux research environment using `ls -la`, `stat`, and `chmod`.
* **Key Deliverable:** Built [`remediate_permissions.sh`](./01-linux-and-bash-security/file-permissions-audit/remediate_permissions.sh) to automatically detect world-writable files, lock down archived hidden files (`.project_x.txt`), and restrict unauthorized directory traversal (`drafts/`).

### 2. OWASP Juice Shop Network Reconnaissance & Vulnerability Evaluation
* **Directory:** [`./02-network-and-vulnerability-analysis/owasp-juice-shop-assessment/`](./02-network-and-vulnerability-analysis/owasp-juice-shop-assessment/)
* **Overview:** Deployed an isolated local virtual lab hosting OWASP Juice Shop to perform active network scanning, service enumeration, and web application vulnerability analysis.
* **Key Deliverable:** Structured technical findings report mapping discovered exposures to actionable remediation controls.

### 3. Security Governance, Risk & Compliance (GRC) Artifacts
* **Directory:** [`./03-security-audits-and-governance/`](./03-security-audits-and-governance/)
* **Overview:** Security posture evaluations, control audits, and incident documentation developed as part of the **Google Cybersecurity Professional Certificate**.

### 4. Applied AI & Biometric Security Projects
* **Directory:** [`./05-applied-ai-and-appsec-projects/`](./05-applied-ai-and-appsec-projects/)
* **Highlights:**
  * **Face Recognition Attendance System with Anti-Spoofing:** Implemented `MobileFaceNet` alongside `AntiSpoofNet` to mitigate presentation attacks and unauthorized identity spoofing.
  * **Khmer Sentiment Analysis (NLP):** Designed machine learning pipelines and sequence-labeling models for low-resource language processing.

---

## 🚀 Quick Start: Running the Linux Remediation Demo

You can test the automated Linux file permissions hardening script directly in any Linux environment or GitHub Codespace:

```bash
git clone [https://github.com/UNG-Seangeang/Cybersecurity_portfolio.git](https://github.com/UNG-Seangeang/Cybersecurity_portfolio.git)
cd Cybersecurity_portfolio/01-linux-and-bash-security/file-permissions-audit
chmod +x remediate_permissions.sh
./remediate_permissions.sh --setup-demo
