pipeline {
    agent any

    stages {
        stage('Create virtual environment') {
            steps {
                sh 'python3 -m venv .venv'
            }
        }

        stage('Install dependencies') {
            steps {
                sh '''
                    . .venv/bin/activate
                    python -m pip install --upgrade pip
                    python -m pip install -r requirements.txt
                '''
            }
        }

        stage('Run tests') {
            steps {
                sh '''
                    . .venv/bin/activate
                    python -m app.tests.tests_app
                    python -m app.tests.tests_libs
                '''
            }
        }

        stage('Docker build') {
            steps {
                sh 'docker build -t tortilla-app .'
            }
        }
    }
}
