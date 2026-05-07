pipeline {
    agent any
    stages {
        stage('Install') {
            steps {
                sh 'python3 -m pip install -r requirements.txt'
            }
        }
        stage('Unit Tests') {
            steps {
                sh 'python3 -m pytest test_gastronomie.py'
            }
        }
    }
}

