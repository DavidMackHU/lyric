# Quick Deployment Guide

## 🚀 Deploy in 10 Minutes

### Backend (Render - Free)

1. **Go to [render.com](https://render.com)** and sign up

2. **Create PostgreSQL Database**
   - New + → PostgreSQL
   - Name: `lyriq-db`
   - Plan: Free

3. **Create Web Service**
   - New + → Web Service
   - Connect GitHub repo
   - Settings:
     - **Name**: `lyriq-backend`
     - **Root Directory**: `backend`
     - **Build Command**: `pip install -r requirements.txt && python manage.py migrate`
     - **Start Command**: `gunicorn lyriq_backend.wsgi:application`

4. **Add Environment Variables** (in Render dashboard):
   ```
   SECRET_KEY=<run: python scripts/generate-secret-key.py>
   DEBUG=False
   ALLOWED_HOSTS=lyriq-backend.onrender.com
   DB_NAME=<from-postgres>
   DB_USER=<from-postgres>
   DB_PASSWORD=<from-postgres>
   DB_HOST=<from-postgres>
   DB_PORT=5432
   CORS_ALLOWED_ORIGINS=https://your-firebase-app.web.app
   ```

5. **Upload Firebase Credentials**
   - In Render, create file: `firebase-credentials.json`
   - Paste your Firebase service account JSON

6. **Deploy** - Render auto-deploys!

### Frontend (Firebase Hosting - Free)

1. **Install Firebase CLI**
   ```bash
   npm install -g firebase-tools
   firebase login
   ```

2. **Initialize**
   ```bash
   firebase init hosting
   ```
   - Select project
   - Public: `dist`
   - SPA: Yes

3. **Create `.env.production`**
   ```env
   VITE_FIREBASE_API_KEY=...
   VITE_FIREBASE_AUTH_DOMAIN=...
   VITE_FIREBASE_PROJECT_ID=...
   VITE_FIREBASE_STORAGE_BUCKET=...
   VITE_FIREBASE_MESSAGING_SENDER_ID=...
   VITE_FIREBASE_APP_ID=...
   VITE_API_BASE_URL=https://lyriq-backend.onrender.com/api
   ```

4. **Build & Deploy**
   ```bash
   npm run build
   firebase deploy --only hosting
   ```

5. **Update CORS**
   - Add Firebase URL to Render's `CORS_ALLOWED_ORIGINS`

## ✅ Done!

Your app is live at: `https://your-project.web.app`

## 🔧 Troubleshooting

**Backend won't start?**
- Check logs in Render
- Verify all env vars are set
- Run migrations: `python manage.py migrate`

**Frontend can't connect?**
- Check `VITE_API_BASE_URL` is correct
- Verify CORS settings
- Check browser console for errors

**Database errors?**
- Verify DB credentials in Render
- Check database is running
- Run migrations

---

Need help? Check [DEPLOYMENT.md](DEPLOYMENT.md) for detailed instructions.


