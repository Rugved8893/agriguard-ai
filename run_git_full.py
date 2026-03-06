import subprocess
import os
import sys

os.chdir(r"C:\Users\HP\OneDrive\Documents\Desktop\AgricultureManagement System")

output_lines = []

def run_cmd(cmd, description):
    output_lines.append(f"\n=== {description} ===")
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=60)
        output_lines.append(f"STDOUT:\n{result.stdout}")
        if result.stderr:
            output_lines.append(f"STDERR:\n{result.stderr}")
        output_lines.append(f"Return code: {result.returncode}")
    except Exception as e:
        output_lines.append(f"ERROR: {str(e)}")

# Step 1: Check git version
run_cmd("git --version", "Git Version")

# Step 2: Check git status
run_cmd("git status", "Git Status")

# Step 3: Git add
run_cmd("git add -A", "Git Add")

# Step 4: Git commit
run_cmd('git commit -m "Updated AgriGuard AI project for presentation"', "Git Commit")

# Step 5: Git push
run_cmd("git push origin main", "Git Push")

# Write to file
with open("git_operation_result.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(output_lines))

print("DONE - Check git_operation_result.txt")

