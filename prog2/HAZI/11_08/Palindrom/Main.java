import java.util.List;

public class Main
{
    public static void main(String[] args)
    {
        String fname = "words_alpha.txt";
        List<String> lines = FileUtils.readLines(fname);
        int result = 0;
        for (String line : lines)
        {
            if (StringUtils.isPalindrome(line))
            {
                result++;
                System.out.println(line);
            }
        }
        System.out.println(result);

    }
}