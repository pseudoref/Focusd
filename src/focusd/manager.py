import yaml
from pathlib import Path

class ProfileManager:
    def __init__(self, profiles_dir: str | None = None):
        self.profiles_dir = Path(profiles_dir or Path(__file__).parent / "profiles")

    def load_profile(self, name: str) -> dict:
        p = Path(name)
        if p.exists():
            return yaml.safe_load(p.read_text())
        candidate = self.profiles_dir / f"{name}.yaml"
        if candidate.exists():
            return yaml.safe_load(candidate.read_text())
        raise FileNotFoundError(f"Profile {name} not found")

    def switch(self, profile_name: str):
        profile = self.load_profile(profile_name)
        # TODO: orchestration: pre-hook, block, apps, governor, post-hook
        print("Would apply profile:", profile.get("name", profile_name))

    def status(self) -> dict:
        return {"profiles_dir": str(self.profiles_dir)}

    def timer(self, duration: str):
        print("Timer stub:", duration)

    def modify_block(self, action: str, host: str):
        print(action, host)

