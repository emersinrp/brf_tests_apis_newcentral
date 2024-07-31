import os
from payloads.person_delivery_window import PERSON_DELIVERY_WINDOW_QUERY, get_person_delivery_window_variables
from helpers.rules import handle_request

def test_person_delivery_window(self):
    endpoint = os.getenv('PERSON_DELIVERY_WINDOW_ENDPOINT')
    headers = {
        'Content-Type': 'application/json',
    }
    payload = {
        'query': PERSON_DELIVERY_WINDOW_QUERY,
        'variables': get_person_delivery_window_variables()
    }
    
    handle_request(self.client, endpoint, headers, payload, "test_person_delivery_window", "Person delivery window GraphQL")
