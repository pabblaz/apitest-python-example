from configurations.urls import BASE_URL
from backend_framework.constants.http_methods import GET, POST, PUT, DELETE
from backend_framework.interfaces.base_http_client import BaseHttpClient

class Api(object):
    POSTS_PATH = '/posts'

    def __init__(self):
        self.base_url = BASE_URL
        self.http_client = BaseHttpClient(base_url=self.base_url)

    def get_posts(self):
        return self.http_client.send_request(path=self.POSTS_PATH, method=GET)

    def get_post(self, post_id):
        return self.http_client.send_request(path=f'{self.POSTS_PATH}/{post_id}', method=GET)
    
    def post_new_post(self, data):
        return self.http_client.send_request(path=self.POSTS_PATH, method=POST, body=data)
    
    def put_post(self, post_id, data):
        return self.http_client.send_request(path=f'{self.POSTS_PATH}/{post_id}', method=PUT, body=data)
    
    def delete_post(self, post_id):
        return self.http_client.send_request(path=f'{self.POSTS_PATH}/{post_id}', method=DELETE)