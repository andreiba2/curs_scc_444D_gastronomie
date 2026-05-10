# Folosim o imagine oficială și ușoară de Python
FROM python:3.13-slim

# Setăm directorul de lucru în interiorul containerului
WORKDIR /app

# Copiem fișierul cu dependențe și instalăm Flask
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiem tot codul aplicației în container
COPY . .

# Setăm o variabilă de mediu pentru a ajuta Python să găsească modulele
ENV PYTHONPATH=/app

# Expunem portul pe care rulează Flask (5000)
EXPOSE 5000

# Comanda pentru a porni aplicația când containerul rulează
CMD ["python", "gastronomie.py"]
