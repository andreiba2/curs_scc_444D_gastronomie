# curs_scc_444D_gastronomie

Minimal Flask site about baklava, built for Docker and Jenkins.

## Run locally

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements-dev.txt
pytest
flask --app app run
```

## Run with Docker

```bash
docker compose up --build
```

Open `http://localhost:8000` after the container starts.

## Jenkins

The `Jenkinsfile` runs the test suite and then builds the Docker image.