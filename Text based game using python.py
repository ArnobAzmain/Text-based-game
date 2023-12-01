#Imports
from colorama import Fore, Style, Back as b
import time
import datetime , csv, pytz


#List of defines-
def red():
  return Fore.RED
def blue():
  return Fore.BLUE
def magenta():
  return Fore.MAGENTA
def green():
  return Fore.GREEN
def cyan():
  return Fore.CYAN
def reset():
  return Style.RESET_ALL
def bright():
  return Style.BRIGHT
def yellow():
  return Fore.YELLOW 
  
#Start of the main programming.
print(bright()+'''\n  Welcome!!! 🎉🎉
   /\_/\\
 =( °w° )=
   )   (  //
  (__ __)//
  ''')

time.sleep(0)
print(blue()+bright()+'''\n> This is a text adventure game made by Arnob 😎'''+reset())

time.sleep(0)
print('''\n> The theme of this game is horror, mystery, and probably adventure.''')

time.sleep(0)
print('\n> Anyways.... Hope you enjoy it.😅 ')

time.sleep(0)
player = input(red()+bright()+'\nEnter your name before we begin:- '+reset()).strip().title()

if player == "Arnob":
  print(Fore.GREEN+bright()+'''\n> 😳😲, You got the same name as the creator's!! 😎 COOL!'''+reset())
  
# Store data🎯🎯🎯🦝🦝🦝🦝
Bangladesh_time = pytz.timezone("Asia/Dhaka")
x = datetime.datetime.now(Bangladesh_time).strftime('%B,%d - %Y  %I:%M:%S %p')

with open ("player_log", "a") as file:
  store = csv.DictWriter(file, fieldnames = ['name','date'])
  store.writerow({'name': player,'date':x})
  # End -------°∆°---------

time.sleep(0)
print ('''\n> You are 18 years old. You live in Truckee, California, USA with your mom and dad and a little sister. You also have a big brother who is already in college in his final year \n''')

time.sleep(0)
print('*nice*')

time.sleep(0)
print('''\n> You just finished your highschool with a GPA of 3.0 and interested in studying engineering. So you look for a good college to get into''')

time.sleep(0)
print('''\n> After looking for a while... you narrowed down to 3 choices:-''')

time.sleep(0)
print('''\n1) Reed College

2) Grinnell College and

3) Colby College''')

time.sleep(0)
print('''\n> Now while any one of them is fine, there are some benefits that comes with each college....''')

time.sleep(0)
print('''\n> For instance, if you were to study in Reed College , you will be
relatively closer to your parent's house and could visit them often especially on weekends.''')

time.sleep(0)
print('\n> But Grinnell College has the best environment out of the three colleges since it is way out of the city in a hilly area surrounded by beautiful nature perfect for a relaxing and calm study environment.')

time.sleep(0)
print('''\n> But you will be very far from your parents or your relatives, so you won't be able to visit them very often''')

time.sleep(0)
print('''\n> On the other hand, if you choose Colby College you will be close to your brother Henry Cooper, who studies in Thomas College, but a bit far from your parents''')

time.sleep(0)
print('''\n> And so about a week later your dad (Joerge Cooper) asks,\n''')

time.sleep(0)
print(Fore.YELLOW + bright()+f'''> "So, {player}, which college are you going to?"'''+ reset())

### PART- 1 BEGIN --------O----------

while True:
  college_choice = input ('\n---> ').strip().title()

  
  if college_choice == "R" or college_choice=="Reed College":

    time.sleep(0)
    print(Fore.YELLOW+ bright()+'''\n> Oh good 👍... Your mother and I can come and visit you often and you can even see us during the weekends. You won't miss out on any family gatherings 😄.''')

    time.sleep(0)
    print('''\n> "Good choice ☺️"'''+ reset())
    break 
    
  elif college_choice in ["Grinnell College","G"] :
    time.sleep(1)
    print(Fore.YELLOW+ bright()+'''\n> "Are you sure son 😅? We can't visit you often nor you can during any events other than anything big like Christmas or Thanksgiving."''')

    time.sleep(0)
    print('''\n> "But, its your choice. Maybe some peace and quiet is necessary for you."''')

    time.sleep(0)
    print('''\n> "Anyway.... Good luck 🍀"'''+ reset())
    break 
    
  elif college_choice == "Colby College":
    print(Fore.YELLOW+ bright()+'''\n> "Amaizing!!!😃 You'll be close to your brother. You can get help from him if you need and its not so far away from us, so we can visit you sometime."''')

    time.sleep(0)
    print('''\n> "Great 👍 choice"'''+ reset())
    break
    
  else:
    print(red()+ '\n😖 typing mistake perhaps'+reset())
    retry = input('\nTry again? (y/n)= ')
    if retry not in ["yes", "y"]:
      break
##### PART-1 FINISH -------- O ---------

### PART-2 BEGIN _________O__________
time.sleep(0)
print('\n> And thus you contacted your college and was informed that you will start your semester from September 5th.')

time.sleep(0)
print('\n> In the mean time your mom (May Cooper) asks,')

time.sleep(0)
print(magenta()+bright()+f"\n> So, {player}, will you be staying in the dorm or where would you stay?...."+reset())

time.sleep(0)
print('\n> You couldnt answer her at that moment because that topic never crossed your mind. So simply you told her that you will let her know in about couple days later')

time.sleep(0)
print('\n> So about a week of thinking about it....')

time.sleep(0)
print('\n> There are 2 options for you...')

time.sleep(0)
print('\n> Either you can live in the college dorm...')

time.sleep(0)
print('\n> Or')

time.sleep(0)
print('\n> Rent a small house for a higher price than the dorm with the added benefit that you will get to live without any troubles from the nearby students in the dorm.\n')

time.sleep(0)
print('> And then again after couple of days late your mom wants to know about your response....')

while True:
  time.sleep(0)
  house = input (magenta()+'''\n> So, is it "the dorm" or "a small house"?'\n\n:- ''').lower().strip()
  original_choice = house

  if house == "the dorm" or house == "dorm":
    
    time.sleep(0)
    print(magenta()+'''\n> "Good 😊.You had me worried there...I thought 💭 you would pick a small house to rent or something. If you did, you would have to get a full time job or something cuz we won't be able to pay it ourself you know....."''')

    time.sleep(0)
    print('\n> Anyway... Glad you choose to live in the dorm.'+ reset())
    break

  
  elif house == "a small house" or house == "small house" or house == "house":
    
    time.sleep(0)
    print(magenta()+'\n> SERIOUSLY!!!😠 YOU WANT TO RENT A HOUSE?!?!?!')
    

    time.sleep(0)
    print('''\n> You'r not the son of Elon Musk or Jeff Bezos... ''')

    time.sleep(0)
    print('''\n> Well... then you have get a part time job or something cuz we won't be able to pay the house rent. Only the college fee.'''+ reset())
    
    while True:
      s = input(magenta()+'''\n> So still gonna live in a house? (yes/no):--> '''+reset())
      
      if s in ["yes", "y"]:
        print(magenta()+'''\n> Then good luck on finding a job or something YOUNG MAN!! 😡.'''+reset())
        break

      elif s in ["n", "no"]:
        print(magenta()+'''\n> Made the right decision 😤😤.'''+reset())
        break

      else:
        print(red()+'''\n> Invalid input.'''+reset())
    break
  
  else:
    print(red()+"\n> Typed something else 😖"+reset())
    retry = input(green()+'\n> Try again? (y/n):- '+reset())
    if retry not in ["y","yes"]:
      break


###🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸  🩸🩸🩸🩸‰«

if house in ["dorm","the dorm","d"] or house in ["house", "the house", "h"] and s in ["no", "n"]:
  time.sleep(0)
  print('''\n> So, as the start of the semester draws near, you say goodbye to your parents and your little sister and go to your college a day earlier to settle in your dorm.''')

  time.sleep(0)
  print(green()+'''\n> *By the way, your dad gifted you a car for entering college* '''+reset())

  time.sleep(0)
  print('''\n😒😒 won't be able to pay rent huh...''')

  time.sleep(0)
  print('''\n> Anyway.. after a looong drive you finally reach your college in the evening and go to your assigned dorm room.''')

  time.sleep(0)
  print('''\n> You do see many other students going to their dorm room as well and some are chatting with each other.''')

  time.sleep(0)
  print('''\n> Your assigned room is on the 2nd floor at the very end of the hall.''')

  time.sleep(0)
  print ('''\n> You enter the room and you are the only one to move in first.''')
  time.sleep(0)
  print('''\n> You thought that your roommate will move in tomorrow or later and then unpacked your belongings.''')

  time.sleep(0)
  print('''\n> After a quick rest, you moved out of your room and met some of your dormmates. Among them,'Harry','Henry' and 'Steven' are the ones you got along with very well and spent most of the time getting to know each other.''')
  time.sleep(0)
  print('\n> * Btw, Steve lives just opposite to your dorm room. *')
  #### Biography of the three friends ↓↓
  time.sleep(0)
  print('''\n> Here is a short bio about these three,''')

  time.sleep(0)
  print(green()+'''\nBrian:-'''+reset())
  
  time.sleep(0)
  print('''\n> Brian is a music enthusiast, and you'll often find him with headphones on, exploring various genres. He's also a coffee aficionado and enjoys trying different blends.
  
Hobbies: In his free time, Brian enjoys playing the guitar and occasionally writes his own songs. He's also a fan of camping/hiking.

College Study: Brian is studying Music Composition, combining his passion for music with his academic pursuits.''')

  time.sleep(0)
  print(cyan()+'''\nHenry:-'''+reset())

  time.sleep(0)
  print('''\n> Henry is a bookworm, always seen with a novel in hand. He has a keen interest in history and often engages in discussions about different eras.
  
Hobbies: Henry is a skilled chess player and participates in local tournaments. He's also an amateur astronomer, fascinated by the mysteries of the cosmos.

College Study: Henry is majoring in History and minoring in Astrophysics, reflecting his diverse interests.''')

  time.sleep(0)
  print(blue()+'''\nSteven:-'''+reset())

  time.sleep(0)
  print('''\n> Steven is a technology geek, always up-to-date with the latest gadgets and software. He's also a foodie, exploring different cuisines and experimenting with cooking.
  
Hobbies: Steven enjoys coding and developing small software projects in his spare time. He's also a fitness enthusiast, hitting the gym often.

College Study: Steven is pursuing a degree in Computer Science, aligning with his passion for technology and programming.''')

  time.sleep(0)
  print('''\n> After getting to know them, time passed quickly, and before you knew it, it was already 11 pm. Realizing the late hour, you and your new friends decided to head back to your rooms. Eager to make a good impression on your first day of college, everyone agreed to turn in early and get a good night's sleep.''')

  time.sleep(0)
  print(blue()+'''\n** Before heading to your rooms, you all exchanged contact information.**'''+reset())

  time.sleep(0)
  print('''\n> When you entered your room, your roommate still hadn't arrived. So you hoped you might meet him the next day.''')

  time.sleep(0)
  print('''\n> As the sun shines, eager to attend your first college class, you brush your teeth and have breakfast with Henry, Brian, and Steve before parting ways.''')

  time.sleep(0)
  print('''\n> Then, you make your way to the assigned classroom for your engineering class.''')

  time.sleep(0)
  print('''\n> Since it's the first day, not much was taught, and the day went by quickly. After all your classes were finished, Brian suggested everyone hang out in the nearby park through message.''')

  time.sleep(0)
  print('''\n> As there wasn't much to do, you agreed and met with everyone, spending the rest of the day chatting about what happened in class.''')

  time.sleep(0)
  print('''\n> Later you all had your dinner 🍽️  together and then headed back to your respective rooms.''')

  time.sleep(0)
  print('''\n> Just like yesterday, your roommate didn't arrive, but this time you were a bit happy because if your roommate doesn't arrive, then you'll have the room all to yourself.''')

  time.sleep(0)
  print('''\n> Just like that, September and October flew by, and your studies became increasingly demanding.''')

  time.sleep(0)
  print('''\n> Winter creeps in, wrapping everything in a chilly embrace. Leaves take a nosedive, and the world turns into a frosty wonderland. It's all about snuggling up, waiting for snowflakes, and feeling that cozy vibe. Winter's here, bringing its cool charm.''')

  time.sleep(0)
  print('''\n> In late November, just before the start of your winter break, Professor Peter Smith announced a small test to assess your performance. The test will be worth 10 marks.''')

  time.sleep(0)
  print('''\n> The test will cover some general topics, including physics, and basic engineering principles that were covered in class.''')

  time.sleep(0)
  print('''\n> With that, you study for the test alongside Henry, Brian, and Steve, who are also preparing for their upcoming tests before the break.''')

  time.sleep(0)
  print('''\n> Eventually, the exam day arrives, and everyone, including yourself sit down to take the test.''')

  time.sleep(0)
  print('''\n> Before everyone starts the exam, the professor states,''')

  time.sleep(0)
  print(yellow()+'''\n> Turn over the exam papers when you are ready. Take a moment to collect your thoughts, read the instructions properly and begin when you feel prepared. Best of luck to each of you.'''+reset())

  time.sleep(0)
  print('''\n> And with that you feel ready to start your exam.''')

  time.sleep(0)
  print(red()+'''\n> *Please type the correct answer EXACTLY as written on the question paper 'ex:- a) answer'. Otherwise, it will be considered incorrect.*\n'''+reset())

  def ques(question, answer, bypass):
    global mark

    time.sleep(0.2)
    print(f'{question}')
    ans = input(f'''\nA:> ''').strip()
    
    if ans in [answer, *bypass]:
      time.sleep(1)
      print('')
      mark +=1
    
    elif ans != answer:
      time.sleep(0.5)
      print('')

  mark = 0

#Q1
  ques("1) What is the formula for the area of a rectangle?\n a) A = Length + Width\n b) A = 2 x Length x Width\n c) A = Length x Width\n d) A = Length/Width", "c) A = Length x Width",["."])
#Q2
  ques("2) What is the SI unit of force?\n a) Watts\n b) Joules\n c) Newton\n d) Pascal","c) Newton",[".","s"])
#Q3
  ques("3) Which programming language is commonly used for web development?\n a) Java\n b) Python\n c) HTML\n d) C++","c) HTML",[".","s"])
#Q4
  ques("4) What term is used to describe the tendency of an object to remain at rest or in uniform motion?\n a) Inertia\n b) Acceleration\n c) Velocity\n d) Momentum","a) Inertia",[".","s"])
  #Q5
  ques("5) Which material is a common semiconductor used in electronic devices?\n a) Copper\n b) Silicon\n c) Aluminum\n d) Gold","b) Silicon",[".","s"])
  #Q6
  ques("6) According to the first law of thermodynamics, energy cannot be created or destroyed, only ____________.\n\n a) Transformed\n b) Increased\n c) Decreased\n d) Stored","a) Transformed",[".","s"])
  #Q7
  ques("7) What property of a fluid is described by the term 'viscosity'?\n a) Density\n b) Resistance to Flow\n c) Volume\n d) Pressure","b) Resistance to Flow",[".","s"])
  #Q8
  ques("8) In static equilibrium, the sum of forces acting on an object is equal to what?\n a) Mass\n b) Velocity\n c) Acceleration\n d) Zero","d) Zero",[".","s"])
  #Q9
  ques("9) What is the primary component of stainless steel?\n a) Iron\n b) Copper\n c) Aluminum\n d) Chromium","d) Chromium",[".","s"])
  #Q10
  ques("10) What is an essential aspect of effective engineering communication?}\n a) Using jargon extensively\n b) Avoiding diagrams and charts\n c) Being concise and clear\n d) Using complicated language","c) Being concise and clear",[".","s"])

  time.sleep(1)
  print(yellow()+'''\n> And time's up! Please pass your papers forward.'''+reset())

  time.sleep(0)
  print('''\n> With that, you have finished your test, and now your winter break begins.''')

  time.sleep(0)
  print('''\n> You thought that you would spend your break with your parents until the end of the break.''')

  time.sleep(0)
  print('''\n> But.......''')

  time.sleep(0)
  print(green()+'''\n **ding**''')

  time.sleep(0)
  print('''\n> "How do you feel about camping in the snow the day after tomorrow? I think it would be a 'cool' way to spend the day, and we can enjoy activities like building snowmen. I don't have everything prepared, so we'll go shopping for the necessary items. I've also invited Henry and Steve, and they are willing to join us."** Also we will be camping for couple of days.**'''+reset())

  time.sleep(0)
  print('''\n> Says Brian.''')

  time.sleep(0)
  print('''\n> Btw, you have never camped in your life, so you will get to experience it for the first time''')

  time.sleep(0)
  print(cyan()+'''\n> So do you 'go camping' or 'go to your parents'? '''+reset())

  while True:
    time.sleep(1)
    choice_2 = input('''\n :--> ''').strip().title()

    if choice_2 in ["Go To Your Parents","Go To My Parents","P","Parents","To Parents"]:
      
      time.sleep(0)
      print('''\n> You messaged Brian that your can't go but instead going to spend the entire break with your family''')
      break

    elif choice_2 in ["Go Camping","Camp","Camping","C"]:
      
      time.sleep(0)
      print('''\n> You messaged Brian that you have never camped before but excited to do so.''')
      break

    else:
      rt = input(red()+'''\n Invalid input.'''+reset())
      
     # Highway story starts ↓↓↓↓↓↓
  if choice_2 in ["Go To Your Parents","Go To My Parents","P","Parents","To Parents"]:
    
    time.sleep(0)
    print('''\n> Brian was a bit upset that you won't be joining, but he wished you good luck and a Merry Christmas.''')

    time.sleep(0)
    print('''\n> And with that, you head to your dorm, clean up, and spend the rest of the day casually using your phone to watch movies and whatnot.''')

    time.sleep(0)
    print('''\n> You want to suprise your parents, so you decided to start your journey in the evening and reach by dinner time.''')

    time.sleep(0)
    print('''\n> You pack your bags and bid farewell to your friends, letting them know you're leaving and to take care of themselves.''')

    time.sleep(0)
    print('''They wished you good luck as well.''')

    time.sleep(0)
    print('''\n> Thus you get in your car and start your journey home...''')

    time.sleep(0)
    print('''\n> ##########''')
    
    # CAMPING STORY STARTS ↓↓↓↓↓↓↓↓↓↓
  elif choice_2 in ["Go Camping","Camp","Camping","C"]:

    time.sleep(0)
    print('''\n> Thus the four of you went to a nearby shop to buy some necessary items for the camp.''')

    time.sleep(0)
    print('''\n> Since Brian has been camping since his childhood and is the more experienced one out of the four, he did most of the shopping.''')

    time.sleep(0)
    print('''\n> For this camp, Brian bought a large tent that we'll all be sharing, a mini stove, a lighter, some food for cooking, and some thick blankets for the cold nights.''')

    time.sleep(0)
    print('''\n> With everything ready for tomorrow's camp, you spend the rest of the day chatting and gossiping about various things in the nearby park.''')

    time.sleep(0)
    print('''\n> Mid-gossip, you consider mentioning that you don't have a roommate and enjoy having the room all to yourself, but you're unsure whether to bring it up or not.''')

    while True:
      tell = input('''\n> Do you want to mention about it? (Yes/No)''').strip().title()
      if tell in ["Y","Yes"]:
        time.sleep(0)
        print('''\n> You mention it to your friends about it.''')
        time.sleep(0)
        print('''\n> Henry and Brian was a bit suprised hearing about it but didn't say much other than be jealous that you get to have your own private room''')
        time.sleep(0)
        print(f'''\n> But Steve responded, mentioning that he had a hunch about it since he hasn't seen anybody other than {player} enter or leave the room.''')
        break
        
      elif tell in ["N","No"]:
        time.sleep(0)
        print('''\n> Thus you didn't mention it and carried on with that chatting...''')
        break
      else:
        print(red()+'''\nWrong input'''+reset())

    time.sleep(0)
    print('''\n> Thus as it was getting late your all went back to your room and slept''')

    time.sleep(0)
    print('''\n> The next morning you woke up excited to go camping.''')

    time.sleep(0)
    print('''\n> Over breakfast, Brian mentioned that we'll be leaving in the afternoon in Henry's car, which is more or less suitable for offroading. We'll head towards the thick forest located behind the campus on the north side.''')

    time.sleep(0)
    print('''\n> Steven asked,''')
    time.sleep(0)
    print(blue()+'''\n> How did you come about this spot? Did someone tell you or something?'''+reset())

    time.sleep(0)
    print('''\n> Brian responded,''')
    time.sleep(0)
    print(green()+'''\n> Professor Clint, along with one of the seniors, mentioned this forest a while back, highlighting how great it is for a camping site. And you know that I like camping. So when they mentioned about it, I was really looking forward to it.''')
    time.sleep(0)
    print('''So instead of going alone, I thought why don't we all go together 😄.'''+reset())

    time.sleep(0)
    print('''\n> And so as after noon approached, you all gathered in the parking lot and packed Henry's car with everything camping related.''')

    time.sleep(0)
    print('''\n> For this camp, Henry brought his telescope, Brian brought his guitar, and Steven brought a small novel to read, while you didn't bring anything. 😒''')

    time.sleep(0)
    print('''\n> And so, with everything set, you all head off.....''')
 
    time.sleep(0)
    
  # 🩸🩸🩸🩸🩸😂 🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸

if house in ["house","the house","h"] and s in ["yes", "y"] :
  print ('''\n> So you started to search for a house as well as for a part time job 😣 online...''')
  
  time.sleep(0)
  print('''\n> Later you came across a small house up for rent.''')

  time.sleep(0)
  print('''\n> The house is pretty old but good enough to stay. So you called the owner and after a long conversation, you were able to rent the house with a reasonable price 👍.''')

  time.sleep(0)
  print('''\n> As for a job...''')

  time.sleep(0)
  print('''\n> There wasn't much available. You only got two options for a job.''')

  time.sleep(0)
  print('''\n> Either you can work as a "delivery driver" in a pizza store.''')

  time.sleep(0)
  print('''\n> Or..''')

  time.sleep(0)
  print('''\n> Work as a "cashier" in a nearby convenient store''')
  
  while True:
    job = input('''\n> what would you choose? :---> ''').lower().strip()
    
    if job in ["cashier","a cashier","c"]:
      time.sleep(0)
      print('''\n> You immediately called the convenience store, letting them know that you are interested in working as a cashier.''')

      time.sleep(0)
      print('''\n> After asking couple of questions like, your name, college name, permanent adress, etc. They accept you and said you can start working the day your semester starts.''')

      time.sleep(0)
      print('''\n> Since its just a cashier job, there wasn't much requirements necessary🥱''')

      time.sleep(0)
      print('''\n> You told your parents about it and they were delighted 😁 to hear that.''')
      break
    
    elif job in ["delivery", "a delivery driver", "driver","d", "the delivery driver", "delivery driver"]:
      time.sleep(1)
      print('''\n> Soon after you emailed Domino's Pizza 🍕 letting them know that you are interested in working as a delievery driver.''')

      time.sleep(1)
      print('''\n> They emailed you back quickly, and informed you that they are willing to hire you but, before they hire, they will personally ask you few questions. So they asked you to drop by their store soon .''')

      time.sleep(0)
      print('''\n> You told your parents about it and they were delighted 😁 to hear that.''')
      break
    
    else:
      print('''\n> Invalid input! Try again.''')
        
  time.sleep(0)    
  print('''\n> Thus as the days draw near, you say goodbye 🫂 to your mom and your little sister.''')

  time.sleep(0)
  print('''\n> *By the way, your dad gifted you a car for entering college* ''')

  time.sleep(0)
  print('''\n> Four days before your semester starts, you moved into your new house with couple of your belongings and few furnitures with your dad, who helped you move the furnitures in and assemble them.''')

  time.sleep(0)
  print('''\n> Upon checking the house upclose, it is older than you imagined but that didn't matter anymore. It was still nice''')

  time.sleep(0)
  print('''\n> Later you and your dad spoke with the owner in person.''')

  time.sleep(0)
  print('''\n> The owner introduced himself as "John Smith" and he seems pretty nice.''')

  time.sleep(0)
  print('''\n> John told you and your dad that his son used to study in the nearby college as well.''')

  time.sleep(0)
  print('''\n> And how you kinda remind him of his son.''')

  time.sleep(0)
  print('''\n> Then soon after he waved goodbye 👋 and left in his car.''')

  time.sleep(0)
  print('''\n> Thus, the help of your dad you were able to finish setting up everything within 3 days and with a few words of your dad's advice, he left.''')

  time.sleep(0)
  print(red()+'''\n> Btw, DON'T DO DRUGS OR ALCOHOL.'''+reset())

  time.sleep(0)
  print(red()+'''\n> *seriously*'''+reset())

  time.sleep(0)
  print('''\n>  So after a good night sleep 💤 and with a light breakfast 🥞 you head towards the store for your job.''')
  
  if job in ["delivery", "a delivery driver", "driver","d", "the delivery driver", "delivery driver"]:

    time.sleep(1)
    print('''\n> You drive to the Domino's Pizza store in which you would be working....''')

    time.sleep(1)
    print('''\n> You enter the store and the scent of freshly baked pizza wafted through the air as you enter the bustling establishment.You find the manager inform her that you are the one that she spoke with on the phone regarding the delivery job.''')
    
    time.sleep(1)
    print('''\n> The manager introduced herself as "Sarah".''')

    time.sleep(1)
    print('''\n> She then takes you to a seat 🪑 in one corner of the store and asks you some basic questions.''')

    def manager(question, answer):
      while True:
        time.sleep(1)
        user_answer = input(f'''\n> Sarah: {question}.\n> reply: ''').title().strip()
        
        if user_answer in answer:
          print('''\n> Sarah: Alright...''')
          break
        else:
          print(red()+'''\n> Please check your answer properly'''+reset())

    time.sleep(1)
    print('''\n> As you two take your seat, the manager says,''')

    time.sleep(1)
    print(magenta()+'''\n> "Don't be nervous, I am not going to ask anything difficult. Just some personal questions to keep record."'''+reset())
    #Question - 1
    manager(magenta()+"What is your name?"+reset(), player)

    #Question - 2
    manager(magenta()+"Your mom's name?"+reset(),["May Cooper","M"])

    #Question - 3
    manager(magenta()+"Your father's name?"+reset(),["Joerge Cooper", "J"])

    #Question - 4
    manager(magenta()+"How old are you?"+reset(),["18", "E"])

    #Question - 5
    manager(magenta()+"Can you drive?"+reset(), ["Yes", "Y"])
    
    #Queation - 6
    manager(magenta()+"Do you have your own car"+reset(), ["Yes","Y"])
    
    #Question - 7
    manager(magenta()+"Where are you from?"+reset(),["Truckee, California","T","Truckee", "California","C","Truckee California"])
    
    #Question - 8
    manager(magenta()+"Do you have any experience in delivery or as a waiter?(yes/no)"+reset(),  ["Yes","No","N","Y"])
    
    time.sleep(1)
    print(magenta()+'''\n> Ok, one last question.'''+reset())
    
    time.sleep(2)
    print(red()+'''\n> This is serious'''+reset())
    
    # Question - 9
    manager(magenta()+"Can you put pineapples on pizza?🧐🧐🧐🧐"+reset(), ["Yes","No","Y","N","."])
    
    time.sleep(0)
    print(magenta()+'''\n> Ok, great 😃!!! It looks like everythings perfect..''')
    
    time.sleep(0)
    print(magenta()+'''\n> You start tomorrow for the night shift from 8 pm to 11:30 pm.'''+reset())
    
    time.sleep(0)
    print('''\n> She the handed you the store uniform and introduced you with everyone and explained how things work here.''')
    
    time.sleep(0)
    print('''\n> And then as everything is settled, you got out of the store and checked the time...''')
  
    time.sleep(0)
    print('''\n> Surprisingly it took an hour to finish everything.''')
  
    time.sleep(0)
    print('''\n> Then you hopped back in your car and went straight back home instead of checking the neighborhood.''')

    time.sleep(0)
    print('''\n> **You tell yourself that you'll have plenty of time to check.**''')

    time.sleep(0)
    print('''\n> After a short drive, you reach home and and throughout the day you didn't do much other than watch Netflix and chat with your highschool friends.''')

    time.sleep(0)
    print('''\n> As the day draw towards the end, you prepare youself for the start of your college the next day 😊''')

  elif job in ["cashier", "c"]:
    time.sleep(1)
    print('''\n> You drive to the convenient store you are supposed to work.''')
    time.sleep(1)
    print('''\n> The sun was shining brightly as you enter the store. The aisles were neatly arranged, and the morning light streamed through the windows, giving the place a warm glow. Mrs. Johnson(manager), already behind the counter, looked up and greets you with a friendly nod''')
    
    time.sleep(1)
    print('''\n> Mrs. Johnson asked, motioning for you to join her,''')
    
    time.sleep(1)
    print(magenta()+f'''\n> "Good morning, {player} ! Ready to dive into your new role?"'''+reset())
    
    time.sleep(1)
    print('''\n> The two of you sat down to discuss your responsibilities, the store's routine, and how you could balance work with his college schedule. Mrs. Johnson emphasized the importance of time management and maintaining a friendly demeanor with customers.''')

    time.sleep(1)
    print('''\n> As the conversation unfolded, you realized that this job wasn't just about earning extra money; it was an opportunity to develop valuable skills and gain real-world experience. Mrs. Johnson hands you a set of guidelines and shared a few stories from her own college days, offering insights into finding balance.''')
    
    time.sleep(1)
    print('''\n> Mrs.Johnson would like to verify some information about yourself an so she asks you some questions...''')
    
    def mr(question, answer):
      while True:
        time.sleep(1)
        user_answer = input(f'''\n> Mrs. Johnson: {question}.\n> reply: ''').title().strip()
        
        if user_answer in answer:
          print('''\n> Mrs.Johnson: Okay...''')
          break
        else:
          print(red()+'''\n> Please check your answer properly'''+reset())

    #Question - 1
    mr(magenta()+"What is your name?"+reset(), player)

    #Question - 2
    mr(magenta()+"Your mom's name?"+reset(),["May Cooper","M"])

    #Question - 3
    mr(magenta()+"Your father's name?"+reset(),["Joerge Cooper", "J"])

    #Question - 4
    mr(magenta()+"How old are you?"+reset(), "18")

    #Question - 5
    mr(magenta()+"Can you drive?"+reset(), "Yes")
    
    #Queation - 6
    mr(magenta()+"Do you have your own car"+reset(), "Yes")
    
    #Question - 7
    mr(magenta()+"Where are you from?"+reset(),["Truckee, California","T","Truckee", "California","C"])
    
    #Question - 8
    mr(magenta()+"Do you have any experience in being a cashier?(yes/no)"+reset(), ["Yes","No"])
    
    time.sleep(0)
    print(magenta()+'''\n> Well thats it then 😄'''+reset())
    
    time.sleep(0)
    print('''\n> Mrs.Johnson said, passing you the store uniform,''')
    
    time.sleep(0)
    print (magenta()+f'''\n> "Your college journey is beginning, and so is your professional one. Make the most of both, {player} 😉."'''+reset())
    
    time.sleep(0)
    print('''\n>She then showed you around the shop and introduced to some of the employees.''')

    time.sleep(0)
    print('''\n> You start your shift from 8 pm to 11:30 pm''')
    
    time.sleep(0)
    print('''\n> Leaving the convenience store, you felt a sense of responsibility and readiness for the day ahead. With a job secured and the first day of college on the horizon, you embraced the morning's dual significance, grateful for the unexpected path that awaited you.''')
    
    time.sleep(0)
    print('''\n> And then as everything is settled, you got out of the store and checked the time...''')
  
    time.sleep(0)
    print('''\n> Surprisingly it took an hour to finish.''')
  
    time.sleep(0)
    print('''\n> Then you hopped back in your car and went straight back home instead of checking the neighborhood.''')

    time.sleep(0)
    print('''\n> **You tell yourself that you'll have plenty of time to check.**''')

    time.sleep(0)
    print('''\n> After a short drive, you reach home and and throughout the day you didn't do much other than watch Netflix and chat with your highschool friends.''')

    time.sleep(0)
    print('''\n> As the day winds down, you gear up for the start of college tomorrow. Getting things sorted, deciding on an outfit, and feeling a mix of excitement and nerves – it's all part of the pre-college vibe. You set your alarm, ready to kick off this new chapter. 🚀✨ 😊''')

# END FOR THE JOB PART 〽️〽️〽️〽️〽️〽️〽️〽️
  # Part - 2 END 🦠🦠🦠🦠🍀🍀🍀
# PART - 3 START
# This is where the House + College horror starts ↓↓↓↓↓↓↓
  time.sleep(1)
  print('''\n> You wake up early and feel happy and nervous. You are going to college today. You get ready and wear a nice outfit. You eat your cereals fast and leave the cereal box on the kitchen counter.''')

  time.sleep(0)
  print('''\n> You go to the college and see many new students like you. You are ready to learn and have fun.''')

  time.sleep(0)
  print('''\n> You go to your first class and see different people. They are also new and excited. The teacher says 'hello' and starts the class. This is the start of your college life.''')

  time.sleep(0)
  print('''\n> On the first day you spoke with some freshmen among which Simon and Ehtan are the ones you got along really well.''')

  time.sleep(0)
  print('''\n> You three spoke about where each other are from and which highschool they studied.''')

  time.sleep(0)
  print('''\n> Later you hung out with them, shared contact info and went home when your college was finished''')

  time.sleep(0)
  print('''\n> You arrived home around 4 o'clock, but upon entering the house....''')

  time.sleep(0)
  print('''\n> A weird and bad smell hit you. You thought,''')

  time.sleep(0)
  print(blue()+'''\n> "I never smelled anything like this while I was in the house 😕"'''+reset())

  time.sleep(0)
  print('''\n> You start searching the house to find where the strange smell is coming from.''')

  time.sleep(0)
  print('''\n> You searched the kitchen, bedroom, closet, bathroom, attic, and more.''')

  time.sleep(0)
  print('''\n> But found no trace of the source of that unsettling smell.''')

  time.sleep(0)
  print('''\n> You even checked around the outside your house, which is close to a thick forest, but found nothing.''')

  time.sleep(0)
  print('''\n> Inside the house, all the windows were shut. You considered that the peculiar smell might be from the old wood 🪵 in this aging house..''')

  time.sleep(0)
  print('''\n> So you opened all the windows and reviewed what was tought in the class and by then the smell went away.''')

  time.sleep(0)
  print('''\n> As the clock strikes 7:30 pm, you prepare for your part-time job leaving the window in the kitchen open and head to your night 🌃 shift.''')

  if job in ["delivery", "a delivery driver", "driver","d", "the delivery driver", "delivery driver"]:

    time.sleep(0)
    print('''\n> You arrive at Domino's and are warmly greeted by everyone. The enticing aroma of freshly baked pizza fills the store. The manager, Sarah, welcomes you and provides information that...''')
    
    time.sleep(0)
    print(magenta()+'''\n> On your first day today, you won't be making deliveries directly yourself...''')

    time.sleep(0)
    print('''\n> Instead, you'll be paired with someone today to observe the delivery process. Starting tomorrow, you'll be handling deliveries on your own. It's a standard procedure as per the company policy for all new delivery drivers.'''+reset())

    time.sleep(0)
    print('''\n> She then introduced you to Bruce, who has been their delivery driver for quite some time.''')

    time.sleep(0)
    print('''\n> Bruce seems to be almost the same age as you and have this calm and chill atmosphere around him.''')

    time.sleep(0)
    print('''\n> You spoke with him a short while and turns out he is 21 years old and is a pretty chill 😎 guy.''')

    time.sleep(0)
    print('''\n> Shortly after your chat, an order arrives. Loading the pizza boxes into Bruce's car, you both head towards the destination.''')

    time.sleep(0)
    print('''\n> Throughout the night you and Bruce went around town delivering boxes after picking them up from the store.''')

    time.sleep(0)
    print('''\n> Bruce gave some friendly adivices like being polite and kind to the customers and to always check if the pizza was paid for or will be paid upon delivered.''')

    time.sleep(0)
    print('''\n> Other than that, there wasn't much....''')

    time.sleep(0)
    print('''\n> During deliveries Bruce said couple of thing about him as well...''')

    time.sleep(0)
    print('''\n> Bruce said that grew up in this town and studied in the nearby college. After graduation he wanted to study in a university. So for this he has to leave the town and this is his very last delivery''')

    time.sleep(0)
    print('''\n> He has been doing this delivery job since his freshmen in the college.''')

    time.sleep(0)
    print('''\n> As your shift was almost finished, there was one last order that came in.''')
    
    time.sleep(0)
    print('''\n> Thus you pick up the pizza from the store and head towards the destiny.''')

    time.sleep(0)
    print('''\n> After completing the order, as you two were heading back to the store, Bruce gave you one last piece or advice.''')

    time.sleep(0)
    print('''\n> Bruce turned the radio off and then,''')

    time.sleep(0)
    print('''\n> Bruce says,''')

    time.sleep(0)
    print('''\n> During night deliveries especially between 10 to 11 pm, if any delivery feels off or you feel uncomfortable delivering...''')
    
    time.sleep(3)
    print(red()+'''JUST RETURN BACK TO THE STORE!'''+reset())

    time.sleep(0)
    print('''\n> and tell or call Sarah (if she is not in store) what happened or how you felt off delivering the pizza.''')

    time.sleep(0)
    print('''\n> She'll take care of the rest.''')

    time.sleep(0)
    print('''\n> You were surprised to hear that, and then the entire drive back to the store was dead quiet. None of you uttered a single sound.''')

    time.sleep(0)
    print('''\n> Later when you reached back to the store and everyone arranged a small farewell party for Bruce. Later he bid farewell and left the store.''')

    time.sleep(0)
    print('''\n> As you were leaving as well, you told Sarah about what Bruce said.''')

    time.sleep(0)
    print('''\n> She was a bit surprised to hear that, but in responce she said,''')

    time.sleep(0)
    print(magenta()+'''\n> If Bruce said that, then thats probably for the best.'''+reset())

    time.sleep(0)
    print('''\n> Later you drive back home not really sure what they meant but did your best to not think about it while driving.''')

    time.sleep(0)
    print('''\n> Thus from that day you did all the deliveries and you felt quite happy doing it.''')

    time.sleep(0)
    print('''\n> One day, close your shift ending, you were sitting in the store hoping it ends without any further deliveries...''')

    time.sleep(0)
    print(green()+'''\n**ring**''')
    time.sleep(0)
    print('''\n  **ring**'''+reset())

    time.sleep(0)
    print('''\n> The phone rings and an order comes through for a small pepperoni pizza.''')

    time.sleep(0)
    print('''\n> You sigh 😔... and waited for the pizza to be ready.''')

    time.sleep(0)
    print('''\n> As the pizza 🍕 was packed and ready to go, you take it in your car and put the address in you GPS and head towards the destination.''')

    time.sleep(0)
    print('''\n> The address was from a place you most rarely get orders from. Also that area is surrounded by thick forest and the houses there are pretty old.''')

    time.sleep(0)
    print('''\n> Anyway, you head towards the address and as you were coming close, you notice that almost half of the street lights are turned off and the ones that are turned on are very dim making them pretty much useless.''')

    time.sleep(0)
    print('''\n> And then as you passing by a very old house, you GPS beeps. Letting you know that you have arrived at your destination.''')

    time.sleep(0)
    print('''\n> You are confused!!!''')

    time.sleep(0)
    print('''\n> You double check the address and its was correct, you even called the store and asked to verify the address but no luck, you are at the right address.''')

    time.sleep(0)
    print('''\n> The house is old and worn down, and the some of the window panels are broken as well... There is no light turned on inside.''')

    time.sleep(0)
    print('''\n> Now you have delivered pizza before where all the lights were turned off but this seems different.''')

    time.sleep(0)
    print('''\n> Now do you 'deliver the pizza' or 'head back store'?''')
    
    while True:
      choice_3 = input('''\n--> ''').strip().title()
      
      if choice_3 in ["Deliver The Pizza","Deliver","Deliver Pizza","D"]:
        
        time.sleep(0)
        print('''\n> You get out of your car to deliver the pizza. You thought you would just drop it and get back in your car but...''')
      
        time.sleep(0)
        print('''The customer didn't pay for the pizza yet.''')

        time.sleep(0)
        print('''\n> As you walk towards the house in the dark, barely being able to see from the moon light, you approach the front door and knock.''')

        time.sleep(0)
        print('''\n> No response....''')

        time.sleep(0)
        print('''\n> You knock again but this time a lot harder.''')

        time.sleep(0)
        print('''\n> Suddenly loud footsteps can be heard sprinting towards the door but....''')

        time.sleep(0)
        print('''\n> It just stops...''')

        time.sleep(0)
        print('''\n> You thought the door would open but it didn't. Instead you can hear heavy breathing just behind the door.''')

        time.sleep(0)
        print(red()+'''/n> "Who is it?"'''+reset())

        time.sleep(0)
        print('''\n> A raspy voice speaks to you.''')

        time.sleep(0)
        print(blue()+'''\n> Pizza delivery'''+reset())

        time.sleep(0)
        print('''\n> You reply, trying to sound calm...''')

        time.sleep(0)
        print('''\n> Expecting that the door would open, you prepare yourself, but there is no reply nor any sound. Its just dead silent. Even the sounds from the cricket has stopped.''')

        time.sleep(0)
        print('''\n> After a whole minute of just standing there, in the dark and quiet place,''')

        time.sleep(0)
        print('''\n> You decide to leave. And as you turn around....''')

        time.sleep(0)
        print(red()+'''\n **creak**'''+reset())

        time.sleep(0)
        print('''\n> The door behind you opened slightly and you can see an old creepy man staring at you.''')
      
        time.sleep(0)
        print(red()+'''\n> "Sorry for that, so how much do I owe you?"'''+reset())

        time.sleep(0)
        print('''\n> The man spoke in a raspy voice.''')

        time.sleep(0)
        print(blue()+'''\n> 5 dollars'''+reset())

        time.sleep(0)
        print('''\n> You reply''')

        time.sleep(0)
        print('''\n> This whole time the man didn't even step foot outside the door''')

        time.sleep(0)
        print('''\n> He then extended his arm holding a 5 dollar bill. At this point asking for a tip is pointless.''')

        time.sleep(0)
        print('''\n> You took the bill out of his hand and handed over the pizza. You noticed that the man had many wrinkles in his hand. So you assumed that he could be 50 or more years old.''')

        time.sleep(0)
        print('''\n> But the way he sprinted towards the door, got you questioning whether he was actually 50 or more.''')

        time.sleep(0)
        print('''\n> You then quickly walked out of there and got back in your car and started to drive off''')

        time.sleep(0)
        print('''\n> All of a sudden your car shakes violently and stops. You pressed the gas pedal hard but it won't move.''')

        time.sleep(0)
        print('''\n> You don't know what to do and kinda sat there for a second. Then you looked at the side view mirror ....''')

        time.sleep(0)
        print('''\n> There is a silhouette of a person crouched down just behind your car..''')

        time.sleep(0)
        print('''\n> slowly coming towards you...''')

        time.sleep(0)
        print('''\n> You are in a panic not sure what to do... ''')

        time.sleep(0)
        print('''\n> Do you 'run' out of your car and head towards the thick forest or 'lock' the door and do nothing?''')
        while True:
          choice_5 = input(':--> ').lower().strip()
          if choice_5 in ["run","r"]:
            print('''\n> You grab your phone and sprint right out of the car and head towards the thick forest.''')
            time.sleep(0)
            print('''\n> You ran and ran untill you got exhausted.''')
            time.sleep(0)
            print('''\n> After catching your breath, you dialed 911 and told everything to the officer.''')
            time.sleep(0)
            print('''\n> You were then instructed to remain hidden somewhere close to your car and wait untill he arrives.''')
            time.sleep(0)
            print('''\n> You then started to walk back carefully and eventually you spoted your car in the distance. But....''')
            time.sleep(0)
            print('''\n> You see a person, unable to see any visible features due to the darkness, just standing there by the driver's door.''')
            time.sleep(0)
            print('''\n> You didn't make a single sound and just stood there waiting for the officer.''')
            time.sleep(0)
            print('''\n> By the time officer arrive, the man left. You explained to him again what happened and found out that your car's left tire were slashed, probably with a knife 🔪''')
            time.sleep(0)
            print('''\n> Later a tow truck was called and you went home afterwards.''')
            time.sleep(0)
            print('''\n> You told Sarah, what happened and she was glad that you weren't hurt and gave you the day off.''')
            time.sleep(0)
            print('''\n> The next day you didn't go to college and stayed home.''')
            break
          elif choice_5 in ["lock","l"]:
            time.sleep(0)
            print('''\n> You quickly went ahead to lock the door and it was already locked.''')
            time.sleep(0)
            print('''\n> And then your just sat there, watching the man slowly approaching you....''')
            time.sleep(0)
            print('''\n> As he came close to your window....''')
            time.sleep(0)
            print(red()+'\n **knock**')
            time.sleep(0)
            print('\n  **knock**'+reset())
            time.sleep(0)
            print('''\n> The man knocked on the glass window, indicating to roll down the window''')
            time.sleep(0)
            print('''\n> You roll down the window just barely.''')
            time.sleep(0)
            print(red()+'''\n> "Sorry, i forgot to give you a tip"'''+reset())
            time.sleep(0)
            print('''\n> That same raspy voice of the man you spoke just before.''')
            time.sleep(0)
            print(blue()+'''\n> "No thanks, it not necessary. Keep it."'''+reset())
            time.sleep(0)
            print('''\n> You reply...''')
            time.sleep(0)
            print('''\n> But he was persistent. He then shoved 2 dollar bill through the small gap of your widow.''')
            time.sleep(0)
            print('''\n> He then left and after collecting youself, you called the tow truck and waited for their arrival.''')
            time.sleep(0)
            print('''\n> You also called your manager and let her know everything that happened.''')
            time.sleep(0)
            print('''\n> She told you to head straight home, not needing to come back to the store. Also she said that you can have tomorrow off.''')
            time.sleep(0)
            print('''\n> Thus the next day you didn't go to college as well.''')
            time.sleep(0)
            print ('''\n> Your friend Simon and Ethan came by your home after college and you hung out with them the rest of the day.''')
            break
            
          else:
            print('''\n* Wrong/invalid input (lock or run)''')
        break
      
      elif choice_3 in ["Head Back","Back","Head Back Store","Head Back To The Store","Head","Store","Back Store"]:
        time.sleep(0)
        print('''\n> You called the manager and told that you feel off about this delivery and want to head back store.''')
        time.sleep(0)
        print('''\n> She didn't stop you rather told you to come back as well..''')
        time.sleep(0)
        print('''\n> As you were turning your car....''')
        time.sleep(0)
        print(red()+'''\n **whistle**'''+reset())
        time.sleep(0)
        print('''\n> You look towards the place where the sound came from...''')
        time.sleep(0)
        print('''\n> You see that the house door was now open and an arm was sticking out of it.''')
        time.sleep(0)
        print(red()+'''\n> "Aren't you going to deliver my pizza?"'''+reset())
        time.sleep(0)
        print('''\n> An old and raspy voice came from there.''')
        time.sleep(0)
        print('''\n> Unsure if you would go back...''')
        time.sleep(0)
        print('''\n> You thought that it was all a misunderstanding, you got out of your car and proceed to approach his house.''')
        time.sleep(0)
        print('''\n> You reach the front door with the pizza and greeted the man in a friendly manner.''')
        time.sleep(0)
        print('''\n> The man spoke,''')
        time.sleep(0)
        print(red()+'''\n> "Sorry for that, so how much do I owe you?"'''+reset())

        time.sleep(0)
        print('''\n> in a raspy voice.''')

        time.sleep(0)
        print(blue()+'''\n> 5 dollars'''+reset())

        time.sleep(0)
        print('''\n> You reply''')
        time.sleep(0)
        print('''\n> This whole time the man didn't even step foot outside the door''')

        time.sleep(0)
        print('''\n> He then extended his arm holding a 5 dollar bill. At this point asking for a tip is pointless.''')

        time.sleep(0)
        print('''\n> You took the bill out of his hand and handed over the pizza. You noticed that the man had many wrinkles in his hand. So you assumed that he could be 50 or more years old.''')
        time.sleep(0)
        print(red()+'''\n> "Its nice to play with young deliver boys....."'''+reset())
        time.sleep(0)
        print('''\n> That was enough to send shivers down your spine.''')
        time.sleep(0)
        print('''\n> You then quickly got back in your car and drove off''')
        time.sleep(0)
        print('''\n> As you were driving off, you see the man.''')
        time.sleep(0)
        print('''\n> This time he was standing out of the door...''')
        time.sleep(0)
        print('''\n> For a brief moment, from the light of your car, you saw the man...''')
        time.sleep(0)
        print(red()+'''\n> He was much older than you thought and he was waving goodbye at you with a grin on his face. And his eyes were wide open'''+reset())
        time.sleep(0)
        print('''\n> Thus you got back to the store and told everyone there about what you saw.''')
        time.sleep(0)
        print('''\n> Everyone was creeped out as well and was relieved that nothing bad happen.''')
        time.sleep(0)
        print('''\n> As it was Thursday that day, you got the day off tomorrow and you didn't let that encounter bother you as much.''')
        time.sleep(0)
        print('''\n> After that you didn't face anything similar like that and carried on hanging out with Simon and Ethan and carried on.''')
      else:
        print(red()+'''\n Wrong or Invalid input (deliver or return)'''+reset())


  elif job in ["cashier", "c"]:
    time.sleep(0)
    print('''\n> You enter the convenient store you'll be working and was greeted my Mrs.Johnson. She explained you how the cash regester worked and untill the next person arrive for their shift you are not allowed to leave.''')
    
    time.sleep(0)
    print('''\n> And that is all there is to it.''')

    time.sleep(0)
    print('''\n> You spend the entire shift standing at the cash register and handling customer transactions, ensuring a smooth and efficient process.''')

    time.sleep(0)
    print('''\n> As your shift was almost finished, the next person to take your shift arrived, you greeted him took your leave and left the store.''')

    time.sleep(0)
    print('''\n> Just like that weeks go by and everyday was the same process''')
    time.sleep(0)
    print('''\n> But on one particular day....''')
    time.sleep(0)
    print('''\n> Almost at the end of your shift....''')
    time.sleep(0)
    print(red()+'''\n> **DING**'''+reset())
    time.sleep(0)
    print('''\n> A customer enters...''')
    time.sleep(0)
    print('''\n> You look at the customer...''')
    time.sleep(0)
    print('''\n> An old man wearing a black mask, hair with little to nothing left, walks to a nearby shelf.''')
    time.sleep(0)
    print('''\n> The way he walks...''')
    time.sleep(0)
    print('''\n> Its like he is drunk or on some drugs or something.''')
    time.sleep(0)
    print('''\n> You shrugged it off and stand there...''')
    time.sleep(0)
    print('''\n> After a few minutes, the man comes to the counter.''')
    time.sleep(0)
    print('''\n> He puts the lighter on the counter and you proceed to run through the scanner and tell him,''')
    time.sleep(0)
    print(blue()+'''\n> That will be 1 dollar and 5 cents'''+reset())
    time.sleep(0)
    print('''\n> He brings out a 6 dollar bill and hands it to you.''')
    time.sleep(0)
    print('''\n> You took the bill and gave him his change.''')
    time.sleep(0)
    print('''\n> As he was about to leave....''')
    time.sleep(0)
    print(red()+'''\n> "I like blood."''')
    time.sleep(0)
    print('''\n> Do YOU?'''+reset())
    time.sleep(0)
    print('''\n> He asked in a raspy voice...''')
    time.sleep(0)
    print('''\n> You are shocked to hear that so suddenly..''')
    time.sleep(0)
    print('''\n> You don't know what to say really.''')
    time.sleep(0)
    print('''\n> So instead you replied,''')
    time.sleep(0)
    print(blue()+'''\n> Have a great day, sir..'''+reset())
    time.sleep(0)
    print('''\n> The man didn't say anything after that, instead he just stared at you for a while.....''')
    time.sleep(0)
    print('''\n> After he just stood there staring at you for what felt like 2 whole minute...''')
    time.sleep(0)
    print('''\n> He walked out the store''')
    time.sleep(0)
    print('''\n> As he was going out, he said something loud enough to understand,''')
    time.sleep(0)
    print(red()+f'''\n> We'll meet again {player}. Soon enough...'''+reset())
    time.sleep(0)
    print(blue()+'''\n> How did he know my name!?!?!?'''+reset())
    time.sleep(0)
    print('''\n> You asked yourself...''')
    time.sleep(0)
    print('''\n> Later you reported it to the manager and she told you that it was probably drunk person you encounter ed and not to think about it too much.''')
    time.sleep(0)
    print('''\n> But as for you name, even she didn't know what to say about that....''')
#    CASHIER STORE ENCOUNTER ☝️☝️☝️☝️
    time.sleep(0)

  time.sleep(0)
  print('''\n> Since then you didn't get that awful/weird smell from the house. You thought that it was most probably the old wood 🪵 causing that smell and how keeping a window open kept that smell from coming back. As for the creepy old man, you didn't face him afterwards.''')

  time.sleep(0)
  print('''\n> One day, in the morning, before taking your breakfast, you found your cereal box on top of your fridge.''')

  time.sleep(0)
  print('''\n> You found it strange..''')

  time.sleep(0)
  print('''\n> Usually you keep it in a fridge not on it.''')

  time.sleep(0)
  print('''\n> Probably you kept it on there when you were hurrying to eat your breakfast before going to class. But anyways, you took your breakfast and kept the creal box in the fridge and went straight to class.''')

  time.sleep(7)
  print('''\n> And just like that a year goes by. You got used to the life of doing a part time job and attending classes.''')

  time.sleep(0)
  print('''\n> But......''')

  time.sleep(0)
  print('''\n> One day after finishing your shift, you got home and as soon as you entered.....''')

  time.sleep(0)
  print(red()+'''\n> Something felt off..''')

  time.sleep(0)
  print('''\n> That smell..''')
  
  time.sleep(0)
  print('''\n> That same smell, as last time, is coming from the house and something feels strange....'''+reset())

  time.sleep(0)
  print('''\n> The house is really cold and pitch-black, with all the lights off. But the moonlight barely lights up the kitchen.''')
  
  time.sleep(0)
  print('''You move further in the house towards the kitchen,passing by the living room, while making the creaking sound of the floor board''')

  time.sleep(0)
  print('''\n> You notice that some of the belongings are not exactly as you kept them as.''')

  time.sleep(0)
  print('''\n> Expecially one of the kitchen chairs, it seems that the chair has been moved and the cereal box is on the kitchen counter which you know for a fact that you didn't keep, and most frightening of all . ''')

  time.sleep(0)
  print(red()+'''\n> The kitchen knife..''')

  time.sleep(0)
  print('''\n> Its missing....'''+reset())

  time.sleep(0)
  print('''\n> You stand still while processing what's going on...''')
  
  time.sleep(0)
  print(red()+'''\n**creak**''')

  time.sleep(0)
  print('''\n> You spin around in terror, and there, in the shadows, is a HORRIFYING sight.....''')

  time.sleep(0)
  print('''\n> A man crouched behind the doorframe in the living room....''')

  time.sleep(0)
  print('''\n> His head is the only thing you can see, his eyes wide and wild, staring at you with a murderous intensity.....''')

  time.sleep(0)
  print('''\n> He clutches a gleaming, sharp object in his hand''')
  
  time.sleep(0)
  print('''\n> Its your knife 🔪''')

  time.sleep(0)
  print('''\n> You feel a cold sweat on your forehead, and your heart pounding in your chest.''')

  time.sleep(0)
  print('''\n> He grins wickedly, revealing his rotten teeth and bloody gums.''')

  time.sleep(0)
  print('''\n> He whispers something in a raspy voice, but you can’t make out the words.''')

  time.sleep(0)
  print('''\n> That voice!!!''')

  time.sleep(0)
  print('''\n> You recognize it!!!''')

  time.sleep(0)
  print('''\n> Its that same voice from that old man you encountered.''')

  time.sleep(0)
  print('''\n> You don't really know what to do in this situation....''')

  time.sleep(0)
  print('''\n> Run out the back door? or Try to fight him?''')

  while True:
    do = input('''n :---> ''').strip().lower()
  
    if do in ["run","run out the back door","r","run back","d","door","back door","out","out the door","out the back door"]:
      time.sleep(0)
      print('''\n> You sprint towards the back door to get out.''')
      time.sleep(0)
      print('''\n> While getting out, you heard loud footsteps 👣 charging at you.''')
      time.sleep(0)
      print('''\n> You felt a sharp pain in your leg.....''')
      time.sleep(0)
      print('''\n> There is a knife sticking through you leg!!!!''')
      time.sleep(0)
      print('''\n> Blood spilling out...''')
      time.sleep(0)
      print('''\n> The man shoved you onto the floor...''')
      time.sleep(0)
      print('''\n> chocking you..''')
      time.sleep(0)
      print('''\n> "Let's Have Fun!!!!"''')
      time.sleep(0)
      print('''\n> He shouted.''')
      time.sleep(0)
      print('''\n> You slowly begin to black out.''')
      time.sleep(0)
      print('''\n> You desperately try to find something to get him off of you...''')
      time.sleep(0)
      print('''\n> But you found nothing......''')
      time.sleep(4)
      print('''\n> As your last attempt, you punch him in the face....''')
      time.sleep(0)
      print('''\n> It was enough to loose his grip and fall off.''')
      time.sleep(0)
      print('''\n> You then sprinted out the back door as he was trying to catch you.''')
      time.sleep(0)
      print('''\n> You SCREAMED''')
      time.sleep(0)
      print('''\n **HELP**''')
      time.sleep(0)
      print('''\n>  **HELP**''')
      time.sleep(0)
      print('''\n> You ran towards your neighbor's house and banged the front door desperately trying to get their attention.''')
      time.sleep(0)
      print('''\n> Your neighbour opened the door with anger''')
      time.sleep(0)
      print('''\n> "WHAT THE HELL DO YOU WANT?!?!??"''')
      time.sleep(0)
      print(blue()+'''\n> "HELP!!! There is a man trying to kill me!" you cried out, blood dripping from your leg.'''+reset())
      time.sleep(0)
      print('''\n> Mr. Khan, your neighbour, looked at you with horror and disbelief. He quickly pulled you inside and slammed the door shut. He grabbed his phone and dialed 911.''')
      time.sleep(0)
      print(blue()+'''\n> "Stay calm, stay calm. Help is on the way,"'''+reset())
      time.sleep(0)
      print('''\n> He said, trying to reassure you.''')
      time.sleep(0)
      print('''\n> You collapsed on his couch, feeling faint. You looked at your leg and saw the knife still embedded in your flesh. You felt a surge of pain and nausea.''')
      time.sleep(0)
      print('''\n> You heard a loud thud on the door. The man had followed you. He was pounding on the door, screaming obscenities.''')
      time.sleep(0)
      print(red()+'''\n> "LET ME IN! LET ME IN! I'M NOT DONE WITH YOU YET!"''')
      time.sleep(0)
      print('''\n> You felt a wave of terror wash over you. You knew he would not stop until he got what he wanted.''')
      time.sleep(0)
      print('''\n> Mr. Khan grabbed a cricket bat from his closet and stood next to the door. He was ready to fight.''')
      time.sleep(0)
      print(blue()+'''\n> "You stay away from him, you bastard!" he shouted.'''+reset())
      time.sleep(0)
      print('''\n> The door cracked under the man's force. He was about to break in.''')
      time.sleep(0)
      print('''\n> Mr. Khan swung the bat at the door, hoping to hit the man.''')
      time.sleep(0)
      print('''\n> He missed...''')
      time.sleep(0)
      print('''\n> The man kicked the door open and entered. He had a crazed look in his eyes. He saw you and grinned wickedly.''')
      time.sleep(0)
      print('''\n> "There you are, my little toy. Time to play some more."''')
      time.sleep(0)
      print('''\n> He lunged at you with his knife.''')
      time.sleep(0)
      print('''\n> Mr. Khan swung the bat again, this time hitting the man's arm.''')
      time.sleep(0)
      print('''\n> The man dropped a knife and groaned in pain.''')
      time.sleep(0)
      print('''\n> Mr. Khan hit him again, this time on his head.''')
      time.sleep(0)
      print('''\n> The man fell to the floor, motionless.''')
      time.sleep(0)
      print('''\n> He had killed him.''')
      time.sleep(0)
      print('''\n> He dropped the bat and gasped for air.''')
      time.sleep(0)
      print('''\n> He checked your pulse and saw that you were still alive.''')
      time.sleep(0)
      print('''\n> He hugged you and said,''')
      time.sleep(0)
      print(blue()+'''\n> "You're safe now. You're safe."'''+reset())
      time.sleep(0)
      print('''\n> You heard sirens outside. The police had arrived.''')
      time.sleep(0)
      print('''\n> They took you and Mr. Khan to the hospital.''')
      time.sleep(0)
      print('''\n> You were both treated for your injuries.''')
      time.sleep(0)
      print('''\n> You thanked Mr. Khan for saving your life.''')
      time.sleep(0)
      print('''\n> He said he was glad he could help and soon you became friends with him after that.''')
      time.sleep(0)
      print(red()+'''\n> But....'''+reset())
      time.sleep(0)
      print('''\n> That incident still lingers in your head from time to time giving you nightmares...''')
      break
      
    elif do in ["try to fight him","try and fight him","t","fight","fight him","try","try to"]:
      time.sleep(0)
      print('''\n> You decide to face the man head on, hoping to overpower him or escape if possible.''')
      time.sleep(0)
      print('''\n> You grab a frying pan from the corner of the living room and swing it at his head with all your force..''')
      time.sleep(0)
      print('''\n> He blocks it with his arm.''')
      time.sleep(0)
      print('''\n> He lunges at you with the knife aimed at your throat.
You duck, trying to dodge his attack. ''')
      time.sleep(0)
      print('''\n> You see a phone on the couch, but before you can reach it....''')
      time.sleep(0)
      print('''\n> he stabs your leg with the knife, making you cry out in agony and drop the pan.''')
      time.sleep(0)
      print('''\n> He kicks you in the face and pins you down on the floor. He whispers in your ear,''')
      time.sleep(0)
      print(red()+bright()+'''\n> "Keeping the window open at night is dangerous!!!!!!" 
      '''+reset())
      time.sleep(0)
      print('''\n> Before anything makes sense......''')
      time.sleep(0)
      print('''\n> He rams the knife into your heart, making you choke on your blood.''')
      time.sleep(0)
      print('''\n> You feel the life draining out of your body, numbing your senses.''')
      time.sleep(0)
      print('''\n> You look into his eyes, hoping to see some reason or mercy, but all you see is.....''')
      time.sleep(0)
      print('''\n> Rage and insanity.''')
      time.sleep(0)
      print('''\n> He grins and says, ''')
      time.sleep(0)
      print(red()+bright()+'''\n> "By the way, cereal boxes don't belong in the fridge."'''+reset())
      time.sleep(0)
      print('''\n> He twists the knife, making you groan one last time before....''')
      time.sleep(0)
      print('''\n> Everthing goes dar......''')
      break
      
    else:
      print(red()+'''\n> Wrong input. Try again.'''+reset())
