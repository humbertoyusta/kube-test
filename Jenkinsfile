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
        stage('Health Check') {
            steps {
                withCredentials([file(credentialsId: 'kubeconfig', variable: 'kubeconfig')]) {
                    script {
                        // Start port-forwarding
                        def portForward = sh(script: "kubectl --kubeconfig=${kubeconfig} port-forward service/pythonapp 4444:4444 &", returnStdout: true).trim()
                        sleep 5 // Sleep for a while to allow port-forwarding to be set up
                        
                        // Perform health check
                        def responseCode = sh(script: "curl -s -o /dev/null -w '%{http_code}' http://localhost:4444/api", returnStdout: true).trim()
                        if (responseCode != '200') {
                            error("Health check failed with response code: ${responseCode}")
                        }
                        
                        // Kill the port-forward process
                        sh 'pkill -f "kubectl --kubeconfig=${kubeconfig} port-forward service/pythonapp 4444:4444"'
                    }
                }
            }
        }
    }
}

