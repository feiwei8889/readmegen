#!/usr/bin/env python3
"""
readmegen CLI — Beautiful README generator with Rich UI.
"""

import os
import sys
import json
from pathlib import Path

import click
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt, Confirm, IntPrompt
from rich.table import Table
from rich.markdown import Markdown
from rich.syntax import Syntax
from rich.text import Text
from rich import box

from .templates import TEMPLATES, list_templates, get_template, render_template
from .generator import generate_readme

console = Console()

BANNER = r"""[bold cyan]
  ██████╗ ███████╗ █████╗ ██████╗ ███╗   ███╗███████╗ ██████╗ ███████╗███╗   ██╗
  ██╔══██╗██╔════╝██╔══██╗██╔══██╗████╗ ████║██╔════╝██╔════╝ ██╔════╝████╗  ██║
  ██████╔╝█████╗  ███████║██║  ██║██╔████╔██║█████╗  ██║  ███╗█████╗  ██╔██╗ ██║
  ██╔══██╗██╔══╝  ██╔══██║██║  ██║██║╚██╔╝██║██╔══╝  ██║   ██║██╔══╝  ██║╚██╗██║
  ██║  ██║███████╗██║  ██║██████╔╝██║ ╚═╝ ██║███████╗╚██████╔╝███████╗██║ ╚████║
  ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═════╝ ╚═╝     ╚═╝╚══════╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝
[/bold cyan]
[dim]             Beautiful READMEs for your GitHub projects — 12 templates • Badges • ToC
[/dim]"""


def show_banner():
    console.print(BANNER)
    console.print()


def collect_project_info(quick=False):
    """Interactive wizard to collect project info."""
    info = {}

    console.print(Panel.fit(
        "[bold yellow]📋 Project Information[/bold yellow]\n"
        "[dim]Let's build your README! Fill in the details below.[/dim]",
        border_style="yellow"
    ))

    info["name"] = Prompt.ask("[bold cyan]Project name[/bold cyan]")
    info["tagline"] = Prompt.ask(
        "[bold cyan]One-line description[/bold cyan]",
        default=f"{info['name']} - a powerful tool"
    )

    if not quick:
        info["description"] = Prompt.ask(
            "[bold cyan]Longer description[/bold cyan] (optional — press Enter to skip)",
            default=""
        )
        info["features"] = Prompt.ask(
            "[bold cyan]Key features[/bold cyan] (comma-separated, e.g. 'Fast, Secure, Easy to use')",
            default="Fast, Reliable, Easy to use"
        )
        info["install_method"] = Prompt.ask(
            "[bold cyan]Install method[/bold cyan]",
            choices=["pip", "npm", "cargo", "go install", "brew", "docker", "curl", "git clone"],
            default="pip"
        )
        info["install_cmd"] = Prompt.ask(
            "[bold cyan]Install command[/bold cyan]",
            default=f"pip install {info['name'].lower().replace(' ', '-')}"
        )
        info["usage_example"] = Prompt.ask(
            "[bold cyan]Quick usage example[/bold cyan] (optional)",
            default=""
        )
        info["license"] = Prompt.ask(
            "[bold cyan]License[/bold cyan]",
            choices=["MIT", "Apache-2.0", "GPL-3.0", "BSD-3-Clause", "Unlicense", "Other"],
            default="MIT"
        )
        info["author"] = Prompt.ask("[bold cyan]Author/Organization[/bold cyan]", default="")
        info["repo_url"] = Prompt.ask("[bold cyan]GitHub repo URL[/bold cyan] (optional)", default="")
        info["badges"] = Prompt.ask(
            "[bold cyan]Badges[/bold cyan] (comma-separated: license, stars, version, python, node, docker, ci, coverage, downloads)",
            default="license, stars, version"
        )
        info["contributing"] = Confirm.ask("[bold cyan]Include Contributing section?[/bold cyan]", default=True)
        info["toc"] = Confirm.ask("[bold cyan]Include Table of Contents?[/bold cyan]", default=True)
        info["screenshots"] = Confirm.ask("[bold cyan]Include screenshot placeholder?[/bold cyan]", default=False)
    else:
        info["description"] = ""
        info["features"] = "Fast, Reliable, Easy to use"
        info["install_method"] = "pip"
        info["install_cmd"] = f"pip install {info['name'].lower().replace(' ', '-')}"
        info["usage_example"] = ""
        info["license"] = "MIT"
        info["author"] = ""
        info["repo_url"] = ""
        info["badges"] = "license, stars, version"
        info["contributing"] = True
        info["toc"] = True
        info["screenshots"] = False

    return info


def show_template_preview(template_name):
    """Show a mini preview of a template."""
    template = get_template(template_name)
    if not template:
        console.print(f"[red]Template '{template_name}' not found.[/red]")
        return

    preview = "\n".join(template["content"].split("\n")[:15]) + "\n..."
    console.print(Panel(
        Syntax(preview, "markdown", theme="monokai", line_numbers=False),
        title=f"[bold]Template: {template['name']}[/bold]",
        border_style="green"
    ))


@click.command()
@click.option("--template", "-t", help="Template name to use")
@click.option("--name", "-n", help="Project name")
@click.option("--tagline", "-d", help="One-line description")
@click.option("--output", "-o", default="README.md", help="Output file path (default: ./README.md)")
@click.option("--list", "list_flag", is_flag=True, help="List all available templates")
@click.option("--preview", "-p", help="Preview a template without generating")
@click.option("--quick", "-q", is_flag=True, help="Quick mode — fewer prompts, faster")
@click.option("--json-input", "json_input", help="Read project info from JSON file")
def main(template, name, tagline, output, list_flag, preview, quick, json_input):
    """readmegen — Generate beautiful README.md files for your GitHub projects."""

    if list_flag:
        show_templates_list()
        return

    if preview:
        show_template_preview(preview)
        return

    non_interactive = bool(name or json_input)

    if not non_interactive:
        show_banner()

    # Load from JSON if provided
    if json_input:
        with open(json_input) as f:
            info = json.load(f)
        console.print(f"[green]✓[/green] Loaded project info from {json_input}")
        # CLI overrides for JSON mode
        if name:
            info["name"] = name
        if tagline:
            info["tagline"] = tagline
    elif name:
        # Non-interactive mode: build info from defaults + CLI args
        info = {
            "name": name,
            "tagline": tagline or f"{name} - a powerful tool",
            "description": f"{name} is a powerful tool that helps you get things done faster.",
            "features": "Fast, Reliable, Easy to use",
            "install_method": "pip",
            "install_cmd": f"pip install {name.lower().replace(' ', '-')}",
            "usage_example": f"{name.lower().replace(' ', '-')} --help",
            "license": "MIT",
            "author": "",
            "repo_url": "",
            "badges": "license, stars, version",
            "toc": True,
            "contributing": True,
            "screenshots": False,
        }
    else:
        info = collect_project_info(quick=quick)
    if not template:
        if non_interactive:
            template = "default"
        else:
            # Choose template interactively
            template_names = list(TEMPLATES.keys())
            console.print()
            template_table = Table(title="Available Templates", box=box.ROUNDED, border_style="cyan")
            template_table.add_column("#", style="dim", width=4)
            template_table.add_column("Template", style="cyan")
            template_table.add_column("Description", style="green")
            template_table.add_column("Best for", style="yellow")

            for i, (tname, tdata) in enumerate(TEMPLATES.items(), 1):
                template_table.add_row(str(i), tname, tdata["description"], tdata["best_for"])

            console.print(template_table)
            console.print()

            choice = Prompt.ask(
                "[bold cyan]Choose template[/bold cyan] (number or name)",
                default="1"
            )
            if choice.isdigit():
                idx = int(choice) - 1
                if 0 <= idx < len(template_names):
                    template = template_names[idx]
            else:
                template = choice if choice in TEMPLATES else "default"

    console.print(f"\n[green]Using template:[/green] [bold]{template}[/bold]")

    # Generate
    with console.status("[bold green]Generating your README...[/bold green]", spinner="dots"):
        readme = generate_readme(info, template)

    # Write output
    output_path = Path(output)
    output_path.write_text(readme)

    console.print()
    console.print(Panel.fit(
        f"[bold green]✨ README generated successfully![/bold green]\n"
        f"[dim]Output:[/dim] [bold]{output_path.absolute()}[/bold]\n"
        f"[dim]Lines:[/dim] {len(readme.splitlines())}\n"
        f"[dim]Template:[/dim] {template}",
        border_style="green"
    ))

    # Show preview
    if not non_interactive and Confirm.ask("\n[bold cyan]Preview in terminal?[/bold cyan]", default=True):
        console.print()
        console.print(Panel(Markdown(readme[:3000]), title="README Preview", border_style="blue"))
        if len(readme) > 3000:
            console.print(f"[dim]... ({len(readme) - 3000} more characters)[/dim]")

    # Hint about Pro version
    console.print()
    console.print(Panel.fit(
        "[bold yellow]🔥 Love readmegen?[/bold yellow]\n"
        "[dim]Get the Pro version with 20+ exclusive templates, custom branding, and priority support.[/dim]\n"
        "[bold cyan]→ gumroad.com/l/readmegen-pro[/bold cyan]\n\n"
        "[dim]Or sponsor the project on GitHub:[/dim]\n"
        "[bold cyan]→ github.com/sponsors/feiwei8889[/bold cyan]",
        border_style="yellow"
    ))


def show_templates_list():
    """Display all available templates."""
    show_banner()
    table = Table(title="📚 Available Templates", box=box.ROUNDED, border_style="cyan")
    table.add_column("Name", style="cyan bold")
    table.add_column("Description", style="green")
    table.add_column("Best For", style="yellow")
    table.add_column("Sections", style="dim")

    for tname, tdata in TEMPLATES.items():
        sections = ", ".join(tdata.get("sections", [])[:5])
        table.add_row(tname, tdata["description"], tdata["best_for"], sections)

    console.print(table)
    console.print()
    console.print("[dim]Use [bold]readmegen --preview <name>[/bold] to preview a template[/dim]")
    console.print("[dim]Use [bold]readmegen --template <name>[/bold] to use a specific template[/dim]")


if __name__ == "__main__":
    main()
