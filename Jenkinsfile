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
                    sh 'kubectl --kubeconfig=${kubeconfig} delete deployment pythonapp || true'
                    sh 'kubectl --kubeconfig=${kubeconfig} delete service pythonapp || true'
                    sh 'kubectl --kubeconfig=${kubeconfig} apply --filename deployment.yaml'
                    sh 'kubectl --kubeconfig=${kubeconfig} apply --filename service.yaml'
                }
            }
        }
    }
}

