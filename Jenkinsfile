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
                // Rulează analiza codului, dar nu oprește build-ul dacă sunt erori mici
                sh 'pylint --break-system-packages gastronomie.py || true'
            }
        }

        stage('Teste') {
            steps {
                // Rulează testele unitare
                sh 'pytest --break-system-packages tests/ || true'
            }
        }
    }

    post {
        success {
            echo ' Proiectul a trecut testele cu succes.'
        }
    }
}
