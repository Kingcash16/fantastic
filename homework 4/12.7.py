#Joshua Jaja ID:1543343 Zylab 12.7
def get_age():
    a = int(input())
    if(a>=18 and a<=75):
        return a
    else:
        raise ValueError("Invalid age.")

def fat_burning_heart_rate(a):
    return ((70 / 100) * (220 - a))

if __name__ == '__main__':
    try:
        a = get_age()
        print("Fat burning heart rate for a",a,"year-old:",fat_burning_heart_rate(a),"bpm")
    except ValueError as ve:
        print(ve.args[0])
        print("Could not calculate heart rate info.\n")