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
            /*int[] scores = new int[10];  // kinullázza

            int[] pontok = {2,5,3,6,7};

            string[] nevek = {"én", "te", "nem"};

            int[,] matrix = new int[3,3]; */
            int[,] matrix = {
                {1,2,3},
                {4,5,6},
                {7,8,9}
            };

            for (var sor = 0; sor < matrix.GetLength(0); sor++)
            {
                for (var oszlop = 0; oszlop < matrix.GetLength(1); oszlop++)
                {
                    Write(matrix[sor,oszlop]);
                    Write(" ");
                }
                WriteLine();
            }

            // WriteLine(string.Join(", ", matrix));
        }
    }
}
