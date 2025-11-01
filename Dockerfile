# Image Python légère
FROM python:3.11-slim

# Réglages de base
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Dépendances système minimales (pour scikit-learn/numpy/scipy wheels)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Installer les dépendances Python nécessaires
RUN pip install --no-cache-dir streamlit scikit-learn joblib

# Copier le code + artefacts + image
COPY app.py .
COPY model.joblib vectorizer.joblib ./
COPY output.png ./

# Port Streamlit
EXPOSE 8501

# Lancer l'app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
