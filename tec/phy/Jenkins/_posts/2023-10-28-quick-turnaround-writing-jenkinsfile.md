---
title: "Quick Turnaround Time Writing a Jenkinsfile on a Remote Raspberry Pi Installation"
---

Working on Jenkinsfiles can sometimes be time-consuming, especially if you're used to a tight feedback loop in other areas of software development. One of the challenges is that testing Jenkinsfiles often involves pushing changes to a Git repository, triggering a build in Jenkins, and then observing the results. This becomes even more challenging when your Jenkins instance is installed on a remote Raspberry Pi. But fear not! This guide will walk you through achieving quick turnaround times when writing and testing Jenkinsfiles on a remote Raspberry Pi installation.

## Prerequisites:

1. A Raspberry Pi with Jenkins installed.
2. Basic knowledge of Git.
3. SSH access to your Raspberry Pi.
4. A local Git repository you wish to integrate with Jenkins.

## Step-by-step Guide:

1. **Local Git Repository**:

   - We'll start by pointing Jenkins to a local Git repository on your Raspberry Pi.
   - In Jenkins, create a new pipeline job.
   - Under the "Pipeline" section, choose "Pipeline script from SCM" and select "Git" as the SCM.
   - Provide the local path to your Git repository in the "Repository URL" field. The format should be: `file:///path/to/your/repo`. If your repository is, for instance, located at `/srv/repos/github.com/rpapub`, input `file:///srv/repos/github.com/rpapub`.

2. **Allow Local Repository Checkout**:

   - By default, Jenkins might restrict checking out from local repositories due to security concerns. To overcome this, we have to set a specific property.
   - Connect to your Raspberry Pi using SSH.
   - Create a directory for Jenkins service overrides:
     ```bash
     sudo mkdir -p /etc/systemd/system/jenkins.service.d/
     ```
   - Edit the override file:
     ```bash
     sudo nano /etc/systemd/system/jenkins.service.d/override.conf
     ```
   - Add the following lines:
     ```
     [Service]
     Environment="JAVA_OPTS=-Djava.awt.headless=true -Dmail.smtp.starttls.enable=true -Dhudson.plugins.git.GitSCM.ALLOW_LOCAL_CHECKOUT=true"
     ```
   - Save the file and exit the editor.

3. **Repository Directory and Permissions**:

   - Set up the directory for your local repository:
     ```bash
     sudo mkdir -p /srv/repos/github.com/rpapub
     ```
   - Adjust ownership and permissions:
     ```bash
     sudo chown -R jenkins:jenkins /srv/repos/github.com/rpapub
     sudo chgrp sudo /srv/repos/github.com/rpapub
     sudo chmod 2775 /srv/repos/github.com/rpapub
     ```

4. **Initialize Your Repository**:

   - If you haven't set up your local Git repository, you can clone your existing GitHub repo:
     ```bash
     cd /srv/repos/github.com/rpapub
     git clone https://github.com/yourusername/yourreponame.git .
     ```

5. **Testing**:

   - Create a new branch specifically for testing:
     ```bash
     git checkout -b test-branch
     ```

6. **Restart Jenkins**:
   - For changes to take effect, restart Jenkins:
     ```bash
     sudo systemctl daemon-reload
     sudo systemctl restart jenkins
     ```

## Wrapping Up

With the steps above, you've set up an environment on your Raspberry Pi where you can quickly iterate on your Jenkinsfile. By using a local repository and allowing local checkouts, you can avoid the overhead of pushing changes to a remote repository for every small modification. This approach is not only efficient but also eases the process of writing and refining Jenkinsfiles.

Remember, while this approach is great for testing and development, it's always good practice to push finalized Jenkinsfiles to a central repository, ensuring that your CI/CD processes are consistent and tracked.

Happy coding!
