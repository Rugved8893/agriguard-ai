import subprocess
import os

os.chdir(r"C:\Users\HP\OneDrive\Documents\Desktop\AgricultureManagement System")

output = []

# Step 1: Check git status
output.append("=== GIT STATUS ===")
result = subprocess.run(["git", "status"], capture_output=True, text=True, shell=True)
output.append(f"STDOUT: {result.stdout}")
output.append(f"STDERR: {result.stderr}")

# Step 2: git add -A
output.append("\n=== GIT ADD -A ===")
result = subprocess.run(["git", "add", "-A"], capture_output=True, text=True, shell=True)
output.append(f"STDOUT: {result.stdout}")
output.append(f"STDERR: {result.stderr}")

# Step 3: git commit
output.append("\n=== GIT COMMIT ===")
msg = "Updated AgriGuard AI project - added AI agent and enhanced models"
result = subprocess.run(["git", "commit", "-m", msg], capture_output=True, text=True, shell=True)
output.append(f"STDOUT: {result.stdout}")
output.append(f"STDERR: {result.stderr}")

# Step 4: git push
output.append("\n=== GIT PUSH ===")
result = subprocess.run(["git", "push", "origin", "main"], capture_output=True, text=True, shell=True)
output.append(f"STDOUT: {result.stdout}")
output.append(f"STDERR: {result.stderr}")

output.append("\n=== COMPLETE ===")

# Write output to file
with open("git_output.txt", "w") as f:
    f.write("\n".join(output))

print("\n".join(output))

