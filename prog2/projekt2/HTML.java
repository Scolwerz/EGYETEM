import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class HTML
{

    // ####################################################
    // Ez az eljaras hozza letre a html-fajlokat a kepekhez
    // ####################################################
    public static void createHtmlForPhotos(String photoPath, String photo)
    {
        int dotPosition = photo.indexOf(".");
        String photoWithoutExtension = photo.substring(0, dotPosition);
        String htmlOfPhoto = photoWithoutExtension + ".html";

        try
        {
            PrintWriter pr = new PrintWriter(photoPath + htmlOfPhoto);
        }
        catch (FileNotFoundException e)
        {
            e.printStackTrace();
        }
    }

    // #########################################################
    // Ez az eljaras modositja a kepekhez tartozo html file-okat
    // #########################################################
    public static void changeHtmlForPhoto (String photoPath, String photo, String photoRootDir)
    {
        List<String> htmlFiles = Directory.listHtml(photoPath);

        int index = 0;
        int position = 0;
        int dotPosition = photo.indexOf(".");

        String[] folders = photoPath.split(File.separator + File.separator);
        String pageName = folders[folders.length-1];
        String photoWithoutExtension = photo.substring(0, dotPosition);
        String htmlOfPhoto = photoWithoutExtension + ".html";

        htmlFiles.remove("index.html");

        for (int i = 0; i < htmlFiles.size(); i++)
        {
            if (htmlFiles.get(i).equals(htmlOfPhoto))
            {
                index = i;
            }
        }

        String[] rootDirArr = photoRootDir.split(File.separator + File.separator);
        String[] pathArr = photoPath.split(File.separator + File.separator);
        position = pathArr.length - rootDirArr.length;


        try (PrintWriter writer = new PrintWriter(photoPath + htmlOfPhoto))
        {
            StringBuilder sb = new StringBuilder();

            sb.append(String.format("""
                <html>
                    <head>"
                        <meta charset="utf-8"/>
                        <title> %s </title>
                    </head>"
                    <body style="background-color: #FFFFFF">
                    <body>
                    <h1> <a href="
                """, pageName));

            for (int i = 0; i < position; i++)
            {
                sb.append("..\\");
            }

            sb.append("""
                index.html>Start Page</a>
                </h1>"
                <hr>;
                <p><a href="index.html">^^</a></p>
                """);
            if (htmlFiles.size() == 1)
            {
                sb.append(String.format("""
                <p> <a href="%s"> << </a> %s <a href="%s"> >> </a> </p>
                <p> <a href="%s"> <img alt="" src="%s"  width="500" height="500"/> </a> </p>
                """,htmlFiles.get(index),photo,htmlFiles.get(index),htmlFiles.get(index),photo));
            }
            else if (index == 0)
            {
                sb.append(String.format("""
                <p> <a href="%s"> << </a> %s <a href="%s"> >> </a> </p>
                <p> <a href="%s"> <img alt="" src="%s"  width="500" height="500"/> </a> </p>
                """,htmlFiles.get(index),photo,htmlFiles.get(index+1),htmlFiles.get(index+1),photo));

            }
            else if (index == htmlFiles.size() - 1)
            {
                sb.append(String.format("""
                <p> <a href="%s"> << </a> %s <a href="%s"> >> </a> </p>
                <p> <img alt="" src="%s"  width="500" height="500"/> </a> </p>
                """,htmlFiles.get(index-1),photo,htmlFiles.get(index),photo));
            }
            else
            {
                sb.append(String.format("""
                <p> <a href="%s"> << </a> %s <a href="%s"> >> </a> </p>
                <p> <a href="%s"> <img alt="" src="%s"  width="500" height="500"/> </a> </p>
                """,htmlFiles.get(index-1),photo,htmlFiles.get(index+1),htmlFiles.get(index+1),photo));
            }

            sb.append("\t</body>\n");
            sb.append("</html>");

            writer.println(sb.toString());
        }
        catch (FileNotFoundException e)
        {
            e.printStackTrace();
        }
    }

    // ##############################################
    // Ez az eljaras hozza letre az index.html file-t
    // ##############################################
    public static void createIndexHtml(String photoPath, String photoRootDir)
    {
        String current = photoPath + "index.html";

        String[] folders = photoPath.split(File.separator + File.separator);
        String pageName = folders[folders.length - 1];

        List<String> files = Directory.getPhotos(photoPath);
        List<String> directories = Directory.listDirectories(photoPath);

        int position;
        String[] rootDirArr = photoRootDir.split(File.separator + File.separator);
        String[] pathArr = photoPath.split(File.separator + File.separator);
        position = pathArr.length - rootDirArr.length;

        try (PrintWriter writer = new PrintWriter(current))
        {
            StringBuilder sb = new StringBuilder();
            sb.append(String.format("""
                <html>
                    <head>
                        <meta charset="utf-8"/>
                        <title>%s</title>
                    </head>
                    <body style="background-color: #FFFFFF">
                    <body>
                        <h1> <a href="
                """, pageName));

            for (int i = 0; i < position; i++)
            {
                sb.append("..\\");
            }

            sb.append("""
                index.html">Start Page</a>
                    </h1>
                    <hr>
                    <h2>Directories:</h2>
                    <p> <a href="../index.html">^^</a> </p>
                """);

            for (String directory : directories)
            {
                sb.append("\t\t<p> <a href=\"" + directory + "\\index.html" + "\">" + directory + "</a></p>\n");
            }

            if (directories.size() == 0)
            {
                sb.append("\t\t<p>There are no subdrirectories in this directory</p>\n");
            }

            sb.append("\t<hr>\n");
            sb.append("\t<h2>Photos:</h2>\n");

            if (files.size() > 0)
            {
                for (String file : files)
                {
                    int dotPosition = file.indexOf(".");
                    String photoWithoutExtension = file.substring(0, dotPosition);
                    String link = photoWithoutExtension + ".html";
                    sb.append("\t\t<p> <a href=\"" + link + "\">" + file + "</a> </p>\n");
                }
            }

            if (files.size() == 0)
            {
                sb.append("\t\t<p>There are no files in this directory</p>\n");
            }

            sb.append("\t</body>\n");
            sb.append("</html>");

            writer.println(sb.toString());
        }
        catch (FileNotFoundException fileNotFoundException)
        {
            fileNotFoundException.printStackTrace();
        }
    }

    // ######################################
    // Ez az eljaras hozza letre a kezdolapot
    // ######################################
    public static void start(String photoPath)
    {
        String current = photoPath + "\\index.html";
        String[] folders = photoPath.split(File.separator + File.separator);
        String pageName = folders[folders.length - 1];

        List<String> files = Directory.getPhotos(photoPath);
        List<String> directories = Directory.listDirectories(photoPath);

        try (PrintWriter writer = new PrintWriter(current))
        {
            StringBuilder sb = new StringBuilder();

            sb.append("""
                <html>
                    <head>
                        <meta charset="utf-8"/>
                        <title>%s</title>
                    </head>
                    <body style="background-color: #FFFFFF">
                    <body>
                        <h1>Start Page</h1>
                    <hr>
                    <h2>Directories:</h2>
                    <p> <a href="../index.html">^^</a> </p>
                """);

            if (directories.size() == 0)
            {
                sb.append("\t\t<p>There are no subdirectories in this directory</p>\n");
            }
            else
            {
                for (String directory : directories)
                {
                    sb.append("\t\t<p><a href=\"" + directory + "\\index.html" + "\">" + directory + "</a></p>\n");
                }
            }

            sb.append("\t<hr>\n\t<h2>Photos:</h2>\n");
            if (files.size() == 0)
            {
                sb.append("\t\t<p>There are no files in this directory</p>\n");
            }
            else
            {
                for (String file : files)
                {
                    int a = file.indexOf('.');
                    String newName = file.substring(0, a);
                    String link = newName + ".html";
                    sb.append("\t\t<p><a href=\"" + link + "\">" + file + "</a></p>\n");
                }
            }

            sb.append("\t</body>\n");
            sb.append("</html>");

            writer.println(sb.toString());
        }
        catch (FileNotFoundException fileNotFoundException)
        {
            fileNotFoundException.printStackTrace();
        }
    }
}