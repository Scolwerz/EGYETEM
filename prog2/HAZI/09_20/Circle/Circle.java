class Circle
{
    public int radius;

    public Circle(int radius)
    {
        this.radius = radius;
    }

    double kerulet()
    {
        return 2 * Math.PI * this.radius;
    }

    double terulet()
    {
        return this.radius * this.radius * Math.PI;
    }
}
