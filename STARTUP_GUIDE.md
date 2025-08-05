# 🚀 FPL Auction App - Quick Start Guide

## Step 1: Backend Setup

### 1.1 Create Environment File
Navigate to the backend folder and create a `.env` file:

```bash
cd fpl-auction/backend
```

Create a new file called `.env` with this content:
```
DATABASE_URL="file:./dev.db"
JWT_SECRET="your-secret-key-change-in-production"
FRONTEND_URL="http://localhost:3000"
PORT=5000
```

### 1.2 Install Dependencies (if not done)
```bash
npm install
```

### 1.3 Setup Database
```bash
npx prisma generate
npx prisma migrate dev --name init
```

### 1.4 Start Backend Server
```bash
npm run dev
```

The backend should now be running at `http://localhost:5000`

## Step 2: Frontend Setup (New Terminal)

### 2.1 Navigate to Frontend
Open a new terminal window:
```bash
cd fpl-auction/frontend
```

### 2.2 Install Dependencies (if not done)
```bash
npm install
```

### 2.3 Start Frontend Server
```bash
npm run dev
```

The frontend should now be running at `http://localhost:3000`

## Step 3: Access the App

Open your web browser and go to: **http://localhost:3000**

## 🎮 How to Use the App

1. **Create a Season** (Admin only - needs to be done via API or database)
2. **Create a Game**:
   - Click "Create New Game"
   - Enter game details
   - Share the join code with other players
3. **Join a Game**:
   - Enter the join code
   - Provide your name and email
4. **Start Auction** (Chairman only):
   - Once all players have joined, chairman can start
   - Nominate players
   - Place bids
   - Build your squad!

## 🔧 Troubleshooting

### If npm commands fail:
1. Make sure you're in the correct directory
2. Try using Node.js Command Prompt instead of PowerShell
3. Run as Administrator if permission errors occur

### If "Cannot find module" errors:
```bash
# In backend folder
rm -rf node_modules
npm install

# In frontend folder  
rm -rf node_modules
npm install
```

### If database errors occur:
```bash
# In backend folder
npx prisma migrate reset
```

### Port already in use:
- Backend: Change PORT in .env file
- Frontend: The dev server will offer an alternative port

## 📝 Quick Test

1. Backend health check: http://localhost:5000/health
2. Frontend should show the landing page
3. Try creating a new game to test functionality

## 🛑 Stopping the Servers

In each terminal window, press `Ctrl + C` to stop the servers. 