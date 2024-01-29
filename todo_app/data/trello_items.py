import requests
import os
from todo_app.data import Item

def get_key_token_params():
    return { 'key': os.getenv('API_KEY'), 'token': os.getenv('API_TOKEN') }
    return token

def build_params(params = {}):
    full_params = get_key_token_params()
    full_params.update(params)
    return full_params

def build_url(endpoint):
    return os.getenv('TRELLO_BASE_URL') + endpoint

def get_items():
    """
    #Fetches all saved items from Trello.

    Returns:
        list: The list of Trello items.
    """
    key=str(os.getenv('API_KEY'))
    token=str(os.getenv('API_TOKEN'))
    board_id = os.getenv('BOARD_ID')
    url = f"https://api.trello.com/1/boards/{board_id}/lists?cards=open&key={key}&token={token}"

    response = requests.get(url=url)
    responseList = response.json()
    
    
    items=[]
    for trello_list in responseList:
      for trello_card in trello_list['cards']:
        item_from_trello_card = Item.Item.from_trello_card(trello_card, trello_list)
        
        items.append(item_from_trello_card)
    
    return items
    

def get_lists():
    """
    Fetches the the lists from Trello.

    Returns:
        list: The list of Trello Lists.
    """
    key=str(os.getenv('API_KEY'))
    token=str(os.getenv('API_TOKEN'))
    board_id = os.getenv('BOARD_ID')
    
    url = f"https://api.trello.com/1/boards/{board_id}/lists?cards=open&key={key}&token={token}"
    response = requests.get(url=url)
    responseList = response.json()
    return responseList

# Get a list with a specified name
def get_list(name):
    lists = get_lists()
    for list in lists :
        if list['name'] == name :
            return list 
        
def get_item(id):
    """
    Fetch a single card from Trello

    Returns:
        Dictionary: The Trello card requested.
    """
    key=str(os.getenv('API_KEY'))
    token=str(os.getenv('API_TOKEN'))
    board_id = os.getenv('BOARD_ID')
    
    url = f"https://api.trello.com/1/boards/{board_id}/lists?cards=open&key={key}&token={token}"
    response = requests.get(url=url)
    card = response.json()
    return card

def add_item(item):
    """
    Adds a Trello card

   
    """
    key=str(os.getenv('API_KEY'))
    token=str(os.getenv('API_TOKEN'))
    board_id = os.getenv('BOARD_ID')

    url = "https://api.trello.com/1/cards"
    headers = {
      "Accept": "application/json"
    }
    query = {
      'key': key,
      'token': token,
      'name' : item['name'],
      'idList' : item['idList']
      
      }

    response = requests.request(
      "POST",
      url,
      params=query
    )
    

    
def save_item(item):
    """
    Updates a Trello card

   
    """
    board_id = os.getenv('BOARD_ID')
    key=str(os.getenv('API_KEY'))
    token=str(os.getenv('API_TOKEN'))
    url = "https://api.trello.com/1/cards/"+item['id']
    
    headers = {
      "Accept": "application/json"
    }

    query = {
      'key': key,
      'token': token,
      'name' : item['name'],
      'idList' : item['status']
    
    }

    response = requests.request(
      "PUT",
      url,
      headers=headers,
      params=query
    )

def delete_item(id):
    """
    Deletes a Trello card

   
    """
    url = "https://api.trello.com/1/cards/"+id
    key=str(os.getenv('API_KEY'))
    token=str(os.getenv('API_TOKEN'))
    board_id = os.getenv('BOARD_ID')
    
    query = {
      'key': key,
      'token': token,
      }

    response = requests.request(
      "DELETE",
      url,
      params=query
    )

# start a item with a id, and move the item from to_do to doing
def start_item(id):
    doing_list = os.getenv('DOING_LISTID')
    card = move_card_to_a_list(id, doing_list)
    return 

# done a item with id, and move the item from doing to done
def complete_item(id):
    done_list = os.getenv('DONE_LISTID')
    card = move_card_to_a_list(id, done_list)
    return 

# this function to move item from one list to another list
def move_card_to_a_list(card_id, list_id):
    params = build_params({ 'idList': list_id })
    url = build_url('cards/' + card_id)
    response = requests.put(url, params = params)
    return  response.json()