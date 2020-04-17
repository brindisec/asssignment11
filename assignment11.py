from Methods import bubble_sort, merge_sort, quick_sort, selection_sort
import random
import time
random.seed()

def main():
    while True:
        methods = [bubble_sort, merge_sort, quick_sort, selection_sort]
        lis = []
        method = None

        while True:
            print("What algorithm would you like to use: ")
            print("1. Bubble Sort")
            print("2. Selection Sort")
            print("3. Merge Sort")
            print("4. Quick Sort")
            print("5. Exit Program")
            value = int(input(("=>")))
            if value == 5 :
                print("The program will now exit")
                exit()
            if 1 <= value <= 4:
                method = methods[value - 1]
                break
            else:
                print("Please try again")

        size = int(input("Please enter the size of the list"))
        list = [random.randrange(1, 100001) for i in range(size)]
        start = time.time()
        list = method(list)
        end = time.time() - start
        print("The sorted list is: ", list)
        print("The sort took", end, "seconds")

if __name__ == '__main__':
    main()

