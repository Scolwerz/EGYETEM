public class Main
{
    public static void main(String[] args)
    {
        if (args.length != 1)
        {
            System.err.println("Hiba! Adj meg egy sztringet!");
            System.exit(1);
        }

        StringBuilder sb = new StringBuilder();
        for (char c : args[0].toCharArray())
        {
            if (Character.isLowerCase(c) == true) sb.append(Character.toUpperCase(c));
            else if (Character.isUpperCase(c) == true) sb.append(Character.toLowerCase(c));
            else sb.append(c);
        }
        System.out.println(sb.toString());
    }
}