@fail_existing_database
Feature: Fixture loading
    In order to have sample data during my behave tests
    As the Maintainer
    I want to load fixtures

    Scenario: Load fixtures
        Then the fixture should be loaded

    Scenario: Load fixtures for this scenario and feature
        Then the fixture for the second scenario should be loaded
