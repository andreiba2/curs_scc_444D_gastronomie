pipeline {
    agent any
    stages {
        stage('Instalare Dependențe') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Execuție Teste') {
            steps {
                sh 'pytest tests/'
            }
        }
    }
}