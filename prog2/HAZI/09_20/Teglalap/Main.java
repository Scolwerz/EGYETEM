import java.util.Scanner;

public class Main
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);

        System.out.print("Add meg a téglalap 2 oldalát!\n1: ");
        int x = sc.nextInt();
        System.out.print("2: ");
        int y = sc.nextInt();

        Teglalap teglalap = new Teglalap(x,y);
        int k = teglalap.kerulet();
        int t = teglalap.terulet();
        System.out.println("A teglalap kerulete: "+k+"\nA teglalap területe: "+t);
    }
}
