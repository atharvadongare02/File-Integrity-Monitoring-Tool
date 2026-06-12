# 🛡️ File Integrity Monitoring Tool (SHA-256)

> Detect unauthorized file changes instantly using cryptographic hashing.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge)
![Security](https://img.shields.io/badge/Cybersecurity-File%20Integrity-red?style=for-the-badge)
![Hashing](https://img.shields.io/badge/SHA--256-Integrity%20Verification-green?style=for-the-badge)

---

## 📖 Overview

The **File Integrity Monitoring (FIM) Tool** is a Python-based cybersecurity utility that helps detect unauthorized modifications, deletions, or tampering of files by leveraging the **SHA-256 cryptographic hashing algorithm**.

Every file has a unique digital fingerprint known as a **hash value**. Even a single-character change in a file generates a completely different hash. This tool creates a trusted baseline of file hashes and continuously compares current file states against that baseline to verify integrity.

Think of it as a digital security guard for your files. 🔐

---

## ✨ Features

✅ Generate secure **SHA-256 hashes** for files

✅ Create a trusted **baseline database**

✅ Detect **file modifications**

✅ Detect **file deletions**

✅ Lightweight and easy to use

✅ No external dependencies required

✅ Ideal for learning cybersecurity fundamentals

---

## 🏗️ How It Works

### Step 1: Create a Baseline

The tool calculates the SHA-256 hash of selected files and stores them in a JSON database.

```text
sample.txt
↓
SHA-256 Hash
↓
Stored in hash_database.json
```

---

### Step 2: Monitor Integrity

When monitoring is executed:

* Current file hashes are recalculated
* Stored hashes are loaded
* Both values are compared

```text
Stored Hash
      vs
Current Hash
```

---

### Step 3: Detect Changes

| Condition    | Result           |
| ------------ | ---------------- |
| Hash Matches | ✅ File Intact    |
| Hash Changed | ⚠️ File Modified |
| File Missing | 🚨 File Deleted  |

---

## 🛠️ Technologies Used

* **Python 3**
* **hashlib** – SHA-256 hash generation
* **json** – Baseline storage
* **os** – File system operations

---

## 📂 Project Structure

```text
File-Integrity-Monitor/
│
├── file_integrity_monitor.py
├── hash_database.json
├── sample.txt
└── README.md
```

---

## 🚀 Example Output

### Baseline Creation

```text
[+] Baseline created for: sample.txt
Baseline hash database saved.
```

### No Changes Detected

```text
[OK] No changes: sample.txt
```

### File Modified

```text
[WARNING] File modified: sample.txt
```

### File Deleted

```text
[!] File deleted: sample.txt
```

---

## 🔒 Cybersecurity Relevance

File Integrity Monitoring is a fundamental security control used in:

* Security Operations Centers (SOC)
* Intrusion Detection Systems (IDS)
* Digital Forensics
* Malware Analysis
* Compliance Monitoring
* Enterprise Security Auditing

Many industry-grade solutions rely on the same core concept of **cryptographic hash verification** to identify unauthorized changes.

---

## 🎯 Learning Outcomes

Through this project, I gained practical experience with:

* Cryptographic hashing concepts
* SHA-256 implementation
* File integrity verification
* Python file handling
* JSON data management
* Basic cybersecurity monitoring techniques
