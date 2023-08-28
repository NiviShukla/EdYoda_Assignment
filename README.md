# EdYoda_Assignment

This is a music sharing app built with Django that allows users to upload music and share it with each other. Users can register on the platform using their email address and log in using their email and password. They can upload music files in different access levels such as public, private, or protected.

## Features

- User Registration: Users can register on the platform using their email address.
- User Login: Users can log in to the platform using their email and password.
- Music File Upload: Users can upload music files to the platform.
- Access Levels:
  - Public Music File: Visible to all users on the platform.
  - Private Music File: Visible only to the user who has uploaded it.
  - Protected Music File: Visible to users who have been granted access via email.
- Protected Music File Details:
  - Users can upload music files as protected and provide a list of email addresses.
  - The system checks if the mentioned email addresses are registered on the platform.
  - If a user with an allowed email address is found, they are granted access to the music file.
- Homepage Display:
  - Upon login, users are shown all the music files they have access to.
  - This includes music files uploaded by the logged-in user, public music files uploaded by other users, and protected files for which the logged-in user has been granted access.
- Access Control:
  - Access to protected music files is based on the logged-in user's email.

## Technologies Used

The following technologies are used to develop this music sharing app:

- Django: Python web framework
- HTML, CSS, JavaScript: Front-end development
- PostgreSQL: Relational database for storing user and music file data

## Installation

To install and run the music sharing app locally, follow these steps:

1. Clone the repository: `https://github.com/NiviShukla/EdYoda_Assignment.git`
2. Navigate to the project directory: `cd music-sharing-app`
3. Create a virtual environment: `python -m venv venv`
4. Install the dependencies: `pip install -r requirements.txt`
5. Set up the database:
   - Update the database settings in the `settings.py` file to match your PostgreSQL configuration.
   - Apply database migrations: `python manage.py migrate`
6. Start the development server: `python manage.py runserver`
7. Open your web browser and visit: `http://localhost:8000`
