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
                sh 'pylint --break-system-packages gastronomie.py'
            }
        }

        stage('Teste') {
            steps {
                // Rulează testele unitare
                sh 'pytest --break-system-packages tests/'
            }
        }
    }

    post {
        success {
            echo ' Proiectul a trecut testele cu succes.'
        }
    }
}
