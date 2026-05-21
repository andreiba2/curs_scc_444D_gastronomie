pipeline {

    agent any

    stages {

        stage('Build Docker Image') {

            steps {

                sh 'docker build -t tajin-app .'

            }
        }

        stage('Stop Old Container') {

            steps {

                sh '''
                    docker stop tajin-container || true
                    docker rm tajin-container || true
                '''

            }
        }

        stage('Run Docker Container') {

            steps {

                sh '''
                    docker run -d \
                    --name tajin-container \
                    -p 5000:5000 \
                    tajin-app
                '''

            }
        }
    }
}
