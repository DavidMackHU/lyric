# LyrIQ - The Lyric Challenge Game

LyrIQ is a web-based lyric-guessing game where users test their music knowledge by completing missing lyrics from their favorite songs. Using the Spotify Web API, users can create "Finish the Lyric" challenges, play challenges created by others, earn points, and climb a global leaderboard.

## Tech Stack

- **Frontend**: React 18 + TypeScript + Vite + Material UI
- **Backend**: Django 4.2 + Django REST Framework
- **Authentication**: Firebase Authentication (Google Sign-in)
- **Database**: PostgreSQL (with Firestore as alternative)
- **API**: Spotify Web API for song search

## Project Structure

```
lyriq/
├── backend/                 # Django backend
│   ├── api/                # Main API app
│   │   ├── models.py       # Database models
│   │   ├── views.py        # API views
│   │   ├── serializers.py  # DRF serializers
│   │   └── urls.py         # API routes
│   ├── lyriq_backend/      # Django project settings
│   ├── manage.py
│   └── requirements.txt
├── src/                    # React frontend
│   ├── components/         # Reusable components
│   ├── contexts/           # React contexts (Auth)
│   ├── pages/              # Page components
│   ├── config/             # Configuration files
│   └── main.tsx
├── package.json
├── vite.config.ts
└── README.md
```

## Prerequisites

- **Node.js** (v18 or higher)
- **Python** (v3.10 or higher)
- **PostgreSQL** (v12 or higher)
- **Firebase Account** (for authentication)
- **Spotify Developer Account** (for API access)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository-url>
cd lyriq
```

### 2. Frontend Setup

```bash
# Install dependencies
npm install

# Create .env file from example
cp .env.example .env

# Edit .env with your Firebase configuration
# (See Firebase Setup section below)
```

### 3. Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file from example
cp .env.example .env

# Edit .env with your configuration values
```

### 4. Database Setup

```bash
# Create PostgreSQL database
createdb lyriq_db

# Or using psql:
psql -U postgres
CREATE DATABASE lyriq_db;
\q

# Run migrations
cd backend
python manage.py makemigrations
python manage.py migrate

# Create superuser (optional, for admin access)
python manage.py createsuperuser
```

### 5. Firebase Setup

1. Go to [Firebase Console](https://console.firebase.google.com/)
2. Create a new project or select an existing one
3. Enable **Authentication** → **Google Sign-in**
4. Get your Firebase configuration:
   - Go to Project Settings → General
   - Scroll to "Your apps" section
   - Copy the config values
5. Add these to your frontend `.env` file:
   ```
   VITE_FIREBASE_API_KEY=your_api_key
   VITE_FIREBASE_AUTH_DOMAIN=your_project.firebaseapp.com
   VITE_FIREBASE_PROJECT_ID=your_project_id
   VITE_FIREBASE_STORAGE_BUCKET=your_project.appspot.com
   VITE_FIREBASE_MESSAGING_SENDER_ID=your_sender_id
   VITE_FIREBASE_APP_ID=your_app_id
   ```
6. For backend authentication:
   - Go to Project Settings → Service Accounts
   - Generate a new private key
   - Save the JSON file securely
   - Add path to `backend/.env`: `FIREBASE_CREDENTIALS_PATH=path/to/service-account.json`

### 6. Running the Application

**Terminal 1 - Backend:**
```bash
cd backend
python manage.py runserver
```
Backend will run on `http://localhost:8000`

**Terminal 2 - Frontend:**
```bash
npm run dev
```
Frontend will run on `http://localhost:3000`

## Development Workflow

### Git Workflow

1. Create a feature branch: `git checkout -b feature/your-feature-name`
2. Make your changes
3. Commit with meaningful messages: `git commit -m "Add feature: description"`
4. Push to your branch: `git push origin feature/your-feature-name`
5. Create a Pull Request

### Code Style

- **Frontend**: Follow TypeScript and React best practices. ESLint is configured.
- **Backend**: Follow PEP 8 Python style guide. Use Django conventions.
- **Commits**: Use clear, descriptive commit messages.

## API Endpoints

### Authentication Required
All endpoints except public challenge viewing require Firebase authentication token in the header:
```
Authorization: Bearer <firebase_token>
```

### User Endpoints
- `GET /api/users/profile/` - Get current user profile
- `POST /api/users/create_profile/` - Create/update user profile

### Challenge Endpoints
- `GET /api/challenges/` - List all public challenges
- `POST /api/challenges/` - Create a new challenge (auth required)
- `GET /api/challenges/{id}/` - Get challenge details
- `POST /api/challenges/{id}/submit_answer/` - Submit answer to challenge
- `GET /api/challenges/{id}/hint/` - Get hint for challenge

### Leaderboard
- `GET /api/leaderboard/` - Get global leaderboard

## Environment Variables

### Frontend (.env)
- `VITE_FIREBASE_*` - Firebase configuration
- `VITE_API_BASE_URL` - Backend API URL

### Backend (backend/.env)
- `SECRET_KEY` - Django secret key
- `DEBUG` - Debug mode (True/False)
- `ALLOWED_HOSTS` - Comma-separated list of allowed hosts
- `DB_*` - PostgreSQL database configuration
- `FIREBASE_CREDENTIALS_PATH` - Path to Firebase service account JSON

## Milestones

- [x] **Milestone 1**: Project Setup & Foundations
- [ ] **Milestone 2**: Authentication & User Profiles
- [ ] **Milestone 3**: Create Lyric Challenges
- [ ] **Milestone 4**: Play Challenges
- [ ] **Milestone 5**: Leaderboards & Social Features
- [ ] **Milestone 6**: Final Polish, Accessibility, and Deployment

## Troubleshooting

### Common Issues

1. **Database connection errors**: Ensure PostgreSQL is running and credentials in `.env` are correct
2. **Firebase authentication fails**: Verify Firebase config values in `.env`
3. **CORS errors**: Check that `CORS_ALLOWED_ORIGINS` in Django settings includes your frontend URL
4. **Module not found**: Ensure all dependencies are installed (`npm install` and `pip install -r requirements.txt`)

## Team Members

- Anijah Dancer
- Preston Frazier
- Sumayia Moore
- Pierre Merry
- David Mack

## License

[Add your license here]


