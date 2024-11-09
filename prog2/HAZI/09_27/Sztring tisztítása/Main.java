public class Main
{
    public static String cleanURL(String inputURL)
    {
        return inputURL.replaceAll("\\s", "");
    }
    public static void main(String[] args)
    {
        String url1 = "192.20.246.138:\n 6666";
        String url2 = "206.130.99.82:\n8080";

        String cleanedUrl1 = cleanURL(url1);
        String cleanedUrl2 = cleanURL(url2);

        System.out.println(url1+" - "+cleanedUrl1+"\n"+url2+" - "+cleanedUrl2);
    }
}