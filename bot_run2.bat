@echo off

call %~dp0C bot_telegram\venv\Scripts\activate

cd %~dp0C bot_telegram


set TOKEN=5593587070:AAFvaWgPzfb9HuXeSV2zBdxLiYt5OzTysSs

python Tele_bott.py 

pause