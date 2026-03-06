@echo off
cd /d "%~dp0"
echo.
echo ================================================
echo Pushing changes to GitHub...
echo ================================================
echo.
git push origin main
echo.
echo ================================================
echo Done! Check the output above for any errors.
echo ================================================
pause

