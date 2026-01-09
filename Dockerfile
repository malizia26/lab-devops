FROM python:3.11-slim

# On installe les versions déjà compilées (plus rapide et plus stable)
RUN apt-get update && apt-get install -y \
    python3-flask \
    python3-psutil \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY app.py .

EXPOSE 5000

# On lance avec python3 pour être sûr d'utiliser les libs système
CMD ["python3", "app.py"]
