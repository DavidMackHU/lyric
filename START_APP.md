# 🚀 How to Start LyrIQ

## ✅ Setup Complete!

All dependencies are installed and database is ready!

---

## 🎯 Start the App (2 Simple Steps)

### Step 1: Start Backend Server

Open **Terminal 1** and run:

```bash
cd backend
python manage.py runserver
```

You should see:
```
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

**Keep this terminal open!** ✅

---

### Step 2: Start Frontend Server

Open **Terminal 2** (new terminal window) and run:

```bash
npm run dev
```

You should see:
```
  VITE v5.x.x  ready in xxx ms

  ➜  Local:   http://localhost:3000/
  ➜  Network: use --host to expose
```

**Keep this terminal open too!** ✅

---

## 🌐 Open in Browser

Visit: **http://localhost:3000**

You should see the LyrIQ home page! 🎉

---

## ✅ What's Working

- ✅ Frontend server running
- ✅ Backend API running
- ✅ Database ready (SQLite for local testing)
- ✅ All pages accessible

## ⚠️ What Needs Setup (Optional)

- 🔐 **Firebase Authentication** - For login (can test without it)
- 🎵 **Spotify API** - For song search (optional)
- 📝 **Environment Variables** - For production deployment

---

## 🧪 Test It Out

1. **Home Page**: Should load at http://localhost:3000
2. **API Health Check**: Visit http://localhost:8000/api/health/
   - Should see: `{"status":"ok","message":"LyrIQ API is running"}`
3. **Browse Pages**: Try navigating (some features need Firebase setup)

---

## 🐛 Troubleshooting

### Backend won't start?
- Make sure port 8000 is not in use
- Check: `python manage.py check`

### Frontend won't start?
- Make sure port 3000 is not in use
- Try: `npm run dev -- --port 3001`

### Can't connect to API?
- Make sure backend is running
- Check `.env.production` has: `VITE_API_BASE_URL=http://localhost:8000/api`

### Database errors?
- SQLite is already set up - should work automatically
- Database file: `backend/db.sqlite3`

---

## 🎯 Next Steps

1. **Test locally** - Make sure everything works
2. **Set up Firebase** - For authentication (see `SIMPLE_SETUP.md`)
3. **Deploy** - When ready (see `DEPLOY_STEP_BY_STEP.md`)

---

**You're all set! Start both servers and open http://localhost:3000** 🚀

