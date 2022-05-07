# CP-TakeItOrLeaveIt

## Description

An app that prompts users to give their 'takes' or opinions based on pop culture moments from the past, present & any future predictions for upcoming events as well. 

## Installation Instructions:
1. Fork and Clone this repository
2. CD into the `CP-TakeItOrLeaveIt` directory
3. Install the needed packages for this project: 
 - This creates the django environment `pipenv shell`
4. Run `python3 manage.py runserver`
5. In your browser of choice type in: 'https://localhost:8000'
6. Signup to create an account to continue through this application
7. Enjoy Take It or Leave It

## Technologies Used:
 - Python
 - Django w/ Templates
 - HTML 
 - CSS
 - Materialize

## User Story:
**As a 'Public' User:**
- Sign Up
- Ability to view all 'Takes' posted by other users(INDEX)
- View specific 'Takes' or posts and view comments left by fellow users(SHOW)

**As a 'Signed In' User**
- Log in
- Create an Event which requires:
    1. An Image
    2. Title of moment
    3. Brief description of the moment
- Create 'Takes' or posts which requires:
    1. An opinion text on said 'Event'
- Leave a like or dislike on a 'take' or post(V2)
- Create comments on other users 'takes' or posts
- Edit a specific post made 
- Delete a specific post made 
- Sign Out

## CRUD Functionality
*Routes for: Events, Takes, & Comments*
| **VERB**| **PATTERN** | **ACTION** | **DESCRIPTION** | **MODEL** |
| ----------- | ----------- | ----------- | ----------- | ----------- |
| GET | /events | Index | All Events | Events |
| GET | events/<int:event_id>/ | Show | Detailed Events Page  | Events |
| POST | /events/create | Create | Creates User Events | Events |
| PUT | events/<int:pk>/update/ | Update | Updates User Events | Events |
| DELETE | events/<int:pk>/delete/| Delete | Deletes a User's specific events| Events |
| ----------- | ----------- | ----------- | ----------- | ----------- |
| GET | events/<int:event_id>/takes/ | Index | Shows all users takes associated with corresponding events | Takes |
| GET | takes/<int:take_id>/| Show | Shows User's takes they've created/Comments creation form | Takes, Comments |
| POST | events/<int:event_id>/takes/create | Create | Creates user's take entry | Takes |
| GET | takes/<int:pk>/update/ | Edit | Edit your specific take entry | Takes |
| DELETE | takes/<int:pk>/delete | Delete | Deletes the users selected take entry | Takes |
| ----------- | ----------- | ----------- | ----------- | ----------- |
| POST | takes/<int:take_id>/comments/ | Show | Shows comments users created for specific take | Comments 


## ERD with Wireframes
- ERD
![alt text](/Images/ERD.jpg)

- Home PAGE
![alt text](/Images/HomePage.png)

- Takes (SHOW)
![alt text](/Images/TAKES.png)

- SIGN-IN/OUT
![alt text](/Images/SIGNIN.png)
![alt text](/Images/SIGNOUT.png)

- Profile
![alt text](/Images/Profile.png)


