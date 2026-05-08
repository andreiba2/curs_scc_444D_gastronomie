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
        stage('Rulare aplicație') {
            steps {
                sh '''
                . venv/bin/activate
                python3 app.py
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