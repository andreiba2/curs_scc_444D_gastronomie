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
                echo 'Rulam testele unitare...'
                sh 'python3 -m unittest test_gastronomie -v'
            }
        }
    }
}

