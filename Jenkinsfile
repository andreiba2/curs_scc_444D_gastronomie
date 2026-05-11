pipeline {
    agent any

    environment {
        PYTHONPATH = "${env.WORKSPACE}"
    }

    stages {
        stage('Instalare Dependente') {
            steps {
                echo 'Instalam pytest si Flask pentru rularea testelor...'
                sh 'python3 -m pip install -r requirements.txt --break-system-packages'
            }
        }
        stage('Verificare fisiere') {
            steps {
                echo 'Afisam toate fisierele descarcate de Jenkins pentru a fi siguri ca folderul app este aici:'
                sh 'ls -R'
            }
        }
        stage('Testare Unitara (Pytest)') {
            steps {
                echo 'Rulam testele unitare cu Pytest...'
                sh 'python3 -m pytest test_gastronomie.py -v'
            }
        }
    }
}

