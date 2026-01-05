**Multiparadigmás beadandó**

Egy Autókozmetikai rendszert írtam meg, melyben egy autónak lehet kiválasztani, hogy mit csináljunk vele.

**Jellemzői:**

- 3 féle takarítási mód van.
- befolyt összeg megjelenítése
- bemenet ellenőrzése
- felhasználó tájékoztatása arról, hogy éppen hol tart az autó takarítása

**3 részből áll a program:**

- Backend (FastAPI): Rest api, ami kezeli az adatbázist és az ütleti logikát.
- Frontend (Streamlit): Itt lehet kereseni a sima felhasználónak és az adminnak lehet továbbléptetni az állapotot.
- Adatbázis (SQLite): Az adatok tárolása

**Paradigmák:**

Objektumorientált (OOP): Az adatbázis modellek osztályként vannak definiálva (models.py) és öröklődést használnak
Funkcionális: Statisztikai számítások(logic.py), függvényekkel.
Procedurális: Itt indul a rendszer és a háttérfolyamat is itt fut.

**Telepítés és futtatás saját gépen:**

1. Git klónozása:
   git clone https://github.com/simiwagyok/Multiparadigmas_Beadando.git

Majd a mappába való belépés
cd CleanCar_Beadando

2. Virtuális környezet létrehozása:
   python -m venv venv

Majd aktiválása:
venv\Scripts\activate

3. Függőségek telepítése:
   pip install -r requirements.txt

4. Terminal:
   python main.py (ez elindítja a frontendet és a backendet)

**Frontend külön elindítása:**
cd .\CleanCar_Beadando\frontend\
 streamlit run app.py

**Backend külön elindítása:**
cd .\CleanCar_Beadando\
 uvicorn backend.main:app --reload

**Futtatás felhőben:**

- Backend link: https://multiparadigmas-beadando.onrender.com
- Frontend link: https://multiparadigmasbeadando.streamlit.app/
