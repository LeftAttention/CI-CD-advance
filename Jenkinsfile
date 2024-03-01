pipeline {
    agent any

    environment {
        // Define your environment variables here
    }

    stages {
        stage('Build') {
            steps {
                script {
                    // Use a virtual environment for Python projects
                    sh 'python -m venv venv'
                    sh '. venv/bin/activate'
                    sh 'pip install -r requirements.txt'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    sh '. venv/bin/activate'
                    sh 'pytest'
                }
            }
            post {
                always {
                    junit 'tests/*.xml' // Adjust the path to where your test results are stored
                }
            }
        }

        stage('Deploy') {
            when {
                branch 'main'
            }
            steps {
                script {
                    // Add your deployment script here
                    echo 'Deploying application...'
                    // Example: sh './deploy_staging.sh'
                }
            }
        }
    }

    triggers {
        // This triggers a build on changes to the main branch
        pollSCM('H/5 * * * *')
    }

    post {
        failure {
            // Send an email if the build fails
            mail to: 'youremail@example.com',
                 subject: "Failed Pipeline: ${currentBuild.fullDisplayName}",
                 body: "Something is wrong with ${env.BUILD_URL}"
        }
        success {
            // Send an email if the build succeeds
            mail to: 'youremail@example.com',
                 subject: "Successful Pipeline: ${currentBuild.fullDisplayName}",
                 body: "Great news! The build was successful. ${env.BUILD_URL}"
        }
    }
}
