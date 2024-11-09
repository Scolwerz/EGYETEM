using System;
using static System.Console;

class Fizzbuzz
{
    public static void Main()
    {
        for (int i = 1; i <= 100; i++)
        {
            if (i % 3 == 0 && i % 5 == 0)
            {
                WriteLine("FizzBuzz");
            }
            else if (i % 3 == 0)
            {
                WriteLine("Fizz");
            }
            else if (i % 5 == 0)
            {
                WriteLine("Buzz");
            }
            else
            {
                WriteLine(i);
            }

            // WriteLine(i % 3 == 0 && i % 5 == 0 ? "FizzBuzz" : i % 3 == 0 ? "Fizz" : i % 5 == 0 ? "Buzz" : i.ToString());
        }
    }
}
