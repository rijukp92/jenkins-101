pipeline {
    agent any  // Allocate an agent for the entire pipeline

    stages {
        stage('WakingUp') {
            steps {
                echo "WakingUp.."
                sh '''
                echo "doing WakingUp stuff.."
                '''
            }
        }
        stage('Eating') {
            steps {
                echo "Eating.."
                sh '''
                echo "doing Eating stuff.."
                '''
            }
        }
        stage('Working') {
            steps {
                echo 'Working....'
                sh '''
                echo "doing Working stuff.."
                '''
            }
        }
    }
}
