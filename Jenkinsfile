pipeline {
    agent any
    stages {
        stage('Testare Automata') {
            steps {
                sh 'python3 -m pip install -r requirements.txt'
                sh 'export PYTHONPATH=$PYTHONPATH:. && python3 -m pytest test_gastronomie.py'
            }
        }
        stage('Construire Container Docker') {
            steps {
                sh 'docker build -t lasagna-app:latest .'
            }
        }
    }
}
