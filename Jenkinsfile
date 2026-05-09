pipeline {

    agent any
    
    environment {
        
        PYTHONPATH = "${env.WORKSPACE}"
    }

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
                    # Create a virtual environment
                    python3 -m venv .venv

                    # Activate it
                    source .venv/bin/activate

                    # Upgrade pip
                    pip install --upgrade pip

                    # Install dependencies
                    pip install -r requirements.txt
                '''
                echo'Dependente descarcate cu succes!'
            }
        }

        stage('Run Tests') {
            steps {
            	echo 'Rulare teste...'
                sh 'python3 pytest test_gulas.py'
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
