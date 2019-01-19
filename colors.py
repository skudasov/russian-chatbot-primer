from colorama import Fore, Back, Style
from colorama import init
init()


red = lambda text: Fore.RED + text + Fore.RESET
green = lambda text: Fore.GREEN + text + Fore.RESET
yellow = lambda text: Fore.LIGHTYELLOW_EX + text + Fore.RESET
