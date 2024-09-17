pipeline {
    agent { 
        node {
            label 'docker-agent-python'
            }
      }
    triggers {
        pollSCM '* * * * *'
    }
    stages {
        stage('Build') {
            steps {
                echo "Building.."
                sh '''
                cd myapp
                pip install -r requirements.txt
                '''
            }
        }
        stage('WhenMaster') {
            when {
                branch 'master'
            }
            steps {
                echo "Testing.."
                sh '''
                cd myapp
                python3 hello.py
                python3 hello.py --name=Jakob
                '''
            }
                
        stage('WhenNotMaster') {
            when {
               not {
                   branch 'master'
               }
            }
            steps {
                echo "Not the master. Fuck off!"
            }
                        
        }
        stage('Deliver') {
            when {
                branch 'master'
            }
            steps {
                echo 'Deliver....'
                sh '''
                echo "doing delivery stuff.."
                '''
            }
        }
    }
}
