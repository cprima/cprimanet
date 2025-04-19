# Fetch all changes from all remotes
git fetch --all

# Get a list of all remote-tracking branches
$remoteBranches = git branch -r | Select-String -Pattern 'origin/'

# Create local branches to track remote branches, if not already existing
foreach ($remoteBranch in $remoteBranches) {
    $localBranch = $remoteBranch -replace 'origin/', ''
    $localBranch = $localBranch.Trim()

    # Check if the local branch already exists
    $localExists = git branch | Select-String -Pattern "^\\s*$localBranch$"

    if ($null -eq $localExists) {
        # Local branch does not exist, create it to track the remote branch
        git checkout -b $localBranch "origin/$localBranch"
    }
}
