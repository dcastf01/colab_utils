import requests


def download_file_from_google_drive(id: str, destination: str):
    """[download file from google drive]

    Args:
        id (str): [id file of drive ]
        destination (str): [name file]
    """    
    def get_confirm_token(response):
        for key, value in response.cookies.items():
            if key.startswith('download_warning'):
                return value

        return None

    def save_response_content(response, destination):
        CHUNK_SIZE = 32768

        with open(destination, "wb") as f:
            for chunk in response.iter_content(CHUNK_SIZE):
                if chunk:  # filter out keep-alive new chunks
                    f.write(chunk)

    URL = "https://docs.google.com/uc?export=download"
   #URL=" https://docs.google.com/open?export=download"

    session = requests.Session()

    response = session.get(URL, params={'id': id}, stream=True)
    token = get_confirm_token(response)

    if token:
        params = {'id': id, 'confirm': token}
        response = session.get(URL, params=params, stream=True)

    save_response_content(response, destination)

def generate_id_destination_to_download(path_txt:str)->dict:
    """[Generate a dictionary with the id is the key and the name of file the value]

    Args:
        path_txt (str): [name file txt where you have the id and key]

    Returns:
        dict: [id:destination]
    """    
      
  with open(path_txt,"r") as f:
    ids_and_name_file_to_download ={line.split(" ")[0]:line.split(" ")[1].split("\n")[0] for line in f}

  return ids_and_name_file_to_download