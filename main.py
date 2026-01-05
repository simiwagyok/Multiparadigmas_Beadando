import uvicorn
import os
import time
from threading import Thread

# 1. Backend indítása
# Mivel a te fájlodban 'app' a változó neve, ez így tökéletes:
def run_backend():
    print("🚀 Backend indítása (FastAPI)...")
    # A "backend.main:app" azt jelenti:
    # backend mappa -> main.py fájl -> app változó
    uvicorn.run("backend.main:app", host="127.0.0.1", port=8000, reload=True)

# 2. Frontend indítása
def run_frontend():
    time.sleep(2) # Várunk picit, hogy a backend betöltsön
    print("🎨 Frontend indítása (Streamlit)...")
    # Feltételezve, hogy a frontend kódod a 'frontend' mappában van 'main.py' néven
    # Ha máshogy hívják (pl. app.py), írd át a végén a nevet!
    os.system("streamlit run frontend/main.py")

if __name__ == "__main__":
    # Két szálon indítjuk a rendszert
    t1 = Thread(target=run_backend)
    t2 = Thread(target=run_frontend)

    t1.start()
    t2.start()

    t1.join()
    t2.join()