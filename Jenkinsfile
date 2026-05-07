pipeline {
    agent {
        docker { image 'python:3.9-slim' }
    }
    stages {
        stage('Install') {
            steps {
                // În interiorul imaginii de python, pip este deja instalat
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Unit Tests') {
            steps {
                sh 'pytest test_gastronomie.py'
            }
        }
    }
}
