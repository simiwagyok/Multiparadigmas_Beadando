import threading
import uvicorn
import os
import sys
from time import sleep

def get_path(filename):
    return os.path.join(os.path.dirname(__file__), filename)

def run_backend():
    uvicorn.run("backend.main:app", host="127.0.0.1", port=8000, reload=False)

def run_frontend():
    sleep(2)
    
    frontend_script = get_path(os.path.join("frontend", "app.py"))
    if not os.path.exists(frontend_script):
        print(f"HIBA: Nem található a fájl itt: {frontend_script}")
        return

    os.system(f"streamlit run {frontend_script}")

if __name__ == "__main__":
    backend_thread = threading.Thread(target=run_backend)
    backend_thread.start()
    run_frontend()