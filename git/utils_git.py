'''
Load a json with the next format and download the repository and you can do commit too 

{
    "GIT_USERNAME": "username",
    "GIT_EMAIL":"email",
    "GIT_TOKEN": "token_of_repository",
    "GIT_REPOSITORY":"name_repository",
    "PROJECT_PATH": "project_path"
     
     }
     
'''


from google.colab import files
import os
import subprocess 
import json
def upload_credential_and_create_env_variables():

  
  uploaded = files.upload()
  
  for file_with_credential in uploaded.keys():
    print('User uploaded file "{name}" with length {length} bytes'.format(
        name=file_with_credential, length=len(uploaded[file_with_credential])))

  with open(file_with_credential, "r") as content:
    credential=json.load(content)

  print( "creating env variables")
  GIT_USERNAME=credential["GIT_USERNAME"]
  os.environ["GIT_USERNAME"]=GIT_USERNAME
  GIT_EMAIL=credential["GIT_EMAIL"]
  os.environ["GIT_EMAIL"]=GIT_EMAIL
  GIT_TOKEN=credential["GIT_TOKEN"]
  os.environ["GIT_TOKEN"]=GIT_TOKEN
  GIT_REPOSITORY=credential["GIT_REPOSITORY"]
  os.environ["GIT_REPOSITORY"]=GIT_REPOSITORY
  PROJECT_PATH=credential["PROJECT_PATH"]
  os.environ["PROJECT_PATH"]=PROJECT_PATH
  print("variables created")
   
def download_repository():
  command="bash /content/colab_utils/git/download_repository.sh"
  try:
    subprocess.run(command.split())
    print("The repository is ready")
  except:
    print("we have a problem, analyze")

def do_commit(commit_text="update repository"):
    os.environ["COMMIT_TEXT"]=commit_text
    command="bash /content/colab_utils/git/do_commit.sh"
    try:
        subprocess.run(command.split())
        print("The commit is ok")
  except:
        print("we have a problem, analyze")
