pipeline {
    agent any
    stages {
        stage('clone') {
            steps {
		echo "Cloning Git"
		sh "rm -rf /var/lib/jenkins/cvat_data"
		sh "mkdir /var/lib/jenkins/cvat_data"
		sh "cd /var/lib/jenkins/cvat_data ; git clone https://github.com/Shivendratiwari0020/dev-cvat.git"
		
            }



        }



        stage('Build') {

            steps {

                sh "cd /var/lib/jenkins/cvat_data/dev-cvat/; docker-compose -f docker-compose.yml -f docker-compose.dev.yml build"

            }



        }



	stage('Test') {

            steps {

                script {

		sh "echo Testing...."

                }

            }

        }



        stage('Deploy') {

            steps {

		echo "Deploy.."
		
                sh "cd /var/lib/jenkins/cvat_data/dev-cvat/ && docker-compose down"
	            sh "docker rm -f '\$(docker ps -aq | grep -v bitbucket)'"
                sh "cd /var/lib/jenkins/cvat_data/dev-cvat/ && docker-compose up -d"
		



            }



        }



    }



}
