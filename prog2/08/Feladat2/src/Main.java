import java.util.Scanner;

public class Main
{
    private final static char[] mely = {'a', 'A', 'á', 'Á', 'o', 'O', 'ó', 'Ó', 'u', 'U', 'ú', 'Ú'};
    private final static char[] magas = {'e', 'E', 'é', 'É', 'i', 'I', 'í', 'Í', 'ö', 'Ö', 'ő', 'Ő', 'ü', 'Ü', 'ű', 'Ű'};

    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        StringBuilder sb = new StringBuilder();

        String text;
        while (true)
        {
            System.out.print("Szöveg: ");
            text = sc.nextLine();
            if (text.equals("*")) {
                break;
            }

            for (char c : text.toCharArray()) {
                boolean isMely = false;
                boolean isMagas = false;
                for (char me : mely) {
                    if (c == me) {
                        isMely = true;
                        break;
                    }
                }
                for (char ma : magas) {
                    if (c == ma) {
                        isMagas = true;
                        break;
                    }
                }
                
                if (isMely) {
                    sb.append(c);
                    sb.append(c);
                }
                else if (!isMagas) {
                    sb.append(c);
                }
            }
            System.out.println("Eredmény: '" + sb + "'\n");
            sb.delete(0, sb.length());
        }

        
        
    }
}