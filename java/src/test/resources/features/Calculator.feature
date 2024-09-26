Feature: Calculator
  Simple calculator for adding **two** numbers

  @mytag
  Scenario: Add two numbers
    Given the first number is 50
    And the second number is 70
    When the two numbers are added
    Then the result should be 120

  @mytag
  Scenario Outline: Add two numbers
    Given the first number is <numberOne>
    And the second number is <numberTwo>
    When the two numbers are added
    Then the result should be <expected>
    Examples:
      | numberOne | numberTwo | expected |
      | 20        | 55        | 75       |
      | 34        | 76        | 110      |


