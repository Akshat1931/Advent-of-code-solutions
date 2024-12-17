from collections import Counter

def get_steps(list1, list2):
    totals = [abs(value - partner_item)
              for value, partner_item in zip(list1, list2)]
    print("Sum Total:", sum(totals))

def read_input(file_name):
    list1, list2 = zip(*((int(num1), int(num2))
                       for num1, num2 in (line.split() for line in open(file_name))))
    return sorted(list1), sorted(list2)

def part_2(list1, list2):
    counts = Counter(list2)
    total_sum = sum(number * counts[number] for number in list1)
    print(f"Sum of counts: {total_sum}")

list1, list2 = read_input("Q1\hi.txt")  

get_steps(list1, list2)  
part_2(list1, list2)     
