#!/bin/bash
echo "CleanCar Indítása..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi
source venv/bin/activate
pip install -r requirements.txt
python main.py
