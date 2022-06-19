# BrownMunde-Health-NIT
This is a health webapp based on django framework

# ABOUT THIS WEBAPP
# TOPIC: Health

# PROBLEM STATEMENT: 
Develop a website/mobile application showcasing the digitalisation in healthcare and providing solutions for a healthy life.
TEAM MEMBERS: Aniruddha Fale( aniruddha.fale@gmail.com ), Harmit Saini( bmovies52@gmail.com ), Siddharth Singh( sidsinghcs@gmail.com )
TECH STACK: front-end (html,css,js), back-end(django with postgreSQL)

# DESCRIPTION:
We have created a web application pertaining to the given topic. Our project consists of 4 major parts:

1> In case of emergencies Appointments with doctors can be booked via the website. We have created a form for this part and users can input their details and descriptions of the problems
   to be sent to the doctors. If the user is logged in, then the previously booked appointments can also be seen in the user's login dropdown in 'My appointments' section.
   
2> Calorie Tracker: Users can track their calories on a daily basis to judge their health and performance. We store the calories burnt in a day in our databases. If a user doesn't
   how many calories he/she has burnt they can just input what activities they've done and with a help of an API we detect how many calories they have burnt.
   
3> Dashboard: From the calories data we've collected in the last section, We display an interactive chart with the help of plotly that displays the information regarding the calories.
   We have also displayed a table below the graph for further readability.
   
4> Excercise Picker: We've made it easier for users to find exercises based on the muscle groups they are targeting. It is as easy as clicking certain body part on the body image
   shown and it redirects to relevant excercises for the muscle targeted.
   
5> Homepage: Our homepage contains news on various new advancements in health( fetched via a news api ) and also contains daily motivation quotes to encourage fitness within the community.

6> BMI calculator: To judge the fitness level, we have integrated a BMI calculator to our website which displays the BMI and fitness level along with that.


# RUNNING THE PROJECT:
To run our project,

1> first download the files from github into your pc.

2> Navigate to the healthproject folder(containing healthapp,healthproject,templates etc).

3> Open this folder in terminal.

4> Type the command 'python manage.py runserver'.

5> Now the website is live. We can access it by clicking the link displayed in terminal. 

6> In case of an error, try the following commands in order:

   i> 'python manage.py makemigrations'
   
   ii> 'python manage.py migrate'
   
   iii> 'python manage.py runserver'
   
7> Website is now up and running on the local machine and we are free to explore it!

 
# LINK TO THE HOSTED WEBSITE: 
GITHUB REPO: https://github.com/sidsingh0/BrownMunde-Health-NIT/tree/master/healthproject

LINK to website : https://digiaid.herokuapp.com/
 
