import streamlit as st
import pandas as pd
import plotly.express as px
import os
from pathlib import Path
from utils import load_parquet_data



# Configuration de la page
st.set_page_config(
    page_title="🏠 Accueil | FILMNS Analytics",
    page_icon="🏠",  # Icône de l’onglet (favicon)
    layout="wide"
)

# Contenu principal
st.title("🏠 Bienvenue sur FILMNS Analytics")
st.subheader("🎬 Analyse de données sur les films et les utilisateurs")

st.markdown("""
Bienvenue dans le tableau de bord **FILMNS** 🎉 !

Ici, vous pouvez :
- 🔍 Explorer les genres de films les plus populaires
- 👥 Analyser le comportement des utilisateurs
- 📈 Suivre l’évolution des évaluations de films au fil des années
- 🏆 Découvrir les meilleurs films selon les notes

Utilisez le menu à gauche pour naviguer entre les pages 📂.
""")

st.success("Commencez votre exploration avec le menu à gauche 👈")