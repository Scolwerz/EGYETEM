using System;
using static System.Console;
using System.Collections;
using System.Collections.Generic;

namespace Example
{
    public class Program
    {
        // java : private final static N = 1000;
        private const int N = 1000;

        public static void Main(string[] args)
        {
            // const int N = 100;

            var result = Enumerable.Range(1, N-1).Where(x => x%3==0 || x%5==0).Sum();
            WriteLine(result);
        }
    }
}
