pipeline {
    agent any
    triggers {
        pollSCM 'H/5 * * * *'
    }
    stages {
        stage('checking') {
            steps {
                echo "Checking.."
                sh '''
                docker version
                '''
            }
        }
        stage('build') {
            agent {
                node {
                    label 'vm'
                    }
            }
            steps {
                echo "Building.."
                sh '''
                docker build . -t yagza/simple-php-site:latest
                '''
            }
        }
       
        stage('image_push') {
            steps {
                echo "pushing.."
                sh '''
                docker image ls
                '''
            }
        }
        stage('deploy') {
            agent {
                node {
                    label 'vm'
                    }
            }
            steps {
                echo 'Deploying....'
                sh '''
                echo "updating php-simple container..."
                docker rm php-simple -f || true
                docker run -d --name php-simple -p 8080:8080 yagza/simple-php-site:latest || true
                '''
                echo 'you may try to connect via http://10.0.0.146:8080'
            }
        }
    }
}
