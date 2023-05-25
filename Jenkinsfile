pipeline {
    agent any
    tools {
        go 'go-1.20.4'
    }
    stages {
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
