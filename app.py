import streamlit as st
import joblib
import os

# --- Titre / mise en page ---
st.set_page_config(page_title="Analyse de Sentiments", page_icon="🧠", layout="centered")
st.title("🧠 Analyse de Sentiments (simple)")
st.caption("Entrez un tweet ci-dessous pour savoir s'il est positif ou négatif.")

# --- Wordcloud (output.png) en haut de page ---
if os.path.exists("output.png"):
    st.image("output.png", caption="Wordcloud global", use_container_width=True)
else:
    st.info("Place le fichier 'output.png' à la racine du projet pour afficher le wordcloud.")

# --- Charger le modèle et le vectorizer (mise en cache pour la perf) ---
@st.cache_resource
def load_artifacts():
    model = joblib.load("model.joblib")
    vectorizer = joblib.load("vectorizer.joblib")
    return model, vectorizer

model, vectorizer = load_artifacts()

# --- Zone de saisie + prédiction ---
tweet = st.text_area("📝 Tweet :", "", height=120)

if st.button("Analyser"):
    if tweet.strip() == "":
        st.warning("⚠️ Écris un tweet d'abord.")
    else:
        vect = vectorizer.transform([tweet])
        prediction = model.predict(vect)[0]
        proba = model.predict_proba(vect)[0]

        sentiment = "😊 Positif" if prediction == 1 else "😞 Négatif"
        st.subheader(f"Résultat : {sentiment}")
        st.write(f"Probabilité négatif : {proba[0]:.2f} | positif : {proba[1]:.2f}")
