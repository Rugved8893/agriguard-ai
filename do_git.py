import subprocess
import os

os.chdir(r"C:\Users\HP\OneDrive\Documents\Desktop\AgricultureManagement System")

# Step 1: git add -A
print("=== Running: git add -A ===")
result = subprocess.run(["git", "add", "-A"], capture_output=True, text=True, shell=True)
print("STDOUT:", result.stdout)
print("STDERR:", result.stderr)

# Step 2: git commit
print("\n=== Running: git commit ===")
msg = "Added SQLite database with comprehensive agricultural data"
result = subprocess.run(["git", "commit", "-m", msg], capture_output=True, text=True, shell=True)
print("STDOUT:", result.stdout)
print("STDERR:", result.stderr)

# Step 3: git push
print("\n=== Running: git push ===")
result = subprocess.run(["git", "push", "origin", "main"], capture_output=True, text=True, shell=True)
print("STDOUT:", result.stdout)
print("STDERR:", result.stderr)

print("\n=== COMPLETE ===")

