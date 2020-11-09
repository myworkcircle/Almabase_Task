# Almabase_Task

A restful api to serve the purpose for fetching data from github.

## Tech/framework used

     python==3.8
     asgiref==3.3.1
     certifi==2020.11.8
     chardet==3.0.4
     Django==3.1.3
     django-environ==0.4.5
     django-rest-framework==0.1.0
     djangorestframework==3.12.2
     idna==2.10
     python-dotenv==0.15.0
     pytz==2020.4
     requests==2.24.0
     sqlparse==0.4.1
     urllib3==1.25.11

# RestApi is hosted at:
http://pallavagarwal.pythonanywhere.com/api/commit/{org}/{n}/{m}/

{org} = organization name
{n} = count of repositories to be entered
{m} = count of commitees required

# In depth overview:

This Django project consists of one App:

    almabase_api

## Rest-API end-point

Get request for the list of members and their respective activity periods.

    api/commit/{organization name}/{value of n}/{value of m}/

**Response:

![microsoft](https://user-images.githubusercontent.com/36321155/98555500-05244a00-22c8-11eb-839b-539e1e974e6c.png)

    
    response starts with the organizaiton name containing repository names containing commitee names and their commit counts
    

    {
        "google": {
        
             "it-cert-automation-practice": {
                 "marga-google": 3,
                 "margamanterola": 1
             },
             "styleguide": {
                 "IsaacG": 15,
                 "tonyruscoe": 10
             },
             "guava": {
                 "cpovirk": 1420,
                 "kluever": 563
             }
    }


# Hosting locally:

     Step-1: Clone the repo to your system.
     
     Step-2: sudo apt install virtualenv
     
     # creating virtual environemnt for the project
     Step-3: $ virtualenv -p python env (or virtualenv -p python3 env , depending on system settings for python)

     Step-4: run $ pip install -r requirements.txt 

     Make sure DEBUG is True for running locally.
     
   #  step-5: create a file with name ".env" in the root directory
   ##           if you have a github personal access token then add two variable inside .env file
              1. username={your_github_usrname}
              2. github_token={your_personal_acess_token}
   ## else
          Remove the headers parameter from the api call
          
     Step-6 Run command: python manage.py makemigrations

     Step-7 Run command: python manage.py migrate

     Step-8 Run command: python manage.py runserver

     step-9 In the url bar enter url example: localhost:8000/api/commit/google/3/2

# API View

Function based API for serving get request.


@api_view()
def commitDetails(request, organization, countOfRepos, countOfCommitees):
    
    here countOfRepos=n and countOfCommitees=m
    #..
    
    
# Important Points:

I have removed .env file as it contains sensitive data for accessing the api.
        
       


