#Algorithm to determine odd or even number

def determine_odd_even():
    num = int(input("Enter a number"))
    mod = num % 2
    print(mod == 0)

new_number = determine_odd_even()

#Algorithm task 2 less than 100

def list_check ():
      
    for x in list:
        if x >= check:
            print(False)
            break
        else:
            print(True)

list = [10, 30, 80, 30]
check = 100 

checking_list = list_check()


#Algorithm task 3 Repeated Names

def repeated_names():
    for i in range(0, len(list)):
        for j in range(i+1, len(list)):
            if(list[i] == list[j]):
                print(True)
            else:
                print(False)
list = ["John", "Kate", "John", "David"]
        
def repeat_name():

    for i in range(0, len(list)):
        for j in range(i+1, len(list)):
            if(list[i] == list[j]):
                print(True)
                break
            else:
                print(False)



name_check = repeat_name()


#Algorith task 4 sort numbers

number_array = [3, 5, 6, 7, 8, 3 ,4, 6, 7, 4]
new_array = []

while number_array:
    minimum = number_array[0]
    for x in number_array:
        if x < minimum:
            minimum = x
    new_array.append(minimum)
    number_array.remove(minimum)

print(new_array)

for i in range(len(number_array)):
    for j in range(i+1, len(number_array)):
        if number_array[i] > number_array[j]:
            number_array[i], number_array[j] = number_array[j], number_array[i]
print(number_array)








  











