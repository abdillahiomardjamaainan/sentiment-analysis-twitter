🧠 Projet — Analyse de sentiments des tweets

Ce projet consiste à analyser les sentiments exprimés dans des tweets en utilisant un modèle de régression logistique entraîné sur un jeu de données de tweets en anglais.
L’objectif est de déterminer automatiquement si un message est positif 😊 ou négatif 😞.

Une application Streamlit permet de tester facilement le modèle :
l’utilisateur entre un tweet et obtient instantanément le résultat de l’analyse.
Un wordcloud est également affiché pour visualiser les mots les plus fréquents du corpus.

🚀 Technologies utilisées

Python 3.11

Scikit-learn (TF-IDF + régression logistique)

NLTK (nettoyage et lemmatisation)

Streamlit (interface web interactive)

GitHub Actions (CI/CD)

Streamlit Cloud (déploiement automatique)

🌐 Déploiement

L’application est hébergée sur Streamlit Cloud et accessible ici :
👉 Lien de déploiement Streamlit

💡 Objectif

Ce projet montre comment :

Prétraiter des données textuelles (tokenisation, stopwords, lemmatisation)

Représenter le texte avec TF-IDF

Entraîner un modèle de machine learning simple mais efficace

Créer une interface interactive pour rendre l’analyse accessible à tous

Mettre en place une intégration et un déploiement continu (CI/CD).

✨ Exemple d’utilisation

📝 I love this movie so much!
→ Résultat : Positif 😊

📝 This day was terrible, nothing worked!
→ Résultat : Négatif 😞
