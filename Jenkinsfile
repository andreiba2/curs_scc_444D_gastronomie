pipeline {
    agent any

    stages {
        stage('Install dependencies') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run tests_app') {
            steps {
                sh 'venv/bin/python -m app.tests.tests_app'
            }
        }

        stage('Run tests_libs') {
            steps {
                sh 'venv/bin/python -m app.tests.tests_libs'
            }
        }

        stage('Docker build') {
            steps {
                sh 'docker build -t tortilla-app .'
            }
        }
    }
}
