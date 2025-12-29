def print_formatted(number):
    # your code goes here
    
    for i in range(1, number+1 ):
        biner = bin(i)[2:]
        hexa = hex(i)[2:].upper()
        oktal = oct(i)[2:]
        print(f"{i:>2} {oktal:>2} {hexa:>2} {biner:>2}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)