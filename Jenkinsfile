pipeline {
    agent any
    
    stages {
        stage('Initializare') {
            steps {
                echo 'Bucataria se pregateste pentru Magda...'
                // Verificam daca avem toate fisierele necesare
                sh 'ls -la' 
            }
        }

        stage('Testare Automata') {
            steps {
                // Instalam Flask si restul bibliotecilor in mediul Jenkins
                sh 'python3 -m pip install -r requirements.txt'
                // Rulam testele tale care acum dau OK
                sh 'python3 test_gastronomie.py'
                echo 'Testele au trecut (PASS)!'
            }
        }

        stage('Construire Imagine Docker') {
            steps {
                // Construim imaginea folosind Dockerfile-ul tau
                sh 'docker build -t carbonara-app:latest .'
                echo 'Imaginea Docker a fost creata cu succes!'
            }
        }
    }
}
