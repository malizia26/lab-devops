FROM python:3.11-slim
WORKDIR /app
# On installe les librairies avant de copier le code pour gagner du temps au build
RUN pip install --no-cache-dir flask psutil
COPY app.py .
EXPOSE 5000
CMD ["python", "app.py"]
