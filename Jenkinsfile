pipeline {
    agent any
    environment {
        PYTHONPATH = "."
    }
    stages {
        stage('Install') {
            steps {
                sh 'python3 -m pip install --break-system-packages -r requirements.txt'
            }
        }
        stage('Unit Tests') {
            steps {
                sh 'python3 -m pytest test_gastronomie.py'
            }
        }
    }
}
