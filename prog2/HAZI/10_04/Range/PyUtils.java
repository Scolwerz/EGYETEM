import java.util.ArrayList;
import java.util.List;

class PyUtils
{
    private PyUtils()
    {
        //nopeldany
    }

    public static List<Integer> range(int upperLimit)
    {
        return range(0, upperLimit, 1);
    }

    public static List<Integer> range(int lowerLimit, int upperLimit)
    {
        return range(lowerLimit, upperLimit, 1);
    }

    public static List<Integer> range(int lowerLimit, int upperLimit, int step)
    {
        List<Integer> result = new ArrayList<>();

        for (int i = lowerLimit; i < upperLimit; i += step)
        {
            result.add(i);
        }

        return result;
    }
}
