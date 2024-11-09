public class Main
{
    public static void main(String[] args)
    {
        HardDisk hd1 = new HardDisk("Toshiba", 20.0);
        HardDisk hd2 = new HardDisk("Seagate", 10.0);

        System.out.println(hd1);
        System.out.println(hd1.getManufacturer());
        System.out.println(hd1.getCapacity());
        System.out.println(hd1.getUsedSpace());
        System.out.println(hd1.getFreeSpace());
        System.out.println(hd1.isBiggerThan(hd2));
        boolean done = hd1.download(4.7);
        System.out.println(done);
        System.out.println(hd1);
        System.out.println(hd1.getFreeSpace());
        done = hd1.download("18.0");
        System.out.println(done);
        System.out.println(hd1.getFreeSpace());
    }
}