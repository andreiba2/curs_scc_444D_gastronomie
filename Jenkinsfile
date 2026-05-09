pipeline {
    agent any

    stages {
        stage('Pregatire') {
            steps {
                echo 'Incepem procesul de testare pentru aplicatia Gastronomie - Ciorba de burta...'
            }
        }
        stage('Testare Unitara') {
            steps {
                echo 'Rulam testele unitare cu Python...'
                sh 'python3 test_gastronomie.py'
            }
        }
    }
}
