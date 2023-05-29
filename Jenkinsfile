pipeline {
    agent any
    stages {
        stage('Build docker image') {
            steps {
                sh 'docker build --tag ttl.sh/pythonapp-hyusta:1h .'
            }
        }
        stage('Push docker image') {
            steps {
                sh 'docker push ttl.sh/pythonapp-hyusta:1h'
            }
        }
        stage('Pull docker image') {
            steps {
                withCredentials([sshUserPrivateKey(credentialsId: 'target-key', keyFileVariable: 'keyFile', usernameVariable: 'userName')]) {
                    sh 'mkdir --parents $HOME/.ssh'
                    sh 'ssh-keyscan 192.168.105.3 > $HOME/.ssh/known_hosts'
                    sh 'ssh -l ${userNam`e} -i ${keyFile} 192.168.105.3 -C docker pull ttl.sh/pythonapp-hyusta:1h'
                }
            }
        }
        stage('Run docker container') {
            steps {
                withCredentials([sshUserPrivateKey(credentialsId: 'target-key', keyFileVariable: 'keyFile', usernameVariable: 'userName')]) {
                    sh 'ssh -l ${userName} -i ${keyFile} 192.168.105.3 -C docker rm --force pythonapp || true'
                    sh 'ssh -l ${userName} -i ${keyFile} 192.168.105.3 -C docker run --detach --publish 4444:4444 --name pythonapp ttl.sh/pythonapp-hyusta:1h'
                }
            }
        }
        stage('Health check') {
            steps {
                sh 'sleep 5'
                sh 'curl --silent http://192.168.105.3:4444/api'
            }
        }
    }
}

