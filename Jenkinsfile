pipeline {
    agent any

    stages {
        stage('Clean virtual environment') {
            steps {
                sh 'rm -rf .venv'
            }
        }

        stage('Create virtual environment') {
            steps {
                sh 'python3 -m venv .venv'
            }
        }

        stage('Install dependencies') {
            steps {
                sh '.venv/bin/python -m pip install --upgrade pip'
                sh '.venv/bin/python -m pip install -r requirements.txt'
            }
        }

        stage('Run tests') {
            steps {
                sh '.venv/bin/python -m pytest app/tests -q'
            }
        }
    }
}
