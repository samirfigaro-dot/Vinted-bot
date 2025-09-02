import streamlit as st
from pyvinted import Vinted

# Inizializza connessione API Vinted
vinted = Vinted()

# Funzione per ottenere annunci (esempio cerca "scarpe")
def get_items(keyword="scarpe"):
    return vinted.items.search(query=keyword, per_page=10)

# --- INTERFACCIA DASHBOARD ---
st.set_page_config(page_title="Vinted Bot", layout="wide")

st.title("🛍️ Pannello Vinted Bot")
st.write("Gestisci i tuoi annunci direttamente da questa interfaccia.")

# Campo di ricerca
keyword = st.text_input("Cerca prodotti su Vinted:", "scarpe")

if st.button("Cerca"):
    items = get_items(keyword)
    if items:
        st.write(f"### Risultati per '{keyword}'")
        for item in items:
            st.write(
                f"**{item['title']}** - {item['price']['amount']} {item['price']['currency']}\n"
                f"[🔗 Link]({item['url']})"
            )
    else:
        st.warning("Nessun annuncio trovato.")
