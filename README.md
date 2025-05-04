# finalprojectJoseSaumat

### INF601 - Advanced Programming in Python
### Jose Saumat
### Final Project


# Final Project 4

## Description

This project will be combine ideas found in miniproject 3 and 4, into a fully functioning community website/app.

## Getting Started

First, clone the repository into your preferred IDE. Make sure to also create a virtual environment for the project if 
your IDE does not automatically create one for you.

### Dependencies

Step 1: Install required packages using the requirements.txt file. Copy and paste the code below into the terminal.

```
pip install -r requirements.txt
```
Step 2: Follow the steps below to initialize the SQL database. Create a Super User. Copy and paste the code below into the terminal.

Keep in mind that when you create the superuser, when you get to the password part, it will not show you
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
Step 5: Set up the site voting

You will want to add a few movies or TV shows to the voting page. To do this, go to the Add Movie/TV Show tab and in the search bar enter
some of your favorite TV shows or movies. Then click the 'add' button. You will get a prompt saying that your choice was added to the list.
This will allow you and the users to use the voting features which make the leaderboard work.

Step 6: Set up the forum

Set up the forum. As an admin, you can add categories and forums for your users. You want to add those in that specific order. You can then
create topics or leave that for your users to start.

### Output

Once everything is set up...

This website should start with an age verification modal. If you are not 18, it will take you to Google.com. If you are 18, it will take you to the Home Page.

For The Regular User:

You may access the following:

- Home page: view my top 10 favorite movies and TV shows, each card is a link to a trailer. 

- About page: contains a brief description of the site along with credit for TMDB's use of their API with their logo, which doubles as a link to their site.

- Movie Voting page: Shows community votes. To vote or add a movie for voting, you must register and be logged in. If you try to vote before you are logged in, 
a modal will appear asking you to log in for voting.

- Leaderboard page: Shows the communities top 10 favorite movies and TV shows. Also displays other titles that have likes, but are not in the top 10 of either category.

- Forum page: Shows discussions about movies and TV shows between users. Anyone can read the forum. To participate in discussions, you must be registered and logged in.

- Login page: Allows users to log in.

- Registration page: Allows users to register for the site.

- Logged Out page: Confirms the user is logged out.

- Quick Search: Anyone may use the quick search on the navigation bar. This uses TMDB's database to search for movies and TV shows. It will not add anything to the voting page.

Once logged in...

- Add Movie / TV page: This page allows the user to add a movie or TV show to the voting page for the community to vote on.

For Admin User:

You have access to everything above, and...

- Admin page: Here you can control everything. Add and remove from the forum and voting page. Add or remove the media content on the site. Assign other trusted users staff powers. Start polls for the community.

You can also remove movies/tv shows from the voting list. 

You can also edit or remove user posts or topics in the forums.


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