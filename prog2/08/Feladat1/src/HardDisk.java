class HardDisk
{
    private String manufacture;
    private double capacity;
    private double used;

    public HardDisk(String manufacture, double capacity)
    {
        this.manufacture = manufacture;
        this.capacity = capacity;
        this.used = 0.0;
    }

    @Override
    public String toString() {
        return String.format("%s(cap: %.1f GB, used: %.1f GB)", this.manufacture, this.capacity, this.used);
    }
    public String getManufacturer() {
        return this.manufacture;
    }
    public double getCapacity() {
        return this.capacity;
    }
    public double getUsedSpace() {
        return this.used;
    }
    public double getFreeSpace() {
        return this.capacity - this.used;
    }
    public boolean download(double size) {
        if (size > this.getFreeSpace()) return false;
        this.used += size;
        return true;
    }
    public boolean download(String sizeStr) {
        double size = Double.parseDouble(sizeStr);
        return download(size);
    }
    public boolean isBiggerThan(HardDisk other) {
        return this.capacity > other.capacity;
    }
}