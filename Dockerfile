# Używamy obrazu bazowego z Pythonem 3.12
FROM python:3.12-slim

# Ustawiamy katalog roboczy
WORKDIR /app

# Kopiujemy plik requirements.txt do kontenera
COPY requirements.txt .

# Instalujemy zależności z requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Kopiujemy cały kod aplikacji do kontenera
COPY . /app

# Ustawiamy zmienną środowiskową dla FastAPI (jeśli Twoja aplikacja jest w 'bookRent.main')
ENV UVICORN_CMD="uvicorn main:app --host 0.0.0.0 --port 8000 --reload"

# Ekspozycja portu 8000
EXPOSE 8000

# Uruchamiamy aplikację FastAPI
CMD ["sh", "-c", "$UVICORN_CMD"]
