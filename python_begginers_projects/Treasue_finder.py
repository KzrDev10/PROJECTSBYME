print('''
      ____________________________________________________________________
      / \-----     ---------  -----------     -------------- ------    ----\
      \_/__________________________________________________________________/
      |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
      |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
      | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
      |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
      |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
      |  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|
      |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|
      |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
      | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
      |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
      |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
      | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
      |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
      | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
      |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
      | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
      |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
      | ~~ ~|__,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
      |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
      |____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
      / \----- ----- ------------  ------- ----- -------  --------  -------\
      \_/__________________________________________________________________/
            ''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure")

choice_1 = input('You\'re at a cross road there are 3 paths left right or you go back l or r or b: ').lower()
if choice_1 == 'b':
      print("You turned back and was attacked by a snake. Game Over")
      print('''

       ---_ ......._-_--.
      (|\ /      / /| \  
      /  /     .'  -=-'   `.
     /  /    .'             )
   _/  /   .'        _.)   /
  / o   o        _.-' /  .'
  \          _.-'    / .'*|
   \______.-'//    .'.' \*|
    \|  \ | //   .'.' _ |*|
     `   \|//  .'.'_ _ _|*|
      .  .// .'.' | _ _ \*|
      \`-|\_/ /    \ _ _ \*
       `/'\__/      \ _ _ \*
      /^|            \ _ _ \*
     '  `             \ _ _ \      A
                       \_
      ''')
elif choice_1 == 'r':
      print("You were eaten by a lion.Game Over")
      print('''

            ,aodObo,
            ,AMMMMP~~~~
      ,MMMMMMMMA.
      ,M;'     `YV'
      AM' ,OMA,
      AM|   `~VMM,.      .,ama,____,amma,..
      MML      )MMMD   .AMMMMMMMMMMMMMMMMMMD.
      VMMM    .AMMY'  ,AMMMMMMMMMMMMMMMMMMMMD
      `VMM, AMMMV'  ,AMMMMMMMMMMMMMMMMMMMMMMM,                ,
      VMMMmMMV'  ,AMY~~''  'MMMMMMMMMMMM' '~~             ,aMM
      `YMMMM'   AMM'        `VMMMMMMMMP'_              A,aMMMM
      AMMM'    VMMA. YVmmmMMMMMMMMMMML MmmmY          MMMMMMM
      ,AMMA   _,HMMMMmdMMMMMMMMMMMMMMMML`VMV'         ,MMMMMMM
      AMMMA _'MMMMMMMMMMMMMMMMMMMMMMMMMMA `'          MMMMMMMM
      ,AMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMa      ,,,   `MMMMMMM
      AMMMMMMMMM'~`YMMMMMMMMMMMMMMMMMMMMMMA    ,AMMV    MMMMMMM
      VMV MMMMMV   `YMMMMMMMMMMMMMMMMMMMMMY   `VMMY'  adMMMMMMM
      `V  MMMM'      `YMMMMMMMV.~~~~~~~~~,aado,`V''   MMMMMMMMM
      aMMMMmv       `YMMMMMMMm,    ,/AMMMMMA,      YMMMMMMMM
      VMMMMM,,v       YMMMMMMMMMo oMMMMMMMMM'    a, YMMMMMMM
      `YMMMMMY'       `YMMMMMMMY' `YMMMMMMMY     MMmMMMMMMMM
      AMMMMM  ,        ~~~~~,aooooa,~~~~~~      MMMMMMMMMMM
            YMMMb,d'         dMMMMMMMMMMMMMD,   a,, AMMMMMMMMMM
            YMMMMM, A       YMMMMMMMMMMMMMY   ,MMMMMMMMMMMMMMM
            AMMMMMMMMM        `~~~~'  `~~~~'   AMMMMMMMMMMMMMMM
            `VMMMMMM'  ,A,                  ,,AMMMMMMMMMMMMMMMM
      ,AMMMMMMMMMMMMMMA,       ,aAMMMMMMMMMMMMMMMMMMMMMMMMM
      ,AMMMMMMMMMMMMMMMMMMA,    AMMMMMMMMMMMMMMMMMMMMMMMMMMMM
      ,AMMMMMMMMMMMMMMMMMMMMMA   AMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
      AMMMMMMMMMMMMMMMMMMMMMMMMAaAMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
      ''')
elif choice_1 == 'l':
      choice_2 = input("You come to a lake. There is a temple at the end of the lake. you can wait or swim S(swim) or W (wait)").lower()
      if choice_2 == 's':
            print("You were attacked by a crocodile. Game Over")
            print('''
                  _.---._     .---.
                  __...---' .---. `---'-.   `.
            .-''__.--' _.'( | )`.  `.  `._ :
            .'__-'_ .--'' ._`---'_.-.  `.   `-`.
                  ~ -._ -._``---. -.    `-._   `.
                        ~ -.._ _ _ _ ..-_ `.  `-._``--.._
                                    -~ -._  `-.  -. `-._``--.._.--''.
                                          ~ ~-.__     -._  `-.__   `. `.
                                                ~~ ~---...__ _    ._ .` `.
                                                            ~  ~--.....--~`
            ''')
      elif choice_2 == "w":
            
            choice_3 = input("A magic boat arrived. Do you take it? Y/N").lower()
            if choice_3 == "n":
                  print("You waited too long and the boat left without you. A lion came and ate you. Game Over")
                  print('''
                        ,aodObo,
            ,AMMMMP~~~~
      ,MMMMMMMMA.
      ,M;'     `YV'
      AM' ,OMA,
      AM|   `~VMM,.      .,ama,____,amma,..
      MML      )MMMD   .AMMMMMMMMMMMMMMMMMMD.
      VMMM    .AMMY'  ,AMMMMMMMMMMMMMMMMMMMMD
      `VMM, AMMMV'  ,AMMMMMMMMMMMMMMMMMMMMMMM,                ,
      VMMMmMMV'  ,AMY~~''  'MMMMMMMMMMMM' '~~             ,aMM
      `YMMMM'   AMM'        `VMMMMMMMMP'_              A,aMMMM
      AMMM'    VMMA. YVmmmMMMMMMMMMMML MmmmY          MMMMMMM
      ,AMMA   _,HMMMMmdMMMMMMMMMMMMMMMML`VMV'         ,MMMMMMM
      AMMMA _'MMMMMMMMMMMMMMMMMMMMMMMMMMA `'          MMMMMMMM
      ,AMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMa      ,,,   `MMMMMMM
      AMMMMMMMMM'~`YMMMMMMMMMMMMMMMMMMMMMMA    ,AMMV    MMMMMMM
      VMV MMMMMV   `YMMMMMMMMMMMMMMMMMMMMMY   `VMMY'  adMMMMMMM
      `V  MMMM'      `YMMMMMMMV.~~~~~~~~~,aado,`V''   MMMMMMMMM
      aMMMMmv       `YMMMMMMMm,    ,/AMMMMMA,      YMMMMMMMM
      VMMMMM,,v       YMMMMMMMMMo oMMMMMMMMM'    a, YMMMMMMM
      `YMMMMMY'       `YMMMMMMMY' `YMMMMMMMY     MMmMMMMMMMM
      AMMMMM  ,        ~~~~~,aooooa,~~~~~~      MMMMMMMMMMM
            YMMMb,d'         dMMMMMMMMMMMMMD,   a,, AMMMMMMMMMM
            YMMMMM, A       YMMMMMMMMMMMMMY   ,MMMMMMMMMMMMMMM
            AMMMMMMMMM        `~~~~'  `~~~~'   AMMMMMMMMMMMMMMM
            `VMMMMMM'  ,A,                  ,,AMMMMMMMMMMMMMMMM
      ,AMMMMMMMMMMMMMMA,       ,aAMMMMMMMMMMMMMMMMMMMMMMMMM
      ,AMMMMMMMMMMMMMMMMMMA,    AMMMMMMMMMMMMMMMMMMMMMMMMMMMM
      ,AMMMMMMMMMMMMMMMMMMMMMA   AMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
      AMMMMMMMMMMMMMMMMMMMMMMMMAaAMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
                  
                  ''')
      
            
            elif choice_3 == "y":
                  print('''
 .  o ..                  
     o . o o.o                
          ...oo               
            __[]__            
         __|_o_o_o\__         
         \""""""""""/         
          \. ..  . /          
     ^^^^^^^^^^^^^^^^^^^^
    
                  ''')
                  print("You arrive at the temple safely. There are 3 doors Red, Blue and Yellow Which one do you choose R/B/Y")
            
                  choice_4 =input("> ").lower()
                  if choice_4 == "r":
                        print("You were burned by fire. Game Over")
                        print('''
                  
                  (  .      )
            )           (              )
                  .  '   .   '  .  '  .
            (    , )       (.   )  (   ',    )
            .' ) ( . )    ,  ( ,     )   ( .
            ). , ( .   (  ) ( , ')  .' (  ,    )
      (_,) . ), ) _) _,')  (, ) '. )  ,. (' )
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                  ''')
                  elif choice_4 == "b":
                        print("You saw the treasure room but was stabbed by a thug. Game Over")
                        print('''
                            ,--.
                           {    }
                           K,   }
                          /  ~Y`
                     ,   /   /
                    {_'-K.__/
                      `/-.__L._
                      /  ' /`\_}
                     /  ' /
             ____   /  ' /
      ,-'~~~~    ~~/  ' /_
    ,'             ``~~~  ',
   (                        Y
  {                         I
 {      -                    `,
 |       ',                   )
 |        |   ,..__      __. Y
 |    .,_./  Y ' / ^Y   J   )|
 \           |' /   |   |   ||
  \          L_/    . _ (_,.'(
   \,   ,      ^^""' / |      )
     \_  \          /,L]     /
       '-_~-,       ` `   ./`
          `'{_            )
              ^^\..___,.--`
                        
                  ''')

                  elif choice_4 == "y":
                        print("You found the treasure! You Win!")
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
      /______/______/______/______/______/______/______/______/______/______/[TomekK]
      *******************************************************************************

            ''')
            
                        
            
            

     