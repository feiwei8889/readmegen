# readmegen

![License](https://img.shields.io/badge/License-MIT-blue.svg) ![Version](https://img.shields.io/badge/version-1.0.0-brightgreen.svg) ![Python](https://img.shields.io/badge/Python-3.9+-blue.svg?logo=python) ![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg) [![Ko-fi](https://img.shields.io/badge/Ko--fi-Donate%20%245-ff5e5b?logo=ko-fi&logoColor=white)](https://ko-fi.com/feiwei8889) [![Ko-fi](https://img.shields.io/badge/Ko--fi-Donate%20%245-ff5e5b?logo=kofi&logoColor=white)](https://ko-fi.com/feiwei8889)

> Beautiful README generator for your GitHub projects — 12 professional templates in seconds


---

<p align="center">
  <a href="https://ko-fi.com/feiwei8889">
    <img src="https://img.shields.io/badge/🔥_Get_readmegen_Pro-$5-ff5e5b?style=for-the-badge&logo=ko-fi&logoColor=white" alt="Get readmegen Pro for $5">
  </a>
</p>

> **Love readmegen?** Get the [Pro version for $5](https://ko-fi.com/feiwei8889) — 20+ exclusive templates, AI-powered suggestions, custom branding, and priority support. Click the button above to upgrade!

---

## 📑 Table of Contents

- [Demo](#-demo)
- [Features](#-features)
- [Installation](#-installation)
- [Usage](#-usage)
- [Templates](#-templates)
- [Pro Version](#-pro-version)
- [Contributing](#-contributing)
- [License](#-license)

## 🎬 Demo

```
$ readmegen

  ██████╗ ███████╗ █████╗ ██████╗ ███╗   ███╗███████╗ ██████╗ ███████╗███╗   ██╗
  ╚════██╗...                                              ██╔════╝ ██╔════╝...
             Beautiful READMEs for your GitHub projects — 12 templates • Badges • ToC

📋 Project Information
  Let's build your README! Fill in the details below.

Project name: MyTool
One-line description: An awesome CLI tool
Key features: Fast, Secure, Open Source
Install method: pip
License: MIT

✨ README generated successfully!
Output: /home/user/project/README.md
Lines: 75
Template: cli-tool
```

## ✨ Features

- 🎨 **12 Professional Templates** — default, minimal, project, API, CLI, library, startup, gamedev, awesome, profile, docker, Chinese
- 🖥️ **Interactive CLI Wizard** — Beautiful Rich-powered UI guides you through every step
- 🏷️ **Auto-generated Badges** — shields.io badges for license, stars, version, Python, Node.js, Docker, CI, coverage, and more
- 📑 **Table of Contents** — Auto-generated, clean navigation
- 🌏 **Multi-language Support** — Including a Chinese-specific template (中文项目)
- ⚡ **Zero Config** — Works out of the box, no setup needed
- 👁️ **Live Preview** — See your README in the terminal before saving
- 🎛️ **Full Customization** — Every section is configurable via CLI flags or interactive prompts
- 📦 **JSON Input** — Batch generate READMEs from JSON config files
- 🚀 **Quick Mode** — Fast path with sensible defaults for power users

## 📦 Installation

```bash
pip install readmegen
```

Or install from source:

```bash
git clone https://github.com/feiwei88898889/readmegen.git
cd readmegen
pip install -e .
```

## 🚀 Usage

### Interactive Mode (recommended)

```bash
readmegen
```

### Quick Mode

```bash
readmegen --quick
```

### Specify Template & Info

```bash
readmegen --template cli-tool --name "MyTool" --tagline "An awesome CLI tool"
```

### List All Templates

```bash
readmegen --list
```

### Preview a Template

```bash
readmegen --preview startup
```

### Batch Generate from JSON

```bash
readmegen --json-input project-info.json
```

## 📚 Templates

| # | Template | Description | Best For |
|---|----------|-------------|----------|
| 1 | `default` | Clean, modern, all-purpose | General projects, libraries, CLI tools |
| 2 | `minimal` | Clean and concise | Small utilities, micro-libraries |
| 3 | `project` | Full-featured | Frameworks, platforms, large libraries |
| 4 | `api` | API documentation | REST/GraphQL APIs, microservices |
| 5 | `cli-tool` | CLI-first design | Command-line tools, dev utilities |
| 6 | `library` | Library/SDK format | npm packages, PyPI libraries |
| 7 | `startup` | Pitch-ready | SaaS products, startups |
| 8 | `gamedev` | Game-focused | Game engines, mods, assets |
| 9 | `awesome` | Curated lists | awesome-X lists, resource collections |
| 10 | `profile` | GitHub profile | Personal branding, profile READMEs |
| 11 | `docker` | Docker/DevOps | Container images, DevOps tools |
| 12 | `chinese` | 中文项目模板 | Chinese open source projects |

## 🔥 Pro Version

Love readmegen? Get the **Pro version** with:

- 🌟 **20+ Exclusive Premium Templates** — SaaS landing, documentation site, changelog, team profiles, and more
- 🎨 **Custom Branding** — Your logo, colors, and custom CSS
- 📊 **Analytics Badges** — npm downloads, PyPI stats, Docker pulls (live)
- 🤖 **AI-Powered Suggestions** — Get smart recommendations for your README content
- ⚡ **Priority Support** — Direct line to the maintainer
- 🔄 **Auto-update Badges** — Keep your badges always current

**[Get readmegen Pro — $5 on Ko-fi](https://ko-fi.com/feiwei8889)**

## 🤝 Contributing

We welcome contributions! Here's how:

1. 🍴 Fork the repository
2. 🌿 Create your feature branch (`git checkout -b feat/amazing-feature`)
3. 💾 Commit your changes (`git commit -m 'Add amazing feature'`)
4. 📤 Push to the branch (`git push origin feat/amazing-feature`)
5. 🔄 Open a Pull Request

## 📄 License

MIT © feiwei

---

<p align="center">
  <sub>Made with ❤️ by <a href="https://github.com/feiwei8889">feiwei</a></sub>
</p>

<p align="center">
  <a href="https://github.com/feiwei88898889/readmegen">⭐ Star us on GitHub!</a>
  •
  <a href="https://github.com/sponsors/feiwei8889">💖 Sponsor</a>
  •
  <a href="https://ko-fi.com/feiwei8889">🔥 Get Pro ($5)</a>
</p>
