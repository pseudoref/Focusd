import subprocess
import yaml
from pathlib import Path

PROFILE_DIR = Path(__file__).resolve().parent.parent.parent / "profiles"
HOOK_DIR = Path(__file__).resolve().parent.parent.parent / "hooks"

def load_profile(name: str):
    profile_path = PROFILE_DIR / f"{name}.yml"
    if not profile_path.exists():
        raise FileNotFoundError(f"Profile '{name}' not found.")

    with open(profile_path, "r") as f:
        return yaml.safe_load(f) or {}

def run_hook(hook_name: str):
    hook_file = HOOK_DIR / hook_name
    if hook_file.exists():
        subprocess.run(["bash", hook_file], check=False)

def apply_profile(profile: dict):
    for app in profile.get("apps", {}).get("start", []):
        subprocess.Popen([app])
    
    for app in profile.get("apps", {}).get("stop", []):
        subprocess.run(["pkill", "-f", app], check=False)

    if "cpu_governor" in profile:
        subprocess.run(
                ["sudo", "cpupower", "frequency-set", "-g", profile["cpu_governor"]],
                check=False,
                )

def switch_profile(name: str):
    print(f"[focusd] Switching to profile: {name}")

    run_hook("pre_switch.sh")

    profile = load_profile(name)
    apply_profile(profile)

    run_hook("post_switch.sh")

    print(f"[focusd] Profile '{name}' activated.")

    
