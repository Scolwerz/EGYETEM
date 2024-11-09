using System;
using static System.Console;
using System.Linq;
using System.Collections;
using System.Collections.Generic;

namespace ZHGenerator
{
    public class Program
    {
        private static Random rand = new Random();
        private static char[] betuk = {'a', 'b', 'c'};

        public static void Main(string[] args)
        {
            const int sorok = 3;
            const int oszlopok = 7;

            for (var i = 0; i < sorok; i++)
            {
                for (var j = 0; j < oszlopok; j++)
                {
                    var index = rand.Next(0,3);
                    var szam = rand.Next(0,10);
                    Write($"{betuk[index]}{szam} ");
                }
                WriteLine();
            }
        }
    }
}