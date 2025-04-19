---
layout: post
title: Using clasp to edit Google Apps Script projects
component: TA_PTC_032
date:   2021-10-27 00:00:00 +0100
abstract: "Develop Google Apps Script projects locally using clasp (Command Line Apps Script Projects)."
---

With Google Apps Scripts being JavaScript the online editor might not meet the developer's preference. Instead of copy&pasting code the Apps Script CLI is an easy way not just to transfer files but version and auto-deploy from the commandline.

Available at https://github.com/google/clasp in true JavaScript it requires Node.js and can then be installed with `npm i @google/clasp -g`.

First command to be issued should be `clasp login` which will authenticate with OAuth and will save credentials in
C:\Users\cpm\.clasprc.json or $HOME/.clasprc.json.

Running `clasp --help` gives a good overview of the functionality, a first introduction is available at https://codelabs.developers.google.com/codelabs/clasp/ .

```bash
Usage: clasp <command> [options]

clasp - The Apps Script CLI

Options:
  -v, --version                               output the current version
  -A, --auth <file>                           path to an auth file or a folder with a '.clasprc.json' file.
  -I, --ignore <file>                         path to an ignore file or a folder with a '.claspignore' file.
  -P, --project <file>                        path to a project file or to a folder with a '.clasp.json' file.
  -W, --why                                   Display some debugging info upon exit.
  -h, --help                                  display help for command

Commands:
  login [options]                             Log in to script.google.com
  logout                                      Log out
  create [options]                            Create a script
  clone [options] [scriptId] [versionNumber]  Clone a project
  pull [options]                              Fetch a remote project
  push [options]                              Update the remote project
  status [options]                            Lists files that will be pushed by clasp
  open [options] [scriptId]                   Open a script
  deployments                                 List deployment ids of a script
  deploy [options]                            Deploy a project
  undeploy [options] [deploymentId]           Undeploy a deployment of a project
  version [description]                       Creates an immutable version of the script
  versions                                    List versions of a script
  list [options]                              List App Scripts projects
  logs [options]                              Shows the StackDriver logs
  run [options] [functionName]                Run a function in your Apps Scripts project
  apis [options]                              List, enable, or disable APIs
    list
    enable <api>
    disable <api>
  setting|settings [settingKey] [newValue]    Update <settingKey> in .clasp.json
  *                                           Any other command is not supported
  paths                                       List current config files path
  help [command]                              display help for command
```

On Linux these CLI helper programs can very conveniently used with a Makefile.


