from os import get_terminal_size
from simple_term_menu import TerminalMenu
import subprocess


def main():
    if get_terminal_size().columns > 120:
        print(
            """
 $$$$$$\            $$\           $$\   $$\               $$\       $$\        $$$$$$$$\                  $$\           
$$  __$$\           $$ |          \__|  $$ |              $$ |      $$ |       \__$$  __|                 $$ |          
$$ /  \__| $$$$$$\  $$ | $$$$$$\  $$\ $$$$$$\    $$$$$$\  $$$$$$$\  $$ | $$$$$$\  $$ | $$$$$$\   $$$$$$\  $$ | $$$$$$$\ 
\$$$$$$\  $$  __$$\ $$ |$$  __$$\ $$ |\_$$  _|   \____$$\ $$  __$$\ $$ |$$  __$$\ $$ |$$  __$$\ $$  __$$\ $$ |$$  _____|
 \____$$\ $$ /  $$ |$$ |$$ /  $$ |$$ |  $$ |     $$$$$$$ |$$ |  $$ |$$ |$$$$$$$$ |$$ |$$ /  $$ |$$ /  $$ |$$ |\$$$$$$\  
$$\   $$ |$$ |  $$ |$$ |$$ |  $$ |$$ |  $$ |$$\ $$  __$$ |$$ |  $$ |$$ |$$   ____|$$ |$$ |  $$ |$$ |  $$ |$$ | \____$$\ 
\$$$$$$  |$$$$$$$  |$$ |\$$$$$$  |$$ |  \$$$$  |\$$$$$$$ |$$$$$$$  |$$ |\$$$$$$$\ $$ |\$$$$$$  |\$$$$$$  |$$ |$$$$$$$  |
 \______/ $$  ____/ \__| \______/ \__|   \____/  \_______|\_______/ \__| \_______|\__| \______/  \______/ \__|\_______/ 
          $$ |                                                                                                          
          $$ |                                                                                                          
          \__|                                                                                                          
"""
        )
    else:
        print(
            """
  ____        _       _ _        _     _     _____           _     
 / ___| _ __ | | ___ (_) |_ __ _| |__ | | __|_   _|__   ___ | |___ 
 \___ \| '_ \| |/ _ \| | __/ _` | '_ \| |/ _ \| |/ _ \ / _ \| / __|
  ___) | |_) | | (_) | | || (_| | |_) | |  __/| | (_) | (_) | \__ \\
 |____/| .__/|_|\___/|_|\__\__,_|_.__/|_|\___||_|\___/ \___/|_|___/
       |_|                                                         
"""
        )

    options = ["1. XSS Vulnerability Scanner ", "entry 2", "entry 3"]
    scripts = ["xssForms.py", "test2", "test3"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()

    subprocess.run(['python',scripts[menu_entry_index]])


if __name__ == "__main__":
    main()
