@echo off
echo Starting FPL Auction App...

REM Check if .env exists
if not exist "backend\.env" (
    echo Creating .env file...
    (
        echo DATABASE_URL="file:./dev.db"
        echo JWT_SECRET="your-secret-key-change-in-production"
        echo FRONTEND_URL="http://localhost:3000"
        echo PORT=5000
    ) > backend\.env
)

REM Start Backend
echo.
echo Starting Backend Server...
start "FPL Backend" cmd /k "cd backend && npm install && npx --yes prisma generate && npx --yes prisma migrate dev --name init && npm run dev"

REM Wait a bit
timeout /t 5 /nobreak > nul

REM Start Frontend
echo Starting Frontend Server...
start "FPL Frontend" cmd /k "cd frontend && npm install && npm run dev"

echo.
echo Both servers are starting!
echo Backend: http://localhost:5000
echo Frontend: http://localhost:3000
echo.
echo Opening browser in 10 seconds...
timeout /t 10 /nobreak > nul

start http://localhost:3000

echo.
echo To stop servers, close the command windows.
pause 