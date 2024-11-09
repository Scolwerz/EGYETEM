class StringUtils
{
    private StringUtils(){}

    public static boolean isPalindrome(String s)
    {
        if (s.length() < 2) return false;
        StringBuilder sb = new StringBuilder();
        for (char c : s.toCharArray())
        {
            sb.append(c);
        }
        return sb.reverse().toString().equals(s);
    }
}
