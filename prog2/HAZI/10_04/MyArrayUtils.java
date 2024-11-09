import java.util.Arrays;

class ArrayStats {
    private int min;
    private int max;

    public ArrayStats(int min, int max)
    {
        this.min = min;
        this.max = max;
    }
}

class MyArrayUtils
{
    private MyArrayUtils() {
        // Nem példányosíható
    }

    public static void fill(int[] tomb, int n) {
        for (int i = 0; i < tomb.length; i++)
        {
            tomb[i] = n;
        }
    }

    public static boolean equals(int[] tomb1, int[] tomb2) {
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

    public static void sort(int[] tomb) {
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

    public static boolean isSorted(int[] tomb) {
        for (int i = 0; i < tomb.length-1; i++)
        {
            if (tomb[i] > tomb[i+1])
            {
                return false;
            }
        }
        return true;
    }

    public static void reverse(int[] tomb) {
        int i = 0, j = tomb.length -1;
        while (i < j)
        {
            int temp = tomb[i];
            tomb[i] = tomb[j];
            tomb[j] = temp;
            i++; j--;
        }
    }

    public static void sortDescending(int[] tomb) {
        Arrays.sort(tomb);
        MyArrayUtils.reverse(tomb);
    }

    public static int getMinElem(int[] tomb) {
        int min = tomb[0];
        for (int i = 1; i < tomb.length; i++)
        {
            if (tomb[i] < min)
            {
                min = tomb[i];
            }
        }
        return min;
    }

    public static int getMaxElem(int[] tomb) {
        int max = tomb[0];
        for (int i = 1; i < tomb.length; i++)
        {
            if (tomb[i] > max)
            {
                max = tomb[i];
            }
        }
        return max;
    }

    public static int[] getMinMax_arr(int[] tomb) {
        int[] result = new int[2];
        result[0] = getMinElem(tomb);
        result[1] = getMaxElem(tomb);
        return result;
    }

    public static ArrayStats getMinMax_class(int[] tomb) {
        int min = getMinElem(tomb);
        int max = getMaxElem(tomb);
        ArrayStats result = new ArrayStats(min, max);
        return result;
    }

}