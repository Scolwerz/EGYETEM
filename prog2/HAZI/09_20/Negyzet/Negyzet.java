class Negyzet
{
    public int length;

    public Negyzet(int length)
    {
        this.length = length;
    }

    int kerulet()
    {
        return 4 * this.length;
    }

    int terulet()
    {
        return this.length * this.length;
    }
}