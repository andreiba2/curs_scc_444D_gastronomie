pipeline {
    agent any

    stages {

        stage('Install dependencies') {
            steps {
                echo 'Installing dependencies...'

                sh '''
                    pip3 install --break-system-packages -r requirements.txt
                '''
            }
        }

        stage('Run tests_app') {
            steps {
                echo 'Running tests_app...'

                sh '''
                    python3 -m app.tests.tests_app
                '''
            }
        }

        stage('Run tests_libs') {
            steps {
                echo 'Running tests_libs...'

                sh '''
                    python3 -m app.tests.tests_libs
                '''
            }
        }

        stage('Docker build') {
            steps {
                echo 'Building Docker image...'

                sh '''
                    docker build -t tortilla-app .
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deployment finished!'
            }
        }
    }
}
