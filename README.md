# finalprojectJoseSaumat

### INF601 - Advanced Programming in Python
### Jose Saumat
### Final Project


# Mini Project 4

## Description

This project will be combine ideas found in miniproject 3 and 4, into a fully functioning community website/app.

## Getting Started

First clone the repository into your preferred IDE. Make sure to also create a virtual environment for the project if 
your IDE does not automatically create one for you.

### Dependencies

Step 1: Install required packages using the requirements.txt file. Copy and paste the code below into the terminal.

```
pip install -r requirements.txt
```
Step 2: Follow the steps below in order to initialize the SQL database. Create a Super User. Copy and paste the code below into the terminal.

Keep in mind that when you create the super user, when you get to the password part, it will not show you
the password you are typing in. It will appear blank. However, it is actually taking in your password.
So, just go with it.

A. This will create any SQL entries that need to go into the database
```
python manage.py makemigrations

```
B. This will apply the migrations
```
python manage.py migrate
```

C. This will create the administrator login for your /admin side of the app
```
python manage.py createsuperuser
```

### Executing program

Step 3: Run the program. Copy and paste the code below into the terminal.

```
python manage.py runserver

or

Click the Play button in your IDE.
```

Step 4: In your terminal you should now see a hyperlink with the address below. Click that link to launch the website in browser,
or paste the line below into a browser.

```
http://127.0.0.1:8000
```
Step 5: Set up the site for regular users

When you first access the site, the Home page movie gallery will not have any movies to vote on. You will need to log in as the super user/admin, then click on 'Add Movie' in the navigation bar. This will take you to a page that says 'Import Movie'. Type in the name of
a favorite movie you have seen, and then click on 'Import'. This will add a movie that can be voted on by all users on the home page.

If you need ideas, you can use the search bar on the far right of the navigation bar. This search bar allows all users to look up
movies using the TMDB API. 

### Output

Once everything is set up...

For The Regular User:

This website should take you to the home page where you should be able to vote on movies. In order to vote, you must register and be 
logged in. If you try to vote before you are logged in, a modal will appear asking you to log in for voting. The site also contains a 
fully functional registration, log in, and logged out page. You can also read the About page which contains a brief description of the 
site along with credit for TMDB's use of their API, and it doubles as a link to their site. The search bar in the navigation menu allows 
you to use TMDB's API to search for movies in their API without adding them to the home page for voting.

For Admin User:

You have access to everything above, but you also gain access to the Add Movie and Admin pages. The Add Movie page will allow you
to add movies that the regular users can vote on. The Admin Panel page will let you see a list of movies, the users, and set access 
for different groups.

## Authors

Contributors names and contact info

- Jose Saumat
- Jason Zeller (via Tutorials)
- Bro Code (via Tutorial)
- Selmi Tech (via Tutorial)

## Acknowledgments

Inspiration, code snippets, etc.
* [Jason Zeller](https://www.youtube.com/watch?v=lo5atoJdNX8)
* [Jason Zeller](https://www.youtube.com/watch?v=piyfP2NLp9A)
* [Jason Zeller](https://www.youtube.com/watch?v=UB7XFf0Q_M4)
* [Jason Zeller](https://www.youtube.com/watch?v=lSqCJqnwCb8&list=PLE5nOs3YmC2RqZfmOSoOM4iqmed2pudrg&index=17)
* [Jason Zeller](https://www.youtube.com/watch?v=KPx2F812vGc&list=PLE5nOs3YmC2RqZfmOSoOM4iqmed2pudrg&index=20)
* [Jason Zeller](https://www.youtube.com/watch?v=VHkIzFJCU-0&list=PLE5nOs3YmC2RqZfmOSoOM4iqmed2pudrg&index=20)
* [BootStrap](https://getbootstrap.com/docs/4.0/components/modal/)
* [Bro Code Lamda Tutorial](https://www.youtube.com/watch?v=IljPHDyBRog)
* [Selmi Tech Django Forum Tutorial](https://www.youtube.com/watch?v=YXmsi13cMhw)

API and Package documentation
* [TMDB API](https://www.themoviedb.org/)
* [Django](https://docs.djangoproject.com/en/5.2/intro/tutorial01/)
* [Django](https://www.w3schools.com/django/)
* [Jinja](https://jinja.palletsprojects.com/en/stable/)
* [Bootstrap](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
* [W3 Schools HTML](https://www.w3schools.com/html/default.asp)
* [W3 Schools CSS](https://www.w3schools.com/css/default.asp)
* [W3 Schools Lambda](https://www.w3schools.com/python/python_lambda.asp)