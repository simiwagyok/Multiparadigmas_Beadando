@echo off
echo CleanCar Rendszer Inditasa...
if not exist venv ( python -m venv venv )
call venv\Scriptsctivate
pip install -r requirements.txt > nul 2>&1
python main.py
pause
