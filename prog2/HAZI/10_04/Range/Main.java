import java.util.ArrayList;
import java.util.List;

public class Main
{
    public static void main(String[] args)
    {
        List<Integer> result1 = new ArrayList<>(), result2 = new ArrayList<>(), result3 = new ArrayList<>(), result4 = new ArrayList<>(), result5 = new ArrayList<>(), result6 = new ArrayList<>(), result7 = new ArrayList<>(), result8 = new ArrayList<>(), result9 = new ArrayList<>(), result10 = new ArrayList<>(), result11 = new ArrayList<>();
        result1 = PyUtils.range(0, 5);    //->    [0, 1, 2, 3, 4]
        // alsó limit: 0; felső limit: 5; alsó limit benne van az eredményben, míg a felső limit nincs benne

        result2 = PyUtils.range(3, 7);   // ->    [3, 4, 5, 6]
        result3 = PyUtils.range(3, 4);   // ->    [3]
        result4 = PyUtils.range(3, 3);   // ->    []
        // a 3-tól indulunk de a 3 már nem lesz benne, így ez egy üres lista lesz

        result5 = PyUtils.range(10);   // ->    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        // ez a felső limit lesz. Ekkor az alsó limit alapértelmezetten 0 lesz.

        result6 = PyUtils.range(1);   // ->    [0]
        result7 = PyUtils.range(0);  //  ->    []
        result8 = PyUtils.range(-4);   // ->    []
        result9 = PyUtils.range(4, 20, 2);  //  ->    [4, 6, 8, 10, 12, 14, 16, 18]
        // indulunk 4-ről; a 20 már nincs benne; lépésköz: 2, azaz vesszük minden második elemet
        result10 = PyUtils.range(4, 10, 1);  //  ->    [4, 5, 6, 7, 8, 9]
        result11 = PyUtils.range(10, 4, 1);   // ->    []

        System.out.println(result1);
        System.out.println(result2);
        System.out.println(result3);
        System.out.println(result4);
        System.out.println(result5);
        System.out.println(result6);
        System.out.println(result7);
        System.out.println(result8);
        System.out.println(result9);
        System.out.println(result10);
        System.out.println(result11);
    }
}
