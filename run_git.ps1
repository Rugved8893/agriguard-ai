$ErrorActionPreference = "Continue"
$projectPath = "C:\Users\HP\OneDrive\Documents\Desktop\AgricultureManagement System"

Set-Location $projectPath

Write-Host "========================================" -ForegroundColor Green
Write-Host "GIT ADD -A" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Green
git add -A 2>&1 | Write-Host

Write-Host "========================================" -ForegroundColor Green
Write-Host "GIT COMMIT" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Green
git commit -m "Added SQLite database with comprehensive agricultural data" 2>&1 | Write-Host

Write-Host "========================================" -ForegroundColor Green
Write-Host "GIT PUSH" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Green
git push origin main 2>&1 | Write-Host

Write-Host "========================================" -ForegroundColor Green
Write-Host "ALL DONE!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green

