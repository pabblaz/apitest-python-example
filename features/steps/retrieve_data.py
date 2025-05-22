from behave import when, then
from constants.expected_status_codes import GET_POSTS_STATUS_CODE, GET_POST_STATUS_CODE

@when('I request all posts')
def step_impl(context):
    context.response = context.api.get_posts()

@when('I request the post number {post_id:d} details')
def step_impl(context, post_id):
    context.response = context.api.get_post(post_id)

@then('the list of posts should not be empty')
def step_impl(context):
    assert context.response.status_code == GET_POSTS_STATUS_CODE, \
        f'Expected status code {GET_POSTS_STATUS_CODE}, but got {context.response.status_code}'

    response_data = context.response.json()
    assert isinstance(response_data, list), 'Response should be a list'
    assert len(response_data) > 0, 'Response should contain at least one post'

@then('it should return the post data')
def step_impl(context):
    assert context.response.status_code == GET_POST_STATUS_CODE, \
        f'Expected status code {GET_POST_STATUS_CODE}, but got {context.response.status_code}'
    
    response_data = context.response.json()
    assert 'id' in response_data, 'Response should contain an id'
    assert 'title' in response_data, 'Response should contain a title'
    assert 'body' in response_data, 'Response should contain a body'
    assert 'userId' in response_data, 'Response should contain a userId'