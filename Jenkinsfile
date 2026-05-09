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
		  sh 'python -m pytest test_gastronomie.py'
	      }
          }
    }
}   
    

