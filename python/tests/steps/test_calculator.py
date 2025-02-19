from pytest_bdd import given, then, when, parsers, scenarios

from currency_converter.calculator import add


scenarios("../features/calculator.feature")


@given(parsers.parse("the first number is {first_number:d}"), target_fixture="context")
def initialize_first_number(first_number):
    return {"first_number": first_number}


@given(parsers.parse("the second number is {second_number:d}"))
def initialize_second_number(context, second_number):
    context["second_number"] = second_number


@when("the two numbers are added")
def add_context_numbers(context):
    context["addition_result"] = add(context["first_number"], context["second_number"])


@then(parsers.parse("the result should be {sum:d}"))
def check_addition(context, sum):
    assert context["addition_result"] == sum
