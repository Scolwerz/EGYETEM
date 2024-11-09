import java.util.Scanner;

public class Main
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);

        System.out.print("Add meg a kör sugarát: ");
        int x = sc.nextInt();
        Circle circle = new Circle(x);
        double k = circle.kerulet();
        double t = circle.terulet();
        System.out.println("A kör kerülete: "+k+"\nA kör területe: "+t);
    }
}
