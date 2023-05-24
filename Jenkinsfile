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
    }
}
