import subprocess
import os
import sys

# Change to project directory
project_dir = r"C:\Users\HP\OneDrive\Documents\Desktop\AgricultureManagement System"
os.chdir(project_dir)

results = []

# Try to find git
git_paths = [
    r"C:\Program Files\Git\cmd\git.exe",
    r"C:\Program Files (x86)\Git\cmd\git.exe",
    "git"
]

git_cmd = None
for path in git_paths:
    try:
        result = subprocess.run([path, "--version"], capture_output=True, text=True)
        if result.returncode == 0:
            git_cmd = path
            results.append(f"Found git at: {path}")
            results.append(f"Version: {result.stdout}")
            break
    except:
        continue

if not git_cmd:
    results.append("Git not found!")
else:
    # Git add
    results.append("\n--- Running: git add -A ---")
    result = subprocess.run([git_cmd, "add", "-A"], capture_output=True, text=True)
    results.append(f"stdout: {result.stdout}")
    results.append(f"stderr: {result.stderr}")
    
    # Git commit
    results.append("\n--- Running: git commit ---")
    result = subprocess.run([git_cmd, "commit", "-m", "Updated AgriGuard AI project for presentation"], capture_output=True, text=True)
    results.append(f"stdout: {result.stdout}")
    results.append(f"stderr: {result.stderr}")
    
    # Git push
    results.append("\n--- Running: git push ---")
    result = subprocess.run([git_cmd, "push", "origin", "main"], capture_output=True, text=True)
    results.append(f"stdout: {result.stdout}")
    results.append(f"stderr: {result.stderr}")
    
    results.append("\n=== COMPLETE ===")

# Write to file
with open("git_log.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(results))

print("\n".join(results))

