import typer
from rich.console import Console
from pathlib import Path
from .manager import ProfileManager
from .switcher import switch_profile

app = typer.Typer()
console = Console()
manager = ProfileManager()

@app.command()
def switch(profile: str):
    console.print(f"[bold]Switching to:[/] {profile}")
    manager.switch(profile)

@app.command()
def status():
    console.print(manager.status())

@app.command()
def timer(duration: str = "25m"):
    manager.timer(duration)
    console.print(f"Timer started: {duration}")

@app.command()
def block(action: str, host: str):
    if action not in ("add", "remove"):
        raise typer.BadParameter("action must be add or remove")
    manager.modify_block(action, host)
    console.print(f"{action} {host}")

@app.command()
def switch(profile: str):
    switch_profile(profile)

if __name__ == "__main__":
    app()

