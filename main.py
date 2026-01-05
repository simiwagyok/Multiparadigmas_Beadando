import threading
import uvicorn
import os
import sys
from time import sleep

# Segédfüggvény az abszolút útvonalhoz
def get_path(filename):
    return os.path.join(os.path.dirname(__file__), filename)

def run_backend():
    # FONTOS: reload=False, mert szálban vagyunk!
    uvicorn.run("backend.main:app", host="127.0.0.1", port=8000, reload=False)

def run_frontend():
    # Kis várakozás, hogy a backend biztosan elinduljon előbb
    sleep(2)
    
    # Abszolút útvonal a frontend fájlhoz
    frontend_script = get_path(os.path.join("frontend", "app.py"))
    
    # Ellenőrizzük, létezik-e a fájl
    if not os.path.exists(frontend_script):
        print(f"HIBA: Nem található a fájl itt: {frontend_script}")
        return

    # Streamlit indítása parancssori hívással
    os.system(f"streamlit run {frontend_script}")

if __name__ == "__main__":
    # Backend indítása külön szálon
    backend_thread = threading.Thread(target=run_backend)
    backend_thread.start()

    # Frontend indítása (ez futhat a fő szálon vagy külön is)
    run_frontend()