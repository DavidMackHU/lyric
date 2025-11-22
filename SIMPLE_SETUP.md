# ⚡ Super Simple Setup - 3 Easy Steps!

## 🎯 The Easiest Way

### Step 1: Copy Template (30 seconds)

**Windows:**
```powershell
Copy-Item .env.production.template .env.production
```

**Mac/Linux:**
```bash
cp .env.production.template .env.production
```

### Step 2: Fill in Values (2 minutes)

Open `.env.production` and replace:
- `your_firebase_api_key_here` → Your Firebase API key
- `your-project-id` → Your Firebase project ID  
- `https://lyriq-backend.onrender.com` → Your Render URL

**Get Firebase values:**
1. Go to: https://console.firebase.google.com
2. Project Settings → Your apps → Web app
3. Copy the values shown

### Step 3: Done! ✅

That's it! Now you can build:
```bash
npm run build
```

---

## 🚀 Even Faster: Use Interactive Script

**Windows:**
```powershell
.\scripts\setup-env.ps1
```

**Mac/Linux:**
```bash
npm run setup-env
```

The script asks you questions and creates the file automatically!

---

## 📋 For Backend (Render)

Still need to add variables in Render, but it's just copy-paste:

1. Go to: https://dashboard.render.com
2. Your service → Environment tab
3. Copy-paste these values (get DB values from your database):

```
SECRET_KEY=I(s,E/Vv.v)6BVW)f]NQfM)R-&aiB=90W;tO}}^tGkCU=(v>mA
DEBUG=False
ALLOWED_HOSTS=lyriq-backend.onrender.com
DB_NAME=lyriq_db
DB_USER=lyriq_user
DB_PASSWORD=[from database]
DB_HOST=[from database]
DB_PORT=5432
CORS_ALLOWED_ORIGINS=https://your-project.web.app
FIREBASE_CREDENTIALS_PATH=/opt/render/project/src/firebase-credentials.json
```

---

## 💡 That's It!

**Frontend**: Copy template → Fill in → Done!  
**Backend**: Copy-paste values in Render → Done!

**Total time: 5 minutes** instead of 20! 🎉


