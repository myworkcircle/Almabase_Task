from django.shortcuts import render
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import APIException,ParseError,NotFound
import os
import  environ
env = environ.Env()
# reading .env file
environ.Env.read_env()

github_token = os.getenv("github_token")
username = os.getenv("username")

headers = {
            "Accept": "application/vnd.github.v3+json",
            "username": username,
            "Authorization":github_token
        }

#function to fetch count of commits of commitees from specified organization
@api_view()
def commitDetails(request, organization, countOfRepos, countOfCommitees):
    
    #url  to fetch repositories of organization in descending order of forks
    forksUrl = "https://api.github.com/search/repositories?q=org:"+organization+"+sort:forks-desc"

    repositoryData = requests.get(forksUrl,headers=headers).json()
    organizationRepositories = repositoryData["items"]

    output = {}
    
    # for avoiding overflows, when input value is greater then number of repositories
    countOfRepos = min(countOfRepos,len(organizationRepositories))

    # iterating for each repository
    for repository in range(countOfRepos):
        repo_name = organizationRepositories[repository]["name"]

        #url for fetching commit details of contributors
        commitUrl = "https://api.github.com/repos/"+organization+"/"+repo_name+"/stats/contributors?q=total+sort:desc"
        
        commiteesDetail = requests.get(commitUrl,headers=headers).json()
        
        #avoiding case:- when contributors are less than countOfCommitees required
        numberOfcontributors = len(commiteesDetail)
        limit = max(-1,numberOfcontributors - countOfCommitees-1) 

        #dict to store commitee_name and commit counts
        commiteeInfo = {}

        #iterating for each commitee
        for commitee in range(numberOfcontributors-1,limit,-1):
            commiteeInfo[commiteesDetail[commitee]["author"]["login"]] = commiteesDetail[commitee]["total"]

        output[repo_name] = commiteeInfo

    return Response({organization : output})
