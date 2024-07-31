import json
from locust import HttpUser, task, between
from dotenv import load_dotenv
import os
from payloads.person_credit import PERSON_CREDIT_QUERY, PERSON_CREDIT_VARIABLES
from helpers.rules import handle_request

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

class GraphQLUser(HttpUser):
    wait_time = between(1, 5)
    host = os.getenv('HOST')
    
    @task
    def test_person_credit(self):
        endpoint = os.getenv('PERSON_CREDIT_ENDPOINT')
        headers = {
            'Content-Type': 'application/json',
        }
        payload = {
            'query': PERSON_CREDIT_QUERY,
            'variables': PERSON_CREDIT_VARIABLES
        }
        
        handle_request(self.client, endpoint, headers, payload, "test_person_credit")
