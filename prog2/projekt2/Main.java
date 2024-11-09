import java.io.File;
import java.util.ArrayList;
import java.util.List;

class Main
{
    public static void main(String[] args)
    {
        List<String> temp = new ArrayList<>();

        try
        {
            if (args.length == 1)
            {
                String rootFolderPath = args[0]; // Gyökérkönyvtár neve
                File file = new File(rootFolderPath);
                if (!file.isDirectory())
                {
                    printError();
                }

                temp.add(file.toString() + File.separator); // Hozzáadja a gyökérkönyvtárat
                List<String> folders = FolderUtils.traverseFolder(file, temp); // Rekurzívan visszaadja a mappák listáját

                for (int i = 0; i < folders.size(); i++)
                {
                    List<String> imageFiles = FolderUtils.getFolderContent(folders.get(i),"images"); // Visszaadja az adott mappa képeit egy listában

                    List<HtmlGenerator> imageHtmls = new ArrayList<>(); // Egy lista a képek HtmlGenerator-ának

                    for (String imageFile : imageFiles)
                    {
                        imageHtmls.add(new HtmlGenerator(folders.get(i), imageFile, rootFolderPath)); // Létrehoz az adott képhez egy HtmlGenerator-t
                        imageHtmls.getLast().createImageHtml(); // Létrehoz egy alap .html-t a képekhez, a későbbi indexelés céljából
                    }

                    for (HtmlGenerator imageHtml : imageHtmls)
                    {
                        imageHtml.editImageHtml(); // Felülírja a előbb létrehozott .html-eket
                    }
                    new HtmlGenerator(folders.get(i) + File.separator, rootFolderPath).createIndexHtml(); // Létrehozza az adott mappa index.html-ét
                }
                new HtmlGenerator(rootFolderPath,rootFolderPath).createIndexHtml(); // Létrehozza a start page index.html-t
            }
            else if (args.length == 2 && (args[0].toLowerCase().equals("-delete") || args[0].toLowerCase().equals("-del"))) // .html file-ok törlése
            {
                String folderRootPath = args[1]; // Gyokerkönyvtár neve
                File file = new File(folderRootPath);
                if (file.isDirectory() == false)
                {
                    printError();
                }

                temp.add(file.toString() + File.separator); // Hozzáadja a gyökérkönyvtárat
                List<String> folders = FolderUtils.traverseFolder(file, temp); // Rekurzívan visszaadja a mappák listáját
                FolderUtils.deleteHtmlFiles(folders); // Kitörli a .html file-okat
            }
            else
            {
                printError();
            }
        }
        catch (NullPointerException e)
        {
            printError();
        }
        catch (Exception e)
        {
            e.printStackTrace();
            System.exit(1);
        }
    }

    private static void printError()
    {
        System.out.println("Használat: java Main (-delete/-del) <mappa elérési útvonala>");
        System.exit(1);
    }
}