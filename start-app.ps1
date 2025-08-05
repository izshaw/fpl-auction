# FPL Auction App Starter Script for Windows PowerShell

Write-Host "Starting FPL Auction App..." -ForegroundColor Green

# Check if .env exists in backend
$envPath = ".\backend\.env"
if (-not (Test-Path $envPath)) {
    Write-Host "Creating .env file..." -ForegroundColor Yellow
    @"
DATABASE_URL="file:./dev.db"
JWT_SECRET="your-secret-key-change-in-production"
FRONTEND_URL="http://localhost:3000"
PORT=5000
"@ | Out-File -FilePath $envPath -Encoding utf8
}

# Start Backend
Write-Host "`nStarting Backend Server..." -ForegroundColor Cyan
$backendScript = @"
cd backend
Write-Host 'Backend Terminal' -ForegroundColor Magenta
Write-Host 'Installing dependencies...' -ForegroundColor Yellow
npm install
Write-Host 'Setting up database...' -ForegroundColor Yellow
npx --yes prisma generate
npx --yes prisma migrate dev --name init
Write-Host 'Starting server...' -ForegroundColor Green
npm run dev
"@
Start-Process powershell -ArgumentList @("-NoExit", "-Command", $backendScript)

# Wait a bit for backend to start
Start-Sleep -Seconds 5

# Start Frontend
Write-Host "Starting Frontend Server..." -ForegroundColor Cyan
$frontendScript = @"
cd frontend
Write-Host 'Frontend Terminal' -ForegroundColor Blue
Write-Host 'Installing dependencies...' -ForegroundColor Yellow
npm install
Write-Host 'Starting server...' -ForegroundColor Green
npm run dev
"@
Start-Process powershell -ArgumentList @("-NoExit", "-Command", $frontendScript)

Write-Host "`nBoth servers are starting!" -ForegroundColor Green
Write-Host "Backend will be at: http://localhost:5000" -ForegroundColor Yellow
Write-Host "Frontend will be at: http://localhost:3000" -ForegroundColor Yellow
Write-Host "`nOpening browser in 10 seconds..." -ForegroundColor Cyan

Start-Sleep -Seconds 10
Start-Process "http://localhost:3000"

Write-Host "`nTo stop the servers, close the terminal windows or press Ctrl+C in each." -ForegroundColor Gray 