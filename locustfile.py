import os
from locust import HttpUser, between, TaskSet, task
from dotenv import load_dotenv
from tests.test_promotion import PromotionTasks
from tests.test_person_credit import test_person_credit
from tests.test_person_delivery_window import test_person_delivery_window

load_dotenv()

class UserBehavior(TaskSet):
    tasks = [PromotionTasks]

    @task(1)
    def create_and_get_promotion(self):
        promotion_tasks = PromotionTasks(self)
        promotion_id = promotion_tasks.test_create_promotion()
        if promotion_id:
            promotion_tasks.test_get_promotion_by_id(promotion_id)

    @task(5)  
    def run_person_credit_test(self):
        test_person_credit(self)

    @task(5)
    def run_person_delivery_window_test(self):
        test_person_delivery_window(self)

class GraphQLUser(HttpUser):
    wait_time = between(1, 5)
    tasks = [UserBehavior]
    host = os.getenv('HOST')
