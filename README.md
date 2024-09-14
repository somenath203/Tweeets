# Tweeets

## Demo video of the application

https://www.youtube.com/watch?v=9J0202Y7sLk

## Introduction

**Tweeets** is a simple web application that allows users to create, edit, and delete tweets. Each tweet consists of a description, and optionally, an image. Users can also view tweets created by other users. 
To interact with the application (create, edit, or delete tweets), users must first authenticate themselves first.

## Features of the Application

- **Create a Tweet**: Users can create a tweet with a description and optionally upload an image to accompany the tweet.
  
- **View Tweets**: All users (both authenticated and unauthenticated) can view tweets created by others on the platform.
  
- **Edit a Tweet**: Users can edit their previously created tweets if they want to make changes.
  
- **Delete a Tweet**: Users have the option to delete their own tweets if they no longer wish them to be visible.
  
- **User Authentication**: Users must authenticate themselves to create, edit, or delete tweets. Without authentication, they can only view tweets posted by others.

## Technologies Used

- **Django**: Used as the main web framework for building the application.
  
- **Jinja Templating Engine**: Provides the structure for the front-end, rendering dynamic content on the pages.
  
- **SQLite3 (db.sqlite3)**: A lightweight database used to store tweets and user information.
  
- **Django.contrib.auth**: Django's built-in authentication system for managing user logins, registrations, and session management.

- **Django Tailwind**: Integrated Tailwind CSS for styling the application, enabling modern and responsive design with utility-first classes..
