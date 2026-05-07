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
                    
                    # Stop and remove all existing baklava containers
                    docker ps -a -q -f "ancestor=baklava-flask-app" | xargs -r docker stop 2>/dev/null || true
                    docker ps -a -q -f "ancestor=baklava-flask-app" | xargs -r docker rm -f 2>/dev/null || true
                    
                    # Kill any other containers using port 8000
                    docker ps -q --filter "publish=8000" | xargs -r docker stop 2>/dev/null || true
                    docker ps -a -q --filter "publish=8000" | xargs -r docker rm -f 2>/dev/null || true
                    
                    # Start the new container
                    docker run -d --name baklava_flask_app -p 8000:8000 baklava-flask-app:${BUILD_NUMBER}
                '''
            }
        }
    }
}