import streamlit as st
from github import Github
import re
from git import Repo
import git


st.title("Git Commit App")

#TODO Insert File directory location here
repo = Repo("Insert file directiory of project here")


#TODO Insert GitHub aceess token here inside quotes
access_token = "Insert Access Token here"
# using an access token
g = Github("access_token")

# Github Enterprise with custom hostname
g = Github(base_url="https://github.com/api/v3", login_or_token="access_token")



#git add
st.write("Step 1. git add -A  is a command that adds all changes to a space that behaves like a container, click button below to add your changes")
result = st.button("git add -A")

st.write(result)

if result:
    # to add all the working files.
    repo.git.add('--all')




#git commit
st.write("Step 2. git commit -m is the command that then takes that container and puts a message on it to create a commit(commit message would go in quotes following the command in terminal)")
st.write("(if error occurs make sure all changes in your file are saved)")

message = st.text_input("Write Commit Message here")
result = st.button("git commit -m ")

st.write(result)

if result:
    repo.git.add('--all')
    repo.git.commit('-m', message)


#git push
st.write("Step 3. git push is the command that sends your commit to GitHub and updates your repository with your changes")
result = st.button("git push")

st.write(result)

if result:
    origin = repo.remote(name='origin')
    origin.push()



#git log
st.write("click here to see your current list of commits")
result = st.button("Commit History")

st.write(result)

if result:
    #TODO insert access token here
    access_token = "Insert Access Token here"
        # using an access token
    g = Github(access_token)

    #TODO insert ("Github Username/GitHub Repo title")
    repo = g.get_repo("GitHub Username/GitHub Repo Title")
    commits = repo.get_commits()
    for commit in commits:
        st.write("Commit: ", commit.commit.message)
        st.write("Author: ", commit.author.login)
        st.write("______________________________")
