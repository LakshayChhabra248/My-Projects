# scoresight/main.py
import sys
import os

# Add the project root directory to the Python path
# This allows us to import modules from the 'scoresight' package
# using absolute paths like 'from scoresight.gui import app_window'
# even when running main.py directly.
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from scoresight.gui.app_window import AppWindow

def run_app():
    """Initializes and runs the ScoreSight application."""
    app = AppWindow()
    app.mainloop()

if __name__ == "__main__":
    print(f"Project Root added to sys.path: {project_root}") # Debug print
    print(f"Current sys.path: {sys.path}") # Debug print
    run_app()