pipeline {
    agent any
    stages {
        stage('Install') {
            steps {
                sh 'python -m pip install -r requirements.txt || python3 -m pip install -r requirements.txt || pip install -r requirements.txt || pip3 install -r requirements.txt'
            }
        }
        stage('Unit Tests') {
            steps {
                sh 'python -m pytest test_gastronomie.py || python3 -m pytest test_gastronomie.py || pytest test_gastronomie.py'
            }
           
        }
    }
}
