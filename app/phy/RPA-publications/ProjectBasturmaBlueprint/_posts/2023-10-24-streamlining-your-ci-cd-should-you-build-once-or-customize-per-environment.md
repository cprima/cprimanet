---
title: "Streamlining Your CI/CD: Should You Build Once or Customize per Environment?"
---

Building and deploying software packages to various environments is a common challenge in the software delivery lifecycle. Whether you build a package separately for each environment or build once and deploy multiple times largely depends on the needs of the organization and the nature of the application. Let's explore both strategies and their pros and cons:

### 1. Build Once, Deploy Many Times:

This is the principle of creating an immutable artifact. Once a version of your software has been built, it's packaged into an artifact that is not modified as it's promoted through various environments.

**Pros:**

- **Consistency**: The exact same artifact is deployed to all environments, reducing the chances of inconsistencies or "it works on my machine" issues.
- **Efficiency**: Building once reduces the computational and time cost of repeated builds.
- **Simplicity**: Fewer steps and processes to manage.

**Cons:**

- **Flexibility**: It might be harder to have environment-specific configurations embedded in the software. However, this is often addressed by externalizing configurations and using environment variables or configuration servers.

**Examples**: Many modern CI/CD best practices advocate for this approach, especially when using containerization tools like Docker. For instance, once a Docker image is built, it can be pushed to a registry and then pulled into various environments without being rebuilt.

### 2. Build Separately for Each Environment:

In this approach, you'd have separate build processes for each environment (e.g., test, staging, prod), potentially with different configurations or even code branches.

**Pros:**

- **Customization**: Allows for environment-specific optimizations or configurations at the build level.
- **Isolation**: Changes in one environment's build process don't affect others.
- **Safety**: In cases where the production build process includes extra security or compliance checks, it ensures these are always run.

**Cons:**

- **Inconsistency**: Risk of differences between environments due to separate builds, which can lead to unforeseen issues.
- **Overhead**: More computational and time cost, as well as added complexity in managing multiple build processes.

**Examples**: Some legacy applications that have deep environment-specific configurations might employ this method. Additionally, some organizations with stringent compliance requirements might have an entirely separate build process for production.

### Considerations for Versioning:

- If you're building once and deploying many times, the version typically remains consistent across environments.
- If you're building separately for each environment, it's a choice:
  - You can keep the same version number if the core application hasn't changed.
  - You can increment versions to reflect build/environment-specific changes.

### Background:

Traditionally, especially before the rise of containers and microservices, it wasn't uncommon for organizations to build separately for each environment, as applications were monolithic and often had deep-rooted environment-specific configurations. However, with the growth of the DevOps movement and technologies like Docker, the trend has shifted towards "build once, deploy many times" to ensure consistency and reduce potential points of failure.

### Conclusion:

For most modern applications, especially those designed with the 12-factor app principles in mind, the "build once, deploy many times" approach is recommended. It ensures consistency, is more efficient, and aligns well with containerized deployments. However, specific use cases, legacy applications, or compliance requirements might necessitate separate builds for different environments.
