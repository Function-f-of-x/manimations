import subprocess
from pathlib import Path

PROJECT_DIR = Path(__file__).parent.resolve()

def render(command: str) -> None:
    """
    command - строка вида: "manim -qh Example.py SquareToCircle"
    Рендерит сцену в новом процессе.
    """
    subprocess.run(command, shell=True, cwd=PROJECT_DIR)
