pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip3 install flask pytest pylint'
            }
        }

        stage('Lint') {
            steps {
                sh 'pylint gastronomie.py app/lib/biblioteca_gastronomie.py app/tests/test_cordon_bleu.py || true'
            }
        }

        stage('Test') {
            steps {
                sh 'python3 -m pytest app/tests/test_cordon_bleu.py -v'
            }
        }
    }

    post {
        success {
            echo 'Toate testele au trecut! ✅'
        }
        failure {
            echo 'Testele au esuat! ❌'
        }
    }
}
