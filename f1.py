import csv

laptimes = []
#laptimes = [lap + 60 for lap in laptimes]

pits = []

def time_format(time):
    minutes = int(time // 60)
    seconds = time % 60
    return f"{minutes}:{seconds:.3f}"

def read_laptimes():
    laptimes = []
    with open('laptimes.csv', 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        next(reader)
        previous_value = 0
        previous_row = None

        for row in reader:
            current_value = int(row[4])
            if current_value > previous_value:
                if previous_row:
                    laptimes.append(float(previous_row[8]))
                previous_value = current_value
            previous_row = row
    return laptimes

def find_pits(laptimes):
    avg_laptime = sum(laptimes) / len(laptimes)
    pits = [i for i, lap in enumerate(laptimes) if lap >= 1.077 * avg_laptime]
    return pits

def calc_racetime(laptimes):
    total_seconds = sum(laptimes)
    return time_format(total_seconds)

def calc_stints(laptimes):
    stint_avgs = []
    stint_mins = []
    stint_maxs = []
    start = 1
    for pit in pits:
        stint = laptimes[start:pit-1]
        if stint:
            stint_avgs.append(sum(stint) / len(stint))
            stint_mins.append(min(stint))
            stint_maxs.append(max(stint))
        start = pit + 1
    last_stint = laptimes[start:]
    if last_stint:
        stint_avgs.append(sum(last_stint) / len(last_stint))
        stint_mins.append(min(last_stint))
        stint_maxs.append(max(last_stint))
    return (stint_avgs, stint_mins, stint_maxs)



laptimes = read_laptimes()
pits = find_pits(laptimes)
print("Total race time:", calc_racetime(laptimes))
for i, (avg, min, max) in enumerate(zip(*calc_stints(laptimes)), start=1):
    print(f"Stint {i}: {time_format(avg)}   ({time_format(min)} - {time_format(max)})")
