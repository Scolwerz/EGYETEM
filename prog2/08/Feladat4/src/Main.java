import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.Collections;

public class Main {
    public static void main(String[] args) {
        List<String> lines = FileUtils.readLines("games.csv");
        lines = cleanDataset(lines);
        List<String> konzolok = getConsoles(lines);
        System.out.println("Elérhető konzolok: " + String.join(", ", konzolok));

        Scanner sc = new Scanner(System.in);
        System.out.print("\nKonzol típusa: ");
        System.out.print("");
        String userInput = sc.nextLine().toUpperCase();
        if (!konzolok.contains(userInput)) {
            System.err.println("Hiba! Nincs ilyen konzol!");
            System.exit(1);
        }
        produceStatistics(userInput, lines);
    }

    private static void produceStatistics(String konzol, List<String> lines) {
        int cnt = 0, total = 0;
        for (String line : lines) {
            String[] parts = line.split(",");
            String currentConsole = parts[0];
            int score = Integer.parseInt(parts[3]);
            if (currentConsole.equals(konzol)) {
                cnt++;
                total += score;
            }
        }
        double avg = (double) total / cnt;
        System.out.printf("Játékok száma: %d\nÁtlagos pontszám: %.2f", cnt, avg);
    }

    private static List<String> getConsoles(List<String> lines) {
        List<String> result = new ArrayList<>();
        for (String line : lines) {
            String[] parts = line.split(",");
            String konzol = parts[0];
            if (!result.contains(konzol)) {
                result.add(konzol);
            }
        }
        Collections.sort(result);
        return result;
    }

    private static List<String> cleanDataset(List<String> lines) {
        lines.remove(0);
        List<String> result = new ArrayList<>();
        for (String line : lines) {
            if (!line.contains("\"")) {
                result.add(line);
            }
        }
        return result;
    }


/*
public class Main
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);

        List<String> consoles = new ArrayList<>();
        int count = -1;
        List<String> games = FileUtils.readLines("games.csv");
        for (String game : games)
        {
            if (count == -1) {
                count++;
                continue;
            }
            if (game.startsWith("\"")) {
                continue;
            }

            String[] parts = game.split(",");
            boolean contains = false;
            for (String console : consoles)
            {
                if (parts[0].equalsIgnoreCase(console)) {
                    contains = true;
                    break;
                }                
            }
            if (!contains) {
                consoles.add(parts[0]);
            }
        }
        Collections.sort(consoles);
        System.out.println("Elérhető konzolok: " + String.join(", ", consoles));
        System.out.print("\n\nKonzol típusa: ");
        String input = sc.nextLine();

        
        count = -1;
        int scoresum = 0;
        for (String game : games)
        {
            if (count == -1) {
                count++;
                continue;
            }
            if (game.startsWith("\"")) {
                continue;
            }

            String[] parts = game.split(",");
            if (parts[0].compareToIgnoreCase(input) == 0)
            {
                count++;
                scoresum += Integer.parseInt(parts[3]);
            }
        }
        float score = (float) scoresum / count;
        System.out.println("Játékok száma: " + count);
        System.out.printf("Átlagos pontszám: %.2f\n", score);        
    }
*/
}