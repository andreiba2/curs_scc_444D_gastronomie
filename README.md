# Baklava Flask Application

**Author:** Olteanu Rares - Cristian

A minimal Turkish dessert (baklava) information website built with Flask, designed to run locally, in Docker, or through Jenkins CI/CD.

## Project Structure

```
.
├── app/                    # Flask application code
│   ├── __init__.py        # Flask app factory and routes
│   ├── static/            # CSS stylesheets
│   │   └── style.css
│   └── templates/         # HTML templates
│       ├── index.html
│       └── detail.html
├── tests/                 # Test suite
│   └── test_app.py
├── requirements.txt       # Production dependencies
├── requirements-dev.txt   # Development + test dependencies
├── Dockerfile             # Docker image definition (non-root user)
├── dockerstart.sh         # Docker entrypoint script
├── docker-compose.yml     # Docker Compose configuration
├── Jenkinsfile            # Jenkins CI/CD pipeline
├── pytest.ini             # Pytest configuration
└── jenkins/               # Jenkins Docker image & config
    ├── Dockerfile         # Custom Jenkins image with Python 3
    ├── plugins.txt        # Jenkins plugins list
    └── scripts/run-jenkins.sh  # Jenkins launcher script
```

## Quick Start

### Option 1: Local Development (Native)

```bash
# Create virtual environment
python3 -m venv .venv
. .venv/bin/activate

# Install dependencies
pip install -r requirements-dev.txt

# Run tests
PYTHONPATH=. pytest tests/

# Start development server
FLASK_ENV=development FLASK_APP=app python -m flask run --port 5000
```

Open `http://localhost:5000` in your browser.

### Option 2: Docker (Recommended for Production)

#### Using Docker Compose:

```bash
docker compose up --build
```

Open `http://localhost:8000` in your browser.

#### Manual Docker Commands:

```bash
# Build image
docker build -t baklava-flask-app:latest .

# Run container
docker run -d --name baklava_flask -p 8000:8000 baklava-flask-app:latest

# View logs
docker logs -f baklava_flask

# Stop container
docker stop baklava_flask
docker rm baklava_flask
```

**Note:** The Docker image runs the application as a non-root `baklava` user for security. The app binds to `0.0.0.0:8000` using Gunicorn.

### Option 3: Jenkins CI/CD

#### Setup Jenkins (First Time Only)

```bash
bash scripts/run-jenkins.sh
```

This will:
- Build a custom Jenkins image with Docker CLI and Python 3 support
- Start a Jenkins controller on `http://localhost:8080`
- Create a persistent home volume

Get the initial admin password:
```bash
sudo docker exec curs-scc-jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```

#### Configure Pipeline Job

1. Open `http://localhost:8080`
2. Log in with the admin password from above
3. Create a **New Item** → Select **Pipeline** → Name it (e.g., `baklava-pipeline`)
4. Under **Pipeline**, select **Pipeline script from SCM**
5. Configure Git:
   - **Repository URL:** `https://github.com/andreiba2/curs_scc_444D_gastronomie.git` (or your local path)
   - **Branch:** `*/dev_Olteanu_Rares`
   - **Script Path:** `Jenkinsfile`
6. Click **Save**

#### Run Pipeline

Click **Build Now** in the job page. The pipeline will:
- Install dependencies in a virtual environment
- Run pytest with `PYTHONPATH=.`
- Build a Docker image (`baklava-flask-app:<BUILD_NUMBER>`)
- Deploy the container on port 8000

Monitor progress in the **Console Output**.

## Development

### Run Tests Locally

```bash
. .venv/bin/activate
PYTHONPATH=. pytest tests/ -v
```

### Add Dependencies

```bash
. .venv/bin/activate
pip install <package-name>
pip freeze > requirements.txt  # Update requirements
```

### Docker Image Details

- **Base Image:** `python:3.13-slim`
- **App User:** `baklava` (non-root for security)
- **Working Directory:** `/home/baklava`
- **Virtual Environment:** `.venv` inside the app directory
- **Port:** `8000`
- **Process Manager:** Gunicorn

## Troubleshooting

### Tests fail with `ModuleNotFoundError: No module named 'app'`

Ensure `PYTHONPATH=.` is set before running pytest:

```bash
PYTHONPATH=. pytest tests/
```

### Docker permission denied on `/var/run/docker.sock`

The Jenkins container needs the host Docker socket mounted and the host's `docker` group GID added. This is handled automatically by `scripts/run-jenkins.sh`.

### Port 8000 already in use

Change the port mapping in `docker-compose.yml` or the `docker run` command:

```bash
docker run -d -p 9000:8000 baklava-flask-app:latest
```

Then access `http://localhost:9000`.

## Deployment

For production, consider:
- Running behind a reverse proxy (Nginx)
- Using environment variables for configuration
- Implementing proper logging and monitoring
- Setting up database persistence if needed
- Using a container orchestration platform (Kubernetes, Docker Swarm)

## License

See [LICENSE](LICENSE) file.
