import random
print('This is a guess game where you get to choose a number 5 times and see if you are correct \nif you get it correctly 10 points is added to your points \nelse if you get it wrongly 1 point is deducted from your points')
point = 0
for i in range(5):
    choice = random.randint(1,2)
    user = int(input('Enter a number: '))
    
    if user == choice:
        point += 10
        print('CORRECT')
    else:
        point -= 1
        print('INCORRECT')
    print(f' Your choice is {user} but Computer chose {choice}')
print(f'Your overall point is {point}')
