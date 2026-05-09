pipeline {
	agent any
	
	stages {
		stage("Environment Setup") {
			steps {
				echo "Creating virtual environment and installing dependencies"
				sh """
					python3 -m venv venv
					. venv/bin/activate
					pip install --upgrade pip
					pip install -r requirements.txt
				"""
			}
		}
		
		stage("Run Unit Tests") {
			steps {
				echo "Running tests using pytest"
				sh """
					. venv/bin/activate
					PYTHONPATH=. pytest --maxfail=1 --disable-warnings -q
				"""
			}
		}
	}
	
	post {
		success {
			echo "All tests passed! :D"
		}
		failure {
			echo "Tests failed! :("
		}
	}
}
