"""
readmegen generator — combines templates with project info to produce README files.
"""

from .templates import TEMPLATES, get_template


def generate_readme(info, template_name="default"):
    """Generate a README from project info and template.

    Args:
        info: dict with project information
        template_name: name of the template to use

    Returns:
        str: The generated README content
    """
    template_data = get_template(template_name)
    if not template_data:
        template_data = TEMPLATES["default"]

    template = template_data["content"]

    # Build all the template variables
    vars_dict = _build_variables(info)

    # Format the template
    try:
        readme = template.format(**vars_dict)
    except KeyError as e:
        # If a key is missing, add it as empty
        missing = str(e).strip("'")
        vars_dict[missing] = f"[{missing}]"
        readme = template.format(**vars_dict)

    return readme


def _build_variables(info):
    """Build all template variables from project info."""
    name = info.get("name", "My Project")
    tagline = info.get("tagline", "An awesome project")
    description = info.get("description", f"{name} is a powerful tool that helps you get things done faster.")
    features_str = info.get("features", "Fast, Reliable, Easy to use")
    features = [f.strip() for f in features_str.split(",") if f.strip()]
    install_cmd = info.get("install_cmd", f"pip install {name.lower().replace(' ', '-')}")
    install_lang = info.get("install_method", "bash").lower()
    if install_lang in ("pip", "python"):
        install_lang = "bash"
    elif install_lang == "npm":
        install_lang = "bash"
    elif install_lang in ("git clone", "curl", "brew"):
        install_lang = "bash"
    usage = info.get("usage_example", "")
    license_name = info.get("license", "MIT")
    author = info.get("author", "")
    repo_url = info.get("repo_url", "")
    badges_str = info.get("badges", "license, stars, version")
    include_toc = info.get("toc", True)
    include_contributing = info.get("contributing", True)
    include_screenshots = info.get("screenshots", False)
    github_username = info.get("github_username", author or "username")

    # Badges
    badges = _generate_badges(badges_str, name, repo_url, license_name, author)

    # Features list
    features_list = "\n".join(f"- ✅ {f}" for f in features) if features else "- ✅ Lightning fast\n- ✅ Easy to use\n- ✅ Well documented"

    # Usage or default
    usage_or_default = usage or f"# Get started with {name}\n{name.lower().replace(' ', '-')} --help"

    # Screenshots
    screenshots_section = ""
    if include_screenshots:
        screenshots_section = """## 📸 Screenshots

<p align="center">
  <img src="assets/screenshot.png" alt="{name} screenshot" width="600"/>
</p>""".format(name=name)

    # Contributing
    contributing_section = ""
    if include_contributing:
        contributing_section = f"""We welcome contributions! Here's how:

1. 🍴 Fork the repository
2. 🌿 Create your feature branch (`git checkout -b feat/amazing-feature`)
3. 💾 Commit your changes (`git commit -m 'Add amazing feature'`)
4. 📤 Push to the branch (`git push origin feat/amazing-feature`)
5. 🔄 Open a Pull Request

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines."""

    # ToC
    toc = ""
    if include_toc:
        toc = """## 📑 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Installation](#-installation)
- [Quick Start](#-quick-start)
- [Documentation](#-documentation)
- [Contributing](#-contributing)
- [License](#-license)
"""

    # Star footer
    star_footer = """<p align="center">
  <sub>Made with ❤️ by <a href="https://github.com/{author}">{author}</a></sub>
</p>

<p align="center">
  <a href="https://github.com/{author}/{repo_name}">⭐ Star us on GitHub!</a>
  •
  <a href="https://ko-fi.com/feiwei8889">🔥 Get readmegen Pro</a>
</p>""".format(author=github_username, repo_name=name.lower().replace(" ", "-"))

    # Additional template variables
    vars_dict = {
        "name": name,
        "tagline": tagline,
        "description": description,
        "badges": badges,
        "toc": toc,
        "features_list": features_list,
        "install_lang": install_lang,
        "install_cmd": install_cmd,
        "usage_or_default": usage_or_default,
        "license": license_name,
        "author_name": author or github_username,
        "repo_url": repo_url or f"https://github.com/{github_username}/{name.lower().replace(' ', '-')}",
        "repo_name": name.lower().replace(" ", "-"),
        "github_username": github_username,
        "screenshots_section": screenshots_section,
        "contributing_section": contributing_section,
        "star_footer": star_footer,
        # Extended template variables
        "logo_url": info.get("logo_url", f"https://raw.githubusercontent.com/{github_username}/{name.lower().replace(' ', '-')}/main/assets/logo.png"),
        "docs_url": info.get("docs_url", f"https://{name.lower().replace(' ', '-')}.readthedocs.io"),
        "api_base_url": info.get("api_base_url", "https://api.example.com/v1"),
        "authentication_text": info.get("authentication_text", "Use API keys to authenticate requests. Include your key in the `Authorization` header:\n\n```bash\ncurl -H \"Authorization: Bearer YOUR_API_KEY\" {api_base_url}/endpoint\n```".format(api_base_url=info.get("api_base_url", "https://api.example.com/v1"))),
        "endpoints_table": info.get("endpoints_table", "| Method | Endpoint | Description |\n|--------|----------|-------------|\n| GET | `/items` | List all items |\n| POST | `/items` | Create an item |\n| GET | `/items/{id}` | Get an item |"),
        "endpoints_detail": info.get("endpoints_detail", ""),
        "errors_text": info.get("errors_text", "The API returns standard HTTP status codes:\n\n- `200` — Success\n- `400` — Bad request\n- `401` — Unauthorized\n- `404` — Not found\n- `429` — Rate limited\n- `500` — Server error"),
        "rate_limit_text": info.get("rate_limit_text", "Rate limits are applied per API key:\n\n- **Free tier**: 100 requests/minute\n- **Pro tier**: 1000 requests/minute"),
        "sdks_text": info.get("sdks_text", "- [Python SDK](https://github.com/...)\n- [JavaScript SDK](https://github.com/...)"),
        "demo_text": info.get("demo_text", f"$ {name.lower().replace(' ', '-')} --help\n\n✨ {name} v1.0.0\nUsage: {name.lower().replace(' ', '-')} [options]"),
        "options_table": info.get("options_table", "| Option | Description | Default |\n|--------|-------------|----------|\n| `--help` | Show help | — |\n| `--version` | Show version | — |\n| `--output` | Output file | stdout |"),
        "examples_section": info.get("examples_section", f"### Basic\n```bash\n{install_cmd}\n```"),
        "config_text": info.get("config_text", f"Configuration is stored in `~/.config/{name.lower().replace(' ', '-')}/config.yaml`."),
        "api_reference_section": info.get("api_reference_section", f"See the [API documentation]({info.get('docs_url', 'https://example.com/docs')}) for detailed reference."),
        "test_command": info.get("test_command", "pytest tests/"),
        "how_it_works_text": info.get("how_it_works_text", f"1. **Install** {name} with a single command\n2. **Configure** your settings\n3. **Launch** and start using it!"),
        "pricing_table": info.get("pricing_table", "| Plan | Price | Features |\n|------|-------|----------|\n| Free | $0 | Basic features |\n| Pro | $9/mo | Advanced features |\n| Enterprise | Custom | Full feature set |"),
        "testimonials_text": info.get("testimonials_text", '> "This tool changed how I work!" — Happy User'),
        "integrations_text": info.get("integrations_text", "- 🔗 GitHub\n- 🔗 Slack\n- 🔗 Discord\n- 🔗 Jira"),
        "security_text": info.get("security_text", "Found a vulnerability? Email us at security@example.com. We take security seriously."),
        "game_links_text": info.get("game_links_text", f"- 🎮 [Play on itch.io](https://itch.io)\n- 🕹️ [Try the demo](https://demo.example.com)"),
        "gameplay_text": info.get("gameplay_text", f"**{name}** is a ..."),
        "install_text": info.get("install_text", f"Download the latest release from [Releases]({repo_url}/releases)."),
        "controls_text": info.get("controls_text", "| Key | Action |\n|-----|--------|\n| WASD | Move |\n| Space | Jump |"),
        "credits_text": info.get("credits_text", f"- **{author or github_username}** — Developer"),
        "contents_list": info.get("contents_list", f"- [Section 1](#section-1)\n- [Section 2](#section-2)"),
        "greeting_text": info.get("greeting_text", "Welcome to my GitHub profile! I'm passionate about building great software."),
        "about_me_text": info.get("about_me_text", f"I'm a software developer who loves building tools that make people's lives easier."),
        "skills_badges": info.get("skills_badges", "![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)  ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black)"),
        "github_stats": info.get("github_stats", f"![GitHub stats](https://github-readme-stats.vercel.app/api?username={github_username}&show_icons=true&theme=radical)"),
        "projects_list": info.get("projects_list", f"- [{name}]({repo_url}) — {tagline}"),
        "blog_posts": info.get("blog_posts", "- [Latest Post](https://blog.example.com)"),
        "social_links": info.get("social_links", f"- [Twitter](https://twitter.com/{github_username})\n- [LinkedIn](https://linkedin.com/in/{github_username})"),
        "docker_image": info.get("docker_image", f"{github_username}/{name.lower().replace(' ', '-')}:latest"),
        "docker_compose_example": info.get("docker_compose_example", f"version: '3.8'\nservices:\n  app:\n    image: {github_username}/{name.lower().replace(' ', '-')}:latest\n    ports:\n      - '8080:8080'"),
        "env_vars_table": info.get("env_vars_table", "| Variable | Description | Default |\n|----------|-------------|----------|\n| `PORT` | Server port | `8080` |"),
        "volumes_text": info.get("volumes_text", "- `/data` — Application data\n- `/config` — Configuration files"),
        "build_command": info.get("build_command", f"docker build -t {github_username}/{name.lower().replace(' ', '-')}:latest ."),
        "prerequisites_list": info.get("prerequisites_list", f"- Python 3.9+\n- pip"),
        "architecture_text": info.get("architecture_text", f"┌─────────────┐\n│   {name}   │\n└──────┬──────┘\n       │\n┌──────┴──────┐\n│   Core     │\n└─────────────┘"),
        "acknowledgments_text": info.get("acknowledgments_text", "Thanks to all contributors and the open source community."),
    }

    return vars_dict


def _generate_badges(badges_str, name, repo_url, license_name, author):
    """Generate markdown badges."""
    if not badges_str:
        return ""

    badge_types = [b.strip().lower() for b in badges_str.split(",") if b.strip()]
    badges = []

    for bt in badge_types:
        if bt in ("license", "mit", "apache"):
            badges.append(
                f"![License](https://img.shields.io/badge/License-{license_name.replace('-', '--')}-blue.svg)"
            )
        elif bt in ("stars", "star"):
            badges.append(
                f"![GitHub stars](https://img.shields.io/github/stars/{author}/{name.lower().replace(' ', '-')}?style=social)"
            )
        elif bt in ("version", "release"):
            badges.append(
                f"![Version](https://img.shields.io/badge/version-1.0.0-brightgreen.svg)"
            )
        elif bt in ("python", "py"):
            badges.append(
                "![Python](https://img.shields.io/badge/Python-3.9+-blue.svg?logo=python)"
            )
        elif bt in ("node", "nodejs", "javascript", "js"):
            badges.append(
                "![Node.js](https://img.shields.io/badge/Node.js-18+-green.svg?logo=node.js)"
            )
        elif bt in ("docker"):
            badges.append(
                "![Docker](https://img.shields.io/badge/Docker-Ready-2496ED.svg?logo=docker)"
            )
        elif bt in ("ci", "build"):
            badges.append(
                "![CI](https://img.shields.io/badge/build-passing-brightgreen.svg)"
            )
        elif bt in ("coverage", "cov"):
            badges.append(
                "![Coverage](https://img.shields.io/badge/coverage-95%25-brightgreen.svg)"
            )
        elif bt in ("downloads", "download"):
            badges.append(
                "![Downloads](https://img.shields.io/badge/downloads-1k%2Fmonth-blue.svg)"
            )
        elif bt in ("prs", "pr"):
            badges.append(
                "![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)"
            )
        elif bt in ("types", "typescript", "ts"):
            badges.append(
                "![TypeScript](https://img.shields.io/badge/TypeScript-Ready-3178C6.svg?logo=typescript)"
            )

    return " ".join(badges) if badges else ""
