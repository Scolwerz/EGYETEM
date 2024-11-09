import java.util.Arrays;

class MyArrayUtils
{
    private MyArrayUtils()
    {
        // Nem példányosíható
    }

    public static void fill(int[] tomb, int n)
    {
        for (int i = 0; i < tomb.length; i++)
        {
            tomb[i] = n;
        }
    }

    public static boolean equals(int[] tomb1, int[] tomb2)
    {
        if (tomb1.length == tomb2.length)
        {
            for (int i = 0; i < tomb1.length; i++)
            {
                if (tomb1[i] != tomb2[i])
                {
                    return false;
                }
                return true;
            }
        }
        return false;
    }

    public static void sort(int[] tomb)
    {
        int n = tomb.length;
        boolean swapped;
        do
        {
            swapped = false;
            for (int i = 1; i < n; i++)
            {
                if (tomb[i - 1] > tomb[i])
                {
                    int temp = tomb[i - 1];
                    tomb[i - 1] = tomb[i];
                    tomb[i] = temp;
                    swapped = true;
                }
            }
        } while (swapped);
    }

    public static void reverse(int[] tomb)
    {
        int i = 0, j = tomb.length -1;
        while (i < j)
        {
            int temp = tomb[i];
            tomb[i] = tomb[j];
            tomb[j] = temp;
            i++; j--;
        }
    }

    public static void sortDescending(int[] tomb)
    {
        Arrays.sort(tomb);
        MyArrayUtils.reverse(tomb);
    }
}