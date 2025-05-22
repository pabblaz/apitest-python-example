from behave import given
from adapters.api import Api


@given('I am connected to the JSONPlaceholder API')
def step_impl(context):
    context.api = Api()
    