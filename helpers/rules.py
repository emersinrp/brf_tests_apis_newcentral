import json
import time
from helpers.log_config import error_logger, success_logger

def handle_request(client, endpoint, headers, payload, request_name, display_name):
    start_time = time.time()
    with client.post(endpoint, headers=headers, json=payload, catch_response=True, name=display_name) as response:
        request_time = time.time() - start_time
        formatted_time = f"{request_time:.3f}"
        if response.status_code == 200:
            success_logger.info(f'Request: {request_name}, Time: {formatted_time}, Status Code: {response.status_code}')
            response.success()
        else:
            error_logger.error(f'Payload: {json.dumps(payload)}, Status Code: {response.status_code}, Response: {response.text}, Time: {formatted_time}')
            response.failure(f'Status Code: {response.status_code}')
