pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code from GitHub...'
                checkout scm
            }
        }
        
        stage('Hello World') {
            steps {
                echo 'Hello from Jenkins pipeline!'
            }
        }
    }
}
