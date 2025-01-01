# Utilisez une image Python officielle
FROM python:3.11-slim

# Définir le répertoire de travail
WORKDIR /app

COPY . /app
# Copier les fichiers requis
COPY requirements.txt requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt
RUN pip install -r requirements.txt
# Installer Gunicorn pour exécuter Flask en production
RUN pip install gunicorn


COPY . .



# Exposez le port 5000
EXPOSE 5000


# Commande pour exécuter l'application Flask avec Gunicorn
CMD ["gunicorn", "-w", "1", "-b", "0.0.0.0:5000", "app:app"]
