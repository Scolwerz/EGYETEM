import java.util.List;
import java.util.ArrayList;

public class Main
{
    public static void main(String[] args)
    {
        //kis,nagy,2szam,spec(. , : ;)

        List<String> data = FileUtils.readLines("passwords.txt");
        int counter = 0;
        for (String line : data)
        {
            int digitCount = 0;
            for (char c : line.toCharArray())
            {
                if (Character.isDigit(c))
                {
                    digitCount++;
                }
            }
            if (!line.equals(line.toLowerCase()) &&
                !line.equals(line.toUpperCase()) &&
                digitCount >= 2 && line.contains(".") ||
                line.contains(",") || line.contains(":") ||
                line.contains(";"))  counter++;
        }
        System.out.println(counter);
    }
}