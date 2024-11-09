import java.util.ArrayList;
import java.util.List;
import java.util.Set;
import java.util.HashSet;
import java.util.Map;
import java.util.HashMap;
import java.util.Entry;

public class Main
{
    public static void main(String[] args)
    {
		String filename = "input.txt";
		List<String> lines = FileUtils.readLines(filename));
		Map<String, Integer> result = new HashMap<>();
		for (String line : lines)
		{
			String parts[] = line.split(" ");
			for(String part : parts)
			{
				if (result.contains(part)
				{
					result.put(part,1);
				}
				else
				{
				result.replace(part,result.get(part)+1);
				}
			}
		}
		int maxValue = 0;
		String maxKey;
		for (Entry e : result.entrySet())
		{
			System.out.println(e.getKey + ": " + e.getValue);
			if (e.getValue > maxValue)
			{
				maxKey = e.getKey;
			}
		}
		System.out.println("\n\nLeggyakoribb szó: " + maxKey + "Előfordulása: " + maxValue);
	}
}