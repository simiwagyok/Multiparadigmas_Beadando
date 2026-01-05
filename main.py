import os
import threading
import time
import uvicorn
import sys

def start_backend():
    # Lokális indításnál közvetlenül hívjuk
    uvicorn.run("backend.main:app", host="127.0.0.1", port=8000, reload=False)

def start_frontend():
    time.sleep(3)
    os.system("streamlit run frontend/app.py")

if __name__ == "__main__":
    t = threading.Thread(target=start_backend, daemon=True)
    t.start()
    try:
        start_frontend()
    except KeyboardInterrupt:
        sys.exit(0)
