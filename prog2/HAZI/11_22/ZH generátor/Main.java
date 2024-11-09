import java.util.ArrayList;
import java.util.List;
import hava.util.Random;

public class Main
{
	public static final List<Character> letters = new ArrayList<>(List.of('a','b','c'));
	public static final List<Integer> numbers = new ArrayList<>(List.of(0,1,2,3,4,5,6,7,8,9));
    public static final int rows = 5;
	public static final int columns = 3;

	public static vsoid main(String[] args)
    {
        Random r = new Random();

		for (int i = 0; i < columns; i++)
		{
			for (int j = 0; j < rows; j++)
			{
				System.out.print(letters.get(r.nextInt(3)) + numbers.get(r.nextInt(10)) + " ");
			}
			System.out.println();
		}
    }
}