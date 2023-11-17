# dreamrealm

Dreamrealm is a Django project that showcases my early understanding of Django, HTML, and CSS. It consists of three apps: dream_realm, realm_forum, and user_auth.

The dream_realm app handles the home page and the albums page. The albums page contains details of J Cole's various albums.

The realm_forum app handles the forums page, which has various forum-related functions such as creating a post, replying to a post, and liking a reply made by the user.

The user_auth app handles all user authentication needed for the project. It allows users to register, log in, and create profiles.

In other words, Dreamrealm is a Django project that allows users to create and view forum threads, as well as view information about J Cole's albums.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [GitHub Repository](#github-repository)
- [Additional Notes](#additional-notes)

- ## Installation

Prerequisites
1. Python: Ensure that you have Python installed on your machine. You can download it from python.org.
   Git:Make sure you have Git installed. You can download it from git-scm.com.
   Pycharm(Recommended but optional) You can install it from https://www.jetbrains.com/help/pycharm/installation-guide.html

Download the zip file from github containing the project clone the project
To Clone the Repository do the Following 
Open your terminal or command prompt.
Clone the repository to your local machine:

2. Virtual Environment (Optional):It's recommended to use a virtual environment to isolate project dependencies. Install virtualenv using: pip install virtualenv


Set Up Virtual Environment (Optional)
Change directory to the project folder:
Create a virtual environment:
Activate the virtual environment:

3. Install Dependencies 
Ensure you are in the project directory and the virtual environment is activated.
Install project dependencies:
pip install -r requirements.txt

4. Apply Database Migrations
Run Django migrations to apply the database schema:
- python manage.py migrate
- python manage.py makemigrations

6. Run the Development Server
Start the Django development server:
python manage.py runserver

Open your web browser and go to http://localhost:8000/ to view the project.


## Usage
When you runserver you will find yourself on the home page below.
![home](https://github.com/EmmanuelMasango/dreamrealm/assets/115074093/f5f72e80-9691-4f2f-950d-a80f3a017409)

As you can see in the footer there are 2 buttons login and register.
Login or register as most functions on this website requrire you to be logged in.

![login](https://github.com/EmmanuelMasango/dreamrealm/assets/115074093/ec8d8652-8530-4357-a2bc-352e6ccd2c0c)

![register](https://github.com/EmmanuelMasango/dreamrealm/assets/115074093/c6923d6c-ccd0-4533-b245-6d5c7e6da160)

Once done you will be redirected to your user page. If you are a new user you can create your user page.
![profile](https://github.com/EmmanuelMasango/dreamrealm/assets/115074093/ca2f3b82-2d2d-4d4c-b852-ab8ead732407)

![updateprofile](https://github.com/EmmanuelMasango/dreamrealm/assets/115074093/2e6dabf1-6578-41c3-9698-c3e7e20fd3db)
Once you have all that completed we can go to access and interact with the albums and forums page. You can access the albums page from the navigation panel at the top of your page. You can select albums to view more details on the album.
![albumspage](https://github.com/EmmanuelMasango/dreamrealm/assets/115074093/b66d8e4f-b465-4715-8f9c-3282a49885ca)

You can access the forums page by going back to the home page and clicking on the forums button. on the forums page you will have the option to view posts, create posts and replay to posts. 
![Screenshot 2023-11-11 170407](https://github.com/EmmanuelMasango/dreamrealm/assets/115074093/ec0f91b8-36bd-4b68-ad61-262d41c80332)

## GitHub Repository

Repository: dreamrealm
[https://github.com/EmmanuelMasango/dreamrealm](https://github.com/EmmanuelMasango/dreamrealm/tree/master)

## Additional Notes 
Dreamrealm project is stored in master branch 
