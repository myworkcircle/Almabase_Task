# Almabase_Task

A restful api to serve the purpose for fetching data from github.

## Tech/framework used

     Python==3.8.5
     Django==3.1.3
     django-rest-framework==0.1.0
     djangorestframework==3.12.2
     django-environ==0.4.5

# RestApi is hosted at:- http://pallavagarwal.pythonanywhere.com/api/commit/{org}/n/m/

In depth overview:

This Django project consists of one App:

    almabase_api

## Rest-API end-point

Get request for the list of members and their respective activity periods.

    api/commit/{organization name}/{value of n}/{value of m}/

**Response:

![microsoft](https://user-images.githubusercontent.com/36321155/98555500-05244a00-22c8-11eb-839b-539e1e974e6c.png)

    
    response starts with the organizaiton name then commiteees name with their commit counts
    

    {
        "microsoft": {
            "vscode": {
                "bpasero": 8569,
                "jrieken": 6678,
                "joaomoreno": 6457,
                "mjbvz": 5334,
                "isidorn": 4903,
                "sandy081": 4814,
                "alexdima": 4671,
                "Tyriar": 3119,
                "aeschli": 2982,
                "roblourens": 2667,
                "rebornix": 2162,
                "weinand": 1024,
                "chrmarti": 984,
                "alexr00": 967,
                "sbatten": 888,
                "dbaeumer": 775,
                "ramya-rao-a": 757
            },
            "TypeScript": {
                "ahejlsberg": 2911,
                "sheetalkamat": 1899,
                "andy-ms": 1707,
                "sandersn": 1626,
                "DanielRosenwasser": 1608,
                "mhegazy": 1324,
                "weswigham": 1271,
                "rbuckton": 1083,
                "vladima": 1022,
                "CyrusNajmabadi": 958,
                "RyanCavanaugh": 596,
                "JsonFreeman": 498,
                "csigs": 493,
                "a-tarasyuk": 313,
                "amcasey": 309,
                "andrewbranch": 278,
                "typescript-bot": 240
            },
            "Windows-universal-samples": {
                "oldnewthing": 79,
                "ontx": 1,
                "supratiksen": 1,
                "turolla": 1
            },
            "terminal": {
                "DHowett": 327,
                "zadjii-msft": 273,
                "miniksa": 208,
                "carlos-zamora": 117,
                "j4james": 67,
                "cinnamon-msft": 49,
                "leonMSFT": 35,
                "skyline75489": 30,
                "PankajBhojwani": 22,
                "lhecker": 20,
                "bitcrazed": 17,
                "greg904": 14,
                "mkitzan": 12,
                "waf": 12,
                "ZoeyR": 11,
                "jsoref": 10,
                "metathinker": 10
            },

}


# Hosting locally:

     Step-1: Clone the repo to your system.

     Step-2: run $ virtualenv -p python env (or virtualenv -p python3 env , depending on system settings for python)

     Step-3: run $ pip install -r requirements.txt 

     Make sure DEBUG is True for running locally.
     
     step-4: create a .env file in the root directory and inside .env
              if you have a github personal access token then add two variable inside .env file
              1. username={your_github_usrname}
              2. github_token={your_personal_acess_token}
              
     Step-7 Run command: python manage.py makemigrations

     Step-8 Run command: python manage.py migrate

     Step-10 Run command: python manage.py runserver

     step-11 In the url bar enter url localhost:8000/api/commit/{org}/n/m

# API View

Function based API for serving get request.


@api_view()
def commitDetails(request, organization, countOfRepos, countOfCommitees):
    
    here countOfRepos=n and countOfCommitees=m
    #..
        
       


