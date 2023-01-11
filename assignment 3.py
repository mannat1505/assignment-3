# question 1
# Program to count occurances of letters
string_name=str(input("Enter the string : "))
list1=string_name.split()
list_l=[]
for e in list1:
    lower_e=e.lower()
    list_l.append(lower_e)
set1=set(list_l)
dic={}
for el in set1:
    count=list_l.count(el)
    dic.update({el:count})
dic2={}
set2={1,2}
set2.clear()
list2=[]
if len(list1)==1:
    for elements in string_name:
        list2.append(elements)
    for el in list2:
        set2.add(el.lower())
    string_l=string_name.lower()
    for elem in set2:
        dic2.update({elem:string_l.count(elem)})
    print("\nDictionary containing 'Letter':'Letter Count' is shown below:")
    print(dic2)
else:
    print("\nDictionary containing {'Word':'Word Count'} is shown below:")
    print(dic)
#question 2
# Program to get next day of a given day
year = int(input("Input a year: "))

if (year % 400 == 0):
    leapyear = True
elif (year % 100 == 0):
    leapyear = False
elif (year % 4 == 0):
    leapyear = True
else:
    leapyear = False

month = int(input("Input a month [1-12]: "))

if month in (1, 3, 5, 7, 8, 10, 12):
    month_length = 31
elif month == 2:
    if leap_year:
        month_length = 29
    else:
        month_length = 28
else:
    month_length = 30


day = int(input("Input a day [1-31]: "))

if day < month_length:
    day += 1
else:
    day = 1
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1
print("The next date is [yyyy-mm-dd] %d-%d-%d." % (year, month, day))

#question 3
#list of tuples
list1 = list(map(int, input("Enter the numbers separated by space:").split()))

    list2 = []
    for e in list1:
        t = (e, e * e)
        list2.append(t)

    print("\nList containing (n,n^2) is shown below:")
    print(list2)

#question 4
rade_point = int(input("Enter grade points:"))
    dic = {10: "Your grade is 'A+' and Outstanding performance.",
           9: "Your grade is 'A' and Excellent performance.",
           8: "Your grade is 'B+' and Very Good performance.",
           7: "Your grade is 'B' and Good performance.",
           6: "Your grade is 'C+' and Average performance.",
           5: "Your grade is 'C' and Below Average performance.",
           4: "Your grade is 'D' and Poor performance."}

    if 4 <= grade_point <= 10:
        statement = dic.get(grade_point)
        print(statement)
    else:
        print("\nError\nPlease enter grade in range [4,10]")

#question 5
grade_point = int(input("Enter grade points:"))
        dic = {10: "Your grade is 'A+' and Outstanding performance.",
               9: "Your grade is 'A' and Excellent performance.",
               8: "Your grade is 'B+' and Very Good performance.",
               7: "Your grade is 'B' and Good performance.",
               6: "Your grade is 'C+' and Average performance.",
               5: "Your grade is 'C' and Below Average performance.",
               4: "Your grade is 'D' and Poor performance."}

        if 4 <= grade_point <= 10:
            statement = dic.get(grade_point)
            print(statement)
        else:
            print("\nError\nPlease enter grade in range [4,10]")
            #Ques6
            string = "ABCDEFGHIJK"
            j = 0
            while len(string) - j * 2 >= 1:
                print(" " * j, string[0: len(string) - j * 2])
                j += 1
#question 6
repeat = "Y"
            dic = {}
            dic2 = {}

            list = ["Y", "y", "n", "N"]
            while repeat == "Y" or repeat == "y":

                name = str(input("Enter student name:"))
                sid = int(input("Enter student SID:"))
                if sid < 0:
                    print("\nError\nSID can't be negative\n")
                else:

                    dic.update({sid: name})

                    dic2.update({name: sid})

                    repeat = str(input("Enter Y to continue or N to end:"))
                if repeat == "N" or repeat == "n":
                    break
                elif (not (repeat in liste)):
                    print("\nError\nPlease enter valid input['Y' or 'N']")
                    repeat = str(input("\nEnter Y to continue or N to end:"))

            print("\nQ.6(a)")
            print("The Dictionary containing {'SID':'Name'} is shown below")
            print(dic)
            print("\nQ.6(b)")
            list_k = sorted(dic2)
            dic3 = {}
            for ele in list_k:
                dic3.update({dic2.get(ele): ele})
            print("The Dictionary after sorting according to name:")
            print(dic3)

            print("\nQ.6(c)")
            sort_dic = sorted(dic)
            dic4 = {}
            for va in sort_dic:
                dic4.update({va: dic.get(va)})
            print("The Dictionary after sorting according to SID:")
            print(dic4)

            print("\nQ.6(d)")
            enter_sid = int(input("Enter SID to get name of student:"))

            output_name = str(dic.get(enter_sid))

            print(f"Name of student with SID {enter_sid} is {output_name}.")

#question 7
n = int(input("Enter number of elements N in fibonacci series:\n[N must be positive Integer]: N="))

            if n <= 0:
                print("\nError\nNumber of elements in fibonacci series must be integer and greater than zero.")

            else:

                if n == 1:
                    print("\nThe fibonacci series with 1 element is shown below\n[1]")
                    print("\nAverage of given fibonacci series is", 1)

                elif n == 2:
                    print("\nThe fibonacci series with 2 element is shown below\n[1,1]")
                    print("\nAverage of given fibonacci series is", 1)

                else:

                    list1 = [1, 1]

                    a = 1
                    b = 1

                    for i in range(n - 2):
                        s = a + b
                        list1.append(s)
                        a = b
                        b = s

                    print(f"\nThe fibonacci series with {n} elements is shown below:")
                    print(list1)

                    sum = 0  # intial sum=0

                    for num in list1:
                        sum = sum + num
                    average = (sum / n)

                    two_decimal = "{:.2f}".format(average)

                    print(f"\nAverage of given fibonacci series is {two_decimal)
#question 8
set1 = {1, 2, 3, 4, 5}
                    set2 = {2, 4, 6, 8}
                    set3 = {1, 5, 9, 13, 17}

                    print(f"Set1= {set1}\nSet2= {set2}\nSet3= {set3}")
                    print("\nQ.8(a)")
                    print("\nA new Set of all 'elements that are in Set1 and Set2 but not both' is:")
                    set_sym_dif = set1.symmetric_difference(set2)
                    print(set_sym_dif)

                    print("\nQ.8(b)")
                    print("\nA new set of all elements that are 'in only one of the three sets Set1,Set2 and Set3' is:")
                    set_u1 = set1.union(set2)

                    set_uf = set_u1.union(set3)

                    set_i1 = set1.intersection(set2)

                    set_if = set_i1.intersection(set3)

                    set_12 = set1.intersection(set2)

                    set_23 = set2.intersection(set3)

                    set_13 = set1.intersection(set3)

                    set_f1 = set_uf - set_12 - set_23 - set_13
                    print(set_f1)

                    print("\nQ.8(c)")
                    set_c1 = set_12.union(set_23)

                    set_c2 = set_c1.union(set_13)

                    set_final = set_c2 - set_if

                    print("\nA new set of elements that are 'exactly in two of the sets Set1, Set2 and Set3' is:")
                    print(set_final)

                    print("\nQ.8(d)")
                    set_d = {1, 2}
                    set_d.clear()
                    for i in range(1, 11):
                        set_d.add(i)
                    set_new = set_d - set1

                    print("\nA new set of all Integers in the 'range 1 to 10' that are 'not in Set1' is:")
                    print(set_new)

                    print("\nQ.8(e)")
                    set_e = set_d - set_uf
                    print("\nA new set of all Integers in the range 1 to 10 that are not in Set1,Set2 and Set3.")
                    print(set_e)
    


