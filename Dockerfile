FROM python:3.9-slim
# Creare user non-root
RUN useradd -m appuser
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
# Setare permisiuni si comutare pe noul user
RUN chown -R appuser:appuser /app
USER appuser
EXPOSE 5000
CMD ["python", "gastronomie.py"]