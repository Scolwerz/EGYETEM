import java.util.List;
import java.util.ArrayList;
import java.util.Collections;

public class Main
{
    public static void main(String[] args)
    {
        List<String> lines = FileUtils.readLines("nevek.csv");
        List<String> ptis = new ArrayList<String>();
        for (String line : lines)
        {
            String[] parts = line.split(";");
            if (parts[2].equalsIgnoreCase("PTI") == true)
            {
                ptis.add(parts[0]);
            }
        }
        Collections.sort(ptis);
        System.out.println(ptis);
    }
}