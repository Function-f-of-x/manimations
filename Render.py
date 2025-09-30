import subprocess
from pathlib import Path

PROJECT_DIR = Path(__file__).parent.resolve()

def render(command: str) -> None:
    """
    command - строка вида: "manim -qh Example.py SquareToCircle"
    Рендерит сцену, а затем коммитит и пушит весь репозиторий.
    """
    # 1️⃣ Рендер сцены
    print(f"Рендеринг команды: {command} ...")
    subprocess.run(command, shell=True, cwd=PROJECT_DIR)

    # 2️⃣ Git: добавляем, коммитим и пушим все изменения
    try:
        print("Сохраняем изменения в GitHub...")
        subprocess.run("git add .", shell=True, cwd=PROJECT_DIR)
        subprocess.run('git commit -m "Автоматический коммит после рендера"', shell=True, cwd=PROJECT_DIR)
        subprocess.run("git push", shell=True, cwd=PROJECT_DIR)
        print("Все изменения сохранены на GitHub ✅")
    except subprocess.CalledProcessError as e:
        print("Ошибка при сохранении в GitHub:", e)
