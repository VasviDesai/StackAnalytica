# Use Case 1 Implementation
Title : Get a list of recommended users who can help with the problem tag along with its analytics. [Detailed Description](https://github.ncsu.edu/pmshah/csc510-project/blob/master/MILESTONE2.md)
</br> </br>
For this use case, user can go to our web-portal using this  [link](https://analytics-portal.herokuapp.com) and can search for popular tags on it. After clicking, user can find the following information:
##### 1. Top trending GitHub repository related to a tag on a particular day
On the homepage of the portal, user can select any language related tag regarding which they have issues. As soon as they click on any tag they are redirected to the analysis part of the portal. 
##### 2. Top users for a selected tag based on various analysis [StackTrends Script](https://github.ncsu.edu/pmshah/csc510-project/blob/master/stacktrends.py)
On analytics page for a particular language, user can find top users to get in touch with regarding their query. These provided users have a highest probability of providing response as soon as possible with more accuracy than others. 

- You can find the python script for fetching live and dynamic data from StackOverflow, and processing various analysis from above link. 
- This script runs as daemon process which updates our JSON data fetched from StackOverFlow for different languages dynamically and feeds it to Tableau Desktop which later feeds it to directly to our web-portal.

This module explains the logic and equations we are using to compare different users on StackOverFlow based on their answers. 

1. StackOverFlow Profile Score: This is a profile score of a user provided by StackOverFlow and is accessible by their API. 
2. Average Response Time Score: Average of Time (number of seconds) taken by the user to respond each question/query related to that tag.
3. Last Active Duration Score: Last active duration of the user is useful to know whether user is immediately available or not. This score is in an inverse relation to the duration.
4. Average upvotes Score: User's upvote score represents how accurate the user is in giving answers which is calculated using number of approved answers for a tag.
5. Normalized Score: This is the final score we are calculating by aggregating, weighing and standardizing all user's score in the range (0-100). Reason for this score is to make all users' scores comparable and eliminating outliers.

More details on [scores](https://github.ncsu.edu/pmshah/csc510-project/blob/master/MILESTONE2.md)
```
NORMALIZED SCORE(n) =  ((Total_Score(n) - AVG_total)/SD) * 100

```
Here, Last Active Score has the highest weightage as it represents the user is recently active to answer.

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
These scores are displayed on the web portal, user can select any user from provided users based on their priority. If user wants a quick answer then they can go with highest "Activity Score", if they want accurate answer than they can go with user having "highest Upvote score" on our portal.

##### 3. Visual representations using interactive charts
Based on all the scores calculated, we have embedded live interactive dashboard using Tableau Desktop and public services in our portal. User can easily compare top users for a tag, simply by interacting with them. User can also download these charts in more than 5 different formats.

Charts here, get updated on a daily basis as soon as live data from StackOverFlow changes. We can adjust this updation frequency from 1 hour to weekly also based on the requirements.

# Use Case 2 Implementation

Title : A software developer wants to refer some code regarding resolving a bug or finding a better implementation. [Detailed Description](https://github.ncsu.edu/pmshah/csc510-project/blob/master/MILESTONE2.md)
<br> <br>
The user can access top 5 trending github repositories for a tag of their choice on the [portal](https://analytics-portal.herokuapp.com). This use case aims at reducing the users task of browsing through GitHub to find trending repositories on that day for the relevant tag. Trending repositories differ on a daily basis and thus the [Python Script](https://github.ncsu.edu/pmshah/csc510-project/blob/master/github_parse_code/github_parse.py) will be updated accordingly thus generating updated json files which are embedded dynamically into the portal.

Code of the npm-package used [trending-api-npm](https://github.com/huchenme/github-trending-api)

The example JSON stub shown below exhibits the schema and structure of the actual data extracted for the trending repositories from the custom GitHub trending API for the tag JavaScript. 
```
{  
   "author":"vuejs",
   "name":"vue",
   "description":"🖖 Vue.js is a progressive, incrementally-adoptable JavaScript framework for building UI on the web.",
   "url":"https://github.com/vuejs/vue"
}
```
The JSON object for trending GitHub repositories has the following pairs:
1. "author" : This field has the name of the author of the repository "veujs"
2. "name" : This represents the repository name "vue"
3. "description" : This field denotes a one line description of the repository "🖖 Vue.js is a progressive, incrementally-adoptable JavaScript framework for building UI on the web."
4. "url" : This field holds the link of the github repository "https://github.com/vuejs/vue"

Now, this JSON file which updates daily (the time parameter can be changed, but for our portal we are showing the top trending repositories for that day) created from the Python Script is them embedded into the portal using JavaScript.

# Use Case 3 Implementation
Title: A software engineer wants to get updates/email notifications regarding the particular tag. [Detailed Description](https://github.ncsu.edu/pmshah/csc510-project/blob/master/MILESTONE2.md)
<br> <br>

In this use case the user can subscribe to trending questions for that particular tag. This use case aims to send the user email updates based on any interval the user specifies (eg. daily, weekly ,monthly) and the portal shall send the user a curated list of top trending question for that particular tag or language.
To implement this use case we have used EmailJS as our SMTP email client and we send the curated data in the form of a list in the body of the email to the user.
```
    var template_params = {
    to_name: 'User',
    message_html:markup
    }
    
    emailjs.send('gmail', 'message_html', template_params)
    .then(function(response) {
       console.log('SUCCESS!', response.status, response.text);
    }, function(error) {
       console.log('FAILED...', error);
    });
    
```

The above code stub performs a asynchronous post request to the SMTP service which sends the email having the list to the email id provided in the text box.

# Task Tracking
### You can find the log of our tasks during this sprint using this file: 
[WORKSHEET.md](https://github.ncsu.edu/pmshah/csc510-project/blob/master/WORKSHEET.md)

- Includes all user stories 
- Includes details of weekly discussions
- Includes details of Sprint Retrospectove

# Updated Screencast
Detailed Updated Screencast of all implementation mentioned above: ([Screencast Link](https://drive.google.com/file/d/19kwusE0EWlC4gsZOEmCeDQZCu0v57d1J/view?usp=sharing))

# Implementation
You can find our portal's link here: [Portal on Heroku](https://analytics-portal.herokuapp.com)
