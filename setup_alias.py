import platform
import sys
from pathlib import Path


def get_rc_file() -> Path:
    system = platform.system()
    if system == "Darwin":
        return Path.home() / ".zshrc"
    elif system == "Linux":
        return Path.home() / ".bashrc"
    elif system == "Windows":
        git_bash = Path("C:/Program Files/Git/bin/bash.exe")
        if git_bash.exists():
            return Path.home() / ".bashrc"
        print("Error: Git Bash not found", file=sys.stderr)
        sys.exit(1)
    else:
        print(f"Error: unsupported platform: {system}", file=sys.stderr)
        sys.exit(1)


def main():
    rc_file = get_rc_file()
    project_root = Path(__file__).resolve().parent
    if platform.system() == "Windows":
        venv_python = project_root / ".venv" / "Scripts" / "python.exe"
    else:
        venv_python = project_root / ".venv" / "bin" / "python"
    entry_script = project_root / "main.py"

    alias_name = "md2p"
    cmd = f'"{venv_python}" "{entry_script}"'
    alias_line = f"alias {alias_name}='{cmd}'\n"

    content = rc_file.read_text() if rc_file.exists() else ""
    header = "# md-to-pdf-config"
    if f"alias {alias_name}=" in content:
        if alias_line.strip() in content:
            print(f"Alias '{alias_name}' already up-to-date in {rc_file}")
        else:
            lines = content.splitlines(keepends=True)
            new_lines = []
            i = 0
            while i < len(lines):
                if lines[i].strip() == header:
                    i += 1
                    continue
                if lines[i].strip().startswith(f"alias {alias_name}="):
                    i += 1
                    continue
                new_lines.append(lines[i])
                i += 1
            new_lines.append(f"\n{header}\n{alias_line}")
            rc_file.write_text("".join(new_lines))
            print(f"Updated alias '{alias_name}' in {rc_file}")
    else:
        with open(rc_file, "a") as f:
            f.write(f"\n{header}\n{alias_line}")
        print(f"Added to {rc_file}")

    print(f"Run: source {rc_file}")
    print(f"Usage: {alias_name} path/to/file.md")


if __name__ == "__main__":
    main()
