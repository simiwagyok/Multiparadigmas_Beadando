import streamlit as st
import requests
import time
import os
import re

API_URL = os.getenv("BACKEND_URL", "https://multiparadigmas-beadando.onrender.com")

st.set_page_config(page_title="Autókozmetika")
st.title("Autókozmetika")

with st.container(border=True):
    st.subheader("Autó hozzáadása:")
    with st.form("uj_auto_form", clear_on_submit=True):
        c1, c2 = st.columns(2)
        uj_rsz = c1.text_input("Rendszám (pl. ABC-123):", max_chars=7).upper()
        uj_tip = c2.text_input("Autó típusa:")
        opcio = st.selectbox("Szolgáltatás:", ["Külső (3500)", "Belső (4500)", "Full (8000)"])
        submitted = st.form_submit_button("Küldés", type="primary")
        
        if submitted:
            if not re.match(r"^[A-Z]{3}-[0-9]{3}$", uj_rsz):
                st.error("Csak ABC-123 formátumban adhatod meg a rendszámot!")
            elif not uj_tip:
                st.error("Nincs megadva típus!")
            else:
                ar = int(opcio.split("(")[1].split(")")[0])
                adatok = {
                    "rendszam": uj_rsz, 
                    "tipus": uj_tip, 
                    "szolgaltatas": opcio.split(" (")[0], 
                    "ar": ar
                }
                
                try:
                    r = requests.post(f"{API_URL}/munkak/", json=adatok)
                    if r.status_code == 200:
                        st.caption("A munka sikeresen rögzítve.")
                        time.sleep(1.5)
                        st.rerun()
                    else:
                        st.error(f"Hiba: {r.text}")
                except Exception as e:
                    st.error(f"Nem érhető el a Backend szerver! ({e})")

st.markdown("---")
st.subheader("Jelenlegi munkáink:")

try:
    resp = requests.get(f"{API_URL}/munkak/aktiv")
    if resp.status_code == 200:
        munkak = resp.json()
        
        if not munkak: 
            st.info("Jelenleg egyetlen munka sincs :(")
            
        for job in munkak:
            with st.container(border=True):
                c1, c2, c3, c4 = st.columns([1.5, 2, 2, 2])
                c1.write(f"**{job['rendszam']}**")
                c2.write(job['tipus'])
                if job['statusz'] == "Várakozás":
                    c3.warning("Sorban áll...")
                    if c4.button("Indítás", key=f"start_{job['id']}"):
                        requests.put(f"{API_URL}/munkak/{job['id']}/start")
                        st.rerun()
                
                elif job['statusz'] == "Mosás":
                    if "Belső" in job['szolgaltatas'] or "Full" in job['szolgaltatas']:
                        c3.info("Takarítás alatt...")
                    else:
                        c3.info("Mosás...")
                    
                    if c4.button("Kész", key=f"done_{job['id']}", type="primary"):
                        requests.put(f"{API_URL}/munkak/{job['id']}/kesz")
                        st.success("Munka kész! Köszönjük, hogy minket választottál!")
                        time.sleep(1)
                        st.rerun()
    else: 
        st.error("Backend hiba")

except Exception as e: 
    st.error(f"Nem érhető el a szerver.")

st.markdown("---")

try:
    stat_resp = requests.get(f"{API_URL}/statisztika")
    if stat_resp.status_code == 200:
        stat = stat_resp.json()
        st.metric("Jelenlegi befolyt összeg:", f"{int(stat['bevetel'])} Ft")
except: 
    pass