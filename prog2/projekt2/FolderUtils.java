import java.io.File;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class FolderUtils
{
    // Rekurzív fájlbejárás ami visszaadja a fájlok elérési útját a "folders" listában
    public static List<String> traverseFolder(File folder, List<String> result)
    {
        File[] files = folder.listFiles();
        if (files != null)
        {
            for (File file : files)
            {
                if (file.isDirectory())
                {
                    result.add(file.toString() + File.separator);
                    System.out.println("### Mappa: " + file.toString() + File.separator);
                    traverseFolder(file, result);
                }
            }
        }
        return result;
    }

    // Visszaadja egy fájl típusát (html / kép / mappa)
    public static String getFileType(File file)
    {
        if (file.isDirectory())
            return "folder";
        else if (file.isFile())
        {
            String strFile = file.toString().toLowerCase();
            if (strFile.endsWith(".html"))
                return "html";
            else if ((strFile.endsWith(".png") || strFile.endsWith(".jpg") || strFile.endsWith(".jpeg") || strFile.endsWith(".gif")))
                return "image";
        }
        return "";
    }

    // Visszaadja egy adott mappa tartalmát (almappák, képek, html file-ok) egy listában
    public static List<String> getFolderContent(String folder, String type)
    {
        List<String> result = new ArrayList<>();

        File file = new File(folder);
        File[] subFiles = file.listFiles();
        if (subFiles != null)
        {
            for (File subFile : subFiles)
            {
                String[] parts = subFile.toString().split(File.separator + File.separator);
                String fileName = parts[parts.length-1]; // .substring(0,parts[parts.length-1].lastIndexOf(".") - ha nem kell a kiterjesztés

                switch (type.toLowerCase() + getFileType(subFile))
                {
                    case "folders" + "folder" : result.add(fileName); break;
                    case "images"  + "image"  : result.add(fileName); break;
                    case "htmls"   + "html"   : result.add(fileName); break;
                }
            }
        }
        Collections.sort(result);
        return result;
    }

    // Kitörli a .html file-okat
    public static void deleteHtmlFiles(List<String> folders)
    {
        for (int i = 0; i < folders.size(); i++)
        {
            List<String> htmls = getFolderContent(folders.get(i),"htmls");

            for (int j = 0; j < htmls.size(); j++)
            {
                File file = new File(folders.get(i) + htmls.get(j));
                file.delete();
            }
        }

        System.out.println("######## HTML FÁJLOK TÖRLÉSE SIKERES ########");
    }
}