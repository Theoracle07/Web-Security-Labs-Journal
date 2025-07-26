# 🔒 Lab 04 – Offline Password Cracking

---

## 📘 Lab Overview

This lab demonstrates how weakly secured cookies can lead to offline password cracking and account takeover. The challenge combines two vulnerabilities: insecure cookie design and stored XSS. Your goal is to steal Carlos’s stay-logged-in cookie, crack his password hash offline, and use it to log in and delete his account.

---

## 🧠 Learning Objectives

- Understand the security risks of encoding sensitive user data in cookies.
- Use XSS to extract cookies from vulnerable users.
- Perform offline hash cracking using public sources.
- Apply Burp Suite for decoding and manipulation.

---

## 🚨 Vulnerabilities Exploited

| Type                  | Impact                              |
|-----------------------|-------------------------------------|
| Stored XSS            | Cookie theft / data exfiltration    |
| Weak Cookie Protection| Offline password cracking / ATO     |

---

## 🎯 Target Outcome

✅ Obtain Carlos’s `stay-logged-in` cookie  
✅ Crack the password hash offline  
✅ Log in as Carlos and delete his account  
