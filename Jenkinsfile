pipeline{
    agent any
    environment{
        DOCKER_TAG = getDockerTag()
    }
       stages{
        stage("Git Checkout"){
            steps{
                git 'https://github.com/Rupeshsolanki/alumni.git'
                }
            
        }
        stage('Docker Build Image'){
            steps{
                sh 'docker build . -t ${DOCKER_TAG}'
            }
        }
        stage('Run Docker Container'){
            steps{
                sh 'docker run  -d -p 8000:8000 ${DOCKER_TAG}'
            }
        }
    }
    
    
}
 def getDockerTag(){
     def tag = sh script: 'git rev-parse HEAD', returnStdout: true
     return tag
 }
