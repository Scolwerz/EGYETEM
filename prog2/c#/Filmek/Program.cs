using System;
using static System.Console;
using System.Linq;
using System.Collections;
using System.Collections.Generic;
using System.IO;
using System.Text;

namespace Filmek
{
    public class Program
    {

        // mainen belül: const int N = 100;
        private const int N = 10;

        private static Random random = new Random();

        public static void Main(string[] args)
        {
            string str = "Batman";
            WriteLine(str[2..^1]);


            string code = @"
<html>
    valami
</html>".Trim();
            WriteLine(code);

            string fullstring = @"ide\bármit'írok'az\string\n";
            WriteLine(fullstring);

            string formazott = $"itt lehetnek valzotok -> {3+2+11}";  // $
            string formazott2 = string.Format("{0} <- itt és itt is lehetnek -> {1}", 4, 22);  // nem kell $
            WriteLine(formazott + "\n" + formazott2);
       

       
            var szamok = new List<int>() {3,5,42};
            WriteLine( string.Join(", ", szamok) );
            new List<int>().AddRange(szamok);
            
            foreach (var szam in szamok)
            {
                WriteLine(szam + 2);
            }
            // for (var i = 0; i < szamok.Count; i++)
            // {
            //     WriteLine(szamok[i] + 2);
            // }


            var szo = "filmek";
            WriteLine(szo);
            WriteLine(szo.ReverseStr());


            var filmek = new List<Movie>()
            {
                new Movie("Terminator", 1984, 8.0),
                new Movie("Aliens", 1986, 8.3),
                new Movie("Lies", 1994, 7.2)
            };
            // foreach (var film in filmek)
            // {
            //     WriteLine(film);
            // }
            WriteLine(string.Join(", ", filmek));

            // Mely filmek pontja >= 7,5, rendezd cím szerint
            var result = filmek
                            .Where(m => m.GetScore() >= 7.5)
                            .OrderBy(m => m.GetTitle())
                            .ToList();
            WriteLine(string.Join(", ", result));
            // (i)Enumerable


            string s = "46";
            // int sz = int.Parse(s);
            // int sz = Convert.ToInt32(sz);
            int sz = s.ToInt();
            WriteLine(sz);


            int intmin = 31;
            int intmax = 112;
            int step = 2;       // [31, 112] *2
            var lista = Enumerable.Range(0, ((intmax - intmin) / step) + 1)
                                .Select(n => n * step + intmin)
                                .ToList();
            WriteLine(string.Join(", ", lista));


            string szoveg = "    usd siu   \t\n asjk  jsjs\t u   ";
            var parts = szoveg.Split(new char[0], StringSplitOptions.RemoveEmptyEntries);
            var parts2 = szoveg.Split().Where(s => s.Length > 0).ToList();
            WriteLine(string.Join(", ", parts));
            WriteLine(string.Join(", ", parts2));


            var fname = "nevek.txt";
            using (var f = new StreamReader(fname))
            {
                string line;
                while ((line = f.ReadLine()) != null)
                {
                    WriteLine($"Sor: {line}");
                }
            }

            var g = new StreamWriter("out.txt");
            g.WriteLine("első");
            g.WriteLine("2.");
            g.WriteLine("{0} {1} éves lesz", "Pisti", 30);
            g.Close();
            WriteLine("out.txt létrehozva");


            if (args.Length == 1 && args[0] == "exit")
            {
                WriteLine("KLilépés...");
                Environment.Exit(1);
            }
            string[] argok = Environment.GetCommandLineArgs();  // benne van a program neve is, amíg alapból nincs


            int[,] matrix = //new int[3,3];
            {
                {1, 2, 3},
                {4, 5, 6},
                {7, 8 ,9}
            };
            for (var sor = 0; sor < matrix.GetLength(0); sor++)
            {
                for (var oszlop = 0; oszlop < matrix.GetLength(1); oszlop++)
                {

                }
            }


            var sb = new StringBuilder();
            sb.Append("valami");
            sb.Append(3.14);
            var text = sb.ToString();
            WriteLine(text);


            for (var i = 0; i < N; i++)
            {
                // Write(random.Next(10) + ", "); // [0, 9]
                // Write(random.Next(5,10) + ", "); // [5, 9]
                Write( Math.Round(random.NextDouble(),2) + ", "); // [0, 1.0)
            }
            WriteLine();


            var set = new HashSet<string>(); //{"alma", körte", "valami"};
            set.Add("Alma");
            set.Add("dió");
            set.Add("körte");
            set.Add("Alma");
            WriteLine(set.Count);
            WriteLine(string.Join(", ", set));

            var redundantlist = new List<int>() {1,2,4,5,2,4,2,2,2,1,5,4,2,2,7,2,6};
            var szurtlist = redundantlist.Distinct().Order().ToArray();
            WriteLine(string.Join(", ", szurtlist));

                                    // kulcs   value
            var map = new Dictionary<string, string>();
            map["elso"] = "egy";
            map["masodik"] = "ketto";
            map["harmadik"] = "harom";
            WriteLine(map["masodik"]);
            WriteLine(map.GetValueOrDefault("harmadikkk", "X"));

            /*foreach (var key in map.Keys)
            {
                Write(key + ", ");
            }
            WriteLine();
            foreach (var value in map.Values)
            {
                Write(value + ", ");
            } */
            foreach (var key in map.Keys)
            {
                Write($"({key} : {map[key]}), " );
            }
            WriteLine();  // v var
            foreach (KeyValuePair<string, string> pair in map)
            {
                WriteLine("{0} : {1}", pair.Key, pair.Value);
            }

        }

        public static List<string> ReadFileLines(string fname)
        {
            var result = new List<string>();
            using (var f = new StreamReader(fname))
            {
                string line;
                while ((line = f.ReadLine()) != null)
                {
                    result.Add(line);
                }
            }
            return result;
        }
    }
}