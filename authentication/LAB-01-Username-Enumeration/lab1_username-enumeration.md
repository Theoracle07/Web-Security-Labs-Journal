 🔐 Lab 1: Username Enumeration via Response Differences

This lab explores a vulnerability where login responses reveal clues about valid usernames, enabling both enumeration and brute-force attacks.

---

 ⚙️ Objective
Identify a valid username by analyzing server responses, then brute-force the associated password to gain access to the user account.

---

## 🧰 Tools Used
- Burp Suite (Proxy & Intruder modules)
- Web browser (Microsoft Edge)

---

 📚 Steps Followed

1. Accessed the vulnerable login page.
2. Intercepted the login request in Burp Proxy with invalid credentials.
3. Sent the `username` parameter to Burp Intruder for enumeration.
4. Used Sniper attack type with a list of usernames.
5. Noted variation in response messages—some said `Invalid username`, while one said `Incorrect password`.
6. Extracted the identified valid username from Intruder results.
7. Reconfigured Intruder for password brute-force using that username.
8. Found the correct password by spotting the response with status `302`.
9. Logged in successfully and accessed the user account page.

---

 📝 Observations

- Error messages provided differential responses, which exposed the presence of valid usernames.
- HTTP status code `302` is a strong indicator of successful login during brute-force attempts.
- Enumeration + targeted brute-force is more efficient than a full cluster bomb attack.

---

 📸 Screenshots

_All relevant screenshots captured during the lab are available in this folder._  
👉 ![Lab 01 Screenshot](authentication/LAB-01-Username-Enumeration/screenshots.png)

---

## ✅ Lab Status: Completed

