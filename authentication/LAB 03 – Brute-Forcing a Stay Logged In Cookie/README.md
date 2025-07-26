 LAB 03 – Brute-Forcing a Stay Logged In Cookie

This lab demonstrates how insecure implementation of "stay logged in" cookies can lead to account takeover via brute-forcing. The cookie stores a Base64-encoded value that combines a username and an MD5-hashed password. By using Burp Intruder, we brute-force Carlos's password and forge a valid cookie to access his account.

## 🎯 Objective

Brute-force Carlos's "stay logged in" cookie to gain access to his account page.

## 🧪 Lab Setup

- Web application vulnerable to weak cookie handling
- Burp Suite (Intruder, Decoder, and Grep Match features)
- List of candidate passwords

## Tools
- Burpsuite
- Browser (Chromium)
