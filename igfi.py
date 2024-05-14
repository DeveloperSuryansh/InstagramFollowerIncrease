# -*- coding: utf-8 -*-
"""
Author: new92
Github: @new92
Leetcode: @new92
PyPI: @new92

IGFI is a python script for increasing the number of followers of an Instagram account.

*********IMPORTANT*********

User's login credentials (such as: username, password) will not be stored or saved !
Will be used only to increase the followers of the user's Instagram account

***************************
"""

try:
    import sys
    from time import sleep
    if sys.version_info[0] < 3:
        print("[✘] Error ! IGFI requires Python 3 ! ")
        sleep(1.3)
        print("""[+] Instructions to download Python 3: 
        Linux: apt install python3
        Windows: https://www.python.org/downloads/
        MacOS: https://docs.python-guide.org/starting/install3/osx/""")
        sleep(3)
        print("[+] Please install Python 3 and then use IGFI ✅")
        sleep(1.2)
        print("[+] Exiting...")
        sleep(0.8)
        quit(0)
    import platform
    from os import system
    from rich.align import Align
    from rich.table import Table
    from rich.live import Live
    from rich.console import Console
    console = Console()
    mods = ['sys', 'time', 'rich', 'platform', 'os', 'logging', 'instagrapi', 'requests', 'instaloader', 'argparse', 'colorama']
    with console.status('[bold dark_orange]Loading module...') as status:
        for mod in mods:
            sleep(0.8)
            console.log(f'[[bold red]{mod}[/]] => [bold dark_green]ok[/]')
    import os
    import instagrapi
    import requests
    import logging
    import instaloader
    import argparse
    import ctypes
    from colorama import init, Fore
except (ImportError, ModuleNotFoundError):
    print("[!] WARNING: Not all packages used in IGFI have been installed !")
    sleep(1)
    print("[+] Ignoring warning...")
    sleep(0.5)
    if sys.platform.startswith('linux') or sys.platform == 'darwin':
        if os.geteuid():
            print("[✘] Root user not detected !")
            sleep(2)
            print("[+] Attempting to enable root user...")
            sleep(1)
            os.execvp("sudo", ["sudo", sys.executable] + sys.argv)
            print("[✔] Done.")
            sleep(0.6)
            print("[+] Loading required modules...")
            sleep(0.4)
        system("sudo pip install -r ./../requirements.txt" if sys.platform.startswith('linux') else "python -m pip install ./../requirements.txt")
    elif platform.system() == 'Windows':
        if not ctypes.windll.shell32.IsUserAnAdmin():
            print("[✘] Root user not detected !")
            sleep(2)
            print("[+] Attempting to enable root user...")
            sleep(1)
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
            if not ctypes.windll.shell32.IsUserAnAdmin():
                print("[+] Root user permission denied.")
                sleep(1)
                print("[+] Exiting...")
                quit()
            print("[✔] Done.")
            sleep(0.6)
            print("[+] Loading required modules...")
            sleep(0.4)
        system("pip install -r ./../requirements.txt")

init(autoreset=True)
RED = Fore.RED
GREEN = Fore.GREEN
YELLOW = Fore.YELLOW

def clear():
    system('cls') if platform.system() == 'Windows' else system('clear')

sleep(0.8)
clear()
console.print("[bold green][✔] Successfully loaded modules.")
sleep(1.1)
clear()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
}

def fpath(fname: str):
    for root, dirs, files in os.walk('/'):
        if fname in dirs:
            return os.path.abspath(os.path.join(root, fname))

def Uninstall() -> str:
    def rmdir(dire):
        DIRS = []
        for root, dirs, files in os.walk(dire):
            for file in files:
                os.remove(os.path.join(root,file))
            for dir in dirs:
                DIRS.append(os.path.join(root,dir))
        for i in range(len(DIRS)):
            os.rmdir(DIRS[i])
        os.rmdir(dire)
    rmdir(fpath('IGFI'))
    return f"{GREEN}[✔] Files and dependencies uninstalled successfully !"

TABLE = [
    [
        "[b white]Author[/]: [i light_green]new92[/]",
        "[green]https://new92.github.io/[/]"
    ],
    [
        "[b white]Github[/]: [i light_green]@new92[/]",
        "[green]https://github.com/new92[/]"
    ],
    [
        "[b white]Leetcode[/]: [i light_green]@new92[/]",
        "[green]https://leetcode.com/new92[/]"
    ],
    [
        "[b white]PyPI[/]: [i light_green]@new92[/]",
        "[green]https://pypi.org/user/new92[/]"
    ]
]

console = Console()
table = Table(show_footer=False)
centered = Align.center(table)

def banner() -> str:
    console.print("""[bold yellow]
██╗░██████╗░███████╗██╗
██║██╔════╝░██╔════╝██║
██║██║░░██╗░█████╗░░██║
██║██║░░╚██╗██╔══╝░░██║
██║╚██████╔╝██║░░░░░██║
╚═╝░╚═════╝░╚═╝░░░░░╚═╝
[/]""", justify='center')

def nums():
    console.print("[bold yellow][1] Increase followers[/]")
    console.print("[bold yellow][2] Show IGFI's info[/]")
    console.print("[bold yellow][3] Clear log[/]")
    console.print("[bold yellow][4] Uninstall IGFI[/]")
    console.print("[bold yellow][5] Exit[/]")
        
def checkUser(username:str) -> bool:
    return username in ['', ' '] or len(username) > 30 or requests.get(f"https://www.instagram.com/{username}/", allow_redirects=False).status_code != 200

def main(username: str, password: str, session: str):
        clear()
        keep="y"
        sleep(1)
        check="n"
        users = {
            'Cristiano Ronaldo' : '173560420',
            'Cardi B' : '1436859892',
            'Kim Kardashian': '18428658',
            'Ariana Grande' : '7719696',
            'Nicki Minaj' : '451573056',
            'Beyonce' : '247944034',
            'Katy Perry' : '407964088',
            'Selena Gomez' : '460563723',
            'Justin Bieber' : '6860189',
            'Lionel Messi' : '427553890',
            'Neymar Jr' : '26669533',
            'Kylian Mbappe' : '4213518589',
            'Dua Lipa' : '12331195',
            'Billie Eilish' : '28527810',
            'Kylie Jenner' : '12281817',
            'Khloe Kardashian' : '208560325',
            'Kourtney Kardashian' : '145821237',
            'Jennifer Lopez' : '305701719',
            'Shakira' : '217867189',
            'National Geographic' : '787132',
            'FC Barcelona' : '260375673',
            'Real Madrid' : '290023231',
            'Champions League' : '1269788896',
            'Chris Brown' : '29394004',
            'Taylor Swift' : '11830955',
            'Kendall Jenner' : '6380930',
            'Virat Kohli' : '2094200507',
            'Zendaya' : '9777455',
            'Marvel' : '204633036',
            'Tom Holland' : '176618189',
            'Emma Watson' : '1418652011',
            'Millie Bobby Brown' : '3439002676',
            'Shawn Mendes' : '212742998',
            'Camila Cabello' : '19596899',
            'NASA' : '528817151',
            'Nike' : '13460080'
        }
        NAMES = list(users.keys())
        sleep(0.6)
        fname = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'files/consent.txt').replace('\\', '/')
        if not os.path.exists(fname):
            con="yes"
            if con:
                logging.basicConfig(
                    filename=fname,
                    level=logging.INFO,
                    format='%(asctime)s [%(levelname)s]: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S'
                )
                logging.info(f'Yes I consent that the author (DeveloperSuryansh) has no responsibility for any loss or damage the script may cause to {username}.')
            else:
                print(f"{YELLOW}[OK]")
                sleep(1)
                print(f"{YELLOW}[1] Exit")
                print(f"{YELLOW}[2] Uninstall IGFI and exit")
                num=int(input(f"{YELLOW}[>] Please enter a number (from the above ones) >>> "))
                valErr = num in [1,2]
                while not valErr:
                    try:
                        print(f"{YELLOW}[1] Exit")
                        print(f"{YELLOW}[2] Uninstall IGFI and exit")
                        num=int(input(f"{YELLOW}[>] Please enter again a number (from the above ones) >>> "))
                        valErr = num in [1,2]
                    except ValueError:
                        print(f"{RED}[✘] Please enter a valid number.")
                        sleep(2)
                        print(f"{GREEN}[+] Acceptable numbers >>> [1,2]")
                        sleep(1)
                if num == 1:
                    clear()
                    print(f"{RED}[+] Exiting...")
                    sleep(1)
                    print(f"{GREEN}[+] See you next time 👋")
                    sleep(1)
                    quit(0)
                else:
                    clear()
                    print(Uninstall())
                    sleep(1)
                    print(f"{RED}[+] Exiting...")
                    sleep(1)
                    print(f"{GREEN}[+] Thank you for choosing to use IGFI 😁")
                    sleep(2)
                    print(f"{GREEN}[+] If you have any suggestions or found a bug or need help feel free to contact me, at this email address: new92github@gmail.com")
                    sleep(2)
                    quit(0)
        sleep(1)
        clear()
        sleep(1)
        ga="y"
        loader = instaloader.Instaloader()
        client=instagrapi.Client()
        if session:
            try:
                loader.load_session_from_file(username)
            except FileNotFoundError:
                print(f"{RED}[✘] Session file not found !")
                sleep(0.8)
                print(f"{GREEN}[+] Logging in...")
                sleep(0.8)
        if not loader.context.is_logged_in:
            loader.login(username, password)
            loader.save_session_to_file()
        sleep(0.8)
        print(f"{YELLOW}[+] Attempting to login using {username} - {password}...")
        sleep(0.8)
        login = client.login(username, password)
        profile = instaloader.Profile.from_username(loader.context, username)
        followers_bef = profile.followers
        FOLLOWERS = [follower.username for follower in profile.get_followers()]
        if login:
            print(f"{GREEN}[✔] Login successful !")
            sleep(0.5)
        else:
            print(f"{RED}[✘] Failed to login.")
            sleep(0.7)
            print(f"{YELLOW}[1] Try with different combinations of usernames / passwords.")
            print(f"{YELLOW}[2] Exit")
            num=int(input(f"{YELLOW}[::] Number (from the above ones) >>> "))
            if num == 1:
                print(f"{YELLOW}[*] To quit the loop enter: <quit> in the username input.")
                sleep(0.9)
                while username != 'quit':
                    username=input(f"{YELLOW}[::] New username >>> ")
                    while checkUser(username):
                        print(f"{RED}[✘] Invalid username !")
                        sleep(0.5)
                        username=input(f"{YELLOW}[::] New username >>> ")
                    sleep(0.8)
                    password = input(f"{YELLOW}[::] New password >>> ")
                    login = client.login(username, password)
                    if login:
                        user = username
                        print(f"{GREEN}[✔] Login successful !")
                        username = '<quit>'
                        sleep(0.5)
                    else:
                        print(f"{RED}[✘] Failed to login.")
                        sleep(0.7)
                        print(f"{GREEN}[+] Retrying...")
                        sleep(0.5)
                username = user
            else:
                print(f"{RED}[+] Exiting...")
                sleep(0.6)
                print(f"{GREEN}[+] See you next time 👋")
                sleep(0.5)
                quit(0)
        sleep(1)
        print(f"{YELLOW}[+] Please wait while IGFI is increasing your followers...")
        sleep(1.7)
        print(f"{YELLOW}[+] To end the process enter <Ctrl> + <C>")
        sleep(1.3)
        clear()
        f = 0
        x = 0
        for i in range(10000):
            try:
                for j in range(len(NAMES)):
                    client.user_follow(users[NAMES[j]])
                    print(f"{YELLOW}[+] Following {NAMES[j]}...")
                    sleep(2)
                    f += 1
                    print(f"{GREEN}[✔] Ok")
                    sleep(0.5)
                for j in range(len(NAMES)):
                    client.user_unfollow(users[NAMES[j]])
                    print(f"{YELLOW}[-] Unfollowing {NAMES[j]}...")
                    sleep(1.5)
                    x += 1
                    sleep(0.5)
                    print(f"{GREEN}[✔] Ok")
                    sleep(1.5)
            except KeyboardInterrupt:
                res = f - x
                if res != 0:
                    suc = f / float(len(NAMES))
                    fail = res / float(len(NAMES))
                    tot = f + x
                    print(f"{GREEN}[✔] Successfully followed/unfollowed a total of {tot} users")
                    sleep(2)
                    print(f"{RED}[✘] Failed to unfollow {abs(res)} users !")
                    sleep(1)
                    print(f"{GREEN}[+] Percentage of success >>> {suc}%")
                    sleep(1)
                    print(f"{RED}[+] Percentage of failure >>> {fail}%")
                    if ga:
                        followers_af = profile.followers
                        if followers_bef - followers_af != 0:
                            followers_af = profile.followers
                            print(f"{GREEN}[✔] Successfully added >>> {followers_af - followers_bef} followers.")
                            sleep(1)
                    if check:
                        print(f"{RED}[✘] WARNING: The data provided may be incorrect if your account is private and you haven't approved the follow requests")
                        sleep(1.5)
                        ADDS = [follower.username for follower in profile.get_followers()]
                        if ADDS == FOLLOWERS:
                            print(f"{RED}[✘] No new followers added ! If your account is private try checking the pending follow requests.")
                        else:
                            print(f"{GREEN}[✔] Found >>> {len(ADDS) - len(FOLLOWERS)} new followers.")
                            sleep(0.7)
                            for i, username in enumerate(ADDS):
                                print(f"{YELLOW}[+] User No{i+1} >>> {username}")
                        sleep(2)
                    print(f"{YELLOW}[*] Users which the script failed to unfollow:")
                    sleep(0.9)
                    print(f'{YELLOW}|---------------|USERS|---------------|')
                    for i in range(res-1, -1, -1):
                        print(f"{YELLOW}[->] User >>> {NAMES[i]}")
                else:
                    print(f"{GREEN}[+] Success >>> 100%")
                    sleep(0.9)
                    print(f"{RED}[+] Fail >>> {res}%")
                    sleep(0.9)
                if keep:
                    name = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'files/log.txt')
                    with open(name, 'w', encoding='utf-8') as f:
                        if res != 0:
                            f.write(f'[✔] Successfully followed/unfollowed a total of {tot} users\n')
                            f.write(f'[✘] Failed to unfollow {abs(res)} users !\n')
                            f.write(f'[+] Percentage of success >>> {suc}%\n')
                            f.write(f'[+] Percentage of failure >>> {fail}%\n')
                            if ga:
                                followers_af = profile.followers
                                if followers_bef - followers_af != 0:
                                    followers_af = profile.followers
                                    f.write(f'[✔] Successfully added >>> {followers_af - followers_bef} followers.\n')
                            if check:
                                ADDS = [follower.username for follower in profile.get_followers()]
                                if ADDS != FOLLOWERS:
                                    print(f"{GREEN}[✔] Found >>> {len(ADDS) - len(FOLLOWERS)} new followers.")
                                    sleep(0.7)
                                    for i, username in enumerate(ADDS):
                                        f.write(f"[+] User No{i+1} >>> {username}\n")
                        else:
                            f.write('[+] Percentage of success >>> 100%\n')
                            f.write(f'[+] Percentage of failure >>> {res}%')
                    print(f"{GREEN}[✔] Successfully saved log !")
                    sleep(2)
                    print(f"{GREEN}[↪] File name >>> log.txt")
                    print(f"{GREEN}[↪] Path >>> {name}")
                    print(f"{GREEN}[↪] File size >>> {os.stat(name).st_size} bytes")
                print("\n")
        res = f - x
        if res != 0:
            suc = round(f / float(len(NAMES)))
            fail = round(res / float(len(NAMES)))
            tot = f + x
            print(f"{GREEN}[✔] Successfully followed/unfollowed a total of {tot} users")
            sleep(2)
            print(f"{RED}[✘] Failed to unfollow {abs(res)} users !")
            sleep(2)
            print(f"{GREEN}[+] Percentage of success >>> {suc}%")
            sleep(1)
            print(f"{RED}[+] Percentage of failure >>> {fail}%")
            sleep(1)
            if ga:
                followers_af = profile.followers
                if followers_bef - followers_af != 0:
                    followers_af = profile.followers
                    print(f"{GREEN}[✔] Successfully added >>> {followers_af - followers_bef} followers.")
                    sleep(1)
            if check:
                print(f"{RED}[✘] WARNING: The data provided may be incorrect if your account is private and you haven't approved the follow requests.")
                sleep(1.5)
                ADDS = [follower.username for follower in profile.get_followers()]
                if ADDS == FOLLOWERS:
                    print(f"{RED}[✘] No new followers added ! Try checking the pending follow requests and try again.")
                else:
                    print(f"{GREEN}[✔] Found >>> {len(ADDS) - len(FOLLOWERS)} new followers.")
                    sleep(0.7)
                    for i, username in enumerate(ADDS):
                        print(f"{YELLOW}[+] User No{i+1} >>> {username}")
                sleep(1.5)
            print(f"{YELLOW}[*] Users script failed to unfollow:")
            sleep(0.8)
            print(f'{YELLOW}|---------------|USERS|---------------|\n')
            for i in range(res,-1,-1):
                print(f"{YELLOW}[+] User >>> {NAMES[i]}")
            sleep(2)
        else:
            print(f"{YELLOW}[+] Success >>> 100%")
            sleep(1)
            print(f"{YELLOW}[+] Fail >>> {res}%")
            sleep(2)
        if keep:
            name = './files/log.txt'
            with open(name, 'w', encoding='utf-8') as f:
                if res != 0:
                    f.write(f'[✔] Successfully followed/unfollowed a total of {tot} users\n')
                    f.write(f'[✘] Failed to unfollow {abs(res)} users !\n')
                    f.write(f'[+] Percentage of success >>> {suc}%\n')
                    f.write(f'[+] Percentage of failure >>> {fail}%\n')
                    if ga:
                        followers_af = profile.followers
                        if followers_bef - followers_af != 0:
                            followers_af = profile.followers
                            f.write(f'[✔] Successfully added >>> {followers_af - followers_bef} followers.\n')
                    if check:
                        ADDS = [follower.username for follower in profile.get_followers()]
                        if ADDS != FOLLOWERS:
                            print(f"{GREEN}[✔] Found >>> {len(ADDS) - len(FOLLOWERS)} new followers.")
                            sleep(0.7)
                            for i, username in enumerate(ADDS):
                                f.write(f"[+] User No{i+1} >>> {username}\n")
                else:
                    f.write('[+] Percentage of success >>> 100%\n')
                    f.write(f'[+] Percentage of failure >>> {res}%')
            sleep(0.6)
            print(f"{GREEN}[✔] Successfully saved log !")
            sleep(1)
            print(f"{GREEN}[↪] File name >>> log.txt")
            sleep(0.5)
            print(f"{GREEN}[↪] Location >>> {name}")
            sleep(0.5)
            print(f"{GREEN}[↪] File size >>> {os.stat(name).st_size} bytes")
    
        quit(0)

if __name__ == '__main__':
    sleep(2)
    clear()
    parser = argparse.ArgumentParser(description='IGFI is the best tool for increasing followers on Instagram.')
    parser.add_argument('-u', '--username', help='The username to increase their followers.')
    parser.add_argument('-p', '--password', help='The password of your instagram account.')
    parser.add_argument('--session', help='The session file to use. To generate it >>> python3 cookies.py')
    args = parser.parse_args()
    if len(sys.argv) < 4:
        if not os.environ.get('DOCKER_CONTAINER'):
            print(f"{RED}[✘] Error: Missing arguments.")
            sleep(0.7)
            print(f"{GREEN}[+] Usage >>> python3 igfi.py -u <username> -p <password> --session <path_to_session_file>")
            sleep(1.5)
            args.username=input(f"{YELLOW}[::] Please enter your username >>> ") if not args.username else args.username
            args.password=input(f"{YELLOW}[::] Please enter your password >>> ") if not args.password else args.password
            args.session=input(f"{YELLOW}[::] Please enter the path to the session file (if created else hit <Enter>) >>> ") if not args.session else args.session
        else:
            args.username = os.environ.get('USERNAME', args.username)
            args.password = os.environ.get('PASSWORD', args.password)
            args.session = os.environ.get('SESSION', args.session)
    main(username=args.username.strip().lower(), password=args.password.strip(), session=args.session.strip().replace('\\', '/'))
