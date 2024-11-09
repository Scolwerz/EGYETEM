public class Mainv1
{
    public static void main(String[] args)
    {
        String fname = "config.txt";
        int n = FileUtils.readFirstLineAsInt(fname);

        String result = "";
        for (int i = 1; i <= n; i++)
        {
            result += i;
        }
        System.out.println(result);
    }
}
