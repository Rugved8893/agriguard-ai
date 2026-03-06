$output = @()

# Check if git is installed
$gitPath = Get-Command git -ErrorAction SilentlyContinue
if ($gitPath) {
    $output += "Git is installed: $($gitPath.Source)"
    $output += "Git version: $(git --version)"
} else {
    $output += "Git is NOT installed"
}

# Check if GitHub CLI is installed
$ghPath = Get-Command gh -ErrorAction SilentlyContinue
if ($ghPath) {
    $output += "GitHub CLI is installed: $($ghPath.Source)"
    $output += "GitHub CLI version: $(gh --version)"
} else {
    $output += "GitHub CLI is NOT installed"
}

# Try to run git commands if available
if ($gitPath) {
    Set-Location "C:\Users\HP\OneDrive\Documents\Desktop\AgricultureManagement System"
    
    $output += ""
    $output += "=== Git Status ==="
    $output += $(git status 2>&1)
    
    $output += ""
    $output += "=== Git Add ==="
    $output += $(git add -A 2>&1)
    
    $output += ""
    $output += "=== Git Commit ==="
    $output += $(git commit -m "Updated AgriGuard AI project for presentation" 2>&1)
    
    $output += ""
    $output += "=== Git Push ==="
    $output += $(git push origin main 2>&1)
}

# Write to file
$output | Out-File -FilePath "C:\Users\HP\OneDrive\Documents\Desktop\AgricultureManagement System\git_result.txt" -Encoding UTF8
Write-Output ($output | Out-String)

