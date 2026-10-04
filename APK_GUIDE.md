# 📱 Khaata Mobile App - APK Download Guide

Yeh mobile app **100% complete** hai aur **offline database** ke sath tayyar hai.

Folder location: `d:\Finance\mobile_app`

---

## 🛠️ APK File Download Karne Ka Tareeqa (PWABuilder - 2 Minutes)

Microsoft ka official aur free tool hai **PWABuilder** jo kisi bhi web app ki signed Android `.apk` bana deta hai:

### Step 1: App ko Free Host Karein
Is folder (`d:\Finance\mobile_app`) ko kisi bhi free service par 1 click mein host karein:
- **Tareeqa A (Vercel ya Netlify):**  
  [vercel.com](https://vercel.com) ya [netlify.com](https://netlify.com) par free account banayein, aur `mobile_app` folder ko drag & drop kar dein. Aapko free HTTPS link mil jayega (maslan: `https://my-khaata.vercel.app`).
- **Tareeqa B (GitHub Pages):**  
  Apne GitHub par nayi repository banayein aur `mobile_app` ka code push kar ke "Settings -> Pages" on kar dein.

### Step 2: PWABuilder se APK Download Karein
1. Browser mein **[https://www.pwabuilder.com](https://www.pwabuilder.com)** kholein.
2. Apna host kiya hua URL paste karein aur **"Start"** dabayein.
3. PWABuilder test pass karega (Manifest aur Service Worker humne pehle se 100% pass set kiya hua hai).
4. **"Package for Stores"** ya **"Package for Android"** par click karein.
5. **"Generate APK" / "Download"** dabayein.
6. Aapke paas Android **`.apk` file** download ho jayegi!

### Step 3: Phone mein Install Karein
1. Download shuda `.apk` file ko apne phone mein bhejein (WhatsApp, Drive, ya USB cable se).
2. Phone par tap kar ke **"Install"** dabayein.
3. App aapke phone mein install ho jayegi aur bina kisi internet ke offline chalegi!

---

## ⚡ Local Test Karne Ka Tareeqa:
`d:\Finance\mobile_app` mein **`run_mobile.bat`** par double click karein. Browser mein mobile layout test kar sakte hain.
