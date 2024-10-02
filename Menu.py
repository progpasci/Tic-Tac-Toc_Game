#! usr/bin/env
class Menu :
    def display_main_menu(self):
        msgMainMenu = [ "WELCOME ", 
                        "TO MY [ X & O ] GAME !.",
                        "1). START GAME.", 
                        "2). QUIT GAME." ]
        print(("-"*33).center(78,' '))
        print(f"\t\t      |\t\t   {msgMainMenu[0]}\t      |")
        print(f"\t\t      |     {msgMainMenu[1]}   |")
        print(f"\t\t      |        {msgMainMenu[2]}        |")
        print(f"\t\t      |        {msgMainMenu[3]}         |")
        print(("-"*33).center(78,' '))
        choise = input("\t\t        Enter Your Choise (1 or 2) :")
        return choise
        
    def display_end_game_menu(self):
        msgEndGameMenu = [ "THANK YOU FOR ENJOYING YOUR TIME IN THIS GAME.", 
                           "YOU WANT TO PLAY AGAIN ?: ",
                           "1). RESTART GAME.", 
                           "2). QUIT GAME." ]
        print(("-"*53).center(64,' '))
        print(f"     |   {msgEndGameMenu[0]}  |")
        print(f"     |\t   ------------------------------------------    |")
        print(f"     |\t            {msgEndGameMenu[1]}\t         |")
        print(f"     |\t\t      {msgEndGameMenu[2]}\t\t         |")
        print(f"     |\t\t      {msgEndGameMenu[3]}\t\t         |")
        print(("-"*53).center(64,' '))
        choise = input("\t    Enter Your Choise (1 or 2) :")
        return choise
