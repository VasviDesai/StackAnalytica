# StackAnalytica
A web tool that provides for a problem tag (eg java, javascript) an integrated view of StackOverflow Users and Github repositories.
CSC 510-Project

Team: <br/>
1. Vasvi C. Desai <br/>
2. Prakshatkumar Shah <br/>
3. Harsh J. Patel <br/>

## Milestone 1 (DESIGN.md)
https://github.ncsu.edu/pmshah/csc510-project/blob/master/DESIGN.md

## Milestone 2
https://github.ncsu.edu/pmshah/csc510-project/blob/master/MILESTONE2.md

## Milestone 3
https://github.ncsu.edu/pmshah/csc510-project/blob/master/MILESTONE3.md

## Milestone 4
https://github.ncsu.edu/pmshah/csc510-project/blob/master/MILESTONE4.md

## Milestone 5 (REPORT.md)
https://github.ncsu.edu/pmshah/csc510-project/blob/master/REPORT.md


# Deployment

## Prerequisites:

Step 1: Create an account on Heroku and install Heroku CLI
Execute the below command and enter your email address and password.
```
Heroku login
```
Step 2: GitHub Account: you need to have a GitHub account.

Step 3: Link the GitHub repository to Heroku.
```
heroku git:remote -a "repo-link"
```
Step 4: Automated Deployment Script: [Link](https://github.ncsu.edu/pmshah/csc510-project/blob/master/Stackanalytica/deploy)

## Process:

The portal is deployed on the Heroku Cloud Platform. Our portal is built upon HTML, JavsScript and Python(Flask). We have used the Heroku Command Line Interface [Documentation Link](https://devcenter.heroku.com/articles/heroku-cli-commands) and GitHub's integration to accomplish continious integration and deployment deployment. All the dependencies of the portal are added to a requirements.txt file that get installed on the fly while deploying the portal using the deploymnet script.
Dependencies to deploy the portal
```
StackAPI==0.1.12
urllib3==1.24.1
python-dateutil==2.8.0
gunicorn==19.9.0
Flask==1.0.2

```

In our script we first create a heroku app bucket which is linked to our ghithub repository. We prepare our code for staging using the git add. command. After the files are staged and ready to be commited you can specify a deployment message and proceed. Then the script pushes our code to the github repository which triggers the heroku build process. As you can see it detects the type of application from the Procfile, and then installs the dependencies and proceeds to create a production bundle to be deployed on the portal. And as we can see the process is completed and now we see that the portal is deployed on this [Portal Link](http://stackanalytica-csc510.herokuapp.com).
Deployment Script
```
#!/bin/bash  
heroku login
heroku create app  
git status
git add .  
read -p "Deployment Message Description: " desc  
git commit -m "$desc"  
git push heroku master
```
Command to execute the above script : 
</br> For Windows ( Open the gitbash cmd or powershell and use ./deploy)
</br> For Mac /Unix users ( sudo sh deploy)
