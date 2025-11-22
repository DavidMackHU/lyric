# 🎯 Final Steps to Get LyrIQ Running

## ✅ Step 1: Frontend Dependencies - DONE!
Frontend dependencies are installed! ✅

---

## 📝 Step 2: Environment Variables

I've created `.env.production` for you. Now you need to fill in your Firebase values.

### Quick Option: Use Template
The file `.env.production` is ready. Open it and replace:
- `your_firebase_api_key_here` → Your Firebase API key
- `your-project-id` → Your Firebase project ID
- etc.

### Get Firebase Values:
1. Go to: https://console.firebase.google.com
2. Select your project
3. ⚙️ Settings → Project Settings
4. Scroll to "Your apps" → Click `</>` (web icon)
5. Copy the config values

**For now (local testing)**, you can leave it as-is - it will use `localhost:8000` for the API.

---

## 🐍 Step 3: Backend Dependencies

Run this in your terminal:

```bash
cd backend
pip install -r requirements.txt
```

**Or if using virtual environment:**
```bash
cd backend
python -m venv venv
venv\Scripts\activate  # Windows
# or: source venv/bin/activate  # Mac/Linux
pip install -r requirements.txt
```

---

## 🗄️ Step 4: Database Setup

### Option A: Use SQLite (Easiest for Testing)

Edit `backend/lyriq_backend/settings.py` temporarily:

Find the `DATABASES` section and replace with:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

Then run:
```bash
cd backend
python manage.py migrate
```

### Option B: Use PostgreSQL (Production)

1. Install PostgreSQL
2. Create database: `createdb lyriq_db`
3. Update `.env` in backend with DB credentials
4. Run migrations: `python manage.py migrate`

---

## 🚀 Step 5: Run the App!

### Terminal 1 - Backend:
```bash
cd backend
python manage.py runserver
```

You should see:
```
Starting development server at http://127.0.0.1:8000/
```

### Terminal 2 - Frontend:
```bash
npm run dev
```

You should see:
```
  VITE v5.x.x  ready in xxx ms

  ➜  Local:   http://localhost:3000/
```

### Open Browser:
Visit: **http://localhost:3000**

---

## ✅ Quick Checklist

- [x] Frontend dependencies installed
- [ ] Environment variables configured (optional for local)
- [ ] Backend dependencies installed
- [ ] Database set up (SQLite or PostgreSQL)
- [ ] Migrations run
- [ ] Backend server running
- [ ] Frontend server running
- [ ] App opens in browser

---

## 🐛 Troubleshooting

### "Module not found" errors
- Make sure you ran `npm install` (✅ done!)
- For backend: Make sure you ran `pip install -r requirements.txt`

### "Cannot connect to API"
- Make sure backend is running on port 8000
- Check `VITE_API_BASE_URL` in `.env.production`

### "Database errors"
- Use SQLite for quick testing (see Step 4 Option A)
- Or set up PostgreSQL properly

### "Firebase auth not working"
- For local testing, you can skip Firebase setup initially
- The app will work, but login won't function
- Set up Firebase for full functionality

---

## 🎯 Next Steps After It Runs

1. **Test locally** - Make sure everything works
2. **Set up Firebase** - For authentication
3. **Deploy** - Follow deployment guides when ready

---

**Let's continue with the backend setup!** 🚀

