internal class Calculator
{
    public int Result { get; internal set; }
    private int _firstNumber;
    private int _secondNumber;

    internal void AddNumbers()
    {
        Result = _firstNumber + _secondNumber;
    }

    internal void SetFirstNumber(int firstNumber)
    {
        _firstNumber = firstNumber;
    }

    internal void SetSecondNumber(int secondNumber)
    {
        _secondNumber = secondNumber;
    }
}