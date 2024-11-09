public class Main
{
    public static void main(String[] args)
    {
        int n = 309; //2^1024 számjegyei
        char[] szamjegyek = new char[n+1];
        for (int i=0; i<n; i++)
        {
            szamjegyek[i]='0';
        }
        szamjegyek[n] = '0'+1;
        szamjegyek[n-1] = '1';

        int maradek = 0;
        int szam;
        for (int i = 0; i < 1024; i++) {
            for (int j = n-1; j >= 0; j--) {
                szam = (szamjegyek[j]-'0')*2+maradek;
                if (szam > 9) {
                    maradek = 1;
                    szam -= 10;
                }
                else {
                    maradek = 0;
                }
                szamjegyek[j] = (char)(szam + 48);
            }
        }

        System.out.printf("2^1024 = %s", szamjegyek);

        int sum = 0;
        for (int i = 1; i < n; i++)
        {
            sum += Math.abs((int)szamjegyek[i] - (int)szamjegyek[i-1]);
        }
        System.out.printf("\n\nMegoldas: %d", sum);
    }
}