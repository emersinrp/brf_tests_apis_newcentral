import pytest
import requests
from dotenv import load_dotenv
import os
from payloads.promotion import generate_promotion_payload
from datetime import datetime

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

HOST = os.getenv('PROMOTION_ENDPOINT')
HEADERS = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
}

def create_promotion():
    payload = generate_promotion_payload()
    response = requests.post(HOST, headers=HEADERS, json=payload)
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    promotion_id = response.text.strip('"')
    assert len(promotion_id) > 0, "Failed to create promotion"
    return promotion_id, payload

@pytest.mark.promotion
def test_create_promotion_response_structure():
    promotion_id, payload = create_promotion()
    assert promotion_id is not None, "Promotion ID should not be None"
    assert len(promotion_id) > 0, "Promotion ID should not be empty"
    # Validação do nome gerado
    assert payload["name"].startswith("TEST AUTOMACAO"), "Promotion name does not start with 'TEST AUTOMACAO'"
