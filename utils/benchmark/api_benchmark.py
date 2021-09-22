import json
import time
from locust import HttpUser, task, between, events
from faker import Faker

class TesttUser(HttpUser):
    wait_time = between(1, 5)

    def on_start(self):
        fake = Faker()
        payload = {
              "user": {
                "username": fake.user_name(),
                "bio": "Fresh",
                "image": "https://cdn.auth0.com/blog/whatabyte/salad-sm.png",
                "email": fake.email(),
                "password": "1234"
              }
            }
        json_data = json.loads(json.dumps(payload))
        response = self.client.post("/api/users", json=json_data)

        jwt_token = response.json().get("user").get("token")

        self.client.headers.update({"Authorization":f"Bearer {jwt_token}"})
        

    @task
    def check_profile(self):
        self.client.get("/api/user")

    @task
    def create_article(self):
        fake = Faker()
        
        payload = {
            "article": {
                "title": fake.sentence(nb_words=6),
                "description": fake.paragraph(nb_sentences=3),
                }
            }

        json_data = json.loads(json.dumps(payload))
        self.client.post("/api/articles", json=json_data)