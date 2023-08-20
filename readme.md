The making of this test project has made some assumptions which are as follow
- the user management system works by creating 3 groups namely Super Admin, Admin and User which are manually created in the Admin Web Interface of the server
- the registration page by default adds all accounts to the User group which only gives them View permission 
- For getting added to Super Admin or Admin, Super Admin's Admin Interface is required which can be improved upon in the future

To start the project:
- First clone it
- install the required packages with 'pip install -r requirements.txt'
- make migrations and migrate
- create a super user and log in with it
- create the 3 groups 'Super Admin', 'Admin', 'User'
- add the current admin to the Super Admin group
- visit the site to see the project