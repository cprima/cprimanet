#!/bin/bash

# Define paths
RepoRoot="$(git rev-parse --show-toplevel)"
HooksDir="$RepoRoot/.git/hooks"
HookScriptPath="$RepoRoot/app/phy/scripts/githooks/pre-commit.ps1"

# Ensure the hooks directory exists
mkdir -p "$HooksDir"

# Copy the pre-commit hook
PreCommitHookPath="$HooksDir/pre-commit"
cp "$HookScriptPath" "$PreCommitHookPath"

# Make the hook executable
chmod +x "$PreCommitHookPath"

echo "Git hooks are set up."
