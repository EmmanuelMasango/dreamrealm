# dreamrealm
Dreamrealm is a Django project that showcases early understanding of Django, HTML, and CSS. It consists of three apps: `dream_realm`, `realm_forum`, and `user_auth`.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Repository Links](#repository-links)
- [Additional Notes](#additional-notes)

## Installation

### Prerequisites

1. **Python**: Ensure that you have Python installed on your machine. [Download Python](https://www.python.org/downloads/).
2. **Git**: Make sure you have Git installed. [Download Git](https://git-scm.com/downloads).
3. **Docker**: Install Docker on your machine. [Download Docker](https://www.docker.com/products/docker-desktop).
4. **PyCharm (Optional but recommended)**: [Install PyCharm](https://www.jetbrains.com/help/pycharm/installation-guide.html).

### Download and Setup
#### Using Venv(Optional)
1. **Clone the Repository:**
   ```In bash
   git clone https://github.com/EmmanuelMasango/dreamrealm.git

   cd dreamrealm
   virtualenv venv

   For Windows: .\venv\Scripts\activate
   For Linux/Unix source venv/bin/activate
   
   pip install -r requirements.txt

2. **Apply Database Migrations:**
   ```In bash
   python manage.py migrate
   python manage.py makemigrations

3. **Run the devlopment server:**
   ```In bash
   python manage.py runserver

Open your web browser and go to http://localhost:8000/ to view the project.

#### Using Docker
1. **Run with Docker (Alternative):**
    ```In bash
    docker build -t dreamrealm:latest .

    docker run -p 8000:8000 dreamrealm:latest

Open your web browser and go to http://localhost:8000/ to access the Dreamrealm Django project running in the Docker container.

## Usage

1. After running the server, find yourself on the home page.
2. In the footer, there are login and register buttons. Login or register as most functions require you to be logged in.
3. Once logged in, you will be redirected to your user page. If you are a new user, create your user page.
4. Access and interact with the albums and forums page from the navigation panel.

![Screenshot 2023-11-11 165906](https://github.com/EmmanuelMasango/dreamrealm/assets/115074093/fd6a4c8c-01d9-48a3-a7fe-4a3fe9fa2605)

![Screenshot 2023-11-11 165951](https://github.com/EmmanuelMasango/dreamrealm/assets/115074093/6016fc96-252a-4e97-908f-2ab496a4f3dc)

![Screenshot 2023-11-11 170045](https://github.com/EmmanuelMasango/dreamrealm/assets/115074093/4bbea7fa-aa78-4324-99b4-4d66cc3572e3)

![updateprofile](https://github.com/EmmanuelMasango/dreamrealm/assets/115074093/8df2a34c-f4d4-49c7-a1b3-93d3a1b2884c)

![profile](https://github.com/EmmanuelMasango/dreamrealm/assets/115074093/bc26a40c-bb46-4a2d-afa0-db5f94489d22)

### Albums Page
Navigate to the albums page from the top navigation panel.
Select albums to view more details on each album.

### Forums Page
Go back to the home page and click on the forums button in the navigation panel.
On the forums page, you can view posts, create posts, and reply to posts.

![albumspage](https://github.com/EmmanuelMasango/dreamrealm/assets/115074093/4003bcac-8563-4e71-9270-8a8b70009cd5)

![Screenshot 2023-11-11 170407](https://github.com/EmmanuelMasango/dreamrealm/assets/115074093/94330c60-62bc-4223-a4c5-94950c57ea83)


## Repository Links

Repository: dreamrealm
[https://github.com/EmmanuelMasango/dreamrealm](https://github.com/EmmanuelMasango/dreamrealm)
[https://hub.docker.com/repository/docker/emmanuelmasango/dreamrealm/general](https://hub.docker.com/repository/docker/emmanuelmasango/dreamrealm/general)

## Additional Notes 
Dreamrealm project is stored in master branch 
