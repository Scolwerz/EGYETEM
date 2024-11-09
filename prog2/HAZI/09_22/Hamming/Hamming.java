public class Hamming
{
    public static void main(String[] args)
    {
        String s1 = "toned";
        String s2 = "roses";

        if (s1.length() == s2.length())
        {
            int hlength = 0;
            for (int i = 0; i < s1.length(); i++)
            {
                if (s1.charAt(i) != s2.charAt(i))
                {
                    hlength++;
                }
            }
        }
    }
}