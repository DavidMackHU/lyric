# 🚀 Complete Deployment Walkthrough

Follow these steps **in order** to deploy LyrIQ. This will take about 15-20 minutes.

---

## PART 1: Backend Setup (Render)

### Step 1: Create Render Account

1. Go to **https://render.com**
2. Click **"Get Started for Free"**
3. Sign up with **GitHub** (recommended) or email
4. Verify your email

**✅ Checkpoint**: You should see the Render dashboard

---

### Step 2: Create PostgreSQL Database

1. In Render dashboard, click **"New +"** (top right)
2. Click **"PostgreSQL"**
3. Fill in:
   - **Name**: `lyriq-db`
   - **Database**: `lyriq_db` (default)
   - **User**: `lyriq_user` (default)
   - **Region**: Choose closest (e.g., "Oregon (US West)")
   - **PostgreSQL Version**: 15
   - **Plan**: **Free**
4. Click **"Create Database"**
5. **Wait 2-3 minutes** for creation

6. **Get Database Info**:
   - Click on your database
   - Click **"Connect"** tab
   - You'll see:
     - **Internal Database URL** (use this)
     - Or individual values:
       - Host: `dpg-xxxxx-a`
       - Port: `5432`
       - Database: `lyriq_db`
       - User: `lyriq_user`
       - Password: `xxxxx`

**📝 Write down these values - you'll need them!**

**✅ Checkpoint**: Database is created and you have connection info

---

### Step 3: Get Firebase Service Account

1. Go to **https://console.firebase.google.com**
2. Select your project (or create one)
3. Click **⚙️ Settings** → **Project Settings**
4. Go to **"Service Accounts"** tab
5. Click **"Generate New Private Key"**
6. Click **"Generate Key"** in popup
7. **JSON file downloads** - save it somewhere safe
8. **Open the JSON file** - you'll need its contents

**✅ Checkpoint**: You have the Firebase JSON file

---

### Step 4: Generate Django Secret Key

Open your terminal in the project root and run:

```bash
python scripts/generate-secret-key.py
```

**Copy the output** - this is your `SECRET_KEY`

**Example output**: `I(s,E/Vv.v)6BVW)f]NQfM)R-&aiB=90W;tO}}^tGkCU=(v>mA`

**✅ Checkpoint**: You have a secret key copied

---

### Step 5: Create Web Service on Render

1. In Render dashboard, click **"New +"** → **"Web Service"**

2. **Connect Repository**:
   - If first time: Click **"Connect GitHub"**
   - Authorize Render
   - Select your **lyriq** repository
   - Click **"Connect"**

3. **Configure Service**:
   - **Name**: `lyriq-backend`
   - **Region**: Same as database
   - **Branch**: `main` (or your main branch)
   - **Root Directory**: `backend` ⚠️ **CRITICAL!**
   - **Runtime**: `Python 3`
   - **Build Command**: 
     ```
     pip install -r requirements.txt
     ```
   - **Start Command**: 
     ```
     gunicorn lyriq_backend.wsgi:application
     ```
   - **Plan**: **Free**

4. **Add Environment Variables**:

   Scroll down to **"Environment Variables"** section.
   Click **"Add Environment Variable"** for each:

   | Variable Name | Value | Notes |
   |-------------|-------|-------|
   | `SECRET_KEY` | `[paste from Step 4]` | The secret key you generated |
   | `DEBUG` | `False` | Must be False for production |
   | `ALLOWED_HOSTS` | `lyriq-backend.onrender.com` | Your backend domain |
   | `DB_NAME` | `lyriq_db` | From Step 2 |
   | `DB_USER` | `lyriq_user` | From Step 2 |
   | `DB_PASSWORD` | `[from Step 2]` | From database connection |
   | `DB_HOST` | `[from Step 2]` | Host from database (e.g., `dpg-xxxxx-a`) |
   | `DB_PORT` | `5432` | Usually 5432 |
   | `CORS_ALLOWED_ORIGINS` | `https://your-project.web.app` | We'll update after frontend |
   | `FIREBASE_CREDENTIALS_PATH` | `/opt/render/project/src/firebase-credentials.json` | Path for credentials file |

5. **Add Firebase Credentials File**:

   - Scroll to **"Environment"** section
   - Look for **"Add File"** or **"Files"** section
   - Create file: `firebase-credentials.json`
   - **Open the JSON file from Step 3** and copy ALL its contents
   - Paste into the file in Render
   - Save

6. Click **"Create Web Service"**

7. **Wait for deployment** (5-10 minutes)
   - Watch the build logs
   - It will show: "Building..." then "Deploying..."
   - Wait for "Live" status

8. **Run Migrations**:
   - Once deployed, click on your service
   - Go to **"Shell"** tab (or "Manual Deploy" → "Run Command")
   - Run:
     ```bash
     python manage.py migrate
     ```
   - Wait for it to complete

9. **Get Your Backend URL**:
   - In service dashboard, you'll see: `https://lyriq-backend.onrender.com`
   - **Copy this URL** - you need it for frontend!

**✅ Checkpoint**: Backend is deployed and running

---

## PART 2: Frontend Setup (Firebase Hosting)

### Step 6: Install Firebase CLI

Open terminal and run:

```bash
npm install -g firebase-tools
```

Verify:
```bash
firebase --version
```

**✅ Checkpoint**: Firebase CLI is installed

---

### Step 7: Login to Firebase

```bash
firebase login
```

- Browser opens
- Sign in with Google account
- Authorize Firebase CLI

**✅ Checkpoint**: Logged into Firebase

---

### Step 8: Initialize Firebase Hosting

1. In project root, run:
   ```bash
   firebase init hosting
   ```

2. **Answer the prompts**:

   ```
   ? Which Firebase features do you want to set up?
   > Hosting: Configure files for Firebase Hosting
   ```
   - Press **Space** to select Hosting
   - Press **Enter**

   ```
   ? Please select an option:
   > Use an existing project
   ```
   - Select your Firebase project
   - Press **Enter**

   ```
   ? What do you want to use as your public directory?
   > dist
   ```
   - Type: `dist`
   - Press **Enter**

   ```
   ? Configure as a single-page app (rewrite all urls to /index.html)?
   > Yes
   ```
   - Type: `y`
   - Press **Enter**

   ```
   ? Set up automatic builds and deploys with GitHub?
   > No
   ```
   - Type: `n`
   - Press **Enter**

   ```
   ? File dist/index.html already exists. Overwrite?
   > No
   ```
   - Type: `n`
   - Press **Enter**

**✅ Checkpoint**: Firebase hosting initialized

---

### Step 9: Get Firebase Config Values

1. Go to **Firebase Console**: https://console.firebase.google.com
2. Select your project
3. Click **⚙️ Settings** → **Project Settings**
4. Scroll to **"Your apps"** section
5. If no web app exists:
   - Click **"</>"** (web icon)
   - Register app
   - Give it a nickname
   - Click **"Register app"**
6. **Copy the config values** - you'll see something like:

   ```javascript
   const firebaseConfig = {
     apiKey: "AIzaSy...",
     authDomain: "your-project.firebaseapp.com",
     projectId: "your-project",
     storageBucket: "your-project.appspot.com",
     messagingSenderId: "123456789",
     appId: "1:123456789:web:abc123"
   };
   ```

**✅ Checkpoint**: You have Firebase config values

---

### Step 10: Create Production Environment File

1. In project root, create `.env.production`:

   **Windows (PowerShell)**:
   ```powershell
   New-Item .env.production
   ```

   **Mac/Linux**:
   ```bash
   touch .env.production
   ```

2. **Open `.env.production`** in a text editor

3. **Add these lines** (replace with YOUR values):

   ```env
   VITE_FIREBASE_API_KEY=AIzaSy...your-api-key
   VITE_FIREBASE_AUTH_DOMAIN=your-project.firebaseapp.com
   VITE_FIREBASE_PROJECT_ID=your-project
   VITE_FIREBASE_STORAGE_BUCKET=your-project.appspot.com
   VITE_FIREBASE_MESSAGING_SENDER_ID=123456789
   VITE_FIREBASE_APP_ID=1:123456789:web:abc123
   VITE_API_BASE_URL=https://lyriq-backend.onrender.com/api
   ```

   **Important**: 
   - Replace all Firebase values with yours from Step 9
   - Replace `VITE_API_BASE_URL` with your backend URL from Step 5

**✅ Checkpoint**: `.env.production` file created with correct values

---

### Step 11: Build Frontend

In project root, run:

```bash
npm install
```

Then:

```bash
npm run build
```

**Wait for build to complete** - should see:
```
✓ built in X.XXs
```

**Check**: `dist` folder should be created

**✅ Checkpoint**: Frontend built successfully

---

### Step 12: Deploy to Firebase

```bash
firebase deploy --only hosting
```

**Wait for deployment** (1-2 minutes)

You'll see:
```
✔  Deploy complete!

Project Console: https://console.firebase.google.com/project/your-project/overview
Hosting URL: https://your-project.web.app
```

**📝 Copy your Hosting URL** - this is your live app!

**✅ Checkpoint**: Frontend is deployed

---

### Step 13: Update CORS in Backend

1. Go back to **Render dashboard**
2. Open your `lyriq-backend` service
3. Go to **"Environment"** tab
4. Find `CORS_ALLOWED_ORIGINS`
5. **Update the value** to:
   ```
   https://your-project-id.web.app,https://your-project-id.firebaseapp.com
   ```
   (Replace `your-project-id` with your actual project ID)
6. Click **"Save Changes"**
7. Render will **automatically redeploy** (wait 2-3 minutes)

**✅ Checkpoint**: CORS updated

---

## PART 3: Final Configuration

### Step 14: Configure Firebase Authentication

1. Go to **Firebase Console**
2. **Authentication** → **Sign-in method**
3. Enable **"Google"**:
   - Click **"Google"**
   - Toggle **"Enable"**
   - Enter support email
   - Click **"Save"**

4. **Authentication** → **Settings** → **Authorized domains**
   - Your Firebase domain should be there automatically
   - If using custom domain, add it

**✅ Checkpoint**: Google Sign-in enabled

---

### Step 15: Test Your Live App! 🎉

1. **Visit your Firebase Hosting URL**:
   - Example: `https://your-project.web.app`

2. **Test these features**:
   - [ ] **Home page loads**
   - [ ] **Click "Login"** → Google Sign-in works
   - [ ] **Profile page** shows your info
   - [ ] **Create Challenge** → Search for a song
   - [ ] **Play Challenge** → Submit an answer
   - [ ] **Leaderboard** displays

3. **Check browser console** (F12) for any errors

**✅ Checkpoint**: App is working!

---

## 🎊 You're Live!

**Your URLs**:
- **Frontend**: `https://your-project.web.app`
- **Backend**: `https://lyriq-backend.onrender.com`

---

## 🔧 Troubleshooting

### Backend Won't Start

**Check Render Logs**:
1. Render dashboard → Your service → **"Logs"** tab
2. Look for error messages
3. Common issues:
   - Missing environment variable
   - Database connection failed
   - Wrong build/start command

**Fix Database Connection**:
- Verify all DB_* variables are correct
- Check database is running (green status)
- Use **Internal Database URL** if available

### Frontend Build Fails

**Check for errors**:
```bash
npm run build
```

**Common fixes**:
- Delete `node_modules` and `dist`, then rebuild
- Check `.env.production` has all variables
- Verify Node.js version: `node --version` (need v18+)

### CORS Errors

**Symptoms**: API calls fail in browser console

**Fix**:
1. Verify `CORS_ALLOWED_ORIGINS` in Render includes your Firebase URL
2. Format: `https://your-project.web.app,https://your-project.firebaseapp.com`
3. Redeploy backend after changes

### Firebase Auth Not Working

**Check**:
1. Firebase config in `.env.production` is correct
2. Google Sign-in is enabled in Firebase Console
3. Authorized domains include your domain
4. Clear browser cache

---

## 📞 Need More Help?

1. **Check detailed docs**:
   - `DEPLOYMENT.md` - Full deployment guide
   - `QUICK_DEPLOY.md` - Quick reference

2. **Check logs**:
   - Render: Dashboard → Service → Logs
   - Firebase: Console → Hosting → Logs
   - Browser: F12 → Console tab

3. **Verify environment variables** are all set correctly

---

## ✅ Deployment Checklist

- [ ] Render account created
- [ ] PostgreSQL database created
- [ ] Backend service deployed
- [ ] Migrations run
- [ ] Firebase CLI installed
- [ ] Firebase hosting initialized
- [ ] `.env.production` created
- [ ] Frontend built
- [ ] Frontend deployed
- [ ] CORS updated
- [ ] Google Sign-in enabled
- [ ] App tested and working

---

**Congratulations! Your LyrIQ app is now live! 🚀🎉**


