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
def upload_credential():

  
  uploaded = files.upload()
  
  for file_with_credential in uploaded.keys():
    print('User uploaded file "{name}" with length {length} bytes'.format(
        name=file_with_credential, length=len(uploaded[file_with_credential])))



  with open(file_with_credential, "r") as content:
    credential=json.load(content)


  print( "set env variables")
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
  command="bash /content/colab_utils/git/download_repository.sh"
  subprocess.run(command.split())

# def do_commit():
#   %cd /content/$GIT_REPOSITORY
#   !git add .
#   !git commit -m 'add imports'
#   !git push origin master 
#   %cd /content
