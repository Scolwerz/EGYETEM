import java.util.ArrayList;
import java.util.List;
import java.util.Set;
import java.util.HashSet;

public class Main
{
    public static void main(String[] args)
    {
		String filename = "input.txt";
		List<String> lines = FileUtils.readLines(filename));
		Set<String> result = new HashSet<>();
		for (String line : lines)
		{
			String parts[] = line.split(" ");
			for(String part : parts)
			{
				result.add(part);
			}
		}
		System.out.println(result.length());
	}
}