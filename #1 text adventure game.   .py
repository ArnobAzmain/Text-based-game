import time 
print("Welcome to this mini text adventure game! Its my very first game that I made. There are some issues here and there and it is still in beta form but anyway hope you enjoy 😄\n")

time.sleep(1)
name = input("""Enter your name before we start = """).strip().title()


#        Intro
print("""\n>> You are watching a TV show in your home. You are alone. All of a sudden you hear 👂 footsteps 👣 outside...
""")
time.sleep(5)
print(""">>Its loud 🔊 enough to hear even through the sounds from your tv.
""")
time.sleep(3)
print(""">>You check the time on you phone.
""")
time.sleep(2)
print(""">>Your shocked!!
""")
time.sleep(2)
print(""">>its 12:13 am!! 
""")
time.sleep(2)
print(
    """>>"You ask yourself, "Who could be walking around my house this late at night? None of my parents are supoosed to come. I mean they didn't send me any message. And my neighbour won't be it too cuz he is out of town.
""")
time.sleep(8)
print(""">>Should you look through the window?
""")
time.sleep(2)
print(""">>Or
""")

time.sleep(1)
print(""">>Just stay silent untill 'it' goes away?\n""")

#      Option 1 List

option1 = [
    "You stay silent and hopefully wait for it to go away",
    "I stay silent and hopefully wait for it to go away", "stay silent",
    "silent", "wait", "stay", "s", "just stay silent untill 'it' goes away"
]
option2 = [
    "you look outside from the nearby window",
    "I look outside from the nearby window", "look outside", "look", "outside",
    "window", "the window", "l", "look through the window",
    "through the window"
]

# Answer for the 1st question

time.sleep(1)
answer1 = input("---->").strip()

# Reply for the 1st option
if answer1 in option1:
  time.sleep(1)
  print(
      """\n>>After a very short second, you hear that the footsteps 👣 slowly walk towards your front door and.....
    """)
  time.sleep(4)
  print(""">>Knocked!!!!!!
    """)
  time.sleep(1)
  print(""">>Now you are scared!!!
    """)
  time.sleep(2)
  print(
      """>>You are staring to panic 🙀, thinking 🤔 what you would do in this situation
    """)
  time.sleep(4)
  print(""">>Answer the door?????
    """)
  time.sleep(1)
  print(""">>Or
    """)
  time.sleep(1)
  print(""">>Still remain silent? 
    """)
  time.sleep(1)
  answer2 = input("---->").strip()

  # Option List for second senario
  option3 = ["answer", "answer the door", "the door", "door", "a"]
  option4 = ["silent", "still remain silent", "remain silent", "s"]

  #This part is for the 1st question
  #   but if answered then afterwards

  if answer2 in option4:
    time.sleep(1)
    print(
        """\n>>After knocking couple of times, the person stopped and for about 5 to 6 minutes, there remain complete silent......
        """)
    time.sleep(6)
    print("""****Ding****
        """)
    time.sleep(2)
    print(
        """>>All of sudden, your phone's notification sound pops up, startling you. And then when you go adhead to check.... 
        """)
    time.sleep(4)
    print(""">>Your heart drops to the ground!!!
        """)
    time.sleep(3)
    print(""">>You got a text message, from an unknown number. It says, 
        """)
    time.sleep(3)
    print(
        f'''>>"I know you are in there , scared, watching TV. I'll come again someday '{name}'. Next time, open the door."
        ''')
    time.sleep(6)
    print(
        """>>After that the man wasn't there and since then you haven't faced that man and later in fear that he might return again, you and your parents moved out to a different town and since then nothing happened. Well at least for now.......
        """)
    time.sleep(7)
    print(
        """>>Hey there! 🤗 I hope you liked the play/game 🎮. This ending 👏 is the short one. If you want something a big longer then I suggest you restart and choose different options. Anyway thanks for playing. 
        Created by:- Arnob""")

  elif answer2 in option3:
    time.sleep(1)
    print(
        """\n>>You opened the door thinking that its a person in need for help. But.....
        """)
    time.sleep(3)
    print(
        """>>As you opened the door, you see that a large man with an axe in hand lunges towards you forcing you to fall down , started to punch you and before you could do anything, you see the axe up in the air and..............
        """)
    time.sleep(9)
    print(
        """>>Hey there! I hope you liked the play/game. This ending is the short one. If you want something a big longer then I suggest you restart and choose different options. And if you still don't known what happened to you, well.... you died 💀. Anyway thanks again for playing. Created by:- Arnob"""
    )

  else:
    print(""">>wrong or invalid 😓answer!!!!.....GG""")

#  This part is with the first questions

elif answer1 in option2:
  time.sleep(1)
  print("""\n>>You slowly but carefully reach your nearby window by the couch.
    """)
  time.sleep(3)
  print(""">>You remove a tiny bit of the courtain. As you look...
    """)
  time.sleep(3)
  print(
      """>>You see a dark silhouette of a man on the other end of the window, trying to look inside.
    """)
  time.sleep(4)
  print(""">>It spots you!!!!
    """)
  time.sleep(3)
  print(
      """>>It then rushes towards your front door and started knocking loudly and saying something...
    """)
  time.sleep(5)
  print(
      """>>The man says, "Hey, I need help! My pickup truck won't start, could I use your phone to contact my office?
    """)
  time.sleep(4)
  print("""should you----\n""")
  time.slee>>p(1)
  print(""">>Let him use your phone?
    """)
  time.sleep(1)
  print(""">>or
    """)
  time.sleep(1)
  print(""">>Don't let him use your phone?
    """)
  #Options for the response

  option5 = ["let him use", "let him use my phone", "let him", "let", "l"]
  option6 = [
      "don't", "dont", "don't let him use my phone",
      "dont let him use my phone"
  ]

  answer3 = input("---->").strip()

  if answer3 in option5:
    time.sleep(1)
    print(
        """\n>>You then slowly went close to your front door with your phone in your hand. But you check through the side window of your door and see no truck anywhere.At least as your eyes can see. So you asked where is his truck? But there is no response! You asked again couple more times but... Its the same. He repeated the same thing again without answering any of your questions.
        """)
    time.sleep(10)
    print(
        """>>You get suspicious. You don't know what to do.\n\nEither call the police? or \nJust refuse him?
        """)

    answer0 = input("--->")

    option12 = ["call", "police", "call the police"]
    option13 = ["refuse", "just refuse him", "just refuse", "r"]

    ########$$$$$3#Work in progress >√√√√√

    if answer0 in option12:
      time.sleep(1)
      print(
          """\n>>You immediately call the police, and as you were on call, the man then rushed out somewhere...
            """)
      time.sleep(5)
      print(
          """>>You thought that the man got scared and went away because he somehow understood that you were on call with the police, but....""")
      time.sleep(6)
      print("""\n>>Thats not the case.....
            """)
      time.sleep(2)
      print(
          """>>You see the silhouette quickly going towards the back. But then it hit you.....
            """)
      time.sleep(5)
      print(">>Your back door isn't locked 🔓 👀.....\n")
      time.sleep(4)
      print(
          """>>Do you rush👣 to you back door and lock 🔓 it? or Go upstairs  to you room and hide there?
            """)

      options14 = [
          "rush", 'rush towards back door', 'i rush towards the back door',
          'i rush', 'lock it', 'lock', "rush to the back door and lock it" 
      ]
      options15 = [
          'go upstairs', 'upstairs', 'go to my room', 'go to the room',
          'go upstairs to my room'
      ]

      answer9 = input('---->')
      if answer9 in options14:
        time.sleep(1)
        print(
            """\n>>You quickly dash towards the back door 🚪 and was able to lock 🔐  it before the man could.
                """)
        time.sleep(5)
        print(
            """>>But there... through the door window you see the horrifying face 👤 of the man.
                """)
        time.sleep(5)
        print(
            """>>His face is pale white, he looks like he is 40-50 years old, messy hair, but his eyes are RED. Like really red.
            """)
        time.sleep(6)
        print(""">>The man didn't try to open the door anymore. It's more like me seeing his face was enough for him. 
Like his goal or objective was met.
              """)
        time.sleep(5)
        print(
            """>>He then had a wide grin on his face. This Disgusting 🤮 and horrible 😷 expression made you almost vomit 🤢.
                """)
        time.sleep(6)
        print(
            """>>He then left slowly backing away from the back door while keeping eye contact with you and then slowly faded into the darkness.
            """)
        time.sleep(5)
        print(">>Shortly the police 🚓 🚨 came. You told them everything as best to your ability. They did a check around the propert but didn't find anything. Later the police contacted you parents, told them everything and to keep you safe they stayed around you house in their car all night.\n")
        time.sleep(9)
        print(
            """>>Later, in the morning 🌅 your parents came from their trip, and after some coversation with the police, your parents decided to move from this town and since then you live someplace really far from that town and never encountered it.
            """)
        time.sleep(10)
        print(">>Hey there! 👋 Thank you 👍 for playing this game. Hope you enjoyed it. This is one of the short endings. If you want something a bit bigger, why not try other options and see where it leads.Anyway....this is my first time ever trying to make a game. I like the way it is  and hope you liked it as well. Don't know if ill  be making more of this or not. Anyway thanks again. Created by:- Arnob👋😉   ")

    elif answer0 in option13:
      time.sleep(1)
      print(
          """>>Even after refusing, he asked again for the phone 📱 and started knocking even harder
          """)
      time.sleep(5)
      print(
          """>>As you remained still, he started to say something outloud in something gibberish like saying some prayer 🤲 or something. This time you are for sure that this is not normal.
          """)
      time.sleep(6)
      print(
          """>>You yelled and screamed for him to go away. And then eveything stopped suddenly. Not a single sound can be heared. Its like everything died or something.
          """)
      time.sleep(5)
      print(
          """>>After a brief silent, he started laughing. Its like the laugh of a devil or something. After that he slowly walked away saying that He will return tomorrow, for YOU!
          """)
      time.sleep(6)
      print(
          """>>Not knowing what to do in this situation, you called one of your friend to come over and stay the night.
          """)
      time.sleep(8)
      print(
          """\n>>After he came you told him everything of what happened. He was shocked but decided to stay the night. Of course you told you parents! Then the next morning you parents told everything to the police and then afterwards you moved from that town and started living in a different town and study in a different school.
          \n""")
      time.sleep(10)
      print(
          """>>Later one day you heard from your friend that the man was caught as we was doing the same thing but to another person.
          """)
      time.sleep(5)
      print(
          """>>In the end you were relieved about it and went on carryin on day peacefully.
          """)
      time.sleep(5)
      print(
          """>>Hey there! 👋 Thank you 👍 for playing 🎴 this game. Hope you enjoyed it. This is my first time ever trying to make a game. I like the way it is  and hope you liked it as well. Don't know if ill 🥶 be making more of this or not. Anyway thanks again. 
          Created by:- Arnob👋😉""")

  elif answer3 in option6:
    time.sleep(1)
    print(
        """>>Instead you began asking questions about his truck, what he does, which comapny he works for, etc.
        """)
    time.sleep(5)
    print(
        """>>But there is no answer! Suddenly he started to bang on the door almost as if he is going to break it! You quickly went upstairs to your room and locked it.
        """)
    time.sleep(6)
    print(""">>Would you call the police? or Just stay locked up? or.....
          """)
    print(""">>Fight him off.
          """)
    answer4 = input("---->").strip()

    option7 = ["call the police", "police"]
    option8 = ["stay locked up", "stay", "stay locked", "locked up"]
    option9 = ["fight", "fight him", "fight off"]

    if answer4 in option9:
      time.sleep(1)
      weapon = input(
          ">>What weapon do you want to fight him with?  = ").strip().title()
      time.sleep(1)
      print(
          f""">>You grabbed a {weapon} and quickly opened the door to charge but you couldn't do anything due to his strength and ended up dying by his hands....Thank you for playing.
           """)

    elif answer4 in option7:
      time.sleep(1)
      print(
          """>>You called the police and while you were on the call you hear glass shatter!!!...
            """)
      time.sleep(2)
      print(
          """>>The police told you to stay put and don't leave the room untill they arrive but....
            """)
      time.sleep(4)
      print(
          """>>Meanwhile you hear that the man got inside the house and walking around downstairs.
            """)
      time.sleep(5)
      print(
          """>>All of a sudden you hear that the man is walking upstairs. He started to open all the doors searching for you.
            """)
      time.sleep(5)
      print(""">>Do you stay put? or hide under the bed? 
            """)

      answer5 = input("---->")

      option10 = ["stay put", "stay", "s", "put"]
      option11 = ["hide under the bed", "hide"]

      if answer5 in option10:
        time.sleep(1)
        print(
            """>>The man then came in front of your door and as it won't open he understood you are there and started to break the door.
                """)
        time.sleep(5)
        print(
            """>>But luckily the police were able to come in fast and when the man was trying to escape, they managed to catch him and take him in custody.
                """)
        time.sleep(5)
        print(
            """>>The next day, the police came and informed you that, that man was serial killer and he was in their wanted list and finally was able to capture him after 7 years.
                """)
        time.sleep(5)
        print(
            """>>"The police then told me that you were lucky and have a good day.
                """)
        time.sleep(2)
        print(
            """>>You wondered if i did open the door.... You wouldn't be here the next day.
                """)
        time.sleep(2)

        print(
            """>>Thank you for playing this mini horror game. Well.... not sure if it is horror. But anyway hope you enjoyed and I will probably see you next time. Bye Bye!!!
             created by:- Arnob""")

      elif answer5 in option11:
        time.sleep(1)
        print(
            """>>As you quickly got under your bed, immediately the door broke!!
                """)
        time.sleep(3)
        print(
            """>>You observe the shoes entering your room and moving around. He went to your closet, opened it, looked around and slowly....
                """)
        time.sleep(4)
        print(
            """>>Came in front of you bed.... Stood there for couple of seconds and as he crouched down to look underneath...
                """)
        time.sleep(5)
        print(""">>POLICE!!!!
                """)
        time.sleep(2)
        print(
            """>>He ran away from your room and you hear many sounds coming downstairs.
                """)
        time.sleep(3)
        print(
            """>>You then got out of your bed and went downstairs and see many police in your house.
                """)
        time.sleep(3)
        print(""">>Two police approached you and asked if you are okay or not.
                """)
        time.sleep(2)
        print(
            """>>You said you are okay and then they asked where your parents were. You told them that they went on a trip. The police officer then told me to call them. The officer then spoke with my parents on the phone and later told me to relax and rest up since there is no more troubles anymore.
                """)
        time.sleep(8)
        print(
            """>>You then went back to your room and tried to sleep but no sleep came and then the next morning you paremts came all worried. You told them what happened and that was it.
                """)
        time.sleep(7)
        print(
            """>>Later you came to know that, that man was a serial killer and after 7 years, and the police finally caught him.
                """)
        time.sleep(5)
        print(
            """>>You then wondered what might have happened if you didn't call the police or what if they didn't have arrived that quickly and mamy thoughts came to you head.
                """)
        time.sleep(6)
        print(
            """>>Ever since then, you never faced something like that and lived peacefully.
                """)
        time.sleep(3)
        print(
            """\n>>Thank you for playing this mini horror game. Well.... not sure if it is horro. But anyway hope you enjoyed and i will probably see you next time. Bye Bye!!! Created by:- Arnob.
                """)

  else:
    print(">>Incorrect typing.... GG")

else:
  print(">>wrong keyword, ...GG")
