
##  USE CASES

## Use Case : 1 
Title : Get a list of recommended users who can help with the problem tag along with its analytics.</br>

### Preconditions: 
User must have a browser and an internet connection. Preferably Google Chrome as a browser with JavaScript enabled.</br>

### Main Flow: 
[S1] User clicks on anyone of the tags/languages or filters them using the text box. </br>
[S2] On clicking the tag the portal gets a list of recommended StackOverflow Users who have a high probability of answering the user's question based on various metrics(like reponse time, verified answers,popularity on StackOverflow.) and visualizations based on which the list was recommended.</br>
### Sub Flows:
[S1] User clicks a tag on the portal. For example Java</br>
[S2] Information gets fetched via a GET request on the StackOverflow and Github server.</br>
[S3] Fetched information undergoes through analytical formulas to determine top users and gets stored in JSON format.</br>
[S4] The data from the JSON file is read using JavaScript and displayed on the web.</br>
[S5] The portal uses these analytics and uses Tableau to display different charts( line chart, histogram ).</br>
[S6] The portal gets a list of developers along with their StackOverflow Id who could probably solve the user's problem. </br>
### Alternative Flow:
[S1] User does not click on any of the languages available.</br>
[S2] Tag/Language entered is not available on StackOverflow.</br>
[S3] There is no internet connection available.</br>
[S4] User has proxy restrictions which prohibit the portal to access the stackoverflow API.</br>
[S5] User enters tag in a different encoding format.</br>
[S6] The tableau public server is down and does not update the charts.</br>

## Use Case : 2
Title : A software developer wants to refer some code regarding resolving a bug or finding a better implementation.</br>
### Preconditions: 
User should have access to github API and a working internet connection.</br>
### Main Flow: 
[S1] User interacts with the portal by clicking on the tag of his problem domain.</br>
[S2] The analytics portal gives a list of top 5 trending repositories on github along with the author and description of the repositories.</br>
[S3] The information is displayed on the portal in the form of a list of cards.</br>
###  Sub Flows:
[S1] User either click on the tag or enter language for which he needs the list of repositories</br>
[S2] On clicking the data the portal sends a GET request to the github-trending-api.</br>
[S3] The API hits the github database and gets the top 5 trending repositories as objects.</br>
[S4] Gets a list with name of author, link of the repository, description and the author of the repository.</br>
### Alternative Flow:
[S1] Incorrect language is entered.</br>
[S2] No internet access or proxy blocking the github api.</br>
[S3] Github API is down for maintainance.</br>
[S4] Slow internet connection.</br>
 
## Use Case : 3
Title: A software engineer wants to get updates/email notifications regarding the particular tag.</br>
### Preconditions: 
User should have a valid email id and cross origin requests enabled in the browser.</br>
### Main Flow: 
[S1] User clicks the subscribe button for a particular tag </br>
[S2] The portal fetches top 10 questions and its answers and sends an email to the user everytime any activity happens regarding that tag.</br>
###  Sub Flows:
[S1] The portal accesses the StackOverflow API and fetches questions for the tag the user clicked on. </br>
[S2] Data is retrieved in the form of a JSON object with the questions and answers.</br>
[S3] User gets an email with the consolidated list of questions and answers for that particular tag.</br>
[S4] The User gets an email notification depending on the frequency provided ( daily/weekly/monthly) containing required activity on tag or language.</br>
### Alternative Flow:
[S1] User does not go to the subscribe page from the portal.</br>
[S2] User closes the browser without clicking the submit button.</br>
[S3] Email Id entered is incorrect or it does not exist. </br>
[S4] The SMCP port for email is blocked in the environment from which the user is accessing the portal.</br>

## MOCKING

There are two entities of data in this project:
1. GitHub trending repositories data
2. StackOverflow User data

Here, we have explained the data scehma for both and have also attached mock .json files for reference.

#### Github Trending Repositories Data Schema

The Mock JSON file which was used for the portal can be accessed using this link.
[Github Trending Mock Data](https://github.ncsu.edu/pmshah/csc510-project/blob/master/GitHub_Mock.json)

The JSON stub shown below exhibits the schema and structure of the data recieved for the trending repositories for each language from the custom GitHub trending API.

```
"Language" :[{
        "Repository_Name" : RepoName,
        "Description" : RepoDescription,
        "Author" : RepoAuthor,
        "Repository_Link" : RepoLink
       }]
```

Here "Language" is the root component which will have values like Python, Java etc and it shall have 5 nested objects which will have corresponding repository details. Each of the 5 nested objects is a trending repository for that "Language".

Going one depth inside the JSON object we have the following pairs:
1. "Repository_Name" : RepoName
This represents the repository name.
2. "Description" : RepoDescription
This field shall have a one line description of the repository.
3. "Author" : RepoAuthor
This field shall have the name of the author of the repository.
4. "Repository_Link: : RepoLink
This field shall have the link of the github repository.

#### Recommended StackOverflow Users Data Schema

The Mock JSON file which was used for the portal and Tableau (mock) Visualizations can be accessed using this link.
[Recommended StackOverflow Users Mock Data](https://github.ncsu.edu/pmshah/csc510-project/blob/master/StackOverflow_Mock.json)

The JSON stub shown below exhibits the schema and structure of the data recieved for the recommended StackOverflow Users for each language from the custom GitHub trending API.

```
"Language" :[{
        "User":UserName,
        "Display_Name" : FullName,
        "Link" : UserProfileLink,
        "Score" : UserScore,
        "Response_Time": AvgTime;
        "Popularity": AvgParameter
       }]
```

Here "Language" is the root component which will have values like Python, Java etc and it shall have 5 nested objects which will have corresponding repository details. Each of the 5 nested objects is a trending repository for that "Language".

Going one depth inside the JSON object we have the following pairs:
1. "User":UserName
This represents the user name selected by the user while creating the account.
2. "Display_Name" : FullName
This field holds the user's full name.
3. "Link" : UserProfileLink
This field stores the link to the user's StackOverflow profile.
4. "Score" : UserScore
Users have reputation on StackOverflow based on upvotes, this field holds that value.
5. "Response_Time": AvgTime;
A custom parameter that represents the average time user takes to respond to questions.
6. "Popularity": AvgParameter
A custom parameter which is actually a normalized average of parameters like- score, number of verified answers and response time.

## PORTAL IMPLEMENTATION

We finished working on 4 different modules of overall project this sprint. All working modules implemented at this stage are as follows:

1. UI Portal (Basic Layout)
2. Core logic of the system
3. Python Script (to fetch relevant data from GitHub)
4. Python Script (to fetch relevant data from StackoverFlow)
5. Tableau Web Data Connector

## MODULE 1: UI Portal

Portal link: [STACKANALYTICA](https://analytics-portal.herokuapp.com/)

We have created a basic layout of our overall system where at this stage, user can come to our portal and see top trending tags and by clicking any of those, they get redirected to a page showing "top users". This list of users indicate the users who can provide an answer to the query with a minimum response time compared to others and in a best possible way.Chart-images are included in place of "Live Tableau Dashboard" for this sprint. 


### Page-wise Description:

#### HOMEPAGE ([Link](https://analytics-portal.herokuapp.com/)):
- As you can see after going to link above, user can find weekly popular tags of StackOverFlow on our homepage. 
- Also, by clicking, any of these tags or searching a tag using provided "search bar", user gets redirected to Analystics Page.

#### ANALYTICS PAGE ([Link](https://analytics-portal.herokuapp.com/Analytics.html))
- User is redirected to this page only after searching or clicking any particular tag. 
- Left side of the page displays list of top 5 users on StackOverFlow and also, left-bottom part contains list of top trending GitHub repositories for the particular tag. 
- On the right side, different visulizations are provided depending on our analysis on the data fetched from StackOverFlow. At this stage, images are used as a place-holder for those charts which wil be replaced by live Tableau charts in following sprint.
- User can use subscribe button provided in the bottom to subscribe for email notifications of a particular tag.

#### SUBSCRIPTION PAGE ([Link](https://analytics-portal.herokuapp.com/EmailSubscription.html))
- User is redirected to this page only after clicking on "subscription" button. The page simply contains a text box where user can enter their email id, and select the frequency (1 day, 3 days or weekly) for notifications.
- For example, if user selects frequency as "3 days" then user will get email notifications of latest trends for that tag every 3 days.

## MODULE 2: Core Logic of the System
This module explains the logic and equations we are using to compare different users on StackOverFlow based on their answers. We are evaluating users based on six parameters:

1. StackOverFlow Profile Score
2. Average Response Time Score
3. Last Active Duration Score
4. Upvotes Score
5. Profile Completion Score
6. Normalized Score

#### Definition of Each Score

#### StackOverFlow Profile Score
- This is the profile score of a user provided by StackOverFlow and is accessible by their API.
- Profile Score is one of the easiest ways to evaluate user profile.
#### Average Response Time Score
- Average of Time (number of seconds) taken by the user to respond each question/query related to that tag.
- This score is in an inverse relation to the "Average Response Time". Hence, users having more response time will get a low score.
- Average response time is useful for us to know, on average how much time does the user take to answer particular query of that tag.

```
Activity Score = 100/(Number of Seconds till last activity)
```

#### Last Active Duration Score
- Last active duration of the user is useful to know whether user is immediately available or not.
- This score is in an inverse relation to the duration.
- For example, user who is active currently will have more score for this parameter than the user who was active 3 days ago.

```
Activity Score = 100/(Number of Seconds till last activity)
```

#### Average upvotes Score
- User's all the answers for a particular tag are considered for this tag and number of upvotes to each answer are taken and averaged for this score.
- user having maximum upvotes will have a greater score

```
Upvotes Score = Average of Number of Upvotes for all answers related to a tag
```
#### Profile Completion Score
- Users who have included their GitHub profile link, reposiotry link and email will have a score of 100.
- Users who have included their GitHub profile link and reposiotry link 75.
- Users who have included email will have a score of 50.
- Users who have no information will have a score of 0.

```
Completion Score =  0 if No contact details
                   50 if only email information
                   75 if GitHub information available
                  100 if all information available
```
#### Normalized Score
- This is the final score we are calculating by aggregating and standardizing all user's score in the range (0-100).
- Reason for this score is to make all users' scores comparable and eliminating outliers.

```
NORMALIZED SCORE(n) =  ((Total_Score(n) - AVG_total)/SD) * 100

where,
Total_Score(n) = StackOverFlow Score + Response-time Score + Activity Score + Upvotes Score + Completion Score
AVG_total = AVG of all users' Total_Score
SD = Standard Deviation of N users' Total_Score

NORMALIZED SCORE(n) belongs to [0,100].

```
After calculating NORMALIZED SCOREs of n users, top 5 users having maximum score are fetched.

## MODULE 3: Python Script (To fetch relevant data from GitHub)
Find our script here: [GitTrends.py](https://github.ncsu.edu/pmshah/csc510-project/blob/master/github_parse.py)
- We have written a python script to fetch the top 5 trending repositories for any programming language from github.
- The script performs a GET request to the npm package "github-trending-api" which returns a promise in the form of a JSON object and then we return the top 5 trending repositories from a plethora of repositories.
- The JSON object returned has the name,author,link and description of each of the trending repositories.
- Below is a sample request for the language "JavaScript" and as we want trending repositories for that day we pass daily as the second parameter.

```
parameters = {"language": language , "since" : daily }
response = requests.get("https://github-trending-api.now.sh/repositories", params=parameters)
```

- The above request returns a JSON object and the schema of the returned object is explained in detail in the Mocking section below.

## MODULE 4: Python Script (To fetch relevant data from StackOverFlow)
Find our script here: [StackTrends.py](https://github.ncsu.edu/pmshah/csc510-project/blob/master/stacktrends.py)
- We have developed a basic script to fetch the data from StackOverFlow using Python. 
- At this stage, we are fetching top users for Java, Python, C#, JavaScript and Golang only.
- Core equations mentioned in module 2 are yet to be implemented in following sprint.

```
resp = requests.get('https://api.stackexchange.com/2.2/tags/'+i+'/top-answerers/month?site=stackoverflow')
gh = resp.json()
```
- Here, the above mentioned link brings the top asnwerers of a month for a particular tag. "i" is the language here which is iterated over list of languages ['JAVA', 'Python,.....]. Duration can be changed from month to year or even weekly.
- After gathering this list, we are fetching Profile ID, Profile score and the response time of the user.
- JSON file containing top scorers by language is created at the end [Detailed explanation in "Mocking"].
## MODULE 5: Tableau Web Data Connector
- 5th module for this sprint is embedding Tableau to web portal.
- We created a mock JSON data of our system using generalised schema of our system and gave it as an input to the Tableau Desktop.
- We generated Live charts for this data.
- We published these charts later from Tableau Desktop to Tableau Public, and using it tried to embed it our HTML scripts.
- At this stage, we can access LIVE chart using tableau dashboard in browser.

For example,
Note: charts below are generated from mock JSON given as input.
#### File [index.html](https://github.ncsu.edu/pmshah/csc510-project/blob/master/index.html) can be downloaded and run to view interactive charts in the browser.
1. You can access these charts from here: Chart 1 [Link](https://public.tableau.com/views/pop_python/Sheet2?:embed=y&:display_count=yes) and Chart 2 [Link](https://public.tableau.com/views/respo_python/Sheet1?:embed=y&:display_count=yes)
2. Chart 1 represents a histogram of a user against popularity of the user based on his answers for Python tag.
3. Chart 2 represents a line chart of user against their average response time.

NOTE: All the modules (1 to 5) are working independent of each other and basic implementations in each module has been done keeping our long term goal in mind.

## TASK TRACKING

#### You can find the log of our tasks during this sprint using this file: 
[WORKSHEET.md](https://github.ncsu.edu/pmshah/csc510-project/blob/master/WORKSHEET.md)

- Includes all user stories 
- Includes details of weekly discussions
- Includes details of Sprint Retrospectove

## SCREENCAST
You can access our screencast video from here : [Screencast Link](https://drive.google.com/file/d/1HLjp9pq_QQqJPtXTkHR3g3sK9h4nbPF3/view?usp=sharing)
