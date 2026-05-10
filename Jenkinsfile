pipeline {
    agent any

    environment {
        // Fortam Python sa caute modulele in folderul principal de lucru al Jenkins
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
                sh 'PYTHONPATH=. python3 -m unittest test_gastronomie.py'
            }
        }
    }
}
