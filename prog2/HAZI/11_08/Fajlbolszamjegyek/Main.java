import java.util.List;

public class Main
{
    public static void main(String[] args)
    {
        String fname = "day01.txt";
        List<Integer> digits = FileUtils.readFirstLineAsListOfDigits(fname);
        int result = 0;
        for (int c : digits)
        {
            result += c;
        }

        // System.out.println(digits);
        System.out.println(result);
    }
}