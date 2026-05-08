pipeline {
    agent any
    stages {
        stage('Testare Piftie') {
            steps {
                sh "export PYTHONPATH=${WORKSPACE} && python3 -m pytest test_piftie.py"
            }
        }
    }
}
