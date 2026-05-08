pipeline {
    agent any
    stages {
        stage('Testare Piftie') {
            steps {
                sh 'PYTHONPATH=. pytest test_piftie.py'
            }
        }
    }
}
