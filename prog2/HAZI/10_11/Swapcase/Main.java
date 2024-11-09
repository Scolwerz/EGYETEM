import java.util.Scanner;

public class Main
{
    public static void main(String[] args)
    {
        //swapcase (Kérjünk be egy szöveget, amiben a kis- és nagybetűket felcseréljük. Pl.: "Hello2023World" -> "hELLO2023wORLD")
        Scanner sc = new Scanner(System.in);
        System.out.println("Adjmeg egy szöveget: ");
        String text = sc.nextLine();
        String result = swapcase(text);
        System.out.println(result);
    }

    static String swapcase(String text)
    {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < text.length(); i++)
        {
            Character c = text.charAt(i);
            if (Character.isLowerCase(c) == true) sb.append(Character.toUpperCase(c));
            else if (Character.isUpperCase(c) == true) sb.append(Character.toLowerCase(c));
            else sb.append(c);
        }
        return sb.toString();
    }
}
