from behave import when, then
import json
from models.post_body import POST_BODY
from models.put_body import PUT_BODY
from constants.expected_status_codes import POST_NEW_POST_STATUS_CODE, PUT_POST_STATUS_CODE

@when('I create a new post with valid data')
def step_impl(context):
    body = json.loads(s=POST_BODY)
    context.response = context.api.post_new_post(body)


@when('I update the post {number} data')
def step_impl(context, number):
    body = json.loads(s=PUT_BODY)
    context.response = context.api.put_post(number, body)


@then('it should return the created post data')
def step_impl(context):
    assert context.response.status_code == POST_NEW_POST_STATUS_CODE, \
        f'Expected status code {POST_NEW_POST_STATUS_CODE}, but got {context.response.status_code}'
    
    response_data = context.response.json()
    assert 'id' in response_data, f'Response should contain an id\n{response_data}'


@then('it should return the updated post data')
def step_impl(context):
    assert context.response.status_code == PUT_POST_STATUS_CODE, \
        f'Expected status code {PUT_POST_STATUS_CODE}, but got {context.response.status_code}'
