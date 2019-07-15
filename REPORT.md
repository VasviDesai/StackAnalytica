# Problem

A software developer while working either in a company or individually might hit a few roadblocks and face issues such as, finding User Wiki or help regarding a language or new open source framework. When faced with issues like these, developers tend to go to platforms like StackOverflow and GitHub. Sometimes, rather than help the developer towards a solution, they might lead the user to get even more confused. The platforms sometimes do not provide a specific solution or StackOverflow sometimes provides too many or too few solutions which make the user more confused, and GitHub lists all repositories for that tag. StackOverflow and Github do not provide the user with a consolidated list of users that can specifically answer the question in the problem area though they provide resources and answers.

Situations like these lead to an impasse, thus slowing the progress of the process. This is a problem because there are times a developer hits a roadblock while trying to solve the problem, like an unresolved bug in a new open source framework or some backward compatibility issue in a particular language or framework. In such situations the person is in a dilemma regarding the steps he should take to deliver the module in time). A portal that can provide an integrated solution to address the issue is needed. Our analytics portal comes into play here, to assist users out of their conundrums by recommending them a probable list of users who are the highly likely to answer the question of the developer, along with daily trending GitHub repositories that would act as an additional resource. 

# Features

Our portal starts with a landing page where the user can select the language/tag he is interested in. Additionally, there is a search bar through which the user can filter the languages available in the portal and hit the search button to access all the features of the portal. Below is the image of the Homepage of the portal.

![alt text](https://github.com/VasviDesai/StackAnalytica/blob/master/HomePage.PNG)

## Top StackOverflow users with Visualizations

This feature provides the user with a list of StackOverflow users who are most probable to answer the user's query along with charts and visualizations that define various metrics to come up with this list.
- To implement this feature we hit the StackOverflow API which returns an object that goes through our python script that has custom scores defined along with their weights and these various metrics are then displayed on the portal.
- Here the users listed are not ordered in a particular order as there are various metrics, So it's subjective to the user using the web application and the user preference to consider which metric is the best for any StackOverflow user. Below is the list of the StackOverflow users along with their scores displayed on the portal.
</br>
<img width="611" alt="screen shot 2019-04-26 at 3 45 20 pm" src="https://media.github.ncsu.edu/user/10114/files/567dfd00-683a-11e9-9cc7-558bd95a4829">


Explanation of each score displayed on the portal
1. Cumulative Score:  An aggregated score considering various weights on the StackOverflow user score, Upvote score, Profile Completion Score and Response Time.
2. Profile Popularity:  This score is based on the average of all upvotes the user has got for his answers for that particular tag. This score also denotes the reputation of the user in the StackOverflow community
3. Last Activity Score: This score is based on how responsive the users are on StackOverflow. To calculate this we have considered the difference of time between answers the user has answered. This helps us in discarding dead accounts that are inactive from a long time in StackOverflow. The higher the activity score the more responsive the user is.

There are three charts displayed on the portal:

#### Chart 1
The below chart has the Users on the X-Axis and response time on the Y-Axis and it shows how responsive the users are having a lower response time means that a particular user is more active.
</br>
![alt text](https://github.com/VasviDesai/StackAnalytica/blob/master/chart1.PNG)




#### Chart 2
The below chart has the Users on the X-Axis and the cumulative score on the Y-Axis and it is a histogram chart where the cumulative score is calculated from the formula explained above.
</br>
![alt text](https://github.com/VasviDesai/StackAnalytica/blob/master/chart2.PNG)


#### Chart 3
The below chart gives a monthly report of the users against the cumulative score. This chart helps in giving an overview of the performance of different users on StackOverflow for a particular language.
</br>
![alt text](https://github.com/VasviDesai/StackAnalytica/blob/master/chart3.PNG)



## Trending Github Repositories
This feature aims to provide the user top 5 trending GitHub repositories for the tag or language the user selected. 
- This feature aims at providing the developer an overview over some highly active repositories on GitHub and also keep the user updated on the trending open source repositories for the language the user selected. 
- Trending repositories update on a daily basis.
- To implement this feature we have used the trending-api-npm package which returns a JSON object on hitting the API endpoint of the package. Implementation of the package can be found here [trending-api-npm](https://github.com/huchenme/github-trending-api).

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
1. "author": This field has the name of the author of the repository "veujs"
2. "name": This represents the repository name "vue"
3. "description": This field denotes a one-line description of the repository "🖖 Vue.js is a progressive, incrementally-adoptable JavaScript framework for building UI on the web."
4. "url": This field holds the link of the GitHub repository "https://github.com/vuejs/vue"

This data is completely dynamic and ingested and updated on the portal as soon as there is any change in any entry of the trending repositories.

Screenshot of the trending GitHub repositories displayed on the portal.
</br>
![alt text](https://github.com/VasviDesai/StackAnalytica/blob/master/Github_Trending.PNG)

## Email Subscription for Trending Questions

This feature aims at providing the users with a list of trending questions for the tag the user selected. 
- Here the portal sends the user email updates based on any interval the user specifies (eg. daily, weekly, monthly) and the portal shall send the user a curated list of top trending question for that particular tag or language.

- To implement this feature we have used EmailJS as our SMTP email client and we send the data in the form of a list in the body of the email to the user.

- Image of the landing page for the email subscription.

![alt text](https://github.com/VasviDesai/StackAnalytica/blob/master/Email_Subscribe.PNG)

- Image of the email received with the list of trending questions.

![alt text](https://github.com/VasviDesai/StackAnalytica/blob/master/Trending_email.png)

# Reflection
- Overall, the project left us with a more detailed and practical knowledge of Agile methodology. Initially, we didn't have much idea but later we found it very helpful to keep track of all the tasks we had divided. Sprint Retrospectives were helpful to know all the hindrances we faced and plan accordingly for the future.
- Learned about creating user stories and prioritizing them, also how to efficiently divide them amongst teammates based on their area of expertise.
- Mainly we learned how to coordinate with the team on a daily basis because of scrum calls
- During these sprints, we learned how to interact with REST APIs and fetch useful data from them. Manipulation of StackOverflow's and GitHub's dynamically fetched data into the charts was one of the most interesting parts of the project.
- We learned to analyze the unstructured data received from REST API's and preprocess them in an appropriate format and generate visualizations and analyze the data in Tableau.
- Due to Tableau Desktop's limitations, we were not able to include Tableau dynamic charts in the portal though we did add a chart with a monthly report of users against their cumulative score. However, we didn't compromise on the services we wanted to provide and thus implemented the daily updating dynamic charts programmatically using javascript framework ChartJS. This part of the project helped us learn data visualization using tools like Tableau and also got a chance to explore the domain of generating dynamic visualizations using programming languages like JavaScript.
- If we could go back in time, we would definitely remove the research part on Tableau which consumed a lot of our efforts and rather focus on improving chartJS interactivity with the user.

# Limitations
Though the portal is completed with all of its core functionalities successfully implemented, we faced some limitations while implementing this part and the same can be covered in the future scope:
- Due to Tableau Desktop's limitations, we were not able to include Tableau charts dynamically. This problem can be solved in the future if we could use a Tableau premium account.
- Due to the free student account on EmailJS which is used under subscription part of the system, we can only send a limited number of emails per day.
- According to StackOverflow API's documentation, if the API requests go beyond 30 per IP in 1 second, they cut the requests. So in future, if we have thousands of user using this portal, we may come across this hurdle.
- As an extension of the scope of our project can include addressing queries formed of sentences using NLP (Natural Language Processing) techniques.
- We could also add support for language frameworks like Java Spring in the future.

# Final Screencast
(Updated based on Feedback provided)
You can access our screencast video from here: [Screencast Link](https://drive.google.com/file/d/1Q9TIG03ocAMnsP1fr4bkJxo0E7icmivY/view?usp=sharing)

# Implementation
You can find our portal's link here: [Portal on Heroku](http://stackanalytica-csc510.herokuapp.com/)
