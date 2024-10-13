import multiprocessing

def square(number):
    return number * number

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Complete the code to use multiprocessing to calculate squares
    with multiprocessing.Pool() as pool:
        results = pool.map(square, numbers)

    print(results)