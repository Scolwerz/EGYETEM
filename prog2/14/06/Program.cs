using System;
using static System.Console;
using System.Collections;
using System.Collections.Generic;
using System.Text;

namespace Example
{
    public class Program
    {
        public static void Main(string[] args)
        {
            var sb = new StringBuilder();

            sb.Append("asda");
            sb.Append(4);

            var result = sb.ToString();

            WriteLine(result);

            // WriteLine(string.Join(", ", matrix));
        }
    }
}
