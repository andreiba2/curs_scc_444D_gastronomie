pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install flask pytest
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    PYTHONPATH=$(pwd) python3 -m pytest tests/ -v
                '''
            }
        }
    }

    post {
        success {
            echo 'Teste PASS!'
        }
        failure {
            echo 'Teste FAIL!'
        }
    }
}
