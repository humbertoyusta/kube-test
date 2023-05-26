pipeline {
    agent any
    tools {
        go 'go-1.20.4'
    }
    stages {
        stage('Tests') {
            steps {
                sh 'rm -f go.mod'
                sh 'go mod init app'
                sh 'go test .'
            }
        }
        stage('Build') {
            steps {
                sh 'go build main.go'
                archiveArtifacts artifacts: 'main', fingerprint: true
            }
        }
        stage('Deploy') {
            steps {
                withCredentials([sshUserPrivateKey(credentialsId: 'target-key', keyFileVariable: 'keyFile', usernameVariable: 'userName')]) {
                    sh 'mkdir -p $HOME/.ssh'
                    sh 'ssh-keyscan 192.168.105.3 > $HOME/.ssh/known_hosts'
                    
                    sh 'ssh ${userName}@192.168.105.3 -i ${keyFile} -C sudo systemctl stop goapp.service'
                    
                    sh 'scp -i ${keyFile} main ${userName}@192.168.105.3:'
                    sh 'scp -i ${keyFile} goapp.service ${userName}@192.168.105.3:'
                    
                    sh 'ssh ${userName}@192.168.105.3 -i ${keyFile} -C sudo cp goapp.service /etc/systemd/system/'
                    sh 'ssh ${userName}@192.168.105.3 -i ${keyFile} -C sudo systemctl daemon-reload'
                    sh 'ssh ${userName}@192.168.105.3 -i ${keyFile} -C sudo systemctl start goapp.service'
                    sh 'ssh ${userName}@192.168.105.3 -i ${keyFile} -C sudo systemctl enable goapp.service'
                }
            }
        }
    }
}

