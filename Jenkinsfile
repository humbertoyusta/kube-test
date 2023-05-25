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
            steps {
                sh 'ssh-keyscan 192.168.105.3 > ~/.ssh/known_hosts'
                sh 'scp -i ~/.ssh/id_rsa hello.txt vagrant@192.168.105.3'
            }
        }
    }
}
