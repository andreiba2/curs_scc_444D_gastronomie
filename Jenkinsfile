pipeline {
    agent any
    stages {
        stage('Install') {
            steps {
                // Adăugăm flag-ul pentru a permite instalarea în mediul gestionat extern
                sh 'python3 -m pip install --break-system-packages -r requirements.txt'
            }
        }
        stage('Unit Tests') {
            steps {
                // Rulăm testele unitare conform cerințelor [cite: 61, 163]
                sh 'python3 -m pytest test_gastronomie.py'
            }
        }
    }
}

