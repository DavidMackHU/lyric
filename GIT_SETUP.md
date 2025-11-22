# 🔧 Git Setup Guide

## Quick Setup Commands

Run these commands **in order** from your project root:

### Step 1: Initialize Git (if not already done)
```bash
git init
```

### Step 2: Configure Git (if not already configured globally)
```bash
git config user.email "your-email@example.com"
git config user.name "Your Name"
```

Or set globally for all repos:
```bash
git config --global user.email "your-email@example.com"
git config --global user.name "Your Name"
```

### Step 3: Add All Files
```bash
git add .
```

### Step 4: Create Initial Commit
```bash
git commit -m "Initial commit: LyrIQ - Complete lyric challenge game"
```

### Step 5: Add Remote Repository
```bash
git remote add origin https://github.com/DavidMackHU/lyric.git
```

### Step 6: Rename Branch to Main
```bash
git branch -M main
```

### Step 7: Push to GitHub
```bash
git push -u origin main
```

---

## ⚠️ Important Notes

### Before Pushing:

1. **Check .gitignore** - Make sure sensitive files are ignored:
   - `.env.production` ✅ (already in .gitignore)
   - `node_modules/` ✅
   - `db.sqlite3` ✅
   - `__pycache__/` ✅

2. **Verify what will be committed**:
   ```bash
   git status
   ```

3. **If you see sensitive files**, remove them:
   ```bash
   git reset HEAD .env.production
   ```

---

## 🚀 All-in-One Script

If you want to run everything at once (Windows PowerShell):

```powershell
# Initialize
git init

# Configure (replace with your info)
git config user.email "david@example.com"
git config user.name "David Mack"

# Add and commit
git add .
git commit -m "Initial commit: LyrIQ - Complete lyric challenge game"

# Set up remote and push
git remote add origin https://github.com/DavidMackHU/lyric.git
git branch -M main
git push -u origin main
```

---

## 🔐 Authentication

When you run `git push`, GitHub may ask for authentication:

### Option 1: Personal Access Token (Recommended)
1. Go to GitHub → Settings → Developer settings → Personal access tokens
2. Generate new token (classic)
3. Give it `repo` permissions
4. Use token as password when prompted

### Option 2: GitHub CLI
```bash
gh auth login
```

### Option 3: SSH Key
Set up SSH key for passwordless pushes

---

## ✅ Verify Push

After pushing, check your GitHub repository:
- Go to: https://github.com/DavidMackHU/lyric
- You should see all your files!

---

## 📝 Future Commits

After initial setup, use these commands:

```bash
git add .
git commit -m "Your commit message"
git push
```

---

**Ready to push? Run the commands above!** 🚀

