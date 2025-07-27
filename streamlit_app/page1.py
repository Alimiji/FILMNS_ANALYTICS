import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path
import os
from utils import load_parquet_data


#from utils import load_parquet_data

# Définition du dossier de sortie
OUTPUT_DIR = Path(__file__).resolve().parent.parent / "output"

st.title("🎬 Analyse Générale des Films et Évaluations")

# Fonction cache pour charger les fichiers parquet
#@st.cache_data
#def load_parquet_data(file_name):

#    file_path = OUTPUT_DIR / file_name
#    return pd.read_parquet(file_path)


genre_df = load_parquet_data("genre_df.parquet")
#st.write(genre_df.head(10))

movies_by_year = load_parquet_data("movies_by_year.parquet")

#st.write(movies_by_year)

top_movies = load_parquet_data("top_movies_by_ratings.parquet")

#st.write(top_movies)

#genre_rating_stats = load_parquet_data("genre_rating_stats.parquet")


ratings_df = load_parquet_data("ratings.parquet")

# Graphique 1 : Top 10 genres par nombre de films
fig_genre = px.bar(
    genre_df,
    x="count",
    y="genre",
    title="Top 10 genres par nombre de films",
    labels={"genre": "Genre", "count": "Nombre <br>de films"},
    color="count",
    color_continuous_scale="viridis",
    orientation='h'
)
fig_genre.update_layout(
    yaxis={'categoryorder': 'total ascending'},
    height=400
)
#fig_genre.update_layout(title_font=dict(size=14))
fig_genre.update_layout(
    font=dict(size=14),
    title_font_size=14
)


 # agrandir la marge droite pour éviter le rognage
#st.plotly_chart(fig_genre, use_container_width=True)


# Graphique 2 : Top 10 genres par nombre d’évaluations et note moyenne
#top10_genre_stats = genre_rating_stats.sort_values("rating_count", ascending=False).head(10)
#fig_genre_rating = px.bar(
#   top10_genre_stats,
#  x="rating_count",
#  y="genre",
#    orientation="h",
#    color="avg_rating",
#    color_continuous_scale="viridis",
#    title="Top 10 genres par nombre d’évaluations et note moyenne",
#    labels={"genre": "Genre", "rating_count": "Nombre d'évaluations", "avg_rating": "Note moyenne"}
#)
#fig_genre_rating.update_layout(
#    yaxis={'categoryorder': 'total ascending'},
#    height=350
#)

#st.plotly_chart(fig_genre_rating)

# Graphique 3 : Top 10 utilisateurs par nombre d’évaluations

ratings_per_user = ratings_df['userId'].value_counts().reset_index()
ratings_per_user.columns = ['userId', 'rating_count']
top_users = ratings_per_user.head(10)
fig_users = px.bar(     top_users,
     x="rating_count",
     y=top_users["userId"].astype(str),
     orientation="h",
     title="Top 10 des utilisateurs par <br> nombre d’évaluations",
     labels={"userId": "Utilisateur", "rating_count": "Nombre d’évaluations"},
     color="rating_count",
     color_continuous_scale="viridis"
)

fig_users.update_layout(
     yaxis={'categoryorder': 'total ascending'},
     height=350
 )

fig_users.update_layout(title_font=dict(size=14), title_x=0.1  # Centre horizontalement (0.0 = gauche, 1.0 = droite
                             )
#st.plotly_chart(fig_top_movies, key="top_movies_chart")

# Graphique 4 : Top 20 des films par nombre d’évaluations

fig_top_movies = px.bar(
   top_movies.sort_values("rating_count", ascending=True),
    x="rating_count",
    y="title",
    color="avg_rating",
    orientation="h",
    title="Top 20 des films par nombre d'évaluations",
    labels={"title": "Titre du film", "rating_count": "Nombre d'évaluations", "avg_rating": "Note moyenne"},
    color_continuous_scale="viridis"
    )
fig_top_movies.update_layout(
    yaxis={'categoryorder': 'total ascending'},
    height=700
)
fig_top_movies.update_layout(title_font=dict(size=14), title_x=0.2  # Centre horizontalement (0.0 = gauche, 1.0 = droite
                             )
#st.plotly_chart(fig_top_movies, key="top_movies_chart")


# Graphique 5 : Nombre de films par année
fig_by_year = px.bar(
    movies_by_year,
    x="year",
    y="movie_count",
    title="Nombre total de films par année (basé sur le titre)",
    labels={"year": "Année", "movie_count": "Nombre de films"},
)
fig_by_year.update_layout(
    xaxis_title="Année",
    yaxis_title="Nombre de films",
    height=500
)
fig_by_year.update_layout(title_font=dict(size=14))


# Mise en page Streamlitfilms

st.markdown(
    """
    <style>
    /* Élargir la largeur de la page principale */
    .main {
        padding-left: 2rem;
        padding-right: 2rem;
        max-width: 95%;
    }

    /* Centrer le contenu */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# --- Première rangée : fig_genre & fig_top_movies côte à côte ---
col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(fig_genre, use_container_width=True)
    # --- Deuxième rangée : fig_users sur toute la largeur ---
    st.plotly_chart(fig_users, use_container_width=True)

with col2:
    st.plotly_chart(fig_top_movies, use_container_width=True)



# --- Séparateur ---
st.divider()

# --- Troisième rangée : évolution par année ---
st.plotly_chart(fig_by_year, use_container_width=True)



