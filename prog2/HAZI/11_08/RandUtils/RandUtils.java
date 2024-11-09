import java.util.List;
import java.util.Random;

class RandUtils
{
    public final static Random r = new Random();

    private RandUtils(){}

    public static int randint(int intmin, int intmax)
    {
        return intmin + r.nextInt(intmax-intmin+1);
    }

    public static int radrange(int intmin, int intmax)
    {
        return intmin + r.nextInt(intmax-intmin);
    }

    public static int choice(List<Integer> nums)
    {
        return nums.get(randint(0,nums.size()-1));
    }
}
