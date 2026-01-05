import time
import threading
from .database import SessionLocal
from .models import AutoJob

# Háttérfolyamat (Procedurális / Concurrency)
def monitor_rendszer():
    db = SessionLocal()
    try:
        v = db.query(AutoJob).filter(AutoJob.statusz == "Várakozás").count()
        m = db.query(AutoJob).filter(AutoJob.statusz == "Mosás").count()
        if v > 0 or m > 0:
            print(f"[MONITOR] Várakozik: {v} | Folyamatban: {m}")
    except:
        pass
    finally:
        db.close()

def futtat_worker():
    while True:
        monitor_rendszer()
        time.sleep(10)

def start_background_worker():
    szal = threading.Thread(target=futtat_worker, daemon=True)
    szal.start()
