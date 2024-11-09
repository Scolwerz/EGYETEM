import java.io.BufferedReader;
import java.io.FileReader;
import java.io.PrintWriter;

public class Main
{
    public static void main(String[] args)
    {
        try
        {
            String line;
            BufferedReader br = new BufferedReader(new FileReader("szoveg.txt"));
            while ((line = br.readLine()) != null)
            {
                System.out.println(line);
            }
            br.close();
        }
        catch (java.io.FileNotFoundException e)
        {
            e.printStackTrace();
        }
        catch (java.io.IOException e)
        {
            e.printStackTrace();
        }


        try
        {
            PrintWriter writer = new PrintWriter("asd.txt", "utf-8");
            writer.println("The first line.");
            writer.println("The second line.");
            writer.close();
        }
        catch (Exception e)
        {
            System.err.println(e);
        }

    }
}
