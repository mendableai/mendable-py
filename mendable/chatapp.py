import os
import requests
import time

class ChatApp:
    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv('MENDABLE_API_KEY')
        if self.api_key is None:
            raise ValueError('No API key provided')
        self.conversation_id = self.start_new_conversation()
        self.history = []
        
    def get_sources(self):
        response = requests.post("https://api.mendable.ai/v0/getSources", json={"api_key": self.api_key}).json()
        if response:
            return response
        else:
            raise Exception('Failed to get sources')

    def delete_source(self, source=None, delete_all=False):
        if not source and not delete_all:
            raise ValueError('Either a source or delete_all must be provided')
        response = requests.post("https://api.mendable.ai/v0/deleteSource", json={"api_key": self.api_key, "source": source, "delete_all": delete_all})
        if response:
            return response
        else:
            raise Exception('Failed to delete source(s)')

    def start_new_conversation(self):
        new_conversation_response = requests.post("https://api.mendable.ai/v0/newConversation", json={"api_key": self.api_key}).json()
        if new_conversation_response.get('conversation_id'):
            return new_conversation_response['conversation_id']
        else:
            raise Exception('Failed to create a new conversation')

    def add(self, _type, url):
        task_id = self._start_ingestion(_type, url)
        while True:
            status = self._check_ingestion_status(task_id)
            if status == 'completed':
                print('Ingestion completed.')
                break
            elif status in ['queued', 'processing', 'pending']:
                print(f'Ingestion status: {status}')
                time.sleep(2.5)
            else:
                raise Exception('Unknown ingestion status')


    def _start_ingestion(self, _type, url):
        # this response can return a 400 error and i want to handle it
        try:
            response = requests.post("https://api.mendable.ai/v0/ingestData", json={"api_key": self.api_key, "url": url, "type": _type})
            # Raise an exception if the request was not successful
            response.raise_for_status()

        except requests.exceptions.HTTPError as err:
            # Check for 400 status code
            if response.status_code == 400:
                print("\n"+response.text+"\n")
            else:
                print('An error occurred: ', err)
            raise Exception('Failed to start data ingestion') 
        response = response.json()
        if response.get('task_id'):
            return response['task_id']
        else:
            raise Exception('Failed to start data ingestion')
        

    def _check_ingestion_status(self, task_id):
        response = requests.post("https://api.mendable.ai/v0/ingestionStatus", json={"task_id": task_id, "api_key": self.api_key}).json()
        status = response.get('status')
        if status:
            return status
        else:
            raise Exception('Failed to check ingestion status')
        

    # Being depricated soon in favor of the new ask() method
    def query(self, question, history=[]):
        response = requests.post("https://api.mendable.ai/v0/mendableChat", json={
            "api_key": self.api_key,
            "question": question,
            "history": history,
            "conversation_id": self.conversation_id,
            "shouldStream": False
        }).json()
        if response.get('answer') and response['answer'].get('text'):
            return response['answer']['text']
        else:
            raise Exception('Failed to send the question or receive an answer')
        
    def ask(self, question, history=[]):
        response = requests.post("https://api.mendable.ai/v0/mendableChat", json={
            "api_key": self.api_key,
            "question": question,
            "history": history,
            "conversation_id": self.conversation_id,
            "shouldStream": False
        }).json()
        if response.get('answer') and response['answer'].get('text'):
            return response
        else:
            raise Exception('Failed to send the question or receive an answer')
    
    def rate_message(self, message_id, message_rating):
        
        response = requests.post("https://api.mendable.ai/v0/rateMessage", json={
            "api_key": self.api_key,
            "message_id": int(message_id),
            "rating_value": message_rating
        })

        if not response.content:
            raise Exception('No content received from the server')

        if response.status_code == 200:
            return "Message Rated"  # Attempt to parse JSON
        else:
            raise Exception(f'Failed to send the question or receive an answer. Status code: {response.status_code}')



    
    
