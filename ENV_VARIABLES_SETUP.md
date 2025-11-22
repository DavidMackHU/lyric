# 🔐 Environment Variables Setup Guide

This guide shows you exactly how to set up all environment variables for LyrIQ deployment.

---

## PART 1: Backend Environment Variables (Render)

### Where to Set Them

1. Go to **Render Dashboard**: https://dashboard.render.com
2. Click on your **`lyriq-backend`** service (or create it first)
3. Go to **"Environment"** tab (left sidebar)
4. Scroll to **"Environment Variables"** section

### Step-by-Step: Adding Variables

For each variable below:

1. Click **"Add Environment Variable"** button
2. Enter the **Key** (variable name)
3. Enter the **Value**
4. Click **"Save Changes"**

### Required Variables

Add these **one by one**:

#### 1. SECRET_KEY
```
Key: SECRET_KEY
Value: I(s,E/Vv.v)6BVW)f]NQfM)R-&aiB=90W;tO}}^tGkCU=(v>mA
```
*(Or generate a new one with: `python scripts/generate-secret-key.py`)*

#### 2. DEBUG
```
Key: DEBUG
Value: False
```
⚠️ **Must be `False` (capital F) for production!**

#### 3. ALLOWED_HOSTS
```
Key: ALLOWED_HOSTS
Value: lyriq-backend.onrender.com
```
*(Replace with your actual Render service URL if different)*

#### 4. DB_NAME
```
Key: DB_NAME
Value: lyriq_db
```
*(Get this from your PostgreSQL database in Render)*

#### 5. DB_USER
```
Key: DB_USER
Value: lyriq_user
```
*(Get this from your PostgreSQL database in Render)*

#### 6. DB_PASSWORD
```
Key: DB_PASSWORD
Value: [your-database-password]
```
**How to get it:**
1. Go to Render Dashboard
2. Click on your PostgreSQL database
3. Click **"Connect"** tab
4. Look for **"Internal Database URL"** or individual password
5. Copy the password value

#### 7. DB_HOST
```
Key: DB_HOST
Value: [your-database-host]
```
**How to get it:**
- From database **"Connect"** tab
- Usually looks like: `dpg-xxxxx-a.oregon-postgres.render.com`
- Or just the hostname part: `dpg-xxxxx-a`

#### 8. DB_PORT
```
Key: DB_PORT
Value: 5432
```
*(Usually 5432 for PostgreSQL)*

#### 9. CORS_ALLOWED_ORIGINS
```
Key: CORS_ALLOWED_ORIGINS
Value: https://your-project-id.web.app,https://your-project-id.firebaseapp.com
```
⚠️ **Important**: 
- Replace `your-project-id` with your actual Firebase project ID
- Use **commas** to separate multiple URLs
- **Update this AFTER** you deploy frontend (Step 13)

**Temporary value** (before frontend is deployed):
```
https://localhost:3000
```

#### 10. FIREBASE_CREDENTIALS_PATH
```
Key: FIREBASE_CREDENTIALS_PATH
Value: /opt/render/project/src/firebase-credentials.json
```
*(This is the path where Render will look for the credentials file)*

### Optional Variables

#### SPOTIFY_CLIENT_ID (Optional)
```
Key: SPOTIFY_CLIENT_ID
Value: [your-spotify-client-id]
```
*(Only if you have Spotify API credentials)*

#### SPOTIFY_CLIENT_SECRET (Optional)
```
Key: SPOTIFY_CLIENT_SECRET
Value: [your-spotify-client-secret]
```
*(Only if you have Spotify API credentials)*

### Adding Firebase Credentials File

**Important**: You also need to upload the Firebase service account JSON file.

1. In Render, go to your service
2. Look for **"Files"** or **"Add File"** section
3. Create a new file named: `firebase-credentials.json`
4. **Get the JSON content**:
   - Go to Firebase Console
   - Project Settings → Service Accounts
   - Click "Generate New Private Key"
   - Download the JSON file
   - **Open the file** and copy ALL its contents
5. **Paste the entire JSON** into the file in Render
6. Save

**Example JSON structure** (yours will have real values):
```json
{
  "type": "service_account",
  "project_id": "your-project",
  "private_key_id": "...",
  "private_key": "-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n",
  "client_email": "...",
  "client_id": "...",
  "auth_uri": "...",
  "token_uri": "...",
  ...
}
```

---

## PART 2: Frontend Environment Variables (Local File)

### Where to Set Them

Create a file named **`.env.production`** in your **project root** (same folder as `package.json`).

### Step-by-Step: Creating the File

#### Windows (PowerShell)
```powershell
New-Item .env.production
```

#### Windows (Command Prompt)
```cmd
type nul > .env.production
```

#### Mac/Linux
```bash
touch .env.production
```

### Required Variables

Open `.env.production` in a text editor and add these lines:

```env
VITE_FIREBASE_API_KEY=your_firebase_api_key_here
VITE_FIREBASE_AUTH_DOMAIN=your-project-id.firebaseapp.com
VITE_FIREBASE_PROJECT_ID=your-project-id
VITE_FIREBASE_STORAGE_BUCKET=your-project-id.appspot.com
VITE_FIREBASE_MESSAGING_SENDER_ID=your_messaging_sender_id
VITE_FIREBASE_APP_ID=your_app_id
VITE_API_BASE_URL=https://lyriq-backend.onrender.com/api
```

### How to Get Firebase Values

1. Go to **Firebase Console**: https://console.firebase.google.com
2. Select your project
3. Click **⚙️ Settings** → **Project Settings**
4. Scroll to **"Your apps"** section
5. If no web app exists:
   - Click **"</>"** (web icon)
   - Register app → Give nickname → Register
6. You'll see a config like this:

```javascript
const firebaseConfig = {
  apiKey: "AIzaSyC...",
  authDomain: "lyriq-project.firebaseapp.com",
  projectId: "lyriq-project",
  storageBucket: "lyriq-project.appspot.com",
  messagingSenderId: "123456789012",
  appId: "1:123456789012:web:abc123def456"
};
```

7. **Map to environment variables**:

| Firebase Config | Environment Variable | Example Value |
|----------------|---------------------|---------------|
| `apiKey` | `VITE_FIREBASE_API_KEY` | `AIzaSyC...` |
| `authDomain` | `VITE_FIREBASE_AUTH_DOMAIN` | `lyriq-project.firebaseapp.com` |
| `projectId` | `VITE_FIREBASE_PROJECT_ID` | `lyriq-project` |
| `storageBucket` | `VITE_FIREBASE_STORAGE_BUCKET` | `lyriq-project.appspot.com` |
| `messagingSenderId` | `VITE_FIREBASE_MESSAGING_SENDER_ID` | `123456789012` |
| `appId` | `VITE_FIREBASE_APP_ID` | `1:123456789012:web:abc123def456` |

### Get Backend URL

For `VITE_API_BASE_URL`:
- After deploying backend on Render, you'll get a URL like: `https://lyriq-backend.onrender.com`
- Add `/api` to the end: `https://lyriq-backend.onrender.com/api`

### Complete Example

Here's what a complete `.env.production` might look like:

```env
VITE_FIREBASE_API_KEY=AIzaSyC1234567890abcdefghijklmnopqrstuvwxyz
VITE_FIREBASE_AUTH_DOMAIN=lyriq-project.firebaseapp.com
VITE_FIREBASE_PROJECT_ID=lyriq-project
VITE_FIREBASE_STORAGE_BUCKET=lyriq-project.appspot.com
VITE_FIREBASE_MESSAGING_SENDER_ID=123456789012
VITE_FIREBASE_APP_ID=1:123456789012:web:abc123def456ghi789
VITE_API_BASE_URL=https://lyriq-backend.onrender.com/api
```

---

## Quick Reference Checklist

### Backend (Render) ✅
- [ ] `SECRET_KEY` - Generated secret key
- [ ] `DEBUG` - Set to `False`
- [ ] `ALLOWED_HOSTS` - Your Render service URL
- [ ] `DB_NAME` - From PostgreSQL database
- [ ] `DB_USER` - From PostgreSQL database
- [ ] `DB_PASSWORD` - From PostgreSQL database
- [ ] `DB_HOST` - From PostgreSQL database
- [ ] `DB_PORT` - Usually `5432`
- [ ] `CORS_ALLOWED_ORIGINS` - Your Firebase URLs (update after frontend deploy)
- [ ] `FIREBASE_CREDENTIALS_PATH` - `/opt/render/project/src/firebase-credentials.json`
- [ ] `firebase-credentials.json` file uploaded

### Frontend (`.env.production`) ✅
- [ ] `VITE_FIREBASE_API_KEY` - From Firebase Console
- [ ] `VITE_FIREBASE_AUTH_DOMAIN` - From Firebase Console
- [ ] `VITE_FIREBASE_PROJECT_ID` - From Firebase Console
- [ ] `VITE_FIREBASE_STORAGE_BUCKET` - From Firebase Console
- [ ] `VITE_FIREBASE_MESSAGING_SENDER_ID` - From Firebase Console
- [ ] `VITE_FIREBASE_APP_ID` - From Firebase Console
- [ ] `VITE_API_BASE_URL` - Your Render backend URL + `/api`

---

## Common Mistakes to Avoid

❌ **Don't** put quotes around values in `.env.production`
```env
# ❌ Wrong
VITE_FIREBASE_API_KEY="AIzaSyC..."

# ✅ Correct
VITE_FIREBASE_API_KEY=AIzaSyC...
```

❌ **Don't** use `localhost` URLs in production
```env
# ❌ Wrong
VITE_API_BASE_URL=http://localhost:8000/api

# ✅ Correct
VITE_API_BASE_URL=https://lyriq-backend.onrender.com/api
```

❌ **Don't** commit `.env.production` to Git
- It should already be in `.gitignore`
- But double-check it's not tracked

❌ **Don't** forget to update `CORS_ALLOWED_ORIGINS` after frontend deploy
- Must include your Firebase hosting URL

---

## Testing Your Variables

### Test Backend Variables

After setting variables in Render:
1. Deploy your service
2. Check logs for any errors
3. Test API endpoint: `https://your-backend.onrender.com/api/health/`
4. Should return: `{"status":"ok","message":"LyrIQ API is running"}`

### Test Frontend Variables

After creating `.env.production`:
1. Build frontend: `npm run build`
2. Check for any errors
3. Preview: `npm run preview`
4. Test in browser - should connect to backend

---

## Need Help?

**Can't find a value?**
- Database values: Render Dashboard → Your Database → Connect tab
- Firebase values: Firebase Console → Project Settings → Your apps
- Backend URL: Render Dashboard → Your Service → URL shown at top

**Variables not working?**
- Check for typos in variable names
- Verify no extra spaces
- Make sure values are correct
- Check logs for specific errors

---

**Once all variables are set, you're ready to deploy! 🚀**

