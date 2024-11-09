import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class FileUtils
{
    // input: a megnyitandó file neve
    // output: egy List<String> objektum, ami az egyes sorokat tartalmazza
    public static List<String> readLines(String fileName)
    {
        List<String> lines = new ArrayList<String>();

        try
        {
            String line;
            BufferedReader br = new BufferedReader(new FileReader(fileName));
            while ((line = br.readLine()) != null)
            {
                lines.add(line);
            }
            br.close();
        }
        catch (FileNotFoundException e)
        {
            e.printStackTrace();
            System.exit(1);
        }
        catch (IOException e)
        {
            e.printStackTrace();
            System.exit(2);
        }

        return lines;
    }

    public static List<Integer> readFirstLineAsListOfDigits(String filename)
    {
        List<Integer> result = new ArrayList<>();
        String sor = FileUtils.readLines(filename).get(0);
        for (char c : sor.toCharArray())
        {
            result.add(Integer.parseInt(""+c));
        }
        return result;
    }

    public static List<Integer> readLinesAsListOfDigits(String filename)
    {
        List<Integer> result = new ArrayList<>();
        List<String> sor = new ArrayList<>();
        sor = FileUtils.readLines(filename);
        
        for (char c : sor.toString().toCharArray())
        {
            result.add(Integer.parseInt(""+c));
        }
        return result;
    }
}
