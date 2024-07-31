import pytest
import requests
from dotenv import load_dotenv
import os
from payloads.person_delivery_window import PERSON_DELIVERY_WINDOW_QUERY, get_person_delivery_window_variables

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

HOST = os.getenv('HOST')
DELIVERY_WINDOW_ENDPOINT = os.getenv('PERSON_DELIVERY_WINDOW_ENDPOINT')
HEADERS = {
    'Content-Type': 'application/json',
}

@pytest.mark.person_delivery_window
def test_person_delivery_window_response_structure():
    """
    Teste de validação da estrutura da resposta da API de delivery window.
    """
    payload = {
        'query': PERSON_DELIVERY_WINDOW_QUERY,
        'variables': get_person_delivery_window_variables()
    }

    response = requests.post(f"{HOST}{DELIVERY_WINDOW_ENDPOINT}", headers=HEADERS, json=payload)
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"

    response_json = response.json()
    data = response_json.get('data')
    assert data is not None, "Data is missing"

    get_person_delivery_window = data.get('get_person_delivery_window')
    assert get_person_delivery_window is not None, "get_person_delivery_window is missing"

    items = get_person_delivery_window.get('items')
    assert isinstance(items, list), "items should be a list"
    
    if len(items) == 0:
        pytest.skip("items list is empty")

    for item in items:
        assert isinstance(item, dict), "Each item should be a dictionary"
        assert 'customer_shared_id' in item, "customer_shared_id is missing"
        assert isinstance(item['customer_shared_id'], str), "customer_shared_id should be a string"

        assert 'delivery_windows' in item, "delivery_windows is missing"
        assert isinstance(item['delivery_windows'], list), "delivery_windows should be a list"

        for window in item['delivery_windows']:
            assert isinstance(window, dict), "Each delivery window should be a dictionary"
            assert 'allowed_low_shelf_life' in window, "allowed_low_shelf_life is missing"
            assert isinstance(window['allowed_low_shelf_life'], bool), "allowed_low_shelf_life should be a boolean"

            assert 'delivery_date' in window, "delivery_date is missing"
            assert isinstance(window['delivery_date'], str), "delivery_date should be a string"

            assert 'expiration_date' in window, "expiration_date is missing"
            assert isinstance(window['expiration_date'], str), "expiration_date should be a string"

        assert 'updated_at' in item, "updated_at is missing"
        assert isinstance(item['updated_at'], str), "updated_at should be a string"

if __name__ == "__main__":
    pytest.main()
