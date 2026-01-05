from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from contextlib import asynccontextmanager
from typing import List
from .database import engine, Base, get_db
from .models import AutoJob
from .schemas import AutoJobCreate, AutoJobResponse, Statisztika
from .worker import start_background_worker
from .logic import szamol_bevetel, szamol_statusz

Base.metadata.create_all(bind=engine)

@asynccontextmanager
async def lifespan(app: FastAPI):
    start_background_worker()
    yield

app = FastAPI(title="CleanCar API", lifespan=lifespan)

@app.get("/")
def root():
    return {"message": "CleanCar API működik"}

@app.get("/munkak/aktiv", response_model=List[AutoJobResponse])
def aktiv_munkak(db: Session = Depends(get_db)):
    return db.query(AutoJob).filter(AutoJob.statusz != "Kész").all()

@app.put("/munkak/{id}/start")
def munka_start(id: int, db: Session = Depends(get_db)):
    job = db.query(AutoJob).filter(AutoJob.id == id).first()
    if not job: raise HTTPException(status_code=404, detail="Nincs ilyen")
    job.statusz = "Mosás"
    db.commit()
    return {"msg": "Elindítva"}

@app.put("/munkak/{id}/kesz")
def munka_kesz(id: int, db: Session = Depends(get_db)):
    job = db.query(AutoJob).filter(AutoJob.id == id).first()
    if not job: raise HTTPException(status_code=404, detail="Nincs ilyen")
    job.statusz = "Kész"
    db.commit()
    return {"msg": "Kész"}

@app.post("/munkak/", response_model=AutoJobResponse)
def uj_munka(munka: AutoJobCreate, db: Session = Depends(get_db)):
    letezo = db.query(AutoJob).filter(AutoJob.rendszam == munka.rendszam.upper(), AutoJob.statusz != "Kész").first()
    if letezo: raise HTTPException(status_code=400, detail="Már a rendszerben van!")
    db_item = AutoJob(rendszam=munka.rendszam.upper(), tipus=munka.tipus, szolgaltatas=munka.szolgaltatas, ar=munka.ar)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.get("/munkak/{rendszam}", response_model=List[AutoJobResponse])
def kereses(rendszam: str, db: Session = Depends(get_db)):
    eredmeny = db.query(AutoJob).filter(AutoJob.rendszam == rendszam.upper()).order_by(AutoJob.letrehozva.desc()).all()
    if not eredmeny: raise HTTPException(status_code=404, detail="Nincs találat")
    return eredmeny

@app.get("/statisztika", response_model=Statisztika)
def leker_stat(db: Session = Depends(get_db)):
    adatok = db.query(AutoJob).all()
    valid = [AutoJobResponse.model_validate(x) for x in adatok]
    return Statisztika(
        bevetel=szamol_bevetel(valid),
        ossz_auto=len(adatok),
        varakozik=szamol_statusz(valid)["Várakozás"],
        kesz=szamol_statusz(valid)["Kész"]
    )
