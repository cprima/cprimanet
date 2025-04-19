---
layout: page
title:  "Procedural Infrastructure Template"
---

<!--
This is an article template you can use as a starting point when writing DigitalOcean procedural tutorials about intrastructure. Once you've reviewed the template, delete the comments and begin writing your outline or article. You'll find some examples of our custom Markdown at the very bottom of the template.

As you write, refer to our style and formatting guidelines for more detailed explanations:

- [do.co/style](https://do.co/style)

Use our [Markdown previewer](https://www.digitalocean.com/community/markdown) to review your article's formatting.

Readers should be able to follow your tutorial from the beginning to the end on a DigitalOcean Droplet. Before submitting your article to the editorial team, please be sure to create a new Droplet and test your article from start to finish on it exactly as written. Cut and paste commands from the article into your terminal to make sure there aren't typos in the commands. If you find yourself executing a command that isn't in the article, incorporate it into the article to make sure the reader gets the exact same results. We will test your article and send it back to you if we run into technical problems, which significantly slows down the publication process.
-->


# How To [Install/Configure/Do Something] on [Distribution]

<!-- Use Title Case for all Titles -->

<!-- Learn about the title, introduction, and Goals sections at https://do.co/style#title-introduction-and-goals -->

<!-- Learn about formatting headers at https://do.co/style#headers -->

<!-- Our articles have a specific structure. Procedural tutorials follow this structure:

* Title
* Introduction (Level 3 heading)
* Prerequisites (Level 2 heading)
* Step 1 — Doing Something (Level 2 heading)
* Step 2 — Doing Something (Level 2 heading)
...
* Step 5 — Doing Something (Level 2 heading)
* Conclusion (Level 2 heading)


Learn more at https://do.co/style/structure -->

### Introduction

Introductory paragraph about the topic that explains what this topic is about and why the reader should care; what problem does it solve?

In this guide, you will [configure/set up/build/deploy] [some thing]...

When you're finished, you'll be able to...

## Prerequisites

<!-- Prerequisites let you leverage existing tutorials so you don't have to repeat installation or setup steps in your tutorial.  Learn more at https://do.co/style#prerequisites -->

Before you begin this guide you'll need the following:

- [number of servers] <OS and OS Version> server(s) <!-- Also specify the amount of RAM the server needs if relevant. -->
- A non-root user with sudo privileges (<insert link to Initial Server Setup article for the OS used in this tutorial>) explains how to set this up.)
- (Optional) If software such as Nginx needs to be installed, link to the proper article describing how to install it.
- (Optional) If the reader needs a fully-qualified domain name (FQDN), mention it here as well.
- (Optional) List any other accounts needed, such as GitHub, Facebook,  or other services.

<!-- Example:
* One Ubuntu 18.04 server with at least 1GB of RAM set up by following [the Ubuntu 18.04 initial server setup guide](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-18-04), including a sudo non-root user and a firewall.
* Nginx installed on your server, as shown in [How To Install Nginx on Ubuntu 16.04](https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-16-04).
* A domain name configured to point to your server. You can learn how to point domains to DigitalOcean Droplets by following the [How To Set Up a Host Name with DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-set-up-a-host-name-with-digitalocean) tutorial.
-->

## Step 1 — Doing Something

<!-- For more information on steps, see https://do.co/style/#steps -->

Introduction to the step. What are we going to do and why are we doing it?

First....

Next...

Finally...

<!-- When showing a command, explain the command first by talking about what it does. Then show the command. Then show its output in a separate output block: -->

Display the status of your firewall with the following command:

```command
sudo ufw status
```

You'll see the following output:

```
[secondary_label Output]
Status: active

To                         Action      From
--                         ------      ----
OpenSSH                    ALLOW       Anywhere                  
<^>Nginx HTTP                 ALLOW       Anywhere<^>
OpenSSH (v6)               ALLOW       Anywhere (v6)             
<^>Nginx HTTP (v6)            ALLOW       Anywhere (v6)<^>
```

<!-- You can use highlighting in output to point out relevant details -->


<!-- When asking the reader to open a file, specify the file and show the command to open it: -->

Open the file `/etc/nginx.conf` in your editor:

```command
sudo nano /etc/nginx.com
```

<!-- When showing a configuration file, try to show only the relevant parts and explain what needs to change.  -->

Change the `root` field so it points to `/var/www/your_domain`:

```nginx
[label /etc/nginx/sites-available/default]
server {
    listen 80 default_server;
    listen [::]:80 default_server ipv6only=on;

    root <^>/var/www/your_domain<^>;
    index index.html index.htm;

    server_name localhost;

    location / {
        try_files $uri $uri/ =404;
    }
}
```

<!-- See do.co/style#commands-and-code-in-steps for more on how to incorporate command and code in your steps. -->

Now transition to the next step by telling the reader what's next.

## Step 2 — Title Case

Another introduction

Your content

Transition to the next step.

## Step 3 — Title Case

Another introduction

Your content

Transition to the next step.

## Conclusion

In this article you [configured/set up/built/deployed] [something]. Now you can....

<!-- Speak  to reader benefits of this technique or procedure and optionally provide places for further exploration. -->
