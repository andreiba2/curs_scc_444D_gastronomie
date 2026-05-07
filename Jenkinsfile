pipeline {
    agent any
    stages {
        stage('Install') {
            steps {
                sh 'python3 -m pip install --break-system-packages -r requirements.txt'
            }
        }
        stage('Unit Tests') {
            steps {
                // Setăm PYTHONPATH chiar înainte de a rula testele
                sh 'export PYTHONPATH=$PYTHONPATH:. && python3 -m pytest test_gastronomie.py'
            }
        }
    }
}

