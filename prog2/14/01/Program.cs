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
            if (args.Length != 1)
            {
                WriteLine("Hiba! Pontosan egy argumentumot adj meg");
                Environment.Exit(1);
            }
            string name = args[0];
            WriteLine($"Hello {name}!");

            var argok = Environment.GetCommandLineArgs();
        }
    }
}
