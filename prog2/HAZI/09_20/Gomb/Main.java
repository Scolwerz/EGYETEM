import java.util.Scanner;

public class Main
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);

        System.out.print("Add meg a gömb sugarát: ");
        int x = sc.nextInt();
        Gomb gomb = new Gomb(x);
        double f = gomb.felszin();
        double t = gomb.terfogat();
        System.out.println("A gömb felszíne: "+f+"\nA gömb térfogata: "+t);
    }
}
