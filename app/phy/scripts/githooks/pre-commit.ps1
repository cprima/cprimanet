# Define paths
$RepoRoot = git rev-parse --show-toplevel
$TargetDir = Join-Path $RepoRoot "biz/marketing/website/_includes/slides"

# Ensure the target directory exists
if (-not (Test-Path $TargetDir)) {
    New-Item -ItemType Directory -Path $TargetDir -Force | Out-Null
}

# Find and process markdown files, excluding 'biz/marketing/website/_site'
Get-ChildItem -Path $RepoRoot -Filter "*.md" -Recurse | Where-Object {
    $_.DirectoryName -match 'resources[/\\]slides' -and
    $_.FullName -notmatch 'biz[/\\]marketing[/\\]website[/\\]_site'
} | ForEach-Object {
    $relativePath = $_.FullName.Substring($RepoRoot.Length + 1)
    $NewFileName = $relativePath -replace "[/\\]", "_"
    $Destination = Join-Path $TargetDir $NewFileName
    Copy-Item -Path $_.FullName -Destination $Destination

    # Add the copied file to the Git index
    git add $Destination
}
