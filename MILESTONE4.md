
# Deployment

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
Command to execute the above script : For Windows ( Open the gitbash cmd or powershell and use ./deploy)
                                      For Mac /Unix users ( sudo sh deploy)

# Data Ingest/Update

## StackOverflow Top Users
Users can go to our web-portal using this  [link](https://stackanalytica-csc510.herokuapp.com/) and can search for popular tags on it. As soon as any of the provided tags on homepage are clicked, our script [StackTrends](https://github.ncsu.edu/pmshah/csc510-project/blob/master/Stackanalytica/stacktrends.py) gets executed.   
- On the backend side, we get the name of the language selected by the user and fetch the data from StackOverFlow dynamically. This dynamic data then goes under different score analysis processes mentioned in detail in previous milestones. 
- At the end, we get a JSON object containing Top Users data based on their cumulative score, popularity and accuracy of their answers to the questions asked related to that tag. Analysis is also based on user's last activity on StackOverFlow which indicates user's availability & responsiveness.
- Sample format of JSONs created:
```
 {  
         "Profile_ID":2901002,
         "display_name":"jezrael",
         "link":"https://stackoverflow.com/users/2901002/jezrael",
         "Score":9.691739408579998,
         "Response_Time":1.2400909414914365,
         "Popularity":0.6621862810057321,
         "last_activity":39
  }
```
- This JSON object is then directly rendered and ingested on our portal. We have written a script which takes this dynamically generated data & then creates Live and interactive charts which can be seen on portal.
- Hence, these charts change whenever the data from StackOverFlow changes, providing latest visualizations to the users. 


## GitHub Trending Repositories

- The githubtrends.py file [link](https://github.ncsu.edu/pmshah/csc510-project/blob/master/Stackanalytica/github_parse.py) is responsible for the getting the latest trending repositories for a particular language. 
- Here the Trending repositories differ on a daily basis and thus the Python Script shall execute a asynchronous fetch call to the API endpoint and the repositories shall be updated and a new list with updated repositories shall be displayed on the portal. We have used the [trending-api-npm](https://github.com/huchenme/github-trending-api) package to get the latest trending repositories.

Code Stub with comments that performs request to get latest trending repositories.

```
import json
import requests


def getTrendingRepo(language, since):
    parameters = {"language": language, "since": since}
    response = requests.get("https://github-trending-api.now.sh/repositories", params=parameters)

    # Get the response data as a python object.  Verify that it's a dictionary.
    data = response.json()
    # print(data)
    custom_data = []
    for i in range(0, 5):
        custom_data.append({
            'author': data[i]['author'],
            'name': data[i]['name'],
            'description': data[i]['description'],
            'url': data[i]['url']
        })
    return custom_data
```

Here we can specify any language and frequency to get the required trending repositories and as soon as the user clicks on a language on the homepage a REST API request is executed on the endpoint of the npm package and fetch the trending repositories as an object where we create an appropriate JSON object to display it on the Analytics page.




# Code Inspection

Final Code of the portal can be found here : [Code Link](https://github.ncsu.edu/pmshah/csc510-project/tree/master/Stackanalytica)

Folder structure of our portal. Below is a tree structure to give a brief overview of the folder structure of our portal. 

```
├── Stackanalytica
│   ├── Procfile
│   ├── __pycache__
│   │   ├── app.cpython-37.pyc
│   │   ├── github_parse.cpython-37.pyc
│   │   └── stacktrends.cpython-37.pyc
│   ├── _gitignore.txt
│   ├── app.py
│   ├── deploy
│   ├── github_parse.py
│   ├── requirements.txt
│   ├── stacktrends.py
│   ├── static
│   │   ├── bootstrap.min.css
│   │   ├── bootstrap.min.js
│   │   ├── chart.min.js
│   │   ├── custom.js
│   │   ├── deeppurple.css
│   │   ├── demo.css
│   │   ├── demo.js
│   │   ├── flag-icon.min.css
│   │   ├── fontawesome-all.min.css
│   │   ├── ionicons.eot
│   │   ├── ------------
│   │   └── usecase3.js
│   └── templates
│       ├── Analytics.html
│       ├── EmailSubscription.html
│       ├── HomePage.html       
│       ├── data.json
│       ├── stacktrend.py
│       ├── styles.css
│       └── usecase3.js
```
All the html files that represent the pages are present in the templates folder. All Javascript libraries, css files are in the static folder. The root of the application is in the app.py file where the portal begins to execute.
The files github_parse.py and stacktrends.py have the core logic for data ingestion and update and have the logic to perform asynchronous requests to the stackoverflow and github server. The file requirements.txt has all dependencies listed to install during the deployment. The deploy file contains the deployment script.
The Homepage.HTML file contains code for the initial landing page. The Analytics.html page has code for the page where it displayes a list of users along with charts. The EmailSubscription.html contains code for the email subscription page which demonstrates the email functionality.

To locally run the portal. Execute the command "python app.py" in the root of the folder where app.py is present.
The portal shall be up and running on 127.0.0.1:5000.

# Task Tracking
### You can find the log of our tasks during this sprint using this file: 
[WORKSHEET.md](https://github.ncsu.edu/pmshah/csc510-project/blob/master/WORKSHEET.md)

- Includes all user stories 
- Includes details of weekly discussions
- Includes details of Sprint Retrospective

# Screencast
You can access our screencast video from here: [Screencast Link](https://drive.google.com/file/d/1OzpIBuLRCSM_BSWw4sbBSHpYguOptQum/view?usp=sharing)

# Implementation
You can find our portal's link here: [Portal on Heroku](http://stackanalytica-csc510.herokuapp.com/)
