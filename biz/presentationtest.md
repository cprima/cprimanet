---
layout: presentation_v1.2.2
theme: solarized
ticker___: foobar
self-contained: false
titleimagefull: "/app/phy/RPA-publications/ProjectBasturmaBlueprint/images/cprima_pipelines_valves_nodes_fe463353-c3ea-484c-a68c-21ad1189e24e.png"
---

<section><h2>title slide 1</h2>Slide 1</section>
<section><h2>title slide 2</h2>Slide 2</section>

<section data-ticker='{"visibility": "visible", "_tickertext__": "foobar" }' >
    <h1>Slide 3</h1>
</section>

<section data-ticker='{"text": "Ticker Content for Section 4"}'>
    <h1>Slide 4</h1>
</section>

<section data-ticker='{"text": "Ticker Content for Section 5"}' >
    <h1>Slide 5</h1>
</section>

<section data-lower-third='{"visibility": "expanded", "layout": "one-line", "content": {"line1": "Foobar"}}'>
    <h1>Slide 6</h1>
</section>

<section>
<h2>Slide with wordcloud</h2>
<p class="stretch" wordcloud-activate="once" wordcloud='{ "minRotation": 0.1, "maxRotation": 0.9, "rotateRatio": 0.8, "rotationSteps": 99, "color": "random-dark", "backgroundColor": "" }'>
30 Les Misérables
20 Victor Hugo
15 Jean Valjean
15 Javert
15 Fantine
15 Cosette
12 Éponine
12 Marius
12 Enjolras
10 Thénardiers
10 Gavroche
10 Bishop Myriel
10 Patron-Minette
10 God
8 ABC Café
8 Paris
8 Digne
8 Elephant of the Bastille
5 silverware
5 Bagne of Toulon
5 loaf of bread
5 Rue Plumet
5 revolution
5 barricade
4 sewers
4 Fex urbis lex orbis
</p>
</section>



<section data-lower-third='{"visibility": "collapsed", "layout": "two-line", "content": {"line1": "Title", "line2": "Subtitle"}}'>
<h2>Example Code</h2>
<pre class="r-stretch r-fit-text"><code data-trim data-noescape>
# Load the project.json file as a JSON object from the specified or default directory
$projectJsonPath = Join-Path -Path $DirectoryPath -ChildPath "project.json"
$projectJson = Get-Content $projectJsonPath -Raw | ConvertFrom-Json

# Retrieve the latest commit message from the git log
$commitMessage = (cd $DirectoryPath && git log --format=%B -n 1) -join " "

# Increment the Semantic Version based on the latest commit message
$incrementedVersion = Increment-SemVer -semVerString $projectJson.projectVersion -commitMessage $commitMessage

# Update the projectVersion in the JSON object
$projectJson.projectVersion = $incrementedVersion

# Convert the JSON object back to a JSON formatted string and save it to the project.json file in the specified or default directory
$projectJson | ConvertTo-Json -Depth 99 | Set-Content $projectJsonPath

# Stage the modified project.json for commit, suppressing e.g. untracked file output
git add $projectJsonPath 2>$null

# Commit the version update to the repository with a message noting the new version number
git commit -m "Version bump in project.json to new version $incrementedVersion" --quiet

# Push the commit to the remote repository
# Uncomment if you really want this script to push
#git push</code></pre>

</section>
