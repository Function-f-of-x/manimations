import subprocess
from pathlib import Path

PROJECT_DIR = Path(__file__).parent.resolve()

def save():
    try:
        print("\n=== Сохраняем все изменения в GitHub ===\n")
        subprocess.run("git add .", shell=True, cwd=PROJECT_DIR)
        subprocess.run('git commit -m "Ручной коммит"', shell=True, cwd=PROJECT_DIR)
        subprocess.run("git push", shell=True, cwd=PROJECT_DIR)
        print("\n=== Все изменения успешно сохранены на GitHub ===\n")
    except subprocess.CalledProcessError as e:
        print("\nОшибка при сохранении в GitHub:", e, "\n")

if __name__ == "__main__":
    save()