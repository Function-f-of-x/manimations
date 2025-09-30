import subprocess
from pathlib import Path

PROJECT_DIR = Path(__file__).parent.resolve()

def render(command: str) -> None:
    print(f"\n=== Рендеринг команды: {command} === \n")
    subprocess.run(f"{command}", shell=True, cwd=PROJECT_DIR)
    print(f"\n=== Рендер завершён ===\n")

    try:
        print("Сохраняем изменения в GitHub...\n")
        subprocess.run("git add .", shell=True, cwd=PROJECT_DIR)
        subprocess.run('git commit -m "Автоматический коммит после рендера"', shell=True, cwd=PROJECT_DIR)
        subprocess.run("git push", shell=True, cwd=PROJECT_DIR)
        print("\n=== Все изменения сохранены на GitHub ===\n")
    except subprocess.CalledProcessError as e:
        print("\nОшибка при сохранении в GitHub:", e, "\n")
