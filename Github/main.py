#Programmer: Github:BabbaWaagen ; Discord:
#KI creator: ;Discord:
#Mental Supporter: Github:DeMika69 ; Discord:

##Import##

from colorama import Fore, Back, Style
from colorama import Fore, Back, Style

## Variables ##

art = r'''
      _..._
    .'     '.      _
   /    .-""-\   _/ \
.-|   /:.   |  |   |
|  \  |:.   /.-'-./
| .-'-;:__.'    =/
.'=  *=|E.S.A _.='
/   _.  |    ;
;-.-'|    \   |
/   | \    _\  _\
\__/'._;.  ==' ==\
         \    \   |
         /    /   /
         /-._/-._/
       \   `\  \
      `-._/._/
'''


##Functions##

def print_LOG(message,Status):
        match Status:
            case "Info":
                print(Fore.CYAN + f'LOGs::INFO::{message}')
                print(Style.RESET_ALL)

            case "Error":
                print(Fore.RED + f'LOGs::ERROR::{message}')
                print(Style.RESET_ALL)

            case _:
                print(Fore.RED + "ERROR IN CODE!!!")
                print(Style.RESET_ALL)



# Init
if __name__ == '__main__':
        print(Fore.CYAN+art)
        print(Style.RESET_ALL)
        print_LOG("INIT","Info")
