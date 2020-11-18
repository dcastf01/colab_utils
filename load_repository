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
def upload_credential():
  global GIT_USERNAME
  global GIT_EMAIL
  global GIT_TOKEN
  global GIT_REPOSITORY
  global PROJECT_PATH
  
  uploaded = files.upload()
  
  for file_with_credential in uploaded.keys():
    print('User uploaded file "{name}" with length {length} bytes'.format(
        name=file_with_credential, length=len(uploaded[file_with_credential])))
  import json

  with open(file_with_credential, "r") as content:
    credential=json.load(content)

  GIT_USERNAME=credential["GIT_USERNAME"]
  GIT_EMAIL=credential["GIT_EMAIL"]
  GIT_TOKEN=credential["GIT_TOKEN"]
  GIT_REPOSITORY=credential["GIT_REPOSITORY"]
  PROJECT_PATH=credential["PROJECT_PATH"]

  !git config --global user.email $GIT_EMAIL
  !git config --global user.name $GIT_USERNAME

  !git clone https://$GIT_USERNAME:$GIT_TOKEN@github.com/$GIT_USERNAME/$GIT_REPOSITORY
  
def do_commit():
  %cd /content/$GIT_REPOSITORY
  !git add .
  !git commit -m 'add imports'
  !git push origin master 
  %cd /content
