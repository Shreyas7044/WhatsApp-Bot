# WhatsApp Bot 🤖📱

This project demonstrates how to build a WhatsApp chatbot using Python, Flask, and Twilio’s WhatsApp API.  
The bot accepts learning-related queries from users and responds with the most relevant GeeksforGeeks articles.

---

## 🚀 Features
- WhatsApp-based chatbot
- Uses Twilio WhatsApp Sandbox
- Flask backend
- Google Search integration
- Returns learning resources automatically

---

## 🧰 System Requirements
- Python 3.9 or newer
- Twilio Account
- WhatsApp installed on mobile
- Internet connection

---

## 🔑 Technologies Used
- Python
- Flask
- Twilio WhatsApp API
- Ngrok
- Google Search API (googlesearch-python)

---

## 🪜 Step-by-Step Setup Guide

### Step 1: Create Twilio Account
1. Visit Twilio official website
2. Sign up and verify email & phone number
3. Go to **Develop → Messaging → Try it out → Send a WhatsApp message**
4. Activate the WhatsApp Sandbox

---

### Step 2: Join WhatsApp Sandbox
- Send the secret sandbox code to: +141555558886

---

### Step 3: Project Setup
Install dependencies: pip install twilio flask requests googlesearch-python

---

### Step 4: Run the Flask App
python3 main.py

---

### Step 5: Expose Local Server using Ngrok
ngrok http 5000

---

### Step 6: Configure Twilio Webhook
- Go to Twilio Console → WhatsApp Sandbox.
- Paste ngrok HTTPS URL in WHEN A MESSAGE COMES IN.
- Append /
- Set method to POST.
- Save changes.

---

## 📸 Screenshot
![Application Screenshot]()

---

## 📌 Future Enhancements
- NLP-based intent detection
- Multiple domain filtering
- Database integration
- Deployment on cloud
