public class Mainv2
{
    public static void main(String[] args)
    {
        String fname = "config.txt";
        int n = FileUtils.readFirstLineAsInt(fname);

        StringBuilder sb = new StringBuilder();
        for (int i = 1; i <= n; i++)
        {
            sb.append(i);
        }
        System.out.println(sb.toString());
    }
}
