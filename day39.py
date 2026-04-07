# KBC Solution

Questions = [["Which language was used to creat FB ?", "Python", "Java", "C++", "php"],["Which language was used to creat FB ?", "Python", "Java", "C++", "php"],["Which language was used to creat FB ?", "Python", "Java", "C++", "php"],["Which language was used to creat FB ?", "Python", "Java", "C++", "php"],["Which language was used to creat FB ?", "Python", "Java", "C++", "php"],["Which language was used to creat FB ?", "Python", "Java", "C++", "php"],["Which language was used to creat FB ?", "Python", "Java", "C++", "php"],["Which language was used to creat FB ?", "Python", "Java", "C++", "php"],["Which language was used to creat FB ?", "Python", "Java", "C++", "php"],["Which language was used to creat FB ?", "Python", "Java", "C++", "php"],["Which language was used to creat FB ?", "Python", "Java", "C++", "php"]]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 10000000]

money = 0

for i in range(0, len(Questions)):
    Question = Questions[i]
    print("kon banega crorepati")
    print(f"Question for Rs. {levels[i]} :")
    print(f"a. {Question[1]}  b. {Question[2]}  ")
    print(f"c. {Question[3]}  d. {Question[4]}  ")
    answer = input("Enter your answer ( 1 - 4 ): ")
    if(answer == "1"):
        print(f"Correct answer you won Rs. {levels[i]} ")
        if ( i == 4 ):
            money = 10000
        elif( i == 9 ):
            money = 320000
        elif( i == 10 ):   
            money = 10000000
    else:
        print("Wrong answer")
        break
    
print(f"Your final amount is Rs. {money}")