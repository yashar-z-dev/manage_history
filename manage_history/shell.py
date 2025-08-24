import os

def detect_shell(debug=False):
    shell_path = os.environ.get("SHELL", "")
    shell_name = os.path.basename(shell_path)

    if debug:
        print(f"[DEBUG] SHELL environment variable: {shell_path}")
        print(f"[DEBUG] Detected shell name: {shell_name}")

    if shell_name == "zsh":
        return "zsh", os.path.expanduser("~/.zsh_history")
    elif shell_name == "bash":
        return "bash", os.path.expanduser("~/.bash_history")
    return None, None
