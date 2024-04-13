import json

# Load UiPath Workflow Analyzer results
with open('uipath-workflow-analyzer_results.json.json', 'r') as f:
    uipath_results = json.load(f)

sonarqube_results = []

severity_mapping = {
    4: 'BLOCKER',
    3: 'CRITICAL',
    2: 'MAJOR'
}

for result in uipath_results:
    issue = {}
    issue['engineId'] = 'uipath-workflow-analyzer'
    issue['ruleId'] = result['ErrorCode']
    issue['type'] = 'CODE_SMELL'  # default, can be adjusted based on your needs
    issue['severity'] = severity_mapping.get(result['ErrorSeverity'], 'MINOR')
    issue['primaryLocation'] = {
        'message': result['Description'],
        'filePath': result['FilePath'] if result['FilePath'] else 'unknown_path'
    }
    # Add recommendation as additional info if available
    if 'Recommendation' in result:
        issue['primaryLocation']['message'] += " Recommendation: " + result['Recommendation']
    sonarqube_results.append(issue)

# Save the results in Generic Issue Import Format
with open('sonarqube_input.json', 'w') as f:
    json.dump(sonarqube_results, f, indent=4)
