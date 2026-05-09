pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python3 pytest test_gulas.py'
            }
        }
    }

    post {
        success {
            echo 'PASS'
        }
        failure {
            echo 'FAIL'
        }
    }
}
