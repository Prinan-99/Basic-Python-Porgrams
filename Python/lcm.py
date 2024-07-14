def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

if __name__ == "__main__":
    print(f"LCM of 4 and 5: {lcm(4, 5)}")
