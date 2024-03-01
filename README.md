# cicd_assignment

Brief description of the project.

## Continuous Integration and Continuous Deployment (CI/CD)

This project is equipped with CI/CD pipelines using both Jenkins and GitHub Actions to automate the testing and deployment processes.

### Jenkins CI/CD Pipeline

#### Overview

The Jenkins pipeline automates the process of installing dependencies, running tests, and deploying the application to different environments based on the branch or conditions met.

#### Configuration

1. **Jenkinsfile**: The `Jenkinsfile` located at the root of this repository defines the pipeline in Jenkins.
   
2. **Setup**: 
   - Ensure Jenkins is installed and running.
   - Install necessary plugins (e.g., Pipeline, Git, Email Extension).
   - Set up a Jenkins job using the Pipeline type and point it to your repository.

3. **Pipeline Stages**:
   - **Build**: Installs the project dependencies.
   - **Test**: Executes the test suite using pytest.
   - **Deploy**: Deploys the application to staging or production based on the branch.

4. **Notifications**: Configured to send email notifications on success or failure.

### GitHub Actions Workflow

#### Overview

GitHub Actions automates the testing and deployment process upon certain triggers such as push to specific branches or release creation.

#### Configuration

1. **Workflow File**: The `.github/workflows/python-app.yml` file defines the GitHub Actions workflow.

2. **Triggers**:
   - Push to `staging` and `main` branches.
   - Creation of a release.

3. **Jobs**:
   - **build-and-test**: Installs dependencies and runs tests.
   - **deploy-to-staging**: Deploys to the staging environment if the push is to the `staging` branch.
   - **deploy-to-production**: Deploys to production when a release is tagged.

4. **Secrets**: Utilize GitHub Secrets to securely store and access sensitive information needed for deployments.

#### Using the Workflow

- Push code to the `staging` branch to trigger the staging deployment.
- Create a tag/release to trigger the production deployment.
