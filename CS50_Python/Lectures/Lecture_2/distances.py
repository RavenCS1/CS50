distances={
    "Voyager 1":163, 
    "Voyager 2":136,
    "Pioneer 10":80,
    "New Horizons":58,
    "Pioneer 11":44
}

def main():
    for distance in distances:
        print(f"{distances[distance]} AU is {convert(distances[distance])} m")


def convert(au):
    return au*149597870700

main()