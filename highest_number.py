
#define 5 variables 
#compare num1 with num2-5
    #if num1 greater print num1
#compare num2 with num1-5 except 2
    #if num2 greater print num2
#compare num3 with num1-5 except 3
    #if num3 greater print num3
#compare num4 with num1-5 except 4
    #if num4 greater print num4
#compare num5 with num1-4 
    #if num5 greater print num5


def highest_number(num1, num2, num3, num4, num5):
    if num1 >= num2 and num1 >= num3 and num1 >= num4 and num1 >= num5:
        print("highest number:", num1) 
    elif num2 >= num1 and num2 >= num3 and num2 >= num4 and num2>= num5:
        print("highest number:", num2) 
    elif num3 >= num1 and num3 >= num2 and num3 >= num4 and num3 >= num5: 
        print("highest number:", num3)
    elif num4 >= num1 and num4 >= num2 and num4 >= num3 and num4 >= num5:
        print("highest number:", num4)
    elif num5 >= num1 and num5 >= num2 and num5 >= num3 and num5 >= num4:
        print("highest number:", num5)

highest_number(
    num1 = int(input("1st:")),
    num2 = int(input("2nd:")),
    num3 = int(input("3rd:")),
    num4 = int(input("4th:")),
    num5 = int(input("5th:"))
    )