import java.util.ArrayList;
import java.util.List;
import java.util.Set;
import java.util.HashSet;
import java.util.Collections;

public class Main
{
    public static void main(String[] args)
    {
		List<Integer> list = new ArrayList<>(List.of(5, 2, 3, 5, 1, 4, -200, 5, 1, 3, 2, 2, 5));
		System.out.println("Eredeti: "+list);
		Set<Integer> set = new HashSet<>(list);
		list = new ArrayList<>(set);
		Collections.sort(list);
		System.out.println("Uj: "+list);
	}
}