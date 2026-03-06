@echo off
cd /d "%~dp0"
echo === Git Status ===
git status
echo.
echo === Git Log (last 3 commits) ===
git log --oneline -3
pause

