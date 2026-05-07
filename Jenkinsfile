pipeline {
    agent any

    stages {
        stage('Pregatire') {
            steps {
                echo 'Incepem procesul de testare pentru aplicatia Gastronomie - Ramen...'
            }
        }
        stage('Testare Unitara') {
            steps {
                echo 'Rulam testele unitare cu Python...'
                sh 'PYTHONPATH=. python3 -m unittest test_gastronomie.py'
            }
        }
    }
}
