# 🚀 Go Live Checklist

## Pre-Deployment Checklist

### ✅ Backend Setup

- [ ] Generate Django secret key: `python scripts/generate-secret-key.py`
- [ ] Set up PostgreSQL database (Render/Railway)
- [ ] Configure all environment variables in hosting platform
- [ ] Upload Firebase service account JSON
- [ ] Run migrations: `python manage.py migrate`
- [ ] Test backend API endpoints
- [ ] Verify CORS settings

### ✅ Frontend Setup

- [ ] Create `.env.production` with production values
- [ ] Update `VITE_API_BASE_URL` to production backend URL
- [ ] Build frontend: `npm run build`
- [ ] Test build locally: `npm run preview`
- [ ] Initialize Firebase Hosting: `firebase init hosting`

### ✅ Firebase Configuration

- [ ] Enable Google Sign-in in Firebase Console
- [ ] Add production domain to authorized domains
- [ ] Verify Firebase config in `.env.production`
- [ ] Test authentication flow

## Quick Deploy Commands

### Backend (Render)
1. Push code to GitHub
2. Connect repo to Render
3. Set environment variables
4. Deploy!

### Frontend (Firebase)
```bash
npm run build
firebase deploy --only hosting
```

## Post-Deployment

- [ ] Test login functionality
- [ ] Test challenge creation
- [ ] Test challenge gameplay
- [ ] Verify leaderboard updates
- [ ] Check mobile responsiveness
- [ ] Monitor error logs
- [ ] Set up monitoring/alerts

## Your Live URLs

**Frontend**: `https://your-project.web.app`  
**Backend**: `https://lyriq-backend.onrender.com`

## Need Help?

- See [QUICK_DEPLOY.md](QUICK_DEPLOY.md) for step-by-step guide
- See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed instructions
- Check platform documentation (Render, Firebase)

---

**Ready? Let's go live! 🎉**


