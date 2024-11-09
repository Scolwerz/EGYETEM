import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Pair
{
    public int a;
    public double b;

    public String toString()
    {
        return "" + this.a+ ", " + this.b;
    }
}

public class Main
{
    public static void main(String[] args)
    {
        int n = 15;
        System.out.println(Arrays.toString(ertekek1(n)));
        System.out.println(ertekek2(n));
        System.out.println(ertekek3(n));
    }

    public static int[] ertekek1(int n)
    {
        int[] result = new int[2];
        result[0] = 2*n;
        result[1] = n*n;
        return result;
    }

    public static Pair ertekek2(int n)
    {
        Pair result = new Pair();
        result.a = n*n;
        result.b = Math.sqrt(n);
        return result;
    }

    public static List<Integer> ertekek3(int n)
    {
        List<Integer> result = new ArrayList<>();
        result.add(2*n);
        result.add(n*n);
        return result;
    }
}