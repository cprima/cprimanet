---
---

## **Setting Up a Jekyll Site for GitHub Pages: A Step-by-Step Guide**

### **Introduction**

GitHub Pages offers a convenient way to host static websites directly from a GitHub repository. One of the most popular static site generators used with GitHub Pages is Jekyll. In this tutorial, we'll guide you through setting up a Jekyll site on an existing GitHub repository and on a feature branch.

### **Prerequisites**

- An existing GitHub repository (already cloned locally).
- A working Ruby and Jekyll installation.

### **1. Branching Out**

Before making changes, it's a good practice to create a separate branch. This ensures that our main branch remains clean and deployable.

Navigate to your repository:

```bash
cd path_to_your_repository
```

Create and switch to a new branch:

```bash
git checkout -b jekyll-setup
```

### **2. Bootstrapping Jekyll**

With Jekyll installed, let's initialize a new site:

```bash
jekyll new . --force
```

The `--force` flag instructs Jekyll to create a new site even if the directory isn't empty.

### **3. Local Testing**

It's always a good idea to test changes locally before pushing to GitHub:

```bash
bundle exec jekyll serve
```

Access your site by opening `http://localhost:4000` in your browser.

### **4. Prepping for GitHub Pages**

To ensure compatibility with GitHub Pages, adjust the `url` field in `_config.yml`.

For user or organization sites:

```yaml
url: "https://yourusername.github.io"
```

For project sites:

```yaml
url: "https://yourusername.github.io/repositoryname"
```

### **5. Committing and Pushing**

Now, commit the Jekyll setup to your feature branch:

```bash
git add .
git commit -m "Set up Jekyll site for GitHub Pages"
```

Push to GitHub:

```bash
git push origin jekyll-setup
```

### **6. Activating GitHub Pages**

Follow these steps on the GitHub web interface:

1. Go to your repository.
2. Navigate to "Settings".
3. In the "GitHub Pages" section, select the `jekyll-setup` branch as the source.
4. Your site will begin building and will soon be available online.

### **7. Wrapping Up**

Once you're content with the Jekyll setup on your feature branch, consider opening a pull request to merge it into your main branch. This provides a clean history and a straightforward deployment process for your Jekyll site on GitHub Pages.

---

**Conclusion**

Setting up a Jekyll site for GitHub Pages can be a breeze when approached systematically. By working on a feature branch, you ensure minimal disruption to your main codebase, allowing for safer experimentation and deployment. With this guide, you're now equipped to get your Jekyll site running smoothly on GitHub Pages. Happy publishing!
