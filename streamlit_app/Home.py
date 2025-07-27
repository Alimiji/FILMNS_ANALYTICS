import streamlit as st

# Interface utilisateur avec Streamlit
st.set_page_config(
    layout="wide",
    page_title="MovieLens Data Analysis",
    page_icon="🎬"  # Emoji Unicode directement
)

# Conteneur pour aligner les éléments horizontalement
col1, col2, col3 = st.columns([1, 4, 1])

# Colonne gauche : Image
with col1:
    st.image(
        "https://github.com/Alimiji/FILMNS_ANALYTICS/blob/main/streamlit_app/alimiji1.jpg",  # Remplacez par le chemin de votre image
        width=200,     # Ajustez la taille si nécessaire
        use_container_width=False,
    )

# Colonne centrale : Titre
with col2:
    st.markdown(
        """
        <h1 style='text-align: center; margin-bottom: 0;'>Exploration des Données MovieLens</h1>
        """,
        unsafe_allow_html=True,
    )

# Colonne droite : Nom et lien LinkedIn
with col3:
    st.markdown(
        """
        <div style='text-align: right;'>
            <a href="https://www.linkedin.com/in/ali-mijiyawa-946609162/" target="_blank" style='text-decoration: none; color: #0077b5;'>
                <strong>Ali MIJIYAWA</strong>
            </a>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.write(" ")
st.write(" ")

# Titre
st.markdown("# **Phase 1 : Développeur Python / Data ingenieur & Architecte API**")
st.write(" ")
st.write(" ")
# Afficher l'image séparément
st.image("diag1.png", use_container_width=True)

st.markdown(
        """
        <a href="https://github.com/Alimiji/dataScience-movie-backend" target="_blank">
            <button style="background-color: #28a745; color: white; padding: 10px 20px; border: none; border-radius: 8px; font-size: 16px;">
                📦 Cliquer pour accéder au Code de la Phase 1
            </button>
        </a>
        """,
        unsafe_allow_html=True
    )

st.write(" ")
st.write(" ")
#st.write(" ")


# Titre
st.markdown("# **Phase 2 : Data Analyst - Exploration et Visualisation**")
# Afficher l'image séparément
st.image("https://raw.githubusercontent.com/Alimiji/FILMNS_ANALYTICS/main/streamlit_app/architect2.png", use_container_width=True)

st.markdown(
        """
        <a href="https://github.com/Alimiji/FILMNS_ANALYTICS" target="_blank">
            <button style="background-color: #28a745; color: white; padding: 10px 20px; border: none; border-radius: 8px; font-size: 16px;">
                📊 Cliquer pour accéder au Code de la Phase 2
            </button>
        </a>
        """,
        unsafe_allow_html=True
    )


st.write(" ")
st.write(" ")
#st.write(" ")


# Titre
st.markdown("#  **Phase 3 : Data Scientist – Machine Learning / MLOps**")
# Afficher l'image séparément
st.image("architect_etape3.png", use_container_width=True)

# ✅ Bouton HTML stylisé
st.markdown(
    """
    <a target="_blank">
        <button style="background-color: #28a745; color: white; padding: 10px 20px; border: none; border-radius: 8px; font-size: 16px;">
            🤖🛠️ Code de la phase 3 est en cours ...
        </button>
    </a>
    """,
    unsafe_allow_html=True
)
