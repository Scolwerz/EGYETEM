import java.util.List;

public class Main
{
    public static void main(String[] args)
    {
        String fname = "szam.txt";
        List<Integer> digits = FileUtils.readFirstLineAsListOfDigits(fname);
        int result = 0;
        for (int i = 0; i < digits.size()-1; i++)
        {
            if (digits.get(i) == digits.get(i+1))
            {
                result += digits.get(i);
            }
        }
        if (digits.get(0) == digits.get(digits.size() - 1))
        {
            result += digits.get(0);
        }

        // System.out.println(digits);
        System.out.println(result);
    }
}