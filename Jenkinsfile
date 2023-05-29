pipeline {
    agent any
    tools {
        go 'go-1.20.4'
    }
    stages {
        stage('Tests') {
            steps {
                sh 'go test .'
            }
        }
        stage('Build') {
            steps {
                sh 'go build main.go'
                archiveArtifacts artifacts: 'main', fingerprint: true
            }
        }
        stage('Build docker image') {
            steps {
                sh 'docker build --tag ttl.sh/goapp-hyusta:1h .'
                sh 'docker push ttl.sh/goapp-hyusta:1h'
            }
        }
        stage('Deploy') {
            steps {
                withCredentials([sshUserPrivateKey(credentialsId: 'target-key', keyFileVariable: 'keyFile', usernameVariable: 'userName')]) {
                    sh 'mkdir --parents $HOME/.ssh'
                    sh 'ssh-keyscan 192.168.105.3 > $HOME/.ssh/known_hosts'
                    sh 'ssh -l ${userName} -i ${keyFile} 192.168.105.3 -C docker rm --force goapp || true'
                    sh 'ssh -l ${userName} -i ${keyFile} 192.168.105.3 -C docker pull ttl.sh/goapp-hyusta:1h'
                    sh 'ssh -l ${userName} -i ${keyFile} 192.168.105.3 -C docker run --detach --publish 4444:4444 --name goapp ttl.sh/goapp-hyusta:1h'
                }
            }
        }
        stage('Health test') {
            steps {
                sh 'curl --silent http://192.168.105.3:4444/api'
            }
        }
    }
}

