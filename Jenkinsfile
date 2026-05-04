pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh '''
                    python3 -m venv .venv
                    . .venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements-dev.txt
                '''
            }
        }

        stage('Unit Testing cu Pytest') {
            steps {
                sh '''
                    . .venv/bin/activate
                    PYTHONPATH=. pytest tests/
                '''
            }
        }

        stage('Docker Build și Deploy') {
            steps {
                sh '''
                    docker build -t baklava-flask-app:${BUILD_NUMBER} .
                    docker stop baklava_flask_app || true
                    docker rm -f baklava_flask_app || true
                    docker run -d --name baklava_flask_app -p 8000:8000 baklava-flask-app:${BUILD_NUMBER}
                '''
            }
        }
    }
}