import subprocess

APPS = {
    "firefox": "firefox",
    "chrome": "google-chrome",
    "terminal": "gnome-terminal",
    "files": "nautilus",
    "vscode": "code",
    "calculator": "gnome-calculator",
}

def open_app(name):
    app = APPS.get(name.lower())
    if app:
        subprocess.Popen([app])
        return f"Opening {name}..."
    return f"Sorry, RudraX doesn't know how to open '{name}'."
