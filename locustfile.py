from locust import HttpUser, between, TaskSet
from dotenv import load_dotenv
import os
from tests.test_person_credit import test_person_credit
from tests.test_person_delivery_window import test_person_delivery_window

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

class UserBehavior(TaskSet):
    tasks = {
        test_person_credit: 1,
        test_person_delivery_window: 1
    }

class GraphQLUser(HttpUser):
    wait_time = between(1, 5)
    tasks = [UserBehavior]
    host = os.getenv('HOST')
