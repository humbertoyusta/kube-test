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
        stage('Deploy to Kubernetes') {
            steps {
                withCredentials([file(credentialsId: 'kubeconfig', variable: 'kubeconfig')]) {
                    sh 'kubectl --kubeconfig=${kubeconfig} run pythonapp --image=ttl.sh/pythonapp-hyusta:1h'
                    sh 'kubectl --kubeconfig=${kubeconfig} expose pod pythonapp --type=ClusterIP --port=4444'
                }
            }
        }
    }
}

