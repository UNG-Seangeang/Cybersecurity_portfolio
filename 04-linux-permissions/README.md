# Linux File Permissions Audit & Remediation

![OS](https://img.shields.io/badge/OS-Linux-FCC624?style=flat-square&logo=linux&logoColor=black)
![Shell](https://img.shields.io/badge/Shell-Bash-4EAA25?style=flat-square&logo=gnu-bash&logoColor=white)
![Security Principle](https://img.shields.io/badge/Principle-Least_Privilege-0A66C2?style=flat-square)
![Focus](https://img.shields.io/badge/Focus-Access_Control_%26_Authorization-critical?style=flat-square)

## Overview & Project Description

As a security professional supporting the research team at a large organization, I am responsible for auditing file system permissions and enforcing the **principle of least privilege (PoLP)**. In this project, I inspected the `/home/researcher2/projects` directory using Linux command-line utilities to verify whether existing user, group, and other access permissions aligned with organizational security policies. Where unauthorized access existed across regular files, hidden archived files, and subdirectories, I used the `chmod` command to restrict permissions and protect sensitive research data.

---

## Table of Contents

1. [Scenario & Security Requirements](#scenario--security-requirements)
2. [Step 1: Check File and Directory Details](#step-1-check-file-and-directory-details)
3. [Step 2: Describe the Permissions String](#step-2-describe-the-permissions-string)
4. [Step 3: Change File Permissions (Regular File)](#step-3-change-file-permissions-regular-file)
5. [Step 4: Change File Permissions on a Hidden File](#step-4-change-file-permissions-on-a-hidden-file)
6. [Step 5: Change Directory Permissions](#step-5-change-directory-permissions)
7. [Remediation Summary Matrix](#remediation-summary-matrix)
8. [Conclusion & Key Takeaways](#conclusion--key-takeaways)

---

## Scenario & Security Requirements

The organization's research team stores active and archived research documents inside `/home/researcher2/projects`, owned by the user `researcher2` and assigned to the `research_team` group. An internal security review requires the directory to comply with three strict authorization policies:

1. **No Public Write Access:** System users outside the user and group (`other`) must **never** have write (`w`) access to any files.
2. **Archived Hidden Files Read-Only:** The hidden archive file `.project_x.txt` must not have write (`w`) permissions for anyone, while granting read (`r`) permissions to both the user (`researcher2`) and the group (`research_team`).
3. **Private Drafts Directory:** Only the owner (`researcher2`) is permitted to access the `drafts` subdirectory and its contents; group and other users must have zero permissions.

---

## Step 1: Check File and Directory Details

To begin the audit, I listed all files and directories within `/home/researcher2/projects`, including hidden items and their current permission strings.

### Command Executed
```bash
researcher2@linux:~/projects$ ls -la
```

### Terminal Output
```text
drwxr-xr-x 3 researcher2 research_team 4096 Oct 18 14:10 .
drwxr-xr-x 5 researcher2 research_team 4096 Oct 18 14:10 ..
drwx--x--- 2 researcher2 research_team 4096 Oct 18 14:10 drafts
-rw--w---- 1 researcher2 research_team   46 Oct 18 14:10 .project_x.txt
-rw-rw-rw- 1 researcher2 research_team   46 Oct 18 14:10 project_k.txt
-rw-r----- 1 researcher2 research_team   46 Oct 18 14:10 project_m.txt
-rw-rw-r-- 1 researcher2 research_team   46 Oct 18 14:10 project_r.txt
-rw-rw-r-- 1 researcher2 research_team   46 Oct 18 14:10 project_t.txt
```

### Technical Explanation
* **`ls`:** Lists the contents of the current working directory.
* **`-l` (Long listing format):** Outputs detailed metadata for every entry, including the 10-character permissions string, number of hard links, owner (`researcher2`), group (`research_team`), size in bytes, last modification timestamp, and filename.
* **`-a` (All files):** Displays hidden files and directories whose names begin with a leading period (`.`), such as `.project_x.txt`. Without the `-a` flag, hidden files remain invisible during standard directory listings.

---

## Step 2: Describe the Permissions String

To demonstrate how Linux permissions are structured, below is a breakdown of the 10-character permissions string for `project_t.txt` (`-rw-rw-r--`):

```text
 -   r w -   r w -   r - -
[1] [2 3 4] [5 6 7] [8 9 10]
 │     │       │       └─── Other permissions (read-only)
 │     │       └─────────── Group permissions (read & write)
 │     └─────────────────── User/Owner permissions (read & write)
 └───────────────────────── File type (- = regular file, d = directory)
```

| Position | Characters | Category | Meaning in `-rw-rw-r--` |
| :--- | :---: | :--- | :--- |
| **1st character** | `-` | **File Type** | A hyphen (`-`) indicates a standard file, whereas `d` indicates a directory (e.g., `drafts`). |
| **2nd–4th characters** | `rw-` | **User (`u`)** | The file owner (`researcher2`) has read (`r`) and write (`w`) permissions, but not execute (`-`). |
| **5th–7th characters** | `rw-` | **Group (`g`)** | Members of `research_team` have read (`r`) and write (`w`) permissions, but not execute (`-`). |
| **8th–10th characters** | `r--` | **Other (`o`)** | All other system accounts have read-only (`r`) access; write and execute permissions are denied (`--`). |

---

## Step 3: Change File Permissions (Regular File)

### Policy Violation Identified
* **Target File:** `project_k.txt`
* **Initial Permissions:** `-rw-rw-rw-`
* **Issue:** The 9th character is `w`, granting **other** users unauthorized write permissions to modify or overwrite the file.

### Remediation Command & Verification
```bash
researcher2@linux:~/projects$ chmod o-w project_k.txt
researcher2@linux:~/projects$ ls -l project_k.txt
-rw-rw-r-- 1 researcher2 research_team 46 Oct 18 14:10 project_k.txt
```

### Technical Explanation
Using symbolic mode with `chmod`, specifying `o-w` removes (`-`) the write (`w`) permission from the **other** (`o`) category on `project_k.txt`. Verifying with `ls -l` confirms the updated permission string is `-rw-rw-r--` (octal equivalent: `664`).

---

## Step 4: Change File Permissions on a Hidden File

### Policy Violation Identified
* **Target File:** `.project_x.txt` (identified as a hidden file due to the leading `.` in its filename)
* **Initial Permissions:** `-rw--w----`
* **Issue:** Because `.project_x.txt` is an archived file, no user should have write access to alter it, and both the owner and group require read access. Initially, the user had write access (`rw-`) and the group had write-only access (`-w-`).

### Remediation Command & Verification
```bash
researcher2@linux:~/projects$ chmod u-w,g-w,g+r .project_x.txt
researcher2@linux:~/projects$ ls -la .project_x.txt
-r--r----- 1 researcher2 research_team 46 Oct 18 14:10 .project_x.txt
```
*(Alternative symbolic command: `chmod u=r,g=r .project_x.txt` | Octal equivalent: `chmod 440 .project_x.txt`)*

### Technical Explanation
Passing `u-w,g-w,g+r` to `chmod` revokes write permissions from both the user (`u-w`) and the group (`g-w`), while granting read permissions to the group (`g+r`). Checking the file with `ls -la` confirms the permissions are now `-r--r-----`, ensuring the archived file is strictly read-only for authorized team members.

---

## Step 5: Change Directory Permissions

### Policy Violation Identified
* **Target Directory:** `drafts`
* **Initial Permissions:** `drwx--x---`
* **Issue:** Only `researcher2` is authorized to access the `drafts` directory. However, the 7th character is `x`, granting the `research_team` group execute permission on the directory (which allows group members to `cd` into the directory and access known filenames inside).

### Remediation Command & Verification
```bash
researcher2@linux:~/projects$ chmod g-x drafts
researcher2@linux:~/projects$ ls -ld drafts
drwx------ 2 researcher2 research_team 4096 Oct 18 14:10 drafts
```

### Technical Explanation
Running `chmod g-x drafts` removes (`-`) the execute (`x`) permission from the **group** (`g`). Verifying the directory metadata with `ls -ld drafts` confirms the permissions string is now `drwx------` (octal equivalent: `700`), restricting access exclusively to `researcher2`.

---

## Remediation Summary Matrix

| File / Directory | Type | Initial Permissions | Vulnerability / Violation | Command Executed | Final Permissions |
| :--- | :--- | :---: | :--- | :--- | :---: |
| `project_k.txt` | Regular File | `-rw-rw-rw-` | World-writable (`other` had `w`) | `chmod o-w project_k.txt` | `-rw-rw-r--` |
| `.project_x.txt` | Hidden File | `-rw--w----` | User/Group had `w`; Group lacked `r` | `chmod u-w,g-w,g+r .project_x.txt` | `-r--r-----` |
| `drafts` | Directory | `drwx--x---` | Group had directory traversal (`x`) | `chmod g-x drafts` | `drwx------` |

---

## Conclusion & Key Takeaways

In this project, I audited and remediated file and directory permissions in `/home/researcher2/projects` to bring the research team's environment into full compliance with organizational security policies. By using `ls -la`, I inspected both standard and hidden items to uncover overly permissive access on `project_k.txt`, `.project_x.txt`, and the `drafts` subdirectory. I then applied `chmod` commands to revoke unauthorized write and directory execution privileges, enforcing the principle of least privilege and protecting the confidentiality and integrity of the research team's data.

### Core Skills Demonstrated
* Auditing Linux file systems using `ls -la` and `ls -ld` to inspect regular files, hidden files, and directories.
* Interpreting 10-character Linux permission strings across user (`u`), group (`g`), and other (`o`) access tiers.
* Enforcing the principle of least privilege (PoLP) and remediating unauthorized access using `chmod` in symbolic mode.
