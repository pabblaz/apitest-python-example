Feature: JSONPlaceholder API Tests
  As a user
  I want to interact with the JSONPlaceholder API
  So that I can verify its correct functionality

  Background: Connect to the JSONPlaceholder API
    Given I am connected to the JSONPlaceholder API

  Scenario: Get all posts
    When I request all posts
    Then the list of posts should not be empty

  Scenario Outline: Get a specific post
    When I request the post number <number> details
    Then it should return the post data
  Examples:
    | number |
    | 1      |
    | 2      |
    | 10     |
    | 12     |

  Scenario: Create a new post
    When I create a new post with valid data
    Then it should return the created post data

  Scenario Outline: Update an existing post
    When I update the post <number> data
    Then it should return the updated post data
  Examples:
    | number |
    | 5      |
    | 6      |
    | 7      |
    | 11    |