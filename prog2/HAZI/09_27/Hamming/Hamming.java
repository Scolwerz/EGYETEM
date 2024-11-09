class Hamming
{
    private Hamming()
    {
        // Nem példányosítható
    }
    public static int distance(String s1, String s2)
    {
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
            return hlength;
        }
        return -1;
    }
}