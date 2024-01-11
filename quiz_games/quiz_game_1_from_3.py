
name = input("Enter Your name: ")
print(f"Hello {name}")
print("This is a quiz game. \nThe purpose of this game is to educate and entertain the people. "
      "\nEvery time when You answer correctly You earn 5 points! "
      "\nIn the end You will have opportunity to learn more about the objects of the questions.")
print(f"Good luck {name}!")

points_counter = 0
wrong_answers_counter = 0
correct_answers_counter = 0

print("Question number: 1")
print("Which is the capital city of New Zealand? \na) Auckland \nb) Wellington \nc) Rotorua")
answer = input("Type Your answer with a, b or c: ")
if answer == "b":
    points_counter += 5
    correct_answers_counter += 1
    print("Correct! You earned 5 points!")
else:
    wrong_answers_counter += 1
    print("Sorry, incorrect answer!")

print("Question number: 2")
print("Which is the smallest country in the world? \na) Nauru \nb) Monaco \nc) Vatican City")
answer = input("Type Your answer with a, b or c: ")
if answer == "c":
    points_counter += 5
    correct_answers_counter += 1
    print("Correct! You earned 5 points!")
else:
    wrong_answers_counter += 1
    print("Sorry, incorrect answer!")

print("Question number: 3")
print("Which is the largest Sea in the world? \na) Black Sea \nb) Coral Sea \nc) Philippine Sea")
answer = input("Type Your answer with a, b or c: ")
if answer == "c":
    points_counter += 5
    correct_answers_counter += 1
    print("Correct! You earned 5 points!")
else:
    wrong_answers_counter += 1
    print("Sorry, incorrect answer!")

print("Question number: 4")
print("Which is the most populated city? \na) Tokyo, Japan \nb) Delhi, India \nc) Shanghai, China")
answer = input("Type Your answer with a, b or c: ")
if answer == "a":
    points_counter += 5
    correct_answers_counter += 1
    print("Correct! You earned 5 points!")
else:
    wrong_answers_counter += 1
    print("Sorry, incorrect answer!")

print("Question number: 5")
print("Which Year Adolf Hitler commits suicide? \na) 1944 \nb) 1947 \nc) 1945")
answer = input("Type Your answer with a, b or c: ")
if answer == "c":
    points_counter += 5
    correct_answers_counter += 1
    print("Correct! You earned 5 points!")
else:
    wrong_answers_counter += 1
    print("Sorry, incorrect answer!")

print("Question number: 6")
print("When the Berlin wall fall? \na) 1989 \nb) 1991 \nc) 1887")
answer = input("Type Your answer with a, b or c: ")
if answer == "a":
    points_counter += 5
    correct_answers_counter += 1
    print("Correct! You earned 5 points!")
else:
    wrong_answers_counter += 1
    print("Sorry, incorrect answer!")

print("Question number: 7")
print("How many states in USA? \na) 54 \nb) 50 \nc) 52")
answer = input("Type Your answer with a, b or c: ")
if answer == "b":
    points_counter += 5
    correct_answers_counter += 1
    print("Correct! You earned 5 points!")
else:
    wrong_answers_counter += 1
    print("Sorry, incorrect answer!")

print("Question number: 8")
print("How many capital cities Danube river passing through? \na) 4 \nb) 3 \nc) 5")
answer = input("Type Your answer with a, b or c: ")
if answer == "a":
    points_counter += 5
    correct_answers_counter += 1
    print("Correct! You earned 5 points!")
else:
    wrong_answers_counter += 1
    print("Sorry, incorrect answer!")

print("Question number: 9")
print("Odysseus is the god of what? \na) War \nb) He is a king and hero \nc) Sun ")
answer = input("Type Your answer with a, b or c: ")
if answer == "b":
    points_counter += 5
    correct_answers_counter += 1
    print("Correct! You earned 5 points!")
else:
    wrong_answers_counter += 1
    print("Sorry, incorrect answer!")

print("Question number: 10")
print("Where come from the tennis player Novak Djokovic? \na) Serbia \nb) Russia \nc) Slovenia")
answer = input("Type Your answer with a, b or c: ")
if answer == "a":
    points_counter += 5
    correct_answers_counter += 1
    print("Correct! You earned 5 points!")
else:
    wrong_answers_counter += 1
    print("Sorry, incorrect answer!")

print("Question number: 11")
print("Where was invented the World Wide Web (WWW)? \na) Norway \nb) USA \nc) England")
answer = input("Type Your answer with a, b or c: ")
if answer == "c":
    points_counter += 5
    correct_answers_counter += 1
    print("Correct! You earned 5 points!")
else:
    wrong_answers_counter += 1
    print("Sorry, incorrect answer!")

print("Question number: 12")
print("In which year the European Union was established? \na) 1993 \nb) 1991 \nc) 1995")
answer = input("Type Your answer with a, b or c: ")
if answer == "a":
    points_counter += 5
    correct_answers_counter += 1
    print("Correct! You earned 5 points!")
else:
    wrong_answers_counter += 1
    print("Sorry, incorrect answer!")

print("Question number: 13")
print("What was the official money value of Greece? \na) Dinar \nb) Drachma \nc) Lev")
answer = input("Type Your answer with a, b or c: ")
if answer == "b":
    points_counter += 5
    correct_answers_counter += 1
    print("Correct! You earned 5 points!")
else:
    wrong_answers_counter += 1
    print("Sorry, incorrect answer!")

print("Question number: 14")
print("Which is the capital city of Bulgaria? \na) Sofia \nb) Belgrade \nc) Athens")
answer = input("Type Your answer with a, b or c: ")
if answer == "a":
    points_counter += 5
    correct_answers_counter += 1
    print("Correct! You earned 5 points!")
else:
    wrong_answers_counter += 1
    print("Sorry, incorrect answer!")

print(f"{name} You earned {points_counter} points!")
success_percentage = correct_answers_counter * 100 / 15
if success_percentage < 50:
    print(f"Sorry {name}, Your success rate is {success_percentage}%! \nGood luck next time!")
elif 50 < success_percentage <= 80:
    print(f"Very good {name}, Your success rate is {success_percentage}%!"
          f" \nStill not perfect, but You can do it to the top!")
else:
    print(f"Excellent {name}, Your success rate is {success_percentage}%! \nYou are the best!")

information = "1 - Wellington has been the capital of New Zealand since 1865. " \
              "\nNew Zealand's first capital city was Old Russell (Okiato) in 1840–41. " \
              "\nAuckland was the second capital from 1841 until 1865, when Parliament was permanently moved to " \
              "Wellington after an argument that persisted for a decade." \
              "\n2 -  The smallest country in the world in terms of population is Vatican City, " \
              "which has approximately 800 citizens." \
              "\n3 - The Philippine Sea is the largest sea in the world. " \
              "\nIt has an area of 2,198,852 square miles, or 5,695,000 square kilometers. " \
              "\nIt is part of the Pacific Ocean, bordered by the Ryukyu Islands, Taiwan, several Japanese and " \
              "Philippine islands, and other small islands." \
              "\n4 - Tokyo, Japan - 37,274,000 (2014)Far and away, the world's most-populated metropolitan, " \
              "Tokyo, Japan, has a life of its own. " \
              "\nThe nation's capital city is located on the East-Central coast of " \
              "the island of Honshu, within the Kantō region. " \
              "\n5 - On April 30, 1945, holed up in a bunker under his headquarters in Berlin, \nAdolf Hitler commits " \
              "suicide by swallowing a cyanide capsule and shooting himself in the head." \
              "\n6 - The fall of the Berlin Wall on November 9, 1989, during the Peaceful Revolution, " \
              "\nmarked the destruction of the Berlin Wall and the figurative Iron Curtain." \
              "\n7 - The United States of America (USA) has 50 states. \nIt is the second largest country in North " \
              "America after Canada (largest) and followed by Mexico (third largest). " \
              "\nThe U.S. has 50 states, a federal district, and five territories." \
              "\n8 -  The Danube flows through four capital cities: Vienna, Bratislava, Budapest, and Belgrade." \
              "\n9 - Odysseus, hero of Homer’s epic poem the Odyssey and one of the most frequently portrayed " \
              "figures in Western literature. \nAccording to Homer, Odysseus was king of Ithaca." \
              "\n10 - Novak Djokovic  is a Serbian professional tennis player who is currently ranked " \
              "world No. 1 in singles by the Association of Tennis Professionals (by 2024)." \
              "\n11 - Sir Tim Berners-Lee is a British computer scientist. " \
              "\nHe was born in London, and his parents were early computer scientists, " \
              "\nworking on one of the earliest computers. He wrote the first web page editor/browser " \
              "\n(“WorldWideWeb.app”) and the first web server (“httpd“). " \
              "\nBy the end of 1990, the first web page was served on the open internet, and in 1991, " \
              "\npeople outside of CERN were invited to join this new web community." \
              "\n12 - The European Union (EU) was founded as a result of the Maastricht Treaty on Nov. 1, 1993. " \
              "\nIt is a political and economic union between European countries that sets policies concerning " \
              "\nthe members’ economies, societies, laws, and, to some extent, security. " \
              "\n13 - Before the introduction of the Euro, Greece had its own currency, the Drachma. " \
              "\nThe Drachma had been used in Greece since ancient times, with its name deriving from the " \
              "Greek word for 'handful'." \
              "\n14 - Sofia  is the capital and largest city of Bulgaria. " \
              "\nIt is situated in the Sofia Valley at the foot of the Vitosha mountain, " \
              "in the western part of the country. "

print("Do You like to learn more about the objects ot the questions?")
answer = input("Please answer with Yes or No: ")
if answer == "Yes":
    print(f"{information}")

else:
    print("Thank You! Good luck!")


