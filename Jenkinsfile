pipeline {
    agent any
    stages {
        stage('Testare Automata') {
            steps {
                sh 'pip install -r requirements.txt'
                sh 'pytest test_gastronomie.py'
            }
        }
        stage('Construire Container Docker') {
            steps {
                sh 'docker build -t lasagna-app:latest .'
            }
        }
    }
}
