pipeline {
    agent any

    environment {
        PYTHONPATH = "${env.WORKSPACE}"
    }

    stages {
        stage('Verificare fisiere') {
            steps {
                echo 'Afisam structura proiectului:'
                sh 'ls -R'
            }
        }

        stage('Instalare dependinte') {
            steps {
                echo 'Instalam dependintele Python:'
                sh 'pip install --break-system-packages -r requirements.txt'
            }
        }

        stage('Testare Unitara') {
            steps {
                echo 'Rulam testele unitare:'
                sh 'python3 test_gastronomie.py'
            }
        }
    }

    post {
        success {
            echo 'Toate testele au trecut cu succes!'
        }
        failure {
            echo 'Au existat erori la rularea testelor.'
        }
    }
}
