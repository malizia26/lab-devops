FROM python:3.11-slim

WORKDIR /app

# On installe juste les librairies, sans compiler (en utilisant les wheels pré-build)
RUN pip install --no-cache-dir flask psutil

COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]
