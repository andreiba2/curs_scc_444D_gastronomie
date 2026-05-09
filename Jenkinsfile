pipeline {
    agent any
    stages {
        stage('Testare Salata Boeuf') {
            steps {
                sh "export PYTHONPATH=${WORKSPACE} && python3 -m pytest test_salata_boeuf.py"
            }
        }
    }
}
