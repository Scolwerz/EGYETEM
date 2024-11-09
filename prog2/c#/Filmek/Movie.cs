namespace Filmek
{
    public class Movie
    {
        private string title;
        private int year;
        private double score;

        public Movie(string title, int year, double score) {
            this.title = title;
            this.year = year;
            this.score = score;
        }

        public string GetTitle() {
            return this.title;
        }

        public int GetYear() {
            return this.year;
        }

        public double GetScore() {
            return this.score;
        }

        public override string ToString()
        {
            return $"({this.title}, {this.year}, {this.score}";
        }
    }
}