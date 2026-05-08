pipeline {
    agent any

    stages {
        stage('Install Python') {
            steps {
                sh 'apt-get update && apt-get install -y python3 python3-pip'
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh '''
                    python3 -m venv venv
                    .source venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run application') {
            steps {
                sh 'PYTHONPATH=$(pwd) python3 -m pytest app/tests/test_cordon_bleu.py -v'
            }
        }
    }

    post {
        success {
            echo 'Success ✅'
        }
        failure {
            echo 'Error ❌'
        }
    }
}