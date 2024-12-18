---
layout: page
title:  "Procedural Softwaredevelopment Template"
---

<!--
This is an article template you can use as a starting point when writing DigitalOcean procedural tutorials about software development. This template is great for Python, JavaScript, or other softwar development tutorials that readers would follow.  Once you've reviewed the template, delete the comments and begin writing your outline or article. You'll find some examples of our custom Markdown at the very bottom of the template.

As you write, refer to our style and formatting guidelines for more detailed explanations:

- [do.co/style](https://do.co/style)

Use our [Markdown previewer](https://www.digitalocean.com/community/markdown) to review your article's formatting.

Readers should be able to follow your tutorial from the beginning to the end on their own computer. Before submitting your article to the editorial team, please be sure to test your article from start to finish on it exactly as written. Cut and paste commands from the article into your terminal to make sure there aren't typos in the commands. If you find yourself executing a command that isn't in the article, incorporate it into the article to make sure the reader gets the exact same results. We will test your article and send it back to you if we run into technical problems, which significantly slows down the publication process.
-->


# How To [Build/Create/Do Something] in [JavaScript/Node.js/Python 3/Go]

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

In this guide, you will [configure/set up/build/] [some thing]...

When you're finished, you'll be able to...

## Prerequisites

<!-- Prerequisites let you leverage existing tutorials so you don't have to repeat installation or setup steps in your tutorial.  Learn more at https://do.co/style#prerequisites -->

To complete this tutorial, you will need:

* A local development environment for [your language] 
* Familiarity with [the language]. You can look at the [tutorial series for the language] to learn more.
* (Optional) If software such as Git, Docker, or other tooling needs to be installed, link to the proper article describing how to install it.
* (Optional) List any other accounts needed, such as GitHub, Facebook,  or other services.

<!-- Example - uncomment to use

* A local development environment for Node.js. Follow [How to Install Node.js and Create a Local Development Environment](https://www.digitalocean.com/community/tutorial_series/how-to-install-node-js-and-create-a-local-development-environment).
* A text editor like [Visual Studio Code](https://code.visualstudio.com/download) or [Atom](https://atom.io/). 
* A web browser like [Firefox](https://www.mozilla.org/en-US/firefox/new/) or [Chrome](https://www.google.com/chrome/).
* Familiarity with JavaScript. You can look at the [How To Code in JavaScript](https://www.digitalocean.com/community/tutorial_series/how-to-code-in-javascript) series to learn more.
* Familiarity with React. You can take a look at our [How To Code in React.js](https://www.digitalocean.com/community/tutorial_series/how-to-code-in-react-js) series.
-->

## Step 1 — Doing Something

<!-- For more information on steps, see https://do.co/style/#steps -->

Introduction to the step. What are we going to do and why are we doing it?

First....

Next...

Finally...

<!-- When showing a command, explain the command first by talking about what it does. Then show the command. Then show its output in a separate output block: -->

Run the following command to create your React app:

```command
npx create-react-app <^>digital-ocean-tutorial<^>
```

You'll see the following output:

```
[secondary_label Output]
...
Success! Created <^>digital-ocean-tutorial at <^>your_file_path/digital-ocean-tutorial<^>
Inside that directory, you can run several commands:

  npm start
    Starts the development server.

  npm run build
    Bundles the app into static files for production.

  npm test
    Starts the test runner.

  npm run eject
    Removes this tool and copies build dependencies, configuration files
    and scripts into the app directory. If you do this, you can’t go back!

We suggest that you begin by typing:

  cd <^>digital-ocean-tutorial<^>
  npm start

Happy hacking!
```

<!-- You can use highlighting in output to point out relevant details -->


<!-- When asking the reader to open a file, be sure to specify the file name:

Open the file `public/index.htm` in your editor.


<!-- When showing the contents of a file, try to show only the relevant parts and explain what needs to change. -->


Modify the title by changning the contents of the `<title>` tag:

```js
[label public/index.html]
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <link rel="icon" href="%PUBLIC_URL%/favicon.ico" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="theme-color" content="#000000" />
    ...
    <title><^>Sandbox<^></title>
  </head>
...
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
