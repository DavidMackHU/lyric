# Quick Setup Guide

This is a condensed setup guide. For detailed instructions, see [README.md](README.md).

## Prerequisites Check

- [ ] Node.js v18+ installed
- [ ] Python 3.10+ installed
- [ ] PostgreSQL installed and running
- [ ] Firebase account created
- [ ] Git installed

## Quick Start (5 minutes)

### 1. Install Dependencies

**Frontend:**
```bash
npm install
```

**Backend:**
```bash
cd backend
python -m venv venv
# Activate venv (Windows: venv\Scripts\activate)
# Activate venv (macOS/Linux: source venv/bin/activate)
pip install -r requirements.txt
```

### 2. Configure Environment

**Frontend:**
```bash
cp .env.example .env
# Edit .env with your Firebase config
```

**Backend:**
```bash
cd backend
cp .env.example .env
# Edit .env with your database and Firebase config
```

### 3. Setup Database

```bash
# Create database
createdb lyriq_db

# Run migrations
cd backend
python manage.py migrate
```

### 4. Run the Application

**Terminal 1 (Backend):**
```bash
cd backend
python manage.py runserver
```

**Terminal 2 (Frontend):**
```bash
npm run dev
```

Visit `http://localhost:3000` in your browser!

## Firebase Setup Checklist

1. [ ] Create Firebase project at https://console.firebase.google.com
2. [ ] Enable Authentication → Google Sign-in
3. [ ] Copy web app config to frontend `.env`
4. [ ] Download service account JSON for backend
5. [ ] Add service account path to `backend/.env`

## Common Issues

- **Port already in use**: Change ports in `vite.config.ts` (frontend) or use `python manage.py runserver 8001` (backend)
- **Database connection error**: Check PostgreSQL is running: `pg_isready`
- **Module not found**: Re-run `npm install` or `pip install -r requirements.txt`

## Next Steps

- Read the full [README.md](README.md) for detailed information
- Check [CONTRIBUTING.md](CONTRIBUTING.md) for development guidelines
- Review the PRD for feature requirements


