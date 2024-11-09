class Gomb
{
    public int radius;

    public Gomb(int radius)
    {
        this.radius = radius;
    }

    double felszin()
    {
        return 4 * Math.PI * this.radius * this.radius;
    }

    double terfogat()
    {
        return (4 * Math.PI * this.radius * this.radius * this.radius) / 3;
    }
}
