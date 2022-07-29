pipeline {
    environment {
     BRANCH_NAME = "${GIT_BRANCH.split("/")[1]}"
     
  }
    agent any
    stages {
       stage('Clone') {
            steps {
               script {
                    if (env.BRANCH_NAME == 'test') 
                    {
                       echo 'Cloning the latest Repo' 
                       sh "sh /var/lib/jenkins/scripts/clone.sh 10.40.41.57 test" 
           
                    } 

                }
            }
      
        }
        
        stage('Build') {
            steps {
               script {
                   if (env.BRANCH_NAME == 'test') 
                    {
                       echo 'Building the latest Images' 
                       sh "sh /var/lib/jenkins/scripts/build.sh 10.40.41.57 test" 
           
                    } 

                }
            }
      
        }
        
       stage('Deploy') {
            steps {
               script {
                   if (env.BRANCH_NAME == 'test') 
                    {
                       echo 'Deploying' 
                       sh "sh /var/lib/jenkins/scripts/deploy.sh 10.40.41.57 test" 
           
                    } 

                }
            }
      
        }
    }
}
