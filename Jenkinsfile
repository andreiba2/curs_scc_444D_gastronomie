pipeline {
    agent any
    
    stages {
        stage('Initializare') {
            steps {
                echo 'Bucataria se pregateste pentru Magda...'
                sh 'ls -la' 
            }
        }

        stage('Testare Automata') {
            steps {
                // Am adaugat flag-ul pentru a trece de eroarea de sistem
                sh 'python3 -m pip install -r requirements.txt --break-system-packages'
                
                // Rulam testele tale care verifica rutele de Carbonara
                sh 'python3 test_gastronomie.py'
                echo 'Testele au trecut cu succes (PASS)!'
            }
        }

        stage('Construire Imagine Docker') {
            steps {
                // Construim imaginea folosind Dockerfile-ul din folder
                sh 'docker build -t carbonara-app:latest .'
                echo 'Imaginea Docker a fost creata cu succes!'
            }
        }
    }
}
