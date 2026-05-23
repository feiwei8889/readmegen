"""
readmegen templates — 12 professionally designed README templates.
"""

TEMPLATES = {
    "default": {
        "name": "Default",
        "description": "Clean, modern, all-purpose template",
        "best_for": "General projects, libraries, CLI tools",
        "sections": ["banner", "badges", "description", "features", "install", "usage", "api", "contributing", "license"],
        "content": """# {name}

{tagline}

{badges}

{toc}

## 📖 Overview

{description}

## ✨ Features

{features_list}

## 🚀 Installation

```{install_lang}
{install_cmd}
```

## 💡 Quick Start

```{install_lang}
{usage_or_default}
```

{screenshots_section}

## 📚 Documentation

For full documentation, visit our [docs site]({docs_url}) or check the [wiki]({repo_url}/wiki).

## 🤝 Contributing

{contributing_section}

## 📄 License

This project is licensed under the **{license}** License — see the [LICENSE](LICENSE) file for details.

---

{star_footer}
""",
    },
    "minimal": {
        "name": "Minimal",
        "description": "Clean and concise — less is more",
        "best_for": "Small utilities, micro-libraries, scripts",
        "sections": ["title", "badges", "install", "usage", "license"],
        "content": """# {name}

{badges}

> {tagline}

## Install

```{install_lang}
{install_cmd}
```

## Usage

```{install_lang}
{usage_or_default}
```

## License

{license} © {author_name}
""",
    },
    "project": {
        "name": "Project",
        "description": "Full-featured for serious projects",
        "best_for": "Frameworks, platforms, large libraries",
        "sections": ["logo", "badges", "toc", "about", "features", "quickstart", "install", "usage", "api", "architecture", "contributing", "changelog", "license", "acknowledgments"],
        "content": """<p align="center">
  <img src="{logo_url}" alt="{name} logo" width="200"/>
</p>

<h1 align="center">{name}</h1>

<p align="center">{tagline}</p>

<p align="center">
  {badges}
</p>

{toc}

## 🎯 About The Project

{description}

## ✨ Features

{features_list}

## ⚡ Quick Start

```{install_lang}
{install_cmd}
```

```{install_lang}
{usage_or_default}
```

{screenshots_section}

## 📦 Installation

Detailed installation instructions for different platforms.

### Prerequisites

{prerequisites_list}

### Setup

```{install_lang}
{install_cmd}
```

## 💻 Usage

### Basic

```{install_lang}
{usage_or_default}
```

### Advanced

For advanced usage, see the [documentation]({docs_url}).

## 🏗️ Architecture

```
{architecture_text}
```

## 🤝 Contributing

{contributing_section}

## 📝 Changelog

See [CHANGELOG.md](CHANGELOG.md) for a list of changes.

## 📄 License

Distributed under the **{license}** License. See `LICENSE` for more information.

## 🙏 Acknowledgments

{acknowledgments_text}

---

{star_footer}
""",
    },
    "api": {
        "name": "API Service",
        "description": "Designed for REST/GraphQL APIs",
        "best_for": "API servers, microservices, backend services",
        "sections": ["badges", "overview", "base_url", "authentication", "endpoints", "errors", "rate_limits", "sdks", "changelog"],
        "content": """# {name} API

{badges}

> {tagline}

{toc}

## 📖 Overview

{description}

## 🔗 Base URL

```
{api_base_url}
```

## 🔐 Authentication

{authentication_text}

## 📡 Endpoints

{endpoints_table}

{endpoints_detail}

## ⚠️ Error Handling

{errors_text}

## 🚦 Rate Limiting

{rate_limit_text}

## 📦 SDKs & Libraries

{sdks_text}

## 📝 Changelog

See [CHANGELOG.md](CHANGELOG.md) for API version history.

---

{star_footer}
""",
    },
    "cli-tool": {
        "name": "CLI Tool",
        "description": "Perfect for command-line tools",
        "best_for": "CLI apps, terminal utilities, dev tools",
        "sections": ["banner", "badges", "demo", "features", "install", "usage", "options", "examples", "config", "contributing", "license"],
        "content": """# {name}

{badges}

> {tagline}

{toc}

## 🎬 Demo

```
{demo_text}
```

## ✨ Features

{features_list}

## 📦 Installation

```{install_lang}
{install_cmd}
```

## 🚀 Usage

```{install_lang}
{usage_or_default}
```

## ⚙️ Options

{options_table}

## 📖 Examples

{examples_section}

## 🔧 Configuration

{config_text}

## 🤝 Contributing

{contributing_section}

## 📄 License

{license} © {author_name}
""",
    },
    "library": {
        "name": "Library/SDK",
        "description": "Ideal for reusable libraries and SDKs",
        "best_for": "npm packages, PyPI libraries, SDKs",
        "sections": ["badges", "description", "features", "install", "quickstart", "api", "examples", "testing", "contributing", "license"],
        "content": """# {name}

{badges}

> {tagline}

{toc}

## 📖 Description

{description}

## ✨ Features

{features_list}

## 📦 Installation

```{install_lang}
{install_cmd}
```

## 🚀 Quick Start

```{install_lang}
{usage_or_default}
```

## 📚 API Reference

{api_reference_section}

## 📖 Examples

{examples_section}

## 🧪 Testing

```{install_lang}
{test_command}
```

## 🤝 Contributing

{contributing_section}

## 📄 License

{license} © {author_name}
""",
    },
    "startup": {
        "name": "Startup/SaaS",
        "description": "Polished pitch-ready README",
        "best_for": "SaaS products, startups, commercial projects",
        "sections": ["hero", "badges", "pitch", "features", "how_it_works", "pricing", "testimonials", "integrations", "security", "get_started"],
        "content": """<p align="center">
  <img src="{logo_url}" alt="{name}" width="120"/>
</p>

<h1 align="center">{name}</h1>
<p align="center"><strong>{tagline}</strong></p>

<p align="center">
  {badges}
</p>

---

## 💡 Why {name}?

{description}

## ✨ Features

{features_list}

## 🏗️ How It Works

{how_it_works_text}

## 💰 Pricing

{pricing_table}

## 💬 What Our Users Say

{testimonials_text}

## 🔌 Integrations

{integrations_text}

## 🔒 Security

{security_text}

## 🚀 Get Started

```{install_lang}
{install_cmd}
```

{screenshots_section}

---

{star_footer}
""",
    },
    "gamedev": {
        "name": "Game Dev",
        "description": "For game projects and mods",
        "best_for": "Game engines, mods, assets, game jam projects",
        "sections": ["banner", "badges", "trailer", "about", "gameplay", "screenshots", "install", "controls", "credits", "license"],
        "content": """# {name}

{badges}

> {tagline}

## 🎮 Play Now

{game_links_text}

## 📖 About

{description}

## 🎯 Gameplay

{gameplay_text}

## 📸 Screenshots

{screenshots_section}

## 💾 Installation

{install_text}

## 🎛️ Controls

{controls_text}

## 👥 Credits

{credits_text}

## 📄 License

{license} © {author_name}
""",
    },
    "awesome": {
        "name": "Awesome List",
        "description": "Curated list collections",
        "best_for": "awesome-X lists, resource collections, curated lists",
        "sections": ["badges", "description", "toc", "categories...", "contributing", "license"],
        "content": """# {name}

{badges}

> {tagline}

{toc}

## 📖 About

{description}

## 📚 Contents

{contents_list}

## 🤝 Contributing

{contributing_section}

## 📄 License

{license} © {author_name}
""",
    },
    "profile": {
        "name": "GitHub Profile",
        "description": "Personal GitHub profile README",
        "best_for": "GitHub profile pages, personal branding",
        "sections": ["greeting", "about", "skills", "stats", "projects", "blog", "connect"],
        "content": """# Hi there, I'm {author_name}! 👋

{badges}

{greeting_text}

## 🧑‍💻 About Me

{about_me_text}

## 🛠️ Skills

{skills_badges}

## 📊 GitHub Stats

{github_stats}

## 🚀 Featured Projects

{projects_list}

## ✍️ Latest Blog Posts

{blog_posts}

## 📫 Connect With Me

{social_links}

---

⭐️ From [{author_name}](https://github.com/{github_username})
""",
    },
    "docker": {
        "name": "Docker/DevOps",
        "description": "For containerized applications",
        "best_for": "Docker images, DevOps tools, infrastructure",
        "sections": ["badges", "description", "quickstart", "docker_run", "compose", "env_vars", "volumes", "build", "examples", "license"],
        "content": """# {name}

{badges}

> {tagline}

{toc}

## 📖 Description

{description}

## 🚀 Quick Start

```bash
docker run {docker_image}
```

## 🐳 Docker Compose

```yaml
{docker_compose_example}
```

## 🔧 Environment Variables

{env_vars_table}

## 💾 Volumes

{volumes_text}

## 🏗️ Build Locally

```bash
{build_command}
```

## 📖 Usage Examples

{examples_section}

## 📄 License

{license} © {author_name}
""",
    },
    "chinese": {
        "name": "中文项目",
        "description": "适合中文开源项目的美化模板",
        "best_for": "Chinese open source projects",
        "sections": ["logo", "badges", "简介", "特性", "快速开始", "安装", "使用", "文档", "贡献", "许可证", "致谢"],
        "content": """<p align="center">
  <img src="{logo_url}" alt="{name}" width="120"/>
</p>

<h1 align="center">{name}</h1>

<p align="center">
  <strong>{tagline}</strong>
</p>

<p align="center">
  {badges}
</p>

{toc}

## 📖 项目简介

{description}

## ✨ 功能特性

{features_list}

## 🚀 快速开始

```{install_lang}
{install_cmd}
```

## 💻 使用示例

```{install_lang}
{usage_or_default}
```

{screenshots_section}

## 📚 文档

完整文档请访问 [{docs_url}]({docs_url})

## 🤝 贡献指南

{contributing_section}

## 📄 开源协议

本项目采用 **{license}** 协议开源，详见 [LICENSE](LICENSE) 文件。

## 🙏 致谢

{acknowledgments_text}

---

{star_footer}
""",
    },
}


def list_templates():
    """Return list of template names and descriptions."""
    return [(name, data["name"], data["description"]) for name, data in TEMPLATES.items()]


def get_template(name):
    """Get a template by name. Returns None if not found."""
    name = name.lower().strip()
    if name in TEMPLATES:
        return TEMPLATES[name]
    # Fuzzy match
    for tname, tdata in TEMPLATES.items():
        if tname.startswith(name) or name in tname:
            return tdata
    return None


def render_template(template):
    """Render a template — returns it as-is since templates use Python format strings."""
    return template
