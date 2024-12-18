import pytest
from pytest_bdd import given, scenario, then, when, parsers

from currency_converter.calculator import add

########################################################################################################################
# How to glue a scenario
########################################################################################################################

# Arguments: feature file path, scenario name
@scenario("../features/calculator.feature", "Add two numbers")
def test_add_two_numbers() -> None:
    pass


@given("the first number is 50", target_fixture="context")
def initialize_first_number_equal_to_50():
    return {"first_number": 50}


@given("the second number is 70")
def initialize_second_number_equal_to_70(context) -> None:
    context["second_number"] = 70


@when("the two numbers are added")
def add_context_numbers(context) -> None:
    context["addition_result"] = add(context["first_number"], context["second_number"])


@then("the result should be 120")
def check_if_addition_value_is_120(context) -> None:
    assert context["addition_result"] == 120


########################################################################################################################
# How to glue a scenario outline
########################################################################################################################


@scenario("../features/calculator.feature", "Add two numbers with templating")
def test_add_two_numbers_with_templating() -> None:
    pass


@given(parsers.parse("the first number is: {first_number:d}"), target_fixture="context")
def initialize_first_number(first_number):
    return {"first_number": first_number}


@given(parsers.parse("the second number is: {second_number:d}"))
def initialize_second_number(context, second_number) -> None:
    context["second_number"] = second_number


# Reuse When step!
@when("the two numbers are added")
def add_context_numbers(context) -> None:
    context["addition_result"] = add(context["first_number"], context["second_number"])


@then(parsers.parse("the result should be: {sum:d}"))
def check_addition(context, sum) -> None:
    assert context["addition_result"] == sum
