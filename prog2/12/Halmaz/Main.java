import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class Main
{
    public static void main(String[] args)
    {
        /*
        Set<String> set = new HashSet<>();
        set.add("asd");
        set.add("assss");
        set.add("asss");
        set.add("dddd");
        set.add("assss");
        set.add("asd");
        System.out.println(set);
        */
        
        // lista -> halmaz
        Set<String> set = new HashSet<>(List.of("aa","bb","dd","aa","cc"));
        System.out.println(set);
    
        //halmaz -> lista
        List<String> list = new ArrayList<>(set);
        System.out.println(list);

        System.out.println();

        for (String s : set)
        {
            System.out.println(s);
        }
    }
}