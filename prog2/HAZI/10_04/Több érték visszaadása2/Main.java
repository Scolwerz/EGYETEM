import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Pair
{
    public int min;
    public int max;

    public String toString()
    {
        return "[" + this.min+ ", " + this.max + "]";
    }
}

public class Main
{
    public static void main(String[] args)
    {
        List<Integer> szamok = new ArrayList<Integer>(List.of(5, 6, 3, 9, 4, 2, 7, 99));
        szamok.add(1);

        System.out.println(szamok); //[5, 6, 3, 9, 4, 2, 7, 99, 1]
        System.out.println(Arrays.toString(getMinMax1(szamok)));
        System.out.println(getMinMax2(szamok));
        System.out.println(getMinMax3(szamok));
    }

    public static int[] getMinMax1(List<Integer> szamok)
    {
        int[] result = new int[2];
        int min = szamok.get(0);
        int max = szamok.get(0);
        for(int i = 1; i < szamok.size(); i++)
        {
            if (szamok.get(i) < min) min = szamok.get(i);
            if (szamok.get(i) > max) max = szamok.get(i);
        }
        result[0] = min;
        result[1] = max;
        return result;
    }

    public static Pair getMinMax2(List<Integer> szamok)
    {
        Pair result = new Pair();
        result.min = szamok.get(0);
        result.max = szamok.get(0);
        for(int i = 1; i < szamok.size(); i++)
        {
            if (szamok.get(i) < result.min) result.min = szamok.get(i);
            if (szamok.get(i) > result.max) result.max = szamok.get(i);
        }
        return result;
    }

    public static List<Integer> getMinMax3(List<Integer> szamok)
    {
        List<Integer> result = new ArrayList<>();
        int min = szamok.get(0);
        int max = szamok.get(0);
        for(int i = 1; i < szamok.size(); i++)
        {
            if (szamok.get(i) < min) min = szamok.get(i);
            if (szamok.get(i) > max) max = szamok.get(i);
        }
        result.add(min);
        result.add(max);
        return result;
    }
}