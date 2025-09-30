#!/bin/bash
# Апельсиновый установщик Manim 🍊

echo -e "\n=== Обновляем системные пакеты ===\n"
sudo apt update

echo -e "\n=== Устанавливаем зависимости для Manim (Cairo, TeX, Pango) ===\n"
sudo apt install -y libcairo2-dev \
    texlive texlive-latex-extra texlive-fonts-extra \
    texlive-latex-recommended texlive-science \
    tipa libpango1.0-dev

echo -e "\n=== Обновляем pip и устанавливаем Python-пакеты ===\n"
python -m pip install --upgrade pip --user
python -m pip install manim --user
python -m pip install IPython==8.21.0 --user

echo -e "\n=== Установка завершена ✅ ===\n"
