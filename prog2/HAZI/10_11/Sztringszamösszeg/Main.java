public class Main
{
    public static void main(String[] args)
    {
        String s = "90146852";
        int result = osszeg(s);
        System.out.println(result);
    }
    static int osszeg(String s)
    {
        char[] szamok = s.toCharArray();
        int result = 0;
        for (char c : szamok)
        {
            result += (c-'0');
            System.out.println(Character.valueOf(c));
        }
        return result;
    }
}
