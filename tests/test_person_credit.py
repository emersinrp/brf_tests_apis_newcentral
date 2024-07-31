import os
from payloads.person_credit import PERSON_CREDIT_QUERY, get_person_credit_variables
from helpers.rules import handle_request

def test_person_credit(self):
    endpoint = os.getenv('PERSON_CREDIT_ENDPOINT')
    headers = {
        'Content-Type': 'application/json',
    }
    payload = {
        'query': PERSON_CREDIT_QUERY,
        'variables': get_person_credit_variables()
    }
    
    handle_request(self.client, endpoint, headers, payload, "test_person_credit", "Person credit GraphQL")
