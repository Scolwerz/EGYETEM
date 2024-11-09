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
            if (args.Length != 2)
            {
                WriteLine("Hiba! Pontosan két argumentumot adj meg");
                Environment.Exit(1);
            }
            var szam1 = int.Parse(args[0]);
            var szam2 = int.Parse(args[1]);
            WriteLine()
        }
    }
}
