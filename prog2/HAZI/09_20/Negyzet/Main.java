import java.util.Scanner;

public class Main
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);

        System.out.print("Add meg a négyzet oldalának hosszát: ");
        int x = sc.nextInt();
        Negyzet negyzet = new Negyzet(x);
        int k = negyzet.kerulet();
        int t = negyzet.terulet();
        System.out.println("A negyzet kerulete: "+k+"\nA negyzet területe: "+t);
    }
}
