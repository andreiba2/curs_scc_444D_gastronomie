pipeline {
    agent any
    stages {
        stage('Instalare Dependențe') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }
        stage('Testare aplicație') {
            steps {
                sh '''
                    . venv/bin/activate
                    python3 test_gastronomie.py
                '''
            }
        }
    }

    post {
        success {
            echo 'Success ✅'
        }
        failure {
            echo 'Error ❌'
        }
    }
}