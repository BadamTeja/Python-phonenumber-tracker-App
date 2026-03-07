pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                checkout scmGit(branches: [[name: '*/master']], 
                extensions: [], 
                userRemoteConfigs: [[credentialsId: 'Git-Creds', url: 'https://github.com/BadamTeja/Python-phonenumber-tracker-App.git']])
            }
        }

        stage('Run Application Test') {
            steps {
                sh 'python3 app.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t badamteja/python-tracker-app:latest .'
            }
        }

        stage('Docker Login') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-creds', usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                    sh 'echo $PASS | docker login -u $USER --password-stdin'
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                sh 'docker push badamteja/python-tracker-app:latest'
            }
        }

    }
}
