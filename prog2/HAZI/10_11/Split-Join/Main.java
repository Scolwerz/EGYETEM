import java.util.Arrays;
import java.util.ArrayList;
import java.util.List;

public class Main
{
    public static void main(String[] args)
    {
        System.out.println("\\.");
    }

    private void split() {
        String s = "demo:x:1001:100::/home/demo:/bin/bash";
        String[] parts = s.split(":");
        for (String part : parts) {
            System.out.println(part);
        }
    }

    private void split() {
        String s = "demo:x:1001:100::/home/demo:/bin/bash";
        String[] parts = s.split(":");
        List<String> li = Arrays.asList(parts);
        System.out.println(li);
    }

    private void split_and_join() {
        String s = "demo:x:1001:100::/home/demo:/bin/bash";
        String[] parts = s.split(":");
        List<String> li = Arrays.asList(parts);
        System.out.println(li);
        System.out.println();

        String res1 = String.join("", li);
        System.out.println(res1);
        String res2 = String.join(";", li);
        System.out.println(res2);
        String res3 = String.join("::::", li);
        System.out.println(res3);
    }

}
