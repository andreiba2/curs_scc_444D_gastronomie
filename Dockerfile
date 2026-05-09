FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5050

CMD ["python3", "-m", "app.tortilla_de_patatas"]
