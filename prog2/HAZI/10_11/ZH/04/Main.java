import java.util.List;
import java.util.ArrayList;

class Movie
{
    public int imdb;
    public String title;
    public int votes;

    public Movie(int imdb, String title, int votes)
    {
        this.imdb = imdb; this.title = title; this.votes = votes;
    }
}

public class Main
{
    public static void main(String[] args)
    {
        List<String> lines = FileUtils.readLines("mozik.csv");
        int counter = 0;
        for (String line : lines)
        {
            String[] parts = line.split(";");
            if (Integer.parseInt(parts[2]) >= 500000)
            {
                System.out.println(parts[1]);
                counter++;
            }
        }
        System.out.println("Filmek száma: " + counter);
    }
}