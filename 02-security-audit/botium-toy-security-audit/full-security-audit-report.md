# 🛡️ Botium Toys Security Audit Report

## 📌 Overview

This project presents a cybersecurity audit of **Botium Toys**, focusing on evaluating its security controls, identifying risks, and assessing compliance with industry standards. The goal is to improve the organization’s overall security posture.

---

## 🎯 Scope & Objectives

### Scope

The audit covers:

* All organizational assets
* Internal systems and networks
* Security controls and processes
* Compliance with relevant standards

### Objectives

* Identify and classify assets
* Evaluate existing controls
* Assess compliance gaps
* Recommend improvements

---

## 🧾 Asset Summary

Botium Toys manages the following assets:

* On-premises IT infrastructure
* Employee devices (laptops, smartphones, peripherals)
* Retail inventory (storefront & warehouse)
* Business systems (e-commerce, accounting, database, etc.)
* Internal network and internet access
* Data storage and retention systems
* Legacy systems requiring manual monitoring

---

## ⚠️ Risk Assessment

* **Risk Score:** 8/10 (High Risk)
* **Main Issue:** Lack of proper controls and asset management

### Key Risks

* Excessive user access to sensitive data
* No encryption for credit card information
* Weak password policies
* No disaster recovery or backup system
* Missing intrusion detection system (IDS)
* Poor legacy system maintenance

---

## 🔐 Controls Assessment

### ✅ Implemented Controls

* Firewall
* Antivirus software
* Manual monitoring of legacy systems
* Password policies *(weak)*
* Physical security:

  * Locks
  * CCTV surveillance
  * Fire detection/prevention systems

### ❌ Missing / Weak Controls

* Least privilege access control
* Encryption for sensitive data
* Centralized password management system
* Reliable backups and disaster recovery plan
* Intrusion Detection System (IDS) *(not implemented effectively)*

---

## 📋 Compliance Assessment

### 💳 PCI DSS

* ❌ Restricted access to cardholder data
* ❌ Encryption of payment data *(missing in practice)*
* ⚠️ Weak password policies
* ⚠️ Partially secure environment

👉 **Status: Partially Compliant (High Risk)**

---

### 🌍 GDPR

* ❌ Data privacy not fully ensured
* ✅ Breach notification (within 72 hours)
* ✅ Data classification practices
* ✅ Privacy policies enforced

👉 **Status: Moderately Compliant**

---

### 🛡️ SOC (Type 1 & 2)

* ❌ Weak access control policies
* ❌ Data confidentiality gaps
* ✅ Data integrity maintained
* ✅ Data availability ensured

👉 **Status: Partially Compliant**

---

## 🚨 Key Findings

* Critical security gaps exist in **access control and encryption**
* Several controls are **present but ineffective**
* Compliance requirements are **not fully met**
* Organization is vulnerable to:

  * Data breaches
  * Financial penalties
  * Operational disruptions

---

## 💡 Recommendations

### 🔐 High Priority

* Implement **encryption** for sensitive data
* Enforce **least privilege access control**
* Strengthen **password policies** and deploy centralized password management

### 🛠️ Medium Priority

* Deploy and configure **Intrusion Detection System (IDS)**
* Establish **regular backups and disaster recovery plan**
* Improve **legacy system maintenance schedule**

### 📊 Compliance Improvements

* Align fully with **PCI DSS requirements**
* Strengthen **GDPR data protection measures**
* Improve **SOC compliance (confidentiality & access control)**

---

## 🧠 Conclusion

Botium Toys currently operates with **high security risk (8/10)** due to missing and weak controls. Immediate action is required to:

* Protect sensitive data
* Ensure regulatory compliance
* Strengthen overall cybersecurity posture

---
