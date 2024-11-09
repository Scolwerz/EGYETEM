using System;

class 1000osszeg
{
    public static void Main(string[] args)
    {
        int limit = 1000;
        int sum = SumMultiplesOf3And5(limit);

        Console.WriteLine($"Azon 1000-nél kisebb számok összege, melyek 3 vagy 5 többszörösei: {sum}");
    }

    private static int SumMultiplesOf3And5(int limit)
    {
        int sum = 0;

        for (int i = 0; i < limit; i++)
        {
            if (i % 3 == 0 || i % 5 == 0)
            {
                sum += i;
            }
        }
        return sum;
    }
}
