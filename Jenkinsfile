pipeline {
    environment {
     BRANCH_NAME = "${GIT_BRANCH.split("/")[1]}"
  }
    agent any
    stages {
       stage('Build') {
            steps {
               script {
                    if (env.BRANCH_NAME == 'master') 
                    {
                        echo 'Building in ${env.BRANCH_NAME}'
                        git url: 'https://github.com/Shivendratiwari0020/dev-cvat.git', branch: 'master'
                        sh "docker-compose -f docker-compose.yml -f docker-compose.dev.yml build"
                    } 
                    if (env.BRANCH_NAME == 'dev') 
                    {  
                        echo 'Building in ${env.BRANCH_NAME}'
                        git url: 'https://github.com/Shivendratiwari0020/dev-cvat.git', branch: 'dev'
                         
                        sh "docker-compose -f docker-compose.yml -f docker-compose.dev.yml build"
                    }
                    
                }
            }
      
        }
        
        stage('Deploy') {
            steps {
               script {
                    if (env.BRANCH_NAME == 'master') 
                    {
                        echo 'Deploy in ${env.BRANCH_NAME} Server'
                        sh "docker-compose down ; --rmi all -v"
                        sh "docker-compose up -d"
                        
                    } 
                    if (env.BRANCH_NAME == 'dev') 
                    {  
                        echo 'Deploy in ${env.BRANCH_NAME} Server'
                        sh "docker-compose down --rmi all -v"
                        sh "docker-compose up -d"
                    }
                    
                }
            }
      
        }
    }
}
