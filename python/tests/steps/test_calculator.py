import pytest
from pytest_bdd import given, scenario, then, when, parsers, scenarios

from currency_converter.calculator import add


scenarios("../features/calculator.feature")


@given("the first number is 50", target_fixture="context")
@given("the second number is 70")
def initialize_first_number_equal_to_50_and_the_second_number_is_equal_to_70():
    return {
        "first_number": 50,
        "second_number": 70,
    }


@when("the two numbers are added")
def add_context_numbers(context) -> None:
    context["addition_result"] = add(context["first_number"], context["second_number"])


@then("the result should be 120")
def check_if_addition_value_is_120(context) -> None:
    assert context["addition_result"] == 120


@given(parsers.parse("the first number is: {first_number:d}"), target_fixture="context")
def initialize_first_number(first_number):
    return {"first_number": first_number}


@given(parsers.parse("the second number is: {second_number:d}"))
def initialize_second_number(context, second_number) -> None:
    context["second_number"] = second_number


@when("the two numbers are added")
def add_context_numbers(context) -> None:
    context["addition_result"] = add(context["first_number"], context["second_number"])


@then(parsers.parse("the result should be: {sum:d}"))
def check_addition(context, sum) -> None:
    assert context["addition_result"] == sum
