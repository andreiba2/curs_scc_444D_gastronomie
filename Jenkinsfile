pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building tortilla app...'
                sh 'python3 -m venv .venv'
                sh '''
                    . .venv/bin/activate
                    python -m pip install --upgrade pip
                    python -m pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                echo 'Testing tortilla app...'
                sh '''
                    . .venv/bin/activate
                    python -m app.tests.tests_app
                    python -m app.tests.tests_libs
                '''
            }
        }

        stage('Docker Build') {
            steps {
                echo 'Building Docker image...'
                sh 'docker build -t tortilla-app .'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying....'
                echo 'Aplicatia poate fi rulata cu: docker run -p 5050:5050 tortilla-app'
            }
        }
    }
}
