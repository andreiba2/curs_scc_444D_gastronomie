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
                    docker run -d --name clatite-container -p 5000:5000 clatite-app
                    sleep 5
                    docker logs clatite-container
                '''
            }
        }

        stage('Cleanup') {
            steps {
                sh '''
                    docker stop clatite-container || true
                    docker rm clatite-container || true
                '''
            }
        }
    }
}
