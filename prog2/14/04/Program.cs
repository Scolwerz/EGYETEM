using System;
using static System.Console;
using System.Collections;
using System.Collections.Generic;

namespace Example
{
    public class Program
    {
        public static void Main(string[] args)
        {
            var szamok = new List<int> {2,4,6,8,10,11,13};
            WriteLine(string.Join(", ", szamok));
            // var result = szamok.First();
            // var result = szamok.Last();
            // var result = szamok.Sum();
            // var result = szamok.Take(3); // első 3 elem
            // var result = szamok.Skip(3); // első 3 elem kivétel
            // var result = szamok.Skip(2).Take(2);
            // var result = szamok.All(x => x > 0); // mindegyik elemre igaz e
            var result = szamok.Any(x => x < 0); // van e amire igaz

            WriteLine(result);
            //WriteLine(string.Join(", ", result));
        }
    }
}
