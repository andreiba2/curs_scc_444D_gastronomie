pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Instalare Dependente') {
            steps {
                sh 'pip install --break-system-packages -r requirements.txt'
            }
        }

        stage('Verificare Cod') {
            steps {
                // Verifica functionalitatea intregii aplicatii
                sh 'python3 -m pylint gastronomie.py'
            }
        }

        stage('Teste') {
            steps {
                // Rulează testele unitare
                sh 'python3 -m pytest tests/'
            }
        }
    }

    post {
        success {
            echo ' Proiectul a trecut testele cu succes.'
        }
    }
}
