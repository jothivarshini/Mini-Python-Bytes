score=0

print('''Welcome! Let's test whether you are a true Potterhead like you claim to be.
We just need you to answer these questions that have been printed on this piece
of parchment for us''')

score = 0

print("Question 1:\n")
print("How did Harry arrive at the Dursley's? \n a.Adoption  b.On the doorstep  c.Through a flight  d.Given away  \n")
ans = input("Answer :  ")
if ans == "b":
    score += 1
    print("That is correct! You're becoming a wizard")
else:
    print("Ooh, that isn't right! Let's see if you get the next one...")
    

print("Question 2:\n")
print("What was Harry's age when he knew about the wizarding world? \n a.11 b.5 c.10 d.7")
ans = input("Answer : ")
if ans == "a":
    score +=1
    print ("That is correct! One point to your House")
else:
    print("Ooh, that isn't right! It's okay, keep trying...")


print("Question 3:\n")
print("What was the name of the letter that Ronald Weasley received? \n a.Letter  b.Parchment  c.Daily Prophet  d.Howler \n")
ans = input("Answer : ")
if ans == "d":
    score +=1
    print ("That is correct!You know about the wizarding world more than we thought! \n")
else:
    print("That is incorrect! Try again next time. \n")



if score == 3:
    print ("Congratulations! You have passed to round 2! Here are some questions that can get a bit more tricky")
else:
    print("We're sorry to say this Muggle, but you haven't passed this round. Good luck on your next try
