Feature: Calculator
	Simple calculator for adding **two** numbers

	Scenario: Add two numbers
		Given the first number is 50
		And the second number is 70
		When the two numbers are added
		Then the result should be 120

	Scenario Outline: Add two numbers with templating
		Given the first number is: <first_number>
		And the second number is: <second_number>
		When the two numbers are added
		Then the result should be: <sum>

		Examples:
			| first_number | second_number | sum | comment                                               |
			| 50           | 70            | 120 | Happy path                                            |
			| 70           | 50            | 120 | Happy path swapped                                    |
			| 50           | -50           | 0   | A number plus its opposite yields to identity element |
			| 50           | 0             | 50  | A number plus identity element yields to the number   |

