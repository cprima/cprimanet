---
layout: post
title: "How to Monitor File Changes Using Bash in WSL2: Overcoming the `inotifywait` Limitation"
date: 2023-11-01
categories: [WSL2, Bash, Development]
---

### Introduction

Developers often need to watch files for changes to auto-generate documentation, rebuild websites, or initiate other automations. The event-driven tool, `inotifywait`, has been the go-to solution for these needs on native Linux systems. But when operating within WSL2 on Windows, things are not so straightforward.

### The `inotifywait` Challenge in WSL2

WSL2 is an impressive implementation of Linux on top of a Windows environment. It allows developers to run a full-fledged Linux distribution alongside their existing Windows installation. However, as with any cross-platform solution, there are nuances.

One of these nuances is how WSL2 handles file systems. While WSL2 does support the `inotify` kernel feature used by tools like `inotifywait`, this support is limited when monitoring files stored on Windows-native filesystems (like `C:` drive) as opposed to the Linux-native filesystem within WSL2. Therefore, if you're trying to watch files on the Windows filesystem using `inotifywait` within WSL2, you'll run into issues. This limitation necessitates alternative solutions.

### Bash-Based File Monitoring as an Alternative

Given the limitations of `inotifywait` in WSL2, developers need a universally applicable method. Bash, combined with common UNIX commands, offers a polling-based approach to monitor file changes.

Here's a Bash script exemplifying this approach:

```bash
prev_mtime=$(stat -c %Y docs/_data/outline.csv)
while true; do
    current_mtime=$(stat -c %Y docs/_data/outline.csv)
    if [[ "$current_mtime" -ne "$prev_mtime" ]]; then
        python3 setup/scripts/generate_outline_md.py
        prev_mtime=$current_mtime
    fi
    sleep 1
done
```

**Script Breakdown**:

- `stat -c %Y docs/_data/outline.csv`: The `stat` command retrieves the last modification timestamp of the file.

- The infinite `while` loop facilitates continuous polling of the file's modification timestamp.

- Inside this loop:
  - The current modification time is compared to the previous one.
  - If they differ, a Python script is executed, followed by an update to the `prev_mtime`.
  - A one-second pause is introduced using `sleep 1` to balance responsiveness and resource usage.

### Key Takeaways

- **Efficiency**: This approach, while universally applicable, is less efficient than event-driven methods due to its polling nature.

- **Flexibility**: The Bash script can be easily tweaked for various files or actions.

- **Portability**: Given the reliance on basic UNIX commands, this approach is portable across many UNIX-like environments, even without additional tools.

### Conclusion

While `inotifywait` serves as an efficient tool for file change monitoring on native Linux, its limitations in WSL2 environments necessitate alternatives. The Bash-based approach, despite its efficiency trade-offs, provides a reliable solution for developers working within WSL2. It exemplifies the adaptability required when bridging the worlds of Windows and Linux.
