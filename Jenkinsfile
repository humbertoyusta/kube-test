pipeline {
    agent any
    stages {
        stage('Build docker image') {
            steps {
                // Build the docker image
                sh 'docker build --tag ttl.sh/pythonapp-hyusta:1h .'
            }
        }
        stage('Push docker image') {
            steps {
                // Push the image to the ttl.sh registry
                sh 'docker push ttl.sh/pythonapp-hyusta:1h'
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                withCredentials([file(credentialsId: 'kubeconfig', variable: 'kubeconfig')]) {
                    sh 'kubectl --kubeconfig=${kubeconfig} apply --filename deployment.yaml'
                    sh 'kubectl --kubeconfig=${kubeconfig} apply --filename service.yaml'
                }
            }
        }
        stage('Health Check') {
            steps {
                withCredentials([file(credentialsId: 'kubeconfig', variable: 'kubeconfig')]) {
                    script {
                        sleep 3 // Wait for the service to be ready
                        def portForward = sh(script: "kubectl --kubeconfig=${kubeconfig} port-forward service/pythonapp 4444:4444 &", returnStdout: true).trim()
                        sleep 3 // Wait for the port-forward to be ready
                        
                        // Check the health of the service
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

