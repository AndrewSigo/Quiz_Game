print('Welcome to my quiz game!')

play = input('Do you want to play? ')

if play.lower() != 'yes':
    quit()
print('Okay! Lets play!')
score = 0

answer = input('What does CPU stand for? ')
if answer.lower() == 'central processing unit':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input('What does GPU stand for? ')
if answer.lower() == 'graphics processing unit':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input('What does RAM stand for? ')
if answer.lower() == 'random access memory':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input('What does SSD stand for? ')
if answer.lower() == 'solid state drive':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

print('You got ' + str(score) + ' questions correct!')
print('You got ' + str((score / 4) * 100) + '%.')