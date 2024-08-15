import os
import time
from locust import TaskSet
from payloads.promotion import generate_promotion_payload
from helpers.log_config import success_logger, error_logger

class PromotionTasks(TaskSet):
    promotion_id = None

    def create_promotion_task(self):
        if not self.promotion_id:
            self.promotion_id = self.test_create_promotion()

    def get_promotion_task(self):
        if self.promotion_id:
            self.test_get_promotion_by_id(self.promotion_id)

    def test_create_promotion(self):
        endpoint = os.getenv('PROMOTION_ENDPOINT')
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        }
        payload = generate_promotion_payload()

        start_time = time.time()
        with self.client.post(endpoint, headers=headers, json=payload, catch_response=True, name="Create Promotion") as response:
            request_time = time.time() - start_time
            formatted_time = f"{request_time:.3f}"
            if response.status_code == 200:
                success_logger.info(f"Request: Create Promotion, Time: {formatted_time}, Status Code: {response.status_code}")
                promotion_id = response.text.strip('"')
                print(f"Generated Promotion ID: {promotion_id}")
                response.success()
                return promotion_id
            else:
                error_logger.error(f"Payload: {payload}, Status Code: {response.status_code}, Response: {response.text}, Time: {formatted_time}")
                response.failure(f"Failed to create promotion with status code {response.status_code}")

    def test_get_promotion_by_id(self, promotion_id):
        endpoint = os.getenv('PROMOTION_ENDPOINT') + promotion_id
        headers = {
            'Accept': 'application/json',
        }

        start_time = time.time()
        with self.client.get(endpoint, headers=headers, catch_response=True, name="Get Promotion By ID") as response:
            request_time = time.time() - start_time
            formatted_time = f"{request_time:.3f}"
            if response.status_code == 200:
                success_logger.info(f"Request: Get Promotion By ID, Time: {formatted_time}, Status Code: {response.status_code}")
                response.success()
                response_json = response.json()
                assert response_json['_id'] == promotion_id, "Promotion ID mismatch"
            else:
                error_logger.error(f"Promotion ID: {promotion_id}, Status Code: {response.status_code}, Response: {response.text}, Time: {formatted_time}")
                response.failure(f"Failed to get promotion with status code {response.status_code}")
