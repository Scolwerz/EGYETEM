import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class HtmlGenerator
{
    // Alap, üres .html-t hoz létre a képekhez
    public static void createImageHtml(String imagePath, String image)
    {
        String htmlName = image.substring(0, image.indexOf(".")) + ".html";

        try
        {
            PrintWriter pw = new PrintWriter(imagePath + htmlName);
        }
        catch (FileNotFoundException e)
        {
            e.printStackTrace();
        }
    }

    // Felülírja a képekhez tartozó .html file-okat
    public static void editImageHtml (String imagePath, String image, String imageRootFolder)
    {
        List<String> htmlFiles = FolderUtils.getFolderContent(imagePath,"htmls"); // .html file-ok listája
        htmlFiles.remove("index.html"); // index.html kitörlése, mert azt nem módosítjuk

        String[] folders = imagePath.split("\\\\");
        String title = folders[folders.length-1];
        String htmlName = image.substring(0, image.indexOf(".")) + ".html";

        int index = 0;
        for (int i = 0; i < htmlFiles.size(); i++) // Aktuális kép indexe a html file-ok listájában
        {
            if (htmlFiles.get(i).equals(htmlName))
            {
                index = i;
            }
        }

        String[] rootFolderParts = imageRootFolder.split("\\\\");
        String[] currentFolderParts = imagePath.split("\\\\");
        int position = rootFolderParts.length - currentFolderParts.length; // Almappák száma vissza a Startpage-ig
        int rootCount = rootFolderParts.length/2; // Gyökérkönyvtár elérési útvonalának tagjainak száma

        try (PrintWriter pw = new PrintWriter(imagePath + htmlName))
        {
            StringBuilder sb = new StringBuilder();
            String htmlContent;

            htmlContent = "<html><head><meta charset=\"utf-8\"\\><title>" + title + "</title></head><body style=\"background-color: #BBBBBB\"><body><h1><a href=\"";
            sb.append(htmlContent);

            for (int i = 0; i < rootCount - position; i++)
            {
                sb.append("..\\");
            }
            htmlContent = "index.html\">Start Page</a></h1><hr><p><a href=\"index.html\">^^</a></p>";
            sb.append(htmlContent);

            if (htmlFiles.size() == 1) // Ha 1 kép van
            {
                htmlContent = "<p><a href=\"" + htmlFiles.get(index) + "\">  </a>" + image + "<a href=\"" + htmlFiles.get(index) + "\">  </a></p>" +
                              "<p><a href=\"" + htmlFiles.get(index) + "\"><img alt=\"\" src=\"" + image + "\" width=\"666\" height=\"666\"/></p>";
                sb.append(htmlContent);                                 // <img alt="" src="image" width="666" height="666"/>
            }
            else if (index == 0) // Ha ez az első kép
            {
                htmlContent = "<p><a href=\"" + htmlFiles.get(index) + "\">  </a>" + image + " <a href=\"" + htmlFiles.get(index + 1) + "\"> >> </a></p>" +
                              "<p><a href=\"" + htmlFiles.get(index + 1) + "\"><img alt=\"\" src=\"" +image + "\" width=\"666\" height=\"666\"/></a></p>";
                sb.append(htmlContent);
            }
            else if (index == htmlFiles.size() - 1) // Ha ez az utolsó kép
            {
                htmlContent = "<p><a href=\"" + htmlFiles.get(index - 1) + "\"> << </a>" + image + "<a href=\"" + htmlFiles.get(index) + "\">  </a></p>" +
                              "<p><img alt=\"\" src=\"" + image + "\" width=\"666\" height=\"666\"/></a></p>";
                sb.append(htmlContent);
            }
            else // Ha a képnek 2 szomszédja van
            {
                htmlContent = "<p><a href=\"" + htmlFiles.get(index - 1) + "\"> << </a>" + image + "<a href=\"" + htmlFiles.get(index + 1) + "\"> >> </a></p>" +
                              "<p><a href=\"" + htmlFiles.get(index + 1) + "\"><img alt=\"\" src=\"" + image + "\" width=\"666\" height=\"666\"/></a></p>";
                sb.append(htmlContent);
            }
            sb.append("</body></html>");

            pw.println(sb.toString());
            sb.delete(0, sb.length() - 1);
        }
        catch (FileNotFoundException e)
        {
            e.printStackTrace();
        }
    }

    // Létrehozza az adott mappa index.html file-át
    public static void createIndexHtml(String folderPath, String folderRootPath)
    {
        String[] subFolders = folderPath.split("\\\\");
        String pageName = subFolders[subFolders.length - 1];

        List<String> folders = FolderUtils.getFolderContent(folderPath,"folders"); // Mappa almappáinak listája
        List<String> images = FolderUtils.getFolderContent(folderPath,"images"); // Mappában lévő file-ok listája

        String[] rootFolderParts = folderRootPath.split("\\\\");
        String[] currentFolderParts = folderPath.split("\\\\");
        int position = rootFolderParts.length - currentFolderParts.length; // Almappák száma vissza a Startpage-ig
        int rootCount = folderRootPath.split("\\\\").length/2; // Gyökérkönyvtár elérési útvonalának tagjainak száma

        try (PrintWriter pw = new PrintWriter(folderPath + "index.html"))
        {
            StringBuilder sb = new StringBuilder();
            String htmlContent;

            /*
            if (isStartPage == 1) // Ha ez igaz, akkor az a startpage készül, ahová nem kell visszalépéi lehetőség
            {
                htmlContent = "<html><head><meta charset=\"utf-8\"\\><title>Start Page</title></head><body style=\"background-color: #BBBBBB\"><h1>Start Page</h1><hr><h2>Directories:</h2>";
                sb.append(htmlContent);
                if (folders.size() == 0) // Ha nincs almappa
                {
                    sb.append("<p>There are no subfolders in this folder</p>");
                }
            }
            else if (isStartPage == 0)
            */

            htmlContent = "<html><head><meta charset=\"utf-8\"\\><title>" + pageName + "</title></head><body style=\"background-color: #BBBBBB\"><body><h1><a href=\"";
            sb.append(htmlContent);

            for (int i = 0; i < rootCount - position; i++)
            {
                sb.append("..\\");
            }
            htmlContent = "index.html\">Start Page</a></h1><hr><h2>Directories:</h2><p><a href=\"..\\index.html\"> << </a></p>";
            sb.append(htmlContent);

            if (folders.size() > 0) // Ha van almappa
            {
                for (String folder : folders)
                {
                    htmlContent = "<li><a href=\"" + folder + "\\index.html" + "\">" + folder + "</a></li>";
                    sb.append(htmlContent);
                }
            }

            sb.append("<hr><h2>Images:</h2>");
            if (images.size() == 0) // Ha nincs kép
            {
                sb.append("<p>There are no images in this folder</p>");
            }
            else // Ha van kép
            {
                for (String image : images)
                {
                    String htmlName = image.substring(0, image.indexOf(".")) + ".html";
                    sb.append("<li><a href=\"" + htmlName + "\">" + image + "</a></li>");
                }
            }
            sb.append("</body></html>");

            pw.println(sb.toString());
            sb.delete(0, sb.length() - 1);
        }
        catch (FileNotFoundException e)
        {
            e.printStackTrace();
        }
    }


    // Létrehozza a Start Page-t
    public static void createStartPage(String folderPath)
    {
        // createIndexHtml(folderPath, folderPath, 1);

        String[] subFolders = folderPath.split("\\\\");
        String pageName = subFolders[subFolders.length - 1];

        List<String> images = FolderUtils.getFolderContent(folderPath,"images");
        List<String> folders = FolderUtils.getFolderContent(folderPath,"folders");

        try (PrintWriter pw = new PrintWriter(folderPath + "\\index.html"))
        {
            StringBuilder sb = new StringBuilder();
            String htmlContent;

            htmlContent = "<html><head><meta charset=\"utf-8\"\\><title>" + pageName + "</title></head><body style=\"background-color: #BBBBBB\"><h1>Start Page</h1><hr><h2>Directories:</h2>";
            sb.append(htmlContent);

            if (folders.size() == 0) // Ha nincs almappa
            {
                sb.append("<p>There are no subfolders in this folder</p>");
            }
            else // Ha van almappa
            {
                for (String folder : folders)
                {
                    sb.append("<li><a href=\"" + folder + "\\index.html" + "\">" + folder + "</a></li>");
                }
            }

            sb.append("<hr><h2>Images:</h2>");
            if (images.size() == 0) // Ha nincs kép
            {
                sb.append("<p>There are no images in this folder</p>");
            }
            else // Ha van kép
            {
                for (String image : images)
                {
                    String htmlName = image.substring(0, image.indexOf('.')) + ".html";
                    sb.append("<li><a href=\"" + htmlName + "\">" + image + "</a></li>");
                }
            }

            sb.append("</body></html>");
            pw.println(sb.toString());
            sb.delete(0, sb.length() - 1);
        }
        catch (FileNotFoundException e)
        {
            e.printStackTrace();
        }
    }
}