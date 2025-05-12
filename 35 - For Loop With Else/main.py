# lets use for loop with else 
# python allows us to use else with for loop and while loop 

# example 

for i in range(7):
    print(i)
else:
    print("The program is in else statement and for loop completed succesfully")
# the else block will run only when the for loop runs completely without any interruption

# what if i use break statement there: will it go in for loop

for i in range(7):
    print(i)
    if i == 5:
        break
else:
    print("The program is in else statement and for loop completed succesfully") 
# this will not execute as it will execute only if the loop completes succesfully 

# how can we do it in while loop ? 

x = 1
while(x < 10):
    print("in while loop ", x)
    x = x + 1
else:
    print("Out of while loop")
# same concept: else runs only when while loop finishes normally (without break)
