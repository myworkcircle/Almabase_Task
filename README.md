# Almabase_Task

A restful api to serve the purpose for fetching data from github.

## Tech/framework used

     Python==3.8.5
     Django==3.1.3
     django-rest-framework==0.1.0
     djangorestframework==3.12.2
     django-environ==0.4.5





## Currently Hosted at PythonAnywhere server: http://pallavagarwal.pythonanywhere.com/fetch/



In depth overview:

This Django project consists of one App:

    almabase_api

## Rest-API end-point

Get request for the list of members and their respective activity periods.

    api/commit/{organization name}/{value of n}/{value of m}/

**Response:

![Screenshot](microsft.png)
    
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


Hosting locally:

Step-1: Clone the repo to your system.

Step-2: run $ virtualenv -p python env (or virtualenv -p python3 env , depending on system settings for python)

Step-3: run $ pip install -r requirements.txt 

Make sure DEBUG is True for running locally.

Step-7 Run command: python manage.py makemigrations

Step-8 Run command: python manage.py migrate

Step-9 Run command: python manage.py populate 10

Step-10 Run command: python manage.py runserver

Steps for Cloud services in this case hosted on PythonAnywhere

    Make sure DEBUG is False
    ALLOWED_HOST is configured according to usecase
    command: python manage.py collectstatic for collecting all the static files in the folder mentioned in STATIC_ROOT

# API View

Function based API for serving get request.


@api_view()
def commitDetails(request, organization, countOfRepos, countOfCommitees):
    
    here countOfRepos=n and countOfCommitees=m
    #..
        
       


