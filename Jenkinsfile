pipeline {
    agent any
    stages {
        stage('Testare Piftie') {
    steps {
        sh """
            export PYTHONPATH=${WORKSPACE}
            echo "--- Structura de fisiere ---"
            ls -R
            echo "--- Path-ul Python ---"
            python3 -c 'import sys; print(sys.path)'
            echo "--- Rulare Teste ---"
            python3 -m pytest test_piftie.py
        """
   	 }
        }
    }
}
