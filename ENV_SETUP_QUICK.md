# ⚡ Quick Environment Variables Setup

## 🎯 Two Places to Set Variables

### 1️⃣ Backend: Render Dashboard
### 2️⃣ Frontend: `.env.production` file

---

## 📍 PART 1: Backend Variables (Render)

### Where to Go:
1. **Render Dashboard**: https://dashboard.render.com
2. Click your **`lyriq-backend`** service
3. Click **"Environment"** tab (left sidebar)
4. Scroll to **"Environment Variables"**

### What to Add:

Click **"Add Environment Variable"** for each:

| Variable | Value | Where to Get It |
|----------|-------|----------------|
| `SECRET_KEY` | `I(s,E/Vv.v)6BVW)f]NQfM)R-&aiB=90W;tO}}^tGkCU=(v>mA` | Already generated (or run `python scripts/generate-secret-key.py`) |
| `DEBUG` | `False` | Type exactly: `False` |
| `ALLOWED_HOSTS` | `lyriq-backend.onrender.com` | Your Render service URL |
| `DB_NAME` | `lyriq_db` | From PostgreSQL database → Connect tab |
| `DB_USER` | `lyriq_user` | From PostgreSQL database → Connect tab |
| `DB_PASSWORD` | `[password]` | From PostgreSQL database → Connect tab |
| `DB_HOST` | `dpg-xxxxx-a` | From PostgreSQL database → Connect tab |
| `DB_PORT` | `5432` | Usually 5432 |
| `CORS_ALLOWED_ORIGINS` | `https://your-project.web.app` | Update after frontend deploy |
| `FIREBASE_CREDENTIALS_PATH` | `/opt/render/project/src/firebase-credentials.json` | Fixed path |

**Also upload**: `firebase-credentials.json` file (see full guide)

---

## 📍 PART 2: Frontend Variables (Local File)

### Create the File:

**Windows PowerShell:**
```powershell
New-Item .env.production
```

**Mac/Linux:**
```bash
touch .env.production
```

### What to Add:

Open `.env.production` and paste this template:

```env
VITE_FIREBASE_API_KEY=
VITE_FIREBASE_AUTH_DOMAIN=
VITE_FIREBASE_PROJECT_ID=
VITE_FIREBASE_STORAGE_BUCKET=
VITE_FIREBASE_MESSAGING_SENDER_ID=
VITE_FIREBASE_APP_ID=
VITE_API_BASE_URL=
```

### How to Fill Values:

#### Firebase Values (First 6):
1. Go to **Firebase Console**: https://console.firebase.google.com
2. **Project Settings** → **Your apps** → Click **`</>`** (web icon)
3. Copy values from the config shown

#### Backend URL (Last one):
- After deploying backend: `https://lyriq-backend.onrender.com/api`
- Replace with your actual Render backend URL

---

## ✅ Quick Checklist

**Backend (Render):**
- [ ] All 10 variables added
- [ ] `firebase-credentials.json` file uploaded
- [ ] Values saved

**Frontend (`.env.production`):**
- [ ] File created in project root
- [ ] All 7 variables filled in
- [ ] No quotes around values
- [ ] File saved

---

## 📖 Need More Details?

See **`ENV_VARIABLES_SETUP.md`** for:
- Detailed explanations
- Screenshot descriptions
- Troubleshooting
- Common mistakes

---

**Ready? Set your variables and deploy! 🚀**


