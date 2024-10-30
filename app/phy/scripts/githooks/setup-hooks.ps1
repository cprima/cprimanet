# Define paths
$RepoRoot = git rev-parse --show-toplevel
$HooksDir = Join-Path $RepoRoot ".git/hooks"
$HookScriptPath = Join-Path $RepoRoot "app/phy/scripts/githooks/pre-commit.ps1"

# Ensure the hooks directory exists
if (-not (Test-Path $HooksDir)) {
    New-Item -ItemType Directory -Path $HooksDir | Out-Null
}

# Determine the shell script to create based on the platform
$PreCommitHookPath = Join-Path $HooksDir "pre-commit"
if ([System.Environment]::OSVersion.Platform -eq [System.PlatformID]::Win32NT) {
    $ScriptContent = "@echo off`r`npwsh -NoProfile -ExecutionPolicy Bypass -File `"$HookScriptPath`"`r`n"
} else {
    $ScriptContent = "#!/bin/sh`npwsh -NoProfile -ExecutionPolicy Bypass -File `"$HookScriptPath`"`n"
}

# Write the script to the pre-commit hook file
Set-Content -Path $PreCommitHookPath -Value $ScriptContent

# Make sure the hook is executable (important on Unix-like systems)
if (-Not [System.Environment]::OSVersion.Platform -eq [System.PlatformID]::Win32NT) {
    chmod +x $PreCommitHookPath
}

Write-Host "Git hooks are set up."
