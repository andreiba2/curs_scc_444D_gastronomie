pipeline {
	agent any
	stages {
	   stage('Checkout') {
	       steps {
		   checkout scm
	       }
	   }
	   stage('Instalare Dependente') {
	       steps {
		   sh 'pip install -r requirements.txt'
	       }
	   }
          stage('Testare') {
	      steps {
		 sh 'ls -l && export PYTHONPATH=$PWD && python3 -m pytest test_gastronomie.py'
	      }
          }
    }
}   
    

