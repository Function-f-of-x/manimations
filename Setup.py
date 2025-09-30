import subprocess

def run(cmd):
    print(f"\n$ {cmd}\n")
    subprocess.run(cmd, shell=True, check=True)

def main():
    print("\n=== Обновляем системные пакеты ===\n")
    run("sudo apt update")

    print("\n=== Устанавливаем зависимости для Manim (Cairo, TeX, Pango) ===\n")
    run("sudo apt install -y libcairo2-dev "
        "texlive texlive-latex-extra texlive-fonts-extra "
        "texlive-latex-recommended texlive-science "
        "tipa libpango1.0-dev")

    print("\n=== Обновляем pip и устанавливаем Python-пакеты ===\n")
    run("python -m pip install --upgrade pip --user")
    run("python -m pip install manim --user")
    run("python -m pip install IPython==8.21.0 --user")

    print("\n=== Установка завершена ===\n")

if __name__ == "__main__":
    main()
