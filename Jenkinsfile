pipeline {
    agent any

    environment {
        
        PYTHONPATH = "${env.WORKSPACE}"
    }

    stages {
        stage('Verificare fisiere') {
            steps {
                echo 'Afisam toate fisierele descarcate de Jenkins pentru a fi siguri ca folderul app este aici:'
                sh 'ls -R'
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
