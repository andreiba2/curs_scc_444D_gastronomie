pipeline {

    agent any

    stages {
    	stage('Verificare') {
            steps {
                echo 'Fisierele descarcate:'
                sh 'ls -R'
            }
        }
        
        stage('Instalare dependinte') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install -r requirements.txt
                '''
                echo'Dependente descarcate cu succes!'
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                . venv/bin/activate
                python3 -m pytest tests/
                '''
            }
        }
    }

    post {
        success {
            echo 'PASS'
        }
        failure {
            echo 'FAIL'
        }
    }
}
