# CleanCar Tracker - Multiparadigmás Beadandó

Ez a projekt egy mikroszerviz-architektúrájú autókozmetikai nyilvántartó rendszer. A rendszer lehetővé teszi autók felvételét, és a mosási folyamat (Várakozás -> Mosás -> Kész) manuális vezérlését egy admin felületen keresztül.

## Architektúra
A rendszer három fő komponensből áll:
1. **Backend (FastAPI):** REST API, amely kezeli az üzleti logikát és az adatbázis műveleteket.
2. **Frontend (Streamlit):** Webes felület az ügyfeleknek (keresés) és az adminisztrátornak (vezérlés).
3. **Adatbázis (SQLite):** Az adatok tartós tárolása.

## Felhasznált Paradigmák
A projekt bemutatja a Python multiparadigmás képességeit:
* **Objektumorientált (OOP):** Az adatbázis modellek (`models.py`) osztályként vannak definiálva, öröklődést használva.
* **Funkcionális:** A statisztikai számítások (`logic.py`) tisztán funkcionális módon, `map`, `filter` és `reduce` függvényekkel történnek.
* **Procedurális:** A rendszer indítása (`main.py`) és a háttérfolyamatok (`worker.py`) imperatív stílusban íródtak.

## Telepítés és Futtatás (Lokálisan)

1. **Klónozás:**
   ```bash
   git clone [https://github.com/FELHASZNALONEV/CleanCar_Beadando.git](https://github.com/FELHASZNALONEV/CleanCar_Beadando.git)
   cd CleanCar_Beadando
   ```

2. **Környezet beállítása:**
   ```bash
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # Linux/Mac:
   source venv/bin/activate
   ```

3. **Függőségek telepítése:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Indítás:**
   A teljes rendszer (Backend + Frontend) egyetlen paranccsal indítható:
   ```bash
   python main.py
   ```
   *Vagy használhatja a mellékelt `start.sh` (Linux) vagy `start.bat` (Windows) fájlokat.*

## Deploy (Felhő)
* **Backend:** Render.com (Web Service)
* **Frontend:** Streamlit Cloud

## Készítette
[Saját Neved]
