# 🚀 Step-by-Step Deployment Walkthrough

## Option 1: Render (Backend) + Firebase Hosting (Frontend)

Let's deploy LyrIQ step by step. This will take about 15-20 minutes.

---

## PART 1: Backend Deployment on Render

### Step 1: Create Render Account

1. Go to **https://render.com**
2. Click **"Get Started for Free"**
3. Sign up with your **GitHub account** (recommended) or email
4. Verify your email if prompted

### Step 2: Create PostgreSQL Database

1. In Render dashboard, click **"New +"** button (top right)
2. Select **"PostgreSQL"**
3. Fill in:
   - **Name**: `lyriq-db`
   - **Database**: `lyriq_db` (leave default)
   - **User**: `lyriq_user` (leave default)
   - **Region**: Choose closest to you
   - **PostgreSQL Version**: 15 (or latest)
   - **Plan**: **Free** (for testing)
4. Click **"Create Database"**
5. **Wait 2-3 minutes** for database to be created
6. **IMPORTANT**: Note down these values (you'll need them):
   - **Internal Database URL** (shown on dashboard)
   - Or click **"Connect"** to see individual values:
     - Host
     - Port (usually 5432)
     - Database name
     - User
     - Password

### Step 3: Prepare Firebase Service Account

1. Go to **Firebase Console**: https://console.firebase.google.com
2. Select your project (or create one if needed)
3. Click the **gear icon** ⚙️ → **Project Settings**
4. Go to **"Service Accounts"** tab
5. Click **"Generate New Private Key"**
6. Click **"Generate Key"** in the popup
7. A JSON file will download - **save this file** (you'll need it)
8. **Keep this file secure** - don't commit it to Git!

### Step 4: Generate Django Secret Key

Open your terminal and run:

```bash
cd backend
python scripts/generate-secret-key.py
```

**Copy the output** - you'll need it in the next step.

Or if you don't have Python locally, use this online generator:
- Go to: https://djecrety.ir/
- Copy the generated key

### Step 5: Create Web Service on Render

1. In Render dashboard, click **"New +"** → **"Web Service"**
2. Connect your GitHub repository:
   - If not connected, click **"Connect GitHub"**
   - Authorize Render to access your repos
   - Select your **lyriq** repository
3. Configure the service:
   - **Name**: `lyriq-backend`
   - **Region**: Same as database
   - **Branch**: `main` (or your main branch)
   - **Root Directory**: `backend` ⚠️ **IMPORTANT!**
   - **Runtime**: `Python 3`
   - **Build Command**: 
     ```bash
     pip install -r requirements.txt
     ```
   - **Start Command**: 
     ```bash
     gunicorn lyriq_backend.wsgi:application
     ```
   - **Plan**: **Free** (for testing)

4. Click **"Advanced"** and add environment variables:

   Click **"Add Environment Variable"** for each:

   ```
   SECRET_KEY
   ```
   Value: Paste the secret key from Step 4

   ```
   DEBUG
   ```
   Value: `False`

   ```
   ALLOWED_HOSTS
   ```
   Value: `lyriq-backend.onrender.com` (or your custom domain)

   ```
   DB_NAME
   ```
   Value: From Step 2 (usually `lyriq_db`)

   ```
   DB_USER
   ```
   Value: From Step 2 (usually `lyriq_user`)

   ```
   DB_PASSWORD
   ```
   Value: From Step 2 (the password)

   ```
   DB_HOST
   ```
   Value: From Step 2 (the host, something like `dpg-xxxxx-a`)

   ```
   DB_PORT
   ```
   Value: `5432`

   ```
   CORS_ALLOWED_ORIGINS
   ```
   Value: `https://your-project-id.web.app,https://your-project-id.firebaseapp.com`
   (We'll update this after frontend deployment)

   ```
   SPOTIFY_CLIENT_ID
   ```
   Value: (Leave empty for now, optional)

   ```
   SPOTIFY_CLIENT_SECRET
   ```
   Value: (Leave empty for now, optional)

5. **Add Firebase Credentials File**:
   - Scroll down to **"Environment"** section
   - Click **"Add File"** or look for file upload option
   - Create a file named: `firebase-credentials.json`
   - Paste the **entire contents** of the JSON file from Step 3
   - Set the path variable:
     ```
     FIREBASE_CREDENTIALS_PATH
     ```
     Value: `/opt/render/project/src/firebase-credentials.json`

6. Click **"Create Web Service"**

7. **Wait for deployment** (5-10 minutes)
   - Watch the build logs
   - If there are errors, check the logs

8. **Run Migrations**:
   - Once deployed, click on your service
   - Go to **"Shell"** tab (or use "Manual Deploy" → "Run Command")
   - Run:
     ```bash
     python manage.py migrate
     ```
   - (Optional) Create superuser:
     ```bash
     python manage.py createsuperuser
     ```

9. **Note your backend URL**:
   - It will be: `https://lyriq-backend.onrender.com`
   - Or check the service dashboard for the exact URL
   - **Copy this URL** - you'll need it for frontend!

---

## PART 2: Frontend Deployment on Firebase Hosting

### Step 6: Install Firebase CLI

Open terminal and run:

```bash
npm install -g firebase-tools
```

Verify installation:
```bash
firebase --version
```

### Step 7: Login to Firebase

```bash
firebase login
```

This will open a browser - sign in with your Google account.

### Step 8: Initialize Firebase Hosting

1. In your project root directory, run:
   ```bash
   firebase init hosting
   ```

2. Follow the prompts:
   - **"Which Firebase features do you want to set up?"**
     - Select: `Hosting` (use spacebar, then Enter)
   
   - **"Please select an option"**
     - Select: `Use an existing project`
   
   - **"Select a default Firebase project"**
     - Choose your Firebase project (or create one)
   
   - **"What do you want to use as your public directory?"**
     - Type: `dist` (this is where Vite builds)
     - Press Enter
   
   - **"Configure as a single-page app?"**
     - Type: `Yes` (y)
   
   - **"Set up automatic builds and deploys with GitHub?"**
     - Type: `No` (n) for now
   
   - **"File dist/index.html already exists. Overwrite?"**
     - Type: `No` (n)

### Step 9: Create Production Environment File

1. In your project root, create `.env.production`:

```bash
# On Windows (PowerShell)
New-Item .env.production

# On Mac/Linux
touch .env.production
```

2. Open `.env.production` and add:

```env
VITE_FIREBASE_API_KEY=your_firebase_api_key_here
VITE_FIREBASE_AUTH_DOMAIN=your-project-id.firebaseapp.com
VITE_FIREBASE_PROJECT_ID=your-project-id
VITE_FIREBASE_STORAGE_BUCKET=your-project-id.appspot.com
VITE_FIREBASE_MESSAGING_SENDER_ID=your_messaging_sender_id
VITE_FIREBASE_APP_ID=your_app_id
VITE_API_BASE_URL=https://lyriq-backend.onrender.com/api
```

**To get Firebase values:**
1. Go to Firebase Console
2. Project Settings (gear icon)
3. Scroll to "Your apps" section
4. Click the web app icon `</>`
5. Copy the config values

**Replace `VITE_API_BASE_URL`** with your Render backend URL from Step 5:
- Should be: `https://lyriq-backend.onrender.com/api`

### Step 10: Build Frontend

```bash
npm install
npm run build
```

This creates a `dist` folder with production files.

**Check for errors** - if build fails, fix issues before proceeding.

### Step 11: Deploy to Firebase

```bash
firebase deploy --only hosting
```

Wait for deployment to complete.

You'll see output like:
```
✔  Deploy complete!

Project Console: https://console.firebase.google.com/project/your-project/overview
Hosting URL: https://your-project.web.app
```

**Copy the Hosting URL** - this is your live app!

### Step 12: Update CORS in Backend

1. Go back to Render dashboard
2. Open your `lyriq-backend` service
3. Go to **"Environment"** tab
4. Find `CORS_ALLOWED_ORIGINS`
5. Update it to include your Firebase URL:
   ```
   https://your-project-id.web.app,https://your-project-id.firebaseapp.com
   ```
6. Click **"Save Changes"**
7. Render will automatically redeploy

---

## PART 3: Final Configuration

### Step 13: Configure Firebase Authentication

1. Go to Firebase Console
2. **Authentication** → **Settings** → **Authorized domains**
3. Your Firebase domain should already be there
4. If using custom domain, add it here

### Step 14: Test Your Live App!

1. Visit your Firebase Hosting URL
2. Test these features:
   - [ ] Login with Google
   - [ ] View profile
   - [ ] Create a challenge
   - [ ] Play a challenge
   - [ ] View leaderboard

### Step 15: (Optional) Set Up Custom Domain

**Firebase Hosting:**
1. Firebase Console → Hosting
2. Click **"Add custom domain"**
3. Follow instructions to verify domain

**Render Backend:**
1. Render dashboard → Your service
2. Settings → Custom Domain
3. Add your domain
4. Update DNS as instructed

---

## 🎉 You're Live!

Your app should now be accessible at:
- **Frontend**: `https://your-project.web.app`
- **Backend**: `https://lyriq-backend.onrender.com`

## 🔧 Troubleshooting

### Backend Issues

**"Database connection failed"**
- Check DB credentials in Render
- Verify database is running (green status)
- Check internal vs external database URL

**"Static files not found"**
- Run: `python manage.py collectstatic` in Render shell
- Check WhiteNoise is in requirements.txt

**"CORS error"**
- Verify `CORS_ALLOWED_ORIGINS` includes your Firebase URL
- Check it's a comma-separated list
- Redeploy after changes

### Frontend Issues

**"Cannot connect to API"**
- Check `VITE_API_BASE_URL` in `.env.production`
- Verify backend URL is correct
- Check browser console for errors

**"Firebase auth not working"**
- Verify Firebase config in `.env.production`
- Check authorized domains in Firebase Console
- Clear browser cache

**"Build fails"**
- Check Node.js version (need v18+)
- Delete `node_modules` and `dist`, then rebuild
- Check for TypeScript errors

### General Issues

**"Service won't start"**
- Check Render logs for errors
- Verify all environment variables are set
- Check build command is correct

**"404 errors"**
- Verify `firebase.json` has correct rewrite rules
- Check `dist` folder exists after build
- Verify single-page app config

---

## 📞 Need Help?

1. Check Render logs: Dashboard → Your Service → Logs
2. Check Firebase logs: Console → Functions → Logs
3. Check browser console for frontend errors
4. Review deployment docs: `DEPLOYMENT.md`

---

**Congratulations! Your LyrIQ app is now live! 🚀**


