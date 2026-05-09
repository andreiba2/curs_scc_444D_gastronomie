pipeline {
    agent any

    stages {
        stage('Install dependencies') {
            steps {
                sh 'pip3 install --break-system-packages -r requirements.txt'
            }
        }

        stage('Run tests_app') {
            steps {
                sh 'PYTHONPATH=. python3 -m app.tests.tests_app'
            }
        }

        stage('Run tests_libs') {
            steps {
                sh 'PYTHONPATH=. python3 -m app.tests.tests_libs'
            }
        }

        stage('Docker build') {
            steps {
                sh 'docker build -t tortilla-app .'
            }
        }
    }
}
