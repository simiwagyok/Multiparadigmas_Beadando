import streamlit as st
import requests
import time
import os
import re

# Ha van környezeti változó (Deploy), azt használja, ha nincs, a localhostot
API_URL = os.getenv("BACKEND_URL", "https://multiparadigmas-beadando.onrender.com")

st.set_page_config(page_title="CleanCar", page_icon="🚗")
st.title("🚗 CleanCar Vezérlő")

# 1. ÚJ AUTÓ
with st.container(border=True):
    st.subheader("➕ Új autó")
    c1, c2 = st.columns(2)
    uj_rsz = c1.text_input("Rendszám (pl. ABC-123)", max_chars=7).upper()
    uj_tip = c2.text_input("Típus")
    opcio = st.selectbox("Szolgáltatás", ["Külső (3500)", "Belső (4500)", "Full (8000)"])
    
    if st.button("Rögzítés", type="primary"):
        if not re.match(r"^[A-Z]{3}-[0-9]{3}$", uj_rsz):
            st.error("❌ Hibás formátum! Helyes: ABC-123")
        elif not uj_tip:
            st.error("❌ Hiányzó típus!")
        else:
            ar = int(opcio.split("(")[1].split(")")[0])
            try:
                r = requests.post(f"{API_URL}/munkak/", json={"rendszam": uj_rsz, "tipus": uj_tip, "szolgaltatas": opcio.split(" (")[0], "ar": ar})
                if r.status_code == 200:
                    st.success("✅ Felvéve!")
                    time.sleep(1)
                    st.rerun()
                else:
                    st.error(f"Hiba: {r.text}")
            except:
                st.error("Nem érhető el a Backend szerver!")

st.markdown("---")

# 2. VEZÉRLÉS
st.subheader("🎛️ Aktív Munkák")
try:
    resp = requests.get(f"{API_URL}/munkak/aktiv")
    if resp.status_code == 200:
        munkak = resp.json()
        if not munkak: st.info("📭 A műhely üres.")
        for job in munkak:
            with st.container(border=True):
                c1, c2, c3, c4 = st.columns([1.5, 2, 2, 2])
                c1.write(f"**{job['rendszam']}**")
                c2.write(job['tipus'])
                
                if job['statusz'] == "Várakozás":
                    c3.warning("⏳ Sorban áll")
                    if c4.button("▶️ INDÍTÁS", key=f"s_{job['id']}"):
                        requests.put(f"{API_URL}/munkak/{job['id']}/start")
                        st.rerun()
                elif job['statusz'] == "Mosás":
                    if "Belső" in job['szolgaltatas'] or "Full" in job['szolgaltatas']:
                        c3.info("🧹 Takarítás...")
                    else:
                        c3.info("💦 Mosás...")
                    if c4.button("✅ KÉSZ", key=f"k_{job['id']}", type="primary"):
                        requests.put(f"{API_URL}/munkak/{job['id']}/kesz")
                        st.balloons()
                        time.sleep(1)
                        st.rerun()
    else: st.error("Backend hiba")
except: st.error("Nem érhető el a szerver.")

st.markdown("---")
# 3. STATISZTIKA
try:
    stat = requests.get(f"{API_URL}/statisztika").json()
    st.metric("💰 Napi Bevétel", f"{int(stat['bevetel'])} Ft")
except: pass
