pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        sh 'python3 --version'
      }
    }
    stage('hello') {
      environment {
        liam_token = credentials('LIAM_USERNAME')
      }
      steps {
        sh 'python3 hello.py --username $liam_token_USR --password $liam_token_PSW'
      }
    }
  }
}
