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
            Write("Szám: ");
            var text = ReadLine();

            try
            {
                int val = int.Parse(text);
                WriteLine($"{val} + 1 = {val+1}");
            }
            catch (FormatException e)
            {
                WriteLine("Számot kell megadni!");
                WriteLine(e.Message);
            }
            finally
            {
                WriteLine("mindig");
            }

            a();

            WriteLine("END");
        }

        public static void a()
        {
            thron new 
        }
    }
}
