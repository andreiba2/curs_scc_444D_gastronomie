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
        stage('Execuție Teste') {
            steps {
                sh '''
                . venv/bin/activate
                python3 -m pytest tests/
                '''
            }
        }
    }
}