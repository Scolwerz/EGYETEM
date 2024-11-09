import java.lang.Math;

public class Main
{
    public static void main(String[] args)
    {
        double x1 = 343;
        double cuberoot = Math.cbrt(x1);
        System.out.println(x1+" köbgyöke: "+cuberoot);

        float x2 = 23.49843f;
        int kerekites = Math.round(x2);
        System.out.println(x2+" egészre kerekítve: "+kerekites);

        double x3 = Math.random();
        System.out.println("Random double érték 0-1 között: "+x3);

        double oszto = Math.random()/Math.nextDown(1.0);
        int intMin = 15;
        int intMax = 32;
        double x31 = intMin*(1.0 - oszto) + intMax*oszto;
        System.out.println("Random szám "+intMin+" és "+intMax+" között: "+x31);

        int x41 = 12, x42 = 15;
        int kisebb = Math.min(x41,x42);
        System.out.println(x41+" és "+x42+" közül visszaadja a kisebbet: "+kisebb);

        double x5 = 3.6363;
        double tangens = Math.tan(x5);
        System.out.println(x5+" tangense: "+tangens);
    }
}
