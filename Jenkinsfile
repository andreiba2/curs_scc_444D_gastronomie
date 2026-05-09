pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install flask pytest'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest tests/test_mici.py -v'
            }
        }
    }

    post {
        success {
            echo 'Teste PASS!'
        }
        failure {
            echo 'Teste FAIL!'
        }
    }
}
