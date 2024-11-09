public class Main
{
    public static void main(String[] args)
    {
        if (args.length != 3) {
            System.err.println("Hiba: adj meg három egész értéket!");
            System.exit(1);
        }

        int a = Integer.parseInt(args[0]);
        int b = Integer.parseInt(args[1]);
        int c = Integer.parseInt(args[2]);

        boolean valid = isValid(a,b,c);
        boolean pitagorasz = pitagorasz(a, b, c);
        if (pitagorasz) {
            System.out.println("derékszögű");
        }
        else if (valid) {
            System.out.println("megszerkeszthető, de nem derékszögű");
        }
        else {
            System.out.println("nem megszerkeszthető");
        }
    }

    public static boolean isValid(int a, int b, int c) {
        return a + b > c && a + c > b && b + c > a;
    }
    static boolean pitagorasz(int a, int b, int c) {
        return a*a+b*b == c*c || a*a+c*c == b*b || b*b+c*c == a*a;
    }
}