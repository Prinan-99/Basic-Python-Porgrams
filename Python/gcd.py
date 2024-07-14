def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    print(f"GCD of 48 and 18: {gcd(48, 18)}")
