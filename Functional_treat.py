def input_data(data_lst, rows_list):
    while True:
        print("1. Input data in 1D array")
        print("2. Input data in 2D array")
        print("3. Back")
        
        select = int(input("Enter your choice: "))
        match select:
            case 1:
                data_lst.clear()
                rows_list.clear()
                user_data = [int(x) for x in input("Enter elements in 1D array (separated by space): ").split()]
                data_lst.extend(user_data)
                print("1d array is successfully loaded")
            case 2:
                data_lst.clear()
                rows_list.clear()
                rows = int(input("Enter the number of rows: "))
                columns = int(input("Enter the number of columns: "))
                
                for _ in range(rows):
                    current_row = []
                    for _ in range(columns):
                        ele = int(input("Enter elements: "))
                        current_row.append(ele)
                    rows_list.append(current_row)
                print("2d array is successfully loaded")
            case 3:
                return
            case _:
                print("Invalid choice")


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)


def sort_asc(lst):
    sorted_list = sorted(lst)
    return sorted_list
      

         
def sort_desc(lst):
    sorted_list = sorted(lst)
    return sorted_list
    

    
def data_stat():
    if rows_list:
        flat_list = [item for row in rows_list for item in row]
        return min(flat_list), max(flat_list), sum(flat_list), sum(flat_list) / len(flat_list)
    elif data_lst:
        return min(data_lst), max(data_lst), sum(data_lst), sum(data_lst) / len(data_lst)







print("Welcome to the Data Analyzer and Transformer program")
data_lst = []
rows_list = []
while True:
    print("Menu: ")
    print("1. Input data")
    print("2. Display Data Summary")
    print("3. Calculate factorial")
    print("4. Filter Data by Threshold")
    print("5. Sort data")
    print("6. Display Data Statistics")
    print("7. Exit")

    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            input_data(data_lst, rows_list)

        case 2:
            if not data_lst and not rows_list:
                print("No data available")
            if data_lst:
               target_list = data_lst
            else:

                flat_list = []
                for rows in rows_list:
                    for items in rows:
                        flat_list.append(items)
                target_list = flat_list
                    
            total_ele = len(target_list)
            minimum = min(target_list)
            maximum = max(target_list)
            total = sum(target_list)
            avg = total / total_ele
            print(f"Total Elements: {total_ele}")
            print(f"Minimum value: {minimum}")
            print(f"Maximum value: {maximum}")
            print(f"Sum of elements: {total}")
            print(f"Average values: {avg}")

        case 3:
            num = int(input("Enter a number for factorial: "))
            if num < 0:
                print("Enter number in positive")
            else:
                print(f"Factorial of {num} is {factorial(num)}")

        case 4:
            threshold = int(input("Enter a threshold value to filter out the data above this value: "))
            if data_lst:
                filtered_list = list(filter(lambda x: x > threshold, data_lst))
                print(f"filtered data above {threshold}: {filtered_list}")

            elif rows_list:
                flat = [item for row in rows_list for item in row]
                filtered_list = list(filter(lambda x: x > threshold, flat))
                print(f"Filtered data above {threshold}: {filtered_list}")

            else:
                print("No data available for filter")
        case 5:
            while True:
                if rows_list:
                    print("Sorting is only available in 1d array")
                    break
                if not data_lst:
                    print("Please enter elements firstly")
                    break

                print("1. Ascending")
                print("2. Descending")
                print("3. Back")
                option = int(input("Enter you choice: "))
                match option:
                    case 1:
                        asc = sort_asc(data_lst)
                        print(f"Sorted array: {asc}")
                    case 2: 
                        desc = sort_desc(data_lst)
                        print(f"Sorted array: {desc}")
                    case 3:
                        break
                    case _:
                        print("Invalid option")
                
        case 6:
            if not data_lst and not rows_list:
                print("No data loaded yet. ")
                continue
            mini, maxim, add, average = data_stat()   
            print(f"Minimum: {mini}")
            print(f"Maximum: {maxim}")
            print(f"Total: {add}")
            print(f"Average: {average}")
        case 7:
            print("Thank you....")
            break
        case _:
            print("Invalid choice")




            

                
            

