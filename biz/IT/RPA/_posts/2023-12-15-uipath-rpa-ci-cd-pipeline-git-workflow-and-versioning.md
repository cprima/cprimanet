---
layout: post
title: "Git Workflow and Versioning"
date: 2023-12-15
---

## Git Workflow with Versioning and Repository Setup

### Initial Repository Setup

- **Creation**: A new repository is created from a template repository. This helps in standardizing the project structure and initial settings.
- **Initial Versioning**: The repository is initialized with the version `0.5.0`, serving as the starting point for the project's lifecycle.

### Main Branch

- **Purpose**: Hosts the stable, production-ready code.
- **Usage**: Receives updates from the integration branch for official releases.
- **Protection**: Restricted to specific roles with enforced pull request reviews and automated status checks.

### Integration Branch

- **Purpose**: Serves as a pre-production staging area.
- **Usage**: Integrates features from development branches for further testing.
- **Protection**: Enforces pull request reviews and automated checks.

### Feature/Development Branches

- **Purpose**: For new features, bug fixes, or enhancements.
- **Usage**: Branches off from main or integration for isolated development.
- **Guidelines**: Regular updates; descriptive commit messages.

### Pull Requests and Code Reviews

- **Process**: Merging changes into integration and main branches.
- **Code Reviews**: Ensure quality and adherence to standards.
- **Versioning Impact**: PR titles reflect changes for version tracking.

### Continuous Integration and Deployment (CI/CD)

- **Automated Testing**: Validates code through tests.
- **Release Management**: Tied to main branch updates; often automated.

### Documentation and Communication

- **Commit Messages/PR Descriptions**: Provide context for changes and versioning intent.

### Conclusion

This comprehensive workflow ensures effective project management, consistency, and clarity throughout the software development lifecycle.

![Git Workflow and Versioning](/biz/IT/RPA/resources/ci-cd-pipeline-git-workflow.png)

## Versioning

Semantic versioning is used to track changes in the project. The version number is stored in the project.json file in the root directory of the repository.

- **Versioning**: Major version increments for changes including "BREAKING", "BREAKING CHANGE", or "major" in commit messages or PR titles.
- **Versioning**: Minor version increments for features with "feat", "feature", or "minor".
- **Versioning**: Patch version increments for fixes or changes with "fix", "bugfix", "patch", or undefined messages.
