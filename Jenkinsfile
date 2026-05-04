pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh '''
                    docker run --rm \
                        -v "$WORKSPACE:/app" \
                        -w /app \
                        python:3.12-slim \
                        sh -lc 'python -m venv .venv && . .venv/bin/activate && pip install --upgrade pip && pip install -r requirements-dev.txt'
                '''
            }
        }

        stage('Unit Testing cu Pytest') {
            steps {
                sh '''
                    docker run --rm \
                        -v "$WORKSPACE:/app" \
                        -w /app \
                        python:3.12-slim \
                        sh -lc '. .venv/bin/activate && pytest tests/'
                '''
            }
        }

        stage('Docker Build și Deploy') {
            steps {
                sh '''
                    docker build -t baklava-flask-app:${BUILD_NUMBER} .
                    docker rm -f baklava_flask_${BUILD_NUMBER} || true
                    docker run -d --name baklava_flask_${BUILD_NUMBER} -p 8000:8000 baklava-flask-app:${BUILD_NUMBER}
                '''
            }
        }
    }
}