class Teglalap
{
    public int length;
    public int width;

    public Teglalap(int length, int width)
    {
        this.length = length;
        this.width = width;
    }

    int kerulet()
    {
        return 2 * (this.length + this.width);
    }

    int terulet()
    {
        return this.length * this.width;
    }
}