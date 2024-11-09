import java.util.List;
import java.util.ArrayList;

class FizzBuzz
{
    public List<String> fblist = new ArrayList<>();

    public FizzBuzz(int count)
    {
        for (int i = 1; i <= count; i++)
        {
            String out = "";
            if (i % 3 == 0) out += "Fizz";
            if (i % 5 == 0) out += "Buzz";
            if (out.isEmpty()) this.fblist.add(""+i);
            else this.fblist.add(out);
        }
    }

    public void start()
    {
        for (String s : this.fblist)
        {
            System.out.println(s);
        }
    }
}
