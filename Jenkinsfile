pipeline {
    agent any
    stages {
        stage('Checkout') { steps { checkout scm } }
        stage('Instalare Dependente') { steps { sh 'pip install -r requirements.txt' } }
        stage('Verificare Cod') { steps { sh 'pylint gastronomie.py' } }
        stage('Teste') { steps { sh 'pytest tests/' } }
    }
}
