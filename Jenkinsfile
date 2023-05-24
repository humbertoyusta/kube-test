pipeline {
    agent any
    tools {
        go 'go-1.20.4'
    }
    environment {
        GITHUB_TOKEN = credentials('github-token')
    }
    stages {
        stage('Checkout Repository') {
            steps {
                withCredentials([string(credentialsId: 'github-token', variable: 'GITHUB_TOKEN')]) {
                    sh('rm -rf go-test && git clone https://${GITHUB_TOKEN}@github.com/humbertoyusta/go-test.git')
                }
            }
        }
        stage('Build') {
            steps {
                dir("go-test") {
                    sh 'go build main.go'
                    archiveArtifacts artifacts: 'main', fingerprint: true
                }
            }
        }
        stage('Tests') {
            steps {
                dir("go-test") {
                    sh 'go mod init app'
                    sh 'go test .'
                }
            }
        }
    }
}
