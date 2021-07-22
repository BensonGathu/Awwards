# Awwards Clone
#### By Benson Gathu
# Description
This project allows users to post their projects for other users to rate according to design, usability and content.
## Live Link
[https://award96.herokuapp.com/](link)

## User Story
- A user can view posted projects and their details.
- A user can post a project to be rated/reviewed.
- A user can rate/ review other users' projects.
- Search for projects.
- View projects overall score.
- A user can view their profile page.
## System Features
* Projects should have a Title, an image of the project's landing page, a detailed description of the project, a link to the live site.
* Your project should have a user profile that at least the following information:

- Profile picture of the user
- User Bio
- Projects the user has posted
- A contact information of the user
* Your application should have a solid authentication system that allows users to sign up or log in to the application before posting or rating a project.
* Projects will be rated/reviewed based on the following criteria:

- Design - This is the overall appearance of the project
- Usability - This can be translated to the user experience and how responsive the project is.
- Content - This includes the technologies used, the font used(is it uniform throughout the project) and grammar
* These criteria will each be rated/review on a scale of 1-10 and the overall score will be their average
* You should create an API so that users can access data from your application. You can create two API endpoints:

- Profile - This endpoint should return all the user profiles with information such as the username, bio, projects of the user and profile picture
- Projects- This endpoint should return information pertaining to all the projects posted in your application.
## Technical Requirements
* Create a specs markdown file that lists down all the projects specifications.
* All your models should contain unit tests to test the different behaviours. All your test should pass.
* Your project should follow the proper folder structure.
* Your project should be deployed to Heroku.
* Your project should contain proper commit messages.
## Technology used
- Django 3.0.6
- Heroku
## License
Copyright (c) [2021] [Benson Gathu]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.