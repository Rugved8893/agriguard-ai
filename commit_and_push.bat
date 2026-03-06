@echo off
cd /d "C:\Users\HP\OneDrive\Documents\Desktop\AgricultureManagement System"
echo === Git Status ===
git status
echo.
echo === Git Add ===
git add -A
echo.
echo === Git Commit ===
git commit -m "Updated AgriGuard AI project for presentation"
echo.
echo === Git Push ===
git push origin main
echo.
echo === DONE ===
pause

