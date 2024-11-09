using System;
using static System.Console;
using System.Linq;
using System.Collections;
using System.Collections.Generic;

namespace Example
{
    private static Random rand = new Random(222);

    public class Program
    {
        public static void Main(string[] args)
        {
            WriteLine(rand.Next(11));       // [0, 11)]
            WriteLine(rand.Next(5,11));     // [5, 11)]
            WriteLine(rand.NextDouble());   // [0.0, 1.0]
        }
    }
}
