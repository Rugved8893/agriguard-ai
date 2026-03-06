#!/usr/bin/env python
"""
Git Commit Script - Commits all changes to the repository
"""
import os
import subprocess

# Change to project directory
os.chdir(r"c:\Users\HP\OneDrive\Documents\Desktop\AgricultureManagement System")

# Run git commands
commands = [
    ["git", "status"],
    ["git", "add", "-A"],
    ["git", "commit", "-m", "Added SQLite database with comprehensive agricultural data\n\n- Created database schema with tables for crops, diseases, regions, seasons\n- Added populate_data.py to initialize database with 42 crops, 27 diseases, 15 regions\n- Created db_util.py for database operations\n- Updated .gitignore to exclude database files\n- Added run.bat for easy project startup"],
    ["git", "log", "--oneline", "-3"]
]

for cmd in commands:
    print(f"\n=== Running: {' '.join(cmd)} ===")
    result = subprocess.run(cmd, capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print("STDERR:", result.stderr)

print("\n=== Done! ===")
print("Changes have been committed to the local repository.")
print("To push to GitHub, run: git push origin main")

