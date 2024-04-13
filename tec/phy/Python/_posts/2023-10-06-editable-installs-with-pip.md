---
abstract: "Editable installs are a powerful tool in the Python developer’s toolkit. They allow for rapid development and testing cycles, improving productivity and reducing the potential for bugs in the production version of the package. Always pair them with virtual environments to get the maximum benefit."
---

## Using Editable Installs with pip

### Introduction

As developers, we often find ourselves in situations where we're actively developing a Python package while also needing to test or use that package elsewhere in our environment. `pip install -e .` comes to our rescue in these scenarios. This command, known as an "editable install", allows us to keep a live link between our development version of the package and the installed package in our environment. This guide will walk you through the importance, usage, and best practices for this handy tool.

### What is `pip install -e .`?

The command `pip install -e .` installs the package in the current directory (`.`) in "editable" mode (`-e`). Instead of copying the package files to the site-packages directory (standard behavior of `pip`), it creates a link there, pointing to our development directory. This means any changes made in the development directory will immediately affect the installed package without requiring a reinstall.

### Why Use Editable Installs?

1. **Rapid Development Cycle**: No need to reinstall the package after every change.
2. **Ease of Debugging**: Test the package in real-time while developing.
3. **Separation of Environments**: Can be used with virtual environments to ensure minimal interference with global packages and dependencies.

### How to Use `pip install -e .`

1. **Setup.py**: Ensure your package has a `setup.py` script at its root. This script informs `pip` about how the package should be installed.
2. **Activate Environment**: If you're using a virtual environment (and you should for development purposes!), ensure it's activated.
3. **Run the Command**: Navigate to the root of your package directory and run `pip install -e .`.

### Best Practices

1. **Use Virtual Environments**: Always work within a virtual environment to avoid potential conflicts with other packages and to keep the global site-packages directory clean.
2. **Commit `setup.py`**: Always commit your `setup.py` to version control. This ensures other developers can also use editable installs, and it's essential for package distribution.
3. **Avoid `sudo`**: Never use `sudo` with `pip`. If you find yourself needing elevated permissions, it's likely you're not in your virtual environment or there's another underlying issue.
4. **Keep Dependencies in Check**: Ensure your `setup.py` accurately reflects your package's dependencies to avoid runtime errors.

### Conclusion

Editable installs are a powerful tool in the Python developer's toolkit. They allow for rapid development and testing cycles, improving productivity and reducing the potential for bugs in the production version of the package. Always pair them with virtual environments to get the maximum benefit.
