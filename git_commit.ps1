cd "C:\Users\HP\OneDrive\Documents\Desktop\AgricultureManagement System"
Write-Host "=== Git Status ===" -ForegroundColor Cyan
git status

Write-Host "`n=== Git Add ===" -ForegroundColor Cyan
git add -A

Write-Host "`n=== Git Commit ===" -ForegroundColor Cyan
git commit -m "Added SQLite database with comprehensive agricultural data

- Created database schema with tables for crops, diseases, regions, seasons
- Added populate_data.py to initialize database with 42 crops, 27 diseases, 15 regions
- Created db_util.py for database operations
- Updated .gitignore to exclude database files
- Added run.bat for easy project startup"

Write-Host "`n=== Git Log (last 3) ===" -ForegroundColor Cyan
git log --oneline -3

