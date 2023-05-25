pipeline {
    agent any
    tools {
        go 'go-1.20.4'
    }
    stages {
        stage('Build') {
            steps {
                sh 'go build main.go'
                archiveArtifacts artifacts: 'main', fingerprint: true
            }
        }
        stage('Tests') {
            steps {
                sh 'rm -f go.mod'
                sh 'go mod init app'
                sh 'go test .'
            }
        }
        stage('Test connection') {
            withCredentials([sshUserPrivateKey(credentialsId: 'target-ssh-key', keyFileVariable: 'keyFile', userNameVariable: 'userName']) {
                steps {
                    sh 'scp -i ${keyFile} main 192.168.105.3:'
                }
            }
        }
    }
}

