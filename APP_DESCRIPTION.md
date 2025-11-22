# 🎵 LyrIQ - The Lyric Challenge Game

## What is LyrIQ?

**LyrIQ** is a web-based lyric-guessing game where music lovers test their knowledge by completing missing lyrics from their favorite songs. Think "Finish the Lyric" meets competitive gaming!

---

## 🎯 Core Concept

Users create "Finish the Lyric" challenges by:
1. Searching for songs using Spotify
2. Selecting lyrics to blank out
3. Creating challenges for others to play

Players then:
1. Browse available challenges
2. Try to complete the missing lyrics
3. Earn points and climb the leaderboard

---

## ✨ Key Features

### 🎮 Challenge Creation
- **Spotify Integration**: Search millions of songs directly from Spotify
- **Lyric Selection**: Choose which part of the lyrics to blank out
- **Custom Hints**: Add optional hints to help players
- **Easy Sharing**: Challenges are automatically public for others to play

### 🎯 Gameplay
- **Play Any Challenge**: Browse and play challenges created by the community
- **Smart Answer Checking**: System handles minor spelling/grammar variations
- **Hint System**: Request hints (reduces score) or reveal the answer
- **Multiple Attempts**: Try again if you get it wrong (score decreases with attempts)

### 📊 Scoring System
- **Base Score**: 100 points for correct answer
- **Hint Penalty**: -50% if hint is used
- **Attempt Penalty**: -10 points per additional attempt
- **Minimum Score**: 0 (can't go negative)

### 🏆 Leaderboard & Stats
- **Global Leaderboard**: See top players ranked by total score
- **Personal Stats**: Track your accuracy, songs played, and challenges created
- **Real-time Updates**: Leaderboard refreshes automatically
- **Top 3 Highlight**: Special display for top performers

### 👤 User Profiles
- **Automatic Creation**: Profile created on first login
- **Google Sign-in**: Quick authentication with Google account
- **Stats Tracking**: 
  - Total score
  - Songs played
  - Accuracy percentage
  - Challenges created
  - Member since date

---

## 🎨 User Experience

### For Challenge Creators
1. **Search**: Type song name or artist in Spotify search
2. **Select**: Pick a song from results
3. **Get Lyrics**: System fetches lyrics automatically
4. **Choose Blank**: Click and drag to select text to blank out
5. **Add Hint** (optional): Provide a helpful hint
6. **Publish**: Challenge is live for others to play!

### For Players
1. **Browse**: View all available challenges
2. **Search**: Find challenges by song, artist, or creator
3. **Play**: Read the lyrics with blanks
4. **Answer**: Type your guess
5. **Get Feedback**: Instant feedback (correct/incorrect)
6. **Earn Points**: Score points for correct answers
7. **Compete**: Climb the global leaderboard

---

## 🛠️ Technical Features

### Frontend
- **React 18** with TypeScript
- **Material UI** for beautiful, responsive design
- **Firebase Authentication** for secure login
- **Responsive Design** - works on desktop, tablet, and mobile
- **Real-time Updates** - leaderboard refreshes automatically

### Backend
- **Django REST API** for robust backend
- **PostgreSQL** database for reliable data storage
- **Spotify Web API** integration for song search
- **Lyrics API** for fetching song lyrics
- **Firebase Admin SDK** for authentication

### Security
- **Protected Routes** - only authenticated users can create/play
- **Firebase Authentication** - secure Google Sign-in
- **CORS Protection** - secure API access
- **Input Validation** - all data validated before saving

---

## 🎯 Target Users

### 🎵 The Music Lover (Jordan)
- Loves testing music knowledge
- Enjoys discovering new songs
- Wants to compete with friends
- **Use Case**: Play challenges daily, try to beat high scores

### 🎨 The Challenge Creator (Alex)
- Creative and enjoys making content
- Wants to share favorite songs
- Likes seeing others play their challenges
- **Use Case**: Create challenges from favorite songs, share with community

### 🎮 The Casual Player (Taylor)
- Plays occasionally for fun
- Not too competitive
- Enjoys simple, quick games
- **Use Case**: Play a few challenges when bored, check leaderboard occasionally

---

## 🚀 How It Works

### Challenge Flow
```
1. Creator searches Spotify → Finds song
2. System fetches lyrics → Displays full lyrics
3. Creator selects text → Creates blank
4. Challenge saved → Available to play
5. Players see challenge → Submit answers
6. System checks answer → Awards points
7. Stats updated → Leaderboard refreshed
```

### Answer Checking
- **Exact Match**: Perfect match = correct
- **Case Insensitive**: "Hello" = "hello" = "HELLO"
- **Partial Match**: If answer is contained in correct answer (or vice versa)
- **Flexible**: Handles minor variations

### Scoring Example
```
First attempt, no hint: 100 points
Second attempt, no hint: 90 points
First attempt, with hint: 50 points
Second attempt, with hint: 40 points
```

---

## 📱 Platform Support

- **Desktop**: Full experience, all features
- **Tablet**: Optimized layout, touch-friendly
- **Mobile**: Responsive design, works on phones

---

## 🎨 Design Philosophy

- **Clean & Modern**: Material UI design system
- **User-Friendly**: Intuitive interface, easy to navigate
- **Fast**: Optimized for quick loading and responses
- **Accessible**: Keyboard navigation, screen reader support
- **Responsive**: Works on all screen sizes

---

## 🔮 Future Enhancements

Planned features (not yet implemented):
- **Real-time Multiplayer**: Battle friends in live lyric challenges
- **Genre Packs**: Pre-made challenge collections by genre
- **Audio Previews**: Play song snippets via Spotify
- **Achievements & Badges**: Unlock rewards for milestones
- **Streak Tracking**: Daily challenge streaks
- **Social Features**: Follow friends, share challenges
- **Challenge Collections**: Create playlists of challenges

---

## 🎓 Educational Value

LyrIQ isn't just fun - it's also educational:
- **Music Discovery**: Find new songs through challenges
- **Lyric Appreciation**: Pay attention to song lyrics
- **Memory Training**: Remember lyrics from favorite songs
- **Cultural Learning**: Explore music from different genres and eras

---

## 🏗️ Architecture

### Tech Stack
- **Frontend**: React + TypeScript + Vite + Material UI
- **Backend**: Django + Django REST Framework
- **Database**: PostgreSQL
- **Authentication**: Firebase Authentication
- **APIs**: Spotify Web API, Lyrics APIs
- **Hosting**: Firebase Hosting (frontend), Render (backend)

### Project Structure
```
lyriq/
├── Frontend (React)
│   ├── Pages (Home, Login, Profile, Create, Play, Leaderboard)
│   ├── Components (Layout, Protected Routes)
│   └── Contexts (Authentication)
│
└── Backend (Django)
    ├── API (Users, Challenges, Leaderboard)
    ├── Services (Spotify, Lyrics)
    └── Models (User, Challenge, Attempt)
```

---

## 🎯 Why LyrIQ?

- **Fun**: Engaging gameplay for music lovers
- **Social**: Compete with friends and community
- **Creative**: Create your own challenges
- **Educational**: Discover new music and lyrics
- **Free**: No cost to play or create
- **Accessible**: Works on any device with a browser

---

## 🎵 Get Started

1. **Sign In**: Use Google account (one-click login)
2. **Explore**: Browse available challenges
3. **Play**: Try to complete the lyrics
4. **Create**: Make your own challenges
5. **Compete**: Climb the leaderboard!

---

**LyrIQ - Where Music Knowledge Meets Fun Competition! 🎵🏆**


