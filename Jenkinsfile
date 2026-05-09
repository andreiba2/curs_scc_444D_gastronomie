pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    export PYTHONPATH=$PYTHONPATH:$(pwd)
                    pytest -v
                '''
            }
        }

        stage('Build Docker image') {
            steps {
                sh '''
                    docker build -t clatite-app .
                '''
            }
        }

        stage('Run Docker container') {
            steps {
                sh '''
<<<<<<< HEAD
                    docker run -d --name clatite_americane-$BUILD_NUMBER -p 5000:5000 clatite-app
=======
                    docker run -d --name clatite_americane-$BUILD_NUMBER -p 5000:5000 clatite-app
>>>>>>> 7973eaee9fd9fa5ccd3faa915a13b173d27697bf
                    sleep 5
                    docker logs clatite_americane-$BUILD_NUMBER
                '''
            }
        }

        stage('Cleanup') {
            steps {
                sh '''
                    docker rm -f clatite_americane-$BUILD_NUMBER || true
                '''
            }
        }
    }
}
