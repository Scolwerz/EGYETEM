public class Main
{
    public static void main(String[] args)
    {
        int test1 = 5;
        int test2 = 14;
        int test3 = 15;

        diamond(test1);
        System.out.println("---");
        diamond(test2);
        System.out.println("---");
        diamond(test3);
        System.out.println("---");
    }

    public static void diamond(int height)
    {
        if (height % 2 == 0)
        {
            System.err.println("Hibás paraméter: A diamond magassága nem páros.");
            return;
        }

        for (int i = 1; i <= height; i += 2)
        {
            int spaces = (height - i) / 2;
            printSpaces(spaces);
            printStars(i);
            System.out.println();
        }

        for (int i = height - 2; i > 0; i -= 2)
        {
            int spaces = (height - i) / 2;
            printSpaces(spaces);
            printStars(i);
            System.out.println();
        }
    }

    public static void printSpaces(int count)
    {
        for (int i = 0; i < count; i++)
        {
            System.out.print(" ");
        }
    }

    public static void printStars(int count)
    {
        for (int i = 0; i < count; i++)
        {
            System.out.print("*");
        }
    }
}