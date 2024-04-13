pipeline {
    // Specifies the agent requirements. This ensures the build runs on an agent with Windows, UiPath, and build capabilities.
    agent {
        label 'windows && uipath && build'
    }

    // Define user input parameters that can be passed to the pipeline when triggered.
    parameters {
        booleanParam(name: 'FORCE_REBUILD', defaultValue: false, description: 'Force a rebuild regardless of other conditions')
        booleanParam(name: 'SKIP_TESTS', defaultValue: false, description: 'Skip test execution for this build')
        choice(name: 'REVIEW_STATUS', choices: ['pending', 'approved', 'rejected'], description: 'Review status for the changes')
    }

    // Once set, environment variables in a declarative pipeline cannot be modified or unset.
    environment {
        FOO = ''
    }

    stages {
stage('Set Environment Variables') {
    steps {
        script {
            echo "Debug: Starting the 'Set Environment Variables' stage."

            // Check if env.payload is set
            if (env.payload) {
                echo "Debug: Payload detected."
                echo "Full payload: ${env.payload}"
                def parsedPayload
                try {
                    parsedPayload = readJSON text: env.payload
                    echo "Debug: Payload successfully parsed as JSON."
                } catch (Exception e) {
                    echo "Debug: Failed to parse payload as JSON. Error: ${e.getMessage()}"
                }

// Handle JSONArray
if (parsedPayload instanceof net.sf.json.JSONArray) {
    echo "Debug: Payload is a JSONArray."

    boolean valuesFound = false
    for (item in parsedPayload) {
        if (valuesFound) break  // Exit the loop if the values have been found

        echo "item is: ${item}"

        if (item instanceof net.sf.json.JSONObject) { // Check if item is a JSONObject

            // // Print all the keys of the JSONObject
            // item.keySet().each { key ->
            //     echo "Key found: ${key}"
            // }

            try {
                if (item.containsKey('full_name')) {
                    echo "##########################################"
                    def parts = item.full_name.split('/')
                    echo "Debug: parts is: ${parts}"
                    echo "Parts: ${parts[0]} and ${parts[1]}."
                    if (parts.size() == 2) {
                        env.GITHUB_ORGANIZATION = parts[0]
                        env.GITHUB_REPO = parts[1]
                        echo "Debug: Set GITHUB_ORGANIZATION to ${env.GITHUB_ORGANIZATION} and GITHUB_REPO to ${env.GITHUB_REPO} from 'full_name' value."
                        valuesFound = true  // Set the flag indicating the values have been found
                        return  // Exit the current iteration
                    } else {
                        echo "Debug: 'full_name' does not have the expected format."
                    }
                } else {
                    echo "Debug: An item in the payload JSON array does not contain expected keys."
                }
            } catch(Exception e) {
                echo "Debug: Exception caught while processing JSONArray item. Message: ${e.message}. Item: ${item}"
            }
        } else {
            echo "Debug: Skipping item since it's not a JSONObject. It's a ${item.getClass().getName()}"
        }
    }
}


 else {
                    echo "Debug: The parsed payload is neither a JSONObject nor a JSONArray."
                }
            } 
            // If the trigger is from the GitHub plugin, set the values
            else if (env.CHANGE_URL?.startsWith('https://github.com/')) {
                echo "Debug: Detected CHANGE_URL, likely triggered by GitHub plugin."
                // Extract organization and repo from the CHANGE_URL
                def matcher = (env.CHANGE_URL =~ /^https:\/\/github\.com\/([^\/]+)\/([^\/]+)/)
                if (matcher.matches()) {
                    params.GITHUB_ORGANIZATION = matcher[0][1]
                    params.GITHUB_REPO = matcher[0][2]
                    echo "Debug: Extracted GITHUB_ORGANIZATION as ${params.GITHUB_ORGANIZATION} and GITHUB_REPO as ${params.GITHUB_REPO} from CHANGE_URL."
                } else {
                    echo "Debug: Failed to extract organization and repo details from CHANGE_URL."
                }
            } else {
                echo "Debug: Neither payload nor CHANGE_URL set. Cannot determine GitHub organization or repo."
            }

            echo "Debug: End of the 'Set Environment Variables' stage."
        }
    }
}



        stage('Validation') {
            steps {
                script {
                    // Check if GITHUB_ORGANIZATION is not empty
                    if (env.GITHUB_ORGANIZATION == '' || env.GITHUB_ORGANIZATION == null) {
                        error("GITHUB_ORGANIZATION is empty. Please provide a valid value.")
                    }

                    // Check if GITHUB_REPO is not empty
                    if (env.GITHUB_REPO == '' || env.GITHUB_REPO == null) {
                        error("GITHUB_REPO is empty. Please provide a valid value.")
                    }

                    // Echo the TRIGGER_TYPE
                    echo "Trigger Type: ${env.TRIGGER_TYPE}"

                    // If TRIGGER_TYPE is 'webhook', then determine what type triggered it
                    if (env.TRIGGER_TYPE == 'webhook') {
                        switch (env.WEBHOOK_SOURCE) {
                            case 'merge':
                                echo "Triggered by a merge event."
                                break
                            case 'pull_request':
                                echo "Triggered by a pull request event."
                                break
                            // Add other webhook event types here as necessary
                            default:
                                echo "Unknown webhook event type: ${env.WEBHOOK_SOURCE}"
                                break
                        }
                    }
                }
            }
        }

        // Initialization stage sets up the environment and checks preconditions.
        stage('Initialization') {
            steps {
                script {
                    echo 'Initializing the build...'
                    // Read the UiPath project's metadata from the project.json.
                    def projectJson = readJSON file: 'project.json'
                    env.BUILD_NUMBER = projectJson.projectVersion
                    echo "Using version from project.json: ${env.BUILD_NUMBER}"

                    // Increment the version number.
                    def (major, minor, patch) = env.BUILD_NUMBER.split(/\./).collect { it.toInteger() }
                    patch++
                    env.BUILD_NUMBER = "${major}.${minor}.${patch}"
                    echo "Incremented version: ${env.BUILD_NUMBER}"

                    if (env.REVIEW_STATUS != 'approved' && env.APPROVAL_REQUIRED) {
                        error("Review is not approved. Halting the build.")
                    }
                }
            }
        }

        // Allows for a manual review step before the build if the conditions are met.
        stage('Review and Approval') {
            when {
                expression { env.APPROVAL_REQUIRED }
            }
            steps {
                script {
                    echo 'Waiting for review and approval...'
                    // Logic to wait for review and approval
                }
            }
        
        }

        // This stage is responsible for cloning the specified GitHub repository.
        stage('Clone Repository') {
            when {
                not {
                    allOf {
                        expression { env.GITHUB_ORGANIZATION.isEmpty() }
                        expression { env.GITHUB_REPO.isEmpty() }
                    }
                }
            }
            steps {
                script {
                    echo "Cloning repository from https://github.com/${env.GITHUB_ORGANIZATION}/${env.GITHUB_REPO}"
                    git branch: "main", url: "https://github.com/${env.GITHUB_ORGANIZATION}/${env.GITHUB_REPO}"
                }
            }
        }


        // Main building process for the UiPath project.
        stage('Build UiPath Project') {
            steps {
                script {
                    echo 'Building the UiPath project...'
                    // Dummy step; this would involve invoking UiPath's CLI or any other method to actually perform the build
                    echo 'Build successful!'
                }
            }
        }

        // Allows for a manual review step after the build and before deployment if conditions are met.
        stage('Post-Build Operations') {
            when {
                expression { env.APPROVAL_REQUIRED }
            }
            steps {
                script {
                    echo 'Waiting for post-build review...'
                    // Logic to wait for post-build review
                }
            }
        }


        // Deals with environment-specific configurations and deploys the UiPath project.
        stage('Environment Parameterization & Deployment') {
            steps {
                script {
                    echo 'Deploying the UiPath project...'
                    // Dummy step; this would involve invoking UiPath's CLI or any other method to actually perform the deployment
                    echo 'Deployment successful!'
                }
            }
        }


        // Runs automated tests unless they are skipped.
        stage('Automated Testing') {
            when {
                not {
                    expression { env.SKIP_TESTS }
                }
            }
            steps {
                script {
                    echo 'Running automated tests...'
                    // Dummy step; this would involve invoking UiPath's CLI or any other method to actually run the tests
                    echo 'Tests successful!'
                }
            }
        }

        // Sends notifications to stakeholders or other systems about the build status.
        stage('Notifications') {
            steps {
                echo 'Sending notifications...'
                // Logic to send notifications based on build results
            }
        }

        // Generates and archives build-related documents and reports.
        stage('Documentation & Reporting') {
            steps {
                echo 'Generating documentation and reports...'
                // Generate any required documentation, logs, or reports
            }
        }
    }

    // Post-build actions to be taken irrespective of the build outcome.
    post {
        // Cleanup actions that need to be taken after every build.
        always {
            echo 'Cleaning up resources...'
            // Logic for cleaning up any temporary files or resources
        }
        // Actions to be taken if the build is successful.
        success {
            echo 'Build completed successfully!'
        }
        // Actions to be taken if the build fails.
        failure {
            echo 'Build failed!'
        }
    }
}
