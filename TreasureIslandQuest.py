print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
path1 = input('You have arrived at a cross road. What path shall you choose? Type "left" or "right": ').lower()

print("\n")

if path1 == "left":
    path2 = input('''You hike for another mile and stumble upon an ocean with an island abroad. 
       Do you choose to swim across, or wait for a boat? Type "swim" or "wait": ''').lower()
    print("\n")

    if path2 == "wait":
        path3 = input('''You spot a home and make your way inside. 
        Inside you notice 2 doors: red, and yellow. Which door do you open? ''').lower()
        print("\n")
        if path3 == "yellow":
            print(''' 

                                       .-----.   ()()
                                      /       \ .'()
                                      |__...__|/
                                      |_....._|
                                    .-'  ___  '-.
                                    \_.-`. .`-._/
              __ .--. _              (|\ (_) /|)
           .-;.-"-.-;`_;-,            ( \_=_/ )
         .(_( `)-;___),-;_),          _(_   _)_
        (.( `\.-._)-.(   ). )       /` ||'-'|| `\
      ,(_`'--;.__\  _).;--'`_)  _  /_/ (_>o<_) \_\
     // )`--..__ ``` _( o )'(';,)\_//| || : || |\\
     \;'        `````  `\\   '.\\--' |`"""""""`|//
     /                   ':.___//     \___,___/\_(
    |                      '---'|      |__|__|
    ;                           ;      ;""|"";
     \                         /       [] | []
      '.                     .'      .'  / \  '.
     jgs'-,.__         __.,-'        `--'   `--'
         (___/`````````\___) 

            
           WHOO-HOO!!! You have found the treasure!!!
            
            
            ''')
        else:
           print('''    (    )
                  ((((()))
                  |o\ /o)|
                  ( (  _')
                   (._.  /\__
                  ,\___,/ '  ')
    '.,_,,       (  .- .   .    )
     \   \\     ( '        )(    )
      \   \\    \.  _.__ ____( .  |
       \  /\\   .(   .'  /\  '.  )
        \(  \\.-' ( /    \/    \)
         '  ()) _'.-|/\/\/\/\/\|
             '\\ .( |\/\/\/\/\/|
               '((  \    /\    /
               ((((  '.__\/__.')
                ((,) /   ((()   )
                 "..-,  (()("   /
            pils  _//.   ((() ."
          _____ //,/" ___ ((( ', ___
                           ((  )
                            / /
                          _/,/'
                        /,/,"

           Uh oh... You have been eaten by hungry beasts...Game over.
           
           ''')

    else:
        print(''' 

                                 ,-
                               ,'::|
                              /::::|
                            ,'::::o\                                      _..
         ____........-------,..::?88b                                  ,-' /
 _.--"""". . . .      .   .  .  .  ""`-._                           ,-' .;'
<. - :::::o......  ...   . . .. . .  .  .""--._                  ,-'. .;'
 `-._  ` `":`:`:`::||||:::::::::::::::::.:. .  ""--._ ,'|     ,-'.  .;'
     """_=--       //'doo.. ````:`:`::::::::::.:.:.:. .`-`._-'.   .;'
         ""--.__     P(       \               ` ``:`:``:::: .   .;'
                "\""--.:-.     `.                             .:/
                  \. /    `-._   `.""-----.,-..::(--"".\""`.  `:\
                   `P         `-._ \          `-:\          `. `:\
                                   ""            "            `-._)
        
        
        
        ''')
        print("Game over! You have been eaten by mysterious sharks.")



else:
    print("Whoops! Seems like you fell through a booby trap! Better luck next time...")













