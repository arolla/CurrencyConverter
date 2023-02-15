using Shouldly;
using TechTalk.SpecFlow;

namespace CurrencyConverter.Tests.Steps
{
    [Binding]
    public sealed class CalculatorStepDefinitions
    {

        // For additional details on SpecFlow step definitions see https://go.specflow.org/doc-stepdef

        private readonly ScenarioContext _scenarioContext;

        public CalculatorStepDefinitions(ScenarioContext scenarioContext)
        {
            _scenarioContext = scenarioContext;
        }

        [Given("the first number is (.*)")]
        public void GivenTheFirstNumberIs(int number)
        {
            _scenarioContext.Add("first", number);
        }

        [Given("the second number is (.*)")]
        public void GivenTheSecondNumberIs(int number)
        {
            _scenarioContext.Add("second", number);
        }

        [When("the two numbers are added")]
        public void WhenTheTwoNumbersAreAdded()
        {
            var first = _scenarioContext.Get<int>("first");
            var second = _scenarioContext.Get<int>("second");

            var sum = Calculator.Add(first, second);

            _scenarioContext.Add("result", sum);
        }

        [Then("the result should be (.*)")]
        public void ThenTheResultShouldBe(int result)
        {
            var actualResult = _scenarioContext.Get<int>("result");
            actualResult.ShouldBe(result);
        }
    }
}
