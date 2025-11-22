# 🎯 Easier Environment Variables Setup

## Option 1: Use the Template (Easiest!)

### Step 1: Copy the Template
```bash
# Windows PowerShell
Copy-Item .env.production.template .env.production

# Mac/Linux
cp .env.production.template .env.production
```

### Step 2: Fill in the Values
Open `.env.production` in any text editor and replace:
- `your_firebase_api_key_here` → Your actual Firebase API key
- `your-project-id` → Your Firebase project ID
- `https://lyriq-backend.onrender.com` → Your actual Render backend URL

**That's it!** ✅

---

## Option 2: Use the Interactive Script

### Windows (PowerShell)
```powershell
.\scripts\setup-env.ps1
```

### Mac/Linux/Windows (Node.js)
```bash
node scripts/setup-env.js
```

The script will **ask you questions** and create the file automatically!

---

## Option 3: Copy-Paste Method (Fastest)

### For Frontend (.env.production)

1. **Get Firebase values** (one-time):
   - Go to: https://console.firebase.google.com
   - Project Settings → Your apps → Web app
   - Copy the config values

2. **Create `.env.production`** and paste this:

```env
VITE_FIREBASE_API_KEY=PASTE_YOUR_API_KEY
VITE_FIREBASE_AUTH_DOMAIN=PASTE_YOUR_AUTH_DOMAIN
VITE_FIREBASE_PROJECT_ID=PASTE_YOUR_PROJECT_ID
VITE_FIREBASE_STORAGE_BUCKET=PASTE_YOUR_STORAGE_BUCKET
VITE_FIREBASE_MESSAGING_SENDER_ID=PASTE_YOUR_SENDER_ID
VITE_FIREBASE_APP_ID=PASTE_YOUR_APP_ID
VITE_API_BASE_URL=https://lyriq-backend.onrender.com/api
```

3. **Replace the PASTE_YOUR_* parts** with actual values

---

## For Backend (Render) - Still Manual (But Simple!)

Render doesn't support scripts, but it's easy:

1. Go to: https://dashboard.render.com
2. Your service → **Environment** tab
3. Click **"Add Environment Variable"**
4. Copy-paste these **one at a time**:

```
SECRET_KEY = I(s,E/Vv.v)6BVW)f]NQfM)R-&aiB=90W;tO}}^tGkCU=(v>mA
DEBUG = False
ALLOWED_HOSTS = lyriq-backend.onrender.com
DB_NAME = lyriq_db
DB_USER = lyriq_user
DB_PASSWORD = [from your database]
DB_HOST = [from your database]
DB_PORT = 5432
CORS_ALLOWED_ORIGINS = https://your-project.web.app
FIREBASE_CREDENTIALS_PATH = /opt/render/project/src/firebase-credentials.json
```

**Tip**: Get DB values from Render → Your Database → Connect tab

---

## 🚀 Even Easier: Use Railway Instead of Render

Railway has a **better UI** for environment variables:

1. Go to: https://railway.app
2. New Project → Deploy from GitHub
3. Add PostgreSQL
4. **Environment variables are easier to manage** - you can import from a file!

**Want to switch?** Railway is actually simpler for beginners!

---

## 📋 Quick Checklist

### Frontend (Choose one method):
- [ ] Option 1: Copy template and fill in
- [ ] Option 2: Run interactive script
- [ ] Option 3: Copy-paste method

### Backend:
- [ ] Add variables in Render (or use Railway for easier setup)

---

## 💡 Pro Tips

1. **Use the template** - It's the fastest way
2. **Keep values in a password manager** - You'll need them again
3. **Test after setting** - Build frontend to verify: `npm run build`
4. **Railway is easier** - Consider switching if Render feels complicated

---

**Which method do you prefer?** The template is usually the fastest! 🎯


