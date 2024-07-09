pipeline {
    agent { 
        node {
            label 'docker-agent-python'
            }
      }
    parameters {
        file(name: 'icon', description: 'icon file')
        file(name: 'logo', description: 'logo file')
    }
    stages {
        stage('Prepare') {
            steps{
                script {
                    def image1 = params.image1
                    def image2 = params.image2
                    sh "cp ${image1} ./logos/image1.png"
                    sh "cp ${image2} ./logos/image2.png"
                }
            }
        }
        stage('Build') {
            steps {
                echo "Building.."
                sh '''
                pip install -r requirements.txt
                '''
            }
        }
        stage('Test') {
            steps {
                echo "Testing.."
                sh '''
                python3 logo_changer.py
                '''
            }
        }
        stage('Deliver') {
            steps {
                echo 'Deliver....'
                sh '''
                echo "doing delivery stuff.."
                '''
            }
        }
    }
}