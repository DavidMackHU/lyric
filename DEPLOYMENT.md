# LyrIQ Deployment Guide

This guide covers deploying LyrIQ to production. We'll deploy the frontend to Firebase Hosting and the backend to Render (or similar platform).

## Prerequisites

- Firebase account with a project
- Render account (or Heroku/Railway alternative)
- PostgreSQL database (provided by Render or external)
- Domain name (optional)

## Deployment Options

### Option 1: Firebase Hosting + Render (Recommended)

**Frontend**: Firebase Hosting (Free tier available)  
**Backend**: Render (Free tier available)  
**Database**: PostgreSQL on Render

### Option 2: Vercel + Railway

**Frontend**: Vercel (Free tier)  
**Backend**: Railway (Free tier with credit card)  
**Database**: PostgreSQL on Railway

## Step-by-Step Deployment

### Part 1: Backend Deployment (Render)

1. **Create Render Account**
   - Go to [render.com](https://render.com)
   - Sign up for a free account

2. **Create PostgreSQL Database**
   - In Render dashboard, click "New +" → "PostgreSQL"
   - Name it `lyriq-db`
   - Choose free tier
   - Note the connection details

3. **Create Web Service**
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Configure:
     - **Name**: `lyriq-backend`
     - **Root Directory**: `backend`
     - **Environment**: `Python 3`
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `gunicorn lyriq_backend.wsgi:application`

4. **Set Environment Variables**
   ```
   SECRET_KEY=<generate-a-secure-secret-key>
   DEBUG=False
   ALLOWED_HOSTS=lyriq-backend.onrender.com,your-domain.com
   DB_NAME=<from-postgres-database>
   DB_USER=<from-postgres-database>
   DB_PASSWORD=<from-postgres-database>
   DB_HOST=<from-postgres-database>
   DB_PORT=5432
   FIREBASE_CREDENTIALS_PATH=/opt/render/project/src/firebase-credentials.json
   SPOTIFY_CLIENT_ID=<your-spotify-client-id>
   SPOTIFY_CLIENT_SECRET=<your-spotify-client-secret>
   CORS_ALLOWED_ORIGINS=https://your-firebase-app.web.app,https://your-firebase-app.firebaseapp.com
   ```

5. **Upload Firebase Credentials**
   - In Render, go to your service
   - Add a file: `firebase-credentials.json`
   - Paste your Firebase service account JSON content

6. **Run Migrations**
   - In Render shell or via dashboard:
     ```bash
     python manage.py migrate
     python manage.py createsuperuser  # Optional
     ```

7. **Note Your Backend URL**
   - Example: `https://lyriq-backend.onrender.com`
   - This will be your `VITE_API_BASE_URL`

### Part 2: Frontend Deployment (Firebase Hosting)

1. **Install Firebase CLI**
   ```bash
   npm install -g firebase-tools
   firebase login
   ```

2. **Initialize Firebase Hosting**
   ```bash
   firebase init hosting
   ```
   - Select your Firebase project
   - Public directory: `dist`
   - Single-page app: Yes
   - Overwrite index.html: No

3. **Build for Production**
   ```bash
   npm run build
   ```

4. **Update Environment Variables**
   Create `.env.production`:
   ```env
   VITE_FIREBASE_API_KEY=your_firebase_api_key
   VITE_FIREBASE_AUTH_DOMAIN=your_project_id.firebaseapp.com
   VITE_FIREBASE_PROJECT_ID=your_project_id
   VITE_FIREBASE_STORAGE_BUCKET=your_project_id.appspot.com
   VITE_FIREBASE_MESSAGING_SENDER_ID=your_messaging_sender_id
   VITE_FIREBASE_APP_ID=your_app_id
   VITE_API_BASE_URL=https://lyriq-backend.onrender.com/api
   ```

5. **Build with Production Variables**
   ```bash
   npm run build
   ```

6. **Deploy**
   ```bash
   firebase deploy --only hosting
   ```

7. **Update CORS in Backend**
   - Add your Firebase hosting URL to `CORS_ALLOWED_ORIGINS` in Render

### Part 3: Post-Deployment Setup

1. **Update Firebase Authentication**
   - Go to Firebase Console → Authentication → Settings
   - Add your production domain to authorized domains

2. **Test the Application**
   - Visit your Firebase hosting URL
   - Test login, challenge creation, and gameplay

3. **Set Up Custom Domain (Optional)**
   - Firebase: Add custom domain in Hosting settings
   - Render: Add custom domain in service settings
   - Update DNS records as instructed

## Alternative: Railway Deployment

### Backend on Railway

1. **Create Railway Account**
   - Go to [railway.app](https://railway.app)
   - Sign up with GitHub

2. **Create New Project**
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your repository

3. **Add PostgreSQL**
   - Click "+ New" → "Database" → "PostgreSQL"
   - Railway automatically provides connection variables

4. **Configure Service**
   - Root Directory: `backend`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn lyriq_backend.wsgi:application`

5. **Set Environment Variables**
   - Same as Render, but use Railway's variable names:
     - `DATABASE_URL` (auto-provided)
     - `SECRET_KEY`
     - `DEBUG=False`
     - etc.

6. **Deploy**
   - Railway auto-deploys on git push

## Environment Variables Reference

### Backend (Production)
```env
SECRET_KEY=<generate-strong-secret>
DEBUG=False
ALLOWED_HOSTS=your-backend-domain.com
DB_NAME=lyriq_db
DB_USER=postgres
DB_PASSWORD=<from-provider>
DB_HOST=<from-provider>
DB_PORT=5432
FIREBASE_CREDENTIALS_PATH=/path/to/firebase-credentials.json
SPOTIFY_CLIENT_ID=<optional>
SPOTIFY_CLIENT_SECRET=<optional>
CORS_ALLOWED_ORIGINS=https://your-frontend-domain.com
```

### Frontend (Production)
```env
VITE_FIREBASE_API_KEY=<from-firebase>
VITE_FIREBASE_AUTH_DOMAIN=<from-firebase>
VITE_FIREBASE_PROJECT_ID=<from-firebase>
VITE_FIREBASE_STORAGE_BUCKET=<from-firebase>
VITE_FIREBASE_MESSAGING_SENDER_ID=<from-firebase>
VITE_FIREBASE_APP_ID=<from-firebase>
VITE_API_BASE_URL=https://your-backend-domain.com/api
```

## Troubleshooting

### Backend Issues

**Database Connection Errors**
- Verify database credentials
- Check if database is accessible from your hosting provider
- Ensure firewall allows connections

**Static Files Not Serving**
- Run `python manage.py collectstatic`
- Verify `STATIC_ROOT` is set correctly
- Check WhiteNoise middleware is enabled

**CORS Errors**
- Add frontend URL to `CORS_ALLOWED_ORIGINS`
- Check `CORS_ALLOW_CREDENTIALS` is set correctly

### Frontend Issues

**API Calls Failing**
- Verify `VITE_API_BASE_URL` is correct
- Check CORS settings on backend
- Ensure backend is accessible

**Firebase Auth Not Working**
- Add production domain to Firebase authorized domains
- Verify Firebase config variables are correct

**Build Errors**
- Check all environment variables are set
- Verify Node.js version matches (v18+)
- Clear `node_modules` and rebuild

## Continuous Deployment

### GitHub Actions (Already Configured)

The project includes a GitHub Actions workflow (`.github/workflows/deploy.yml`) that:
- Builds the frontend on push to `main`
- Deploys to Firebase Hosting automatically

To enable:
1. Add secrets to GitHub repository:
   - `VITE_FIREBASE_*` variables
   - `VITE_API_BASE_URL`
   - `FIREBASE_SERVICE_ACCOUNT` (JSON content)

2. Push to `main` branch to trigger deployment

## Monitoring & Maintenance

### Backend Monitoring
- Render/Railway provide logs and metrics
- Set up error tracking (Sentry, etc.)
- Monitor database connections

### Frontend Monitoring
- Firebase Hosting provides analytics
- Set up error tracking
- Monitor API response times

### Database Maintenance
- Regular backups (automated on most platforms)
- Monitor database size
- Optimize queries as needed

## Security Checklist

- [ ] `DEBUG=False` in production
- [ ] Strong `SECRET_KEY` generated
- [ ] All environment variables secured
- [ ] CORS configured correctly
- [ ] Firebase authorized domains set
- [ ] HTTPS enabled (automatic on most platforms)
- [ ] Database credentials secured
- [ ] API rate limiting considered

## Cost Estimation

### Free Tier (Suitable for MVP)
- **Firebase Hosting**: Free (10 GB storage, 360 MB/day transfer)
- **Render**: Free tier (750 hours/month)
- **Railway**: $5/month credit (free tier available)
- **PostgreSQL**: Included with Render/Railway

### Paid Tier (For Scale)
- **Firebase Hosting**: Pay-as-you-go after free tier
- **Render**: $7/month for web service
- **Railway**: Pay-as-you-go
- **PostgreSQL**: $7/month on Render

## Support

For deployment issues:
1. Check platform documentation
2. Review error logs
3. Verify environment variables
4. Test locally first

---

**Ready to deploy?** Follow the steps above and your LyrIQ app will be live! 🚀


