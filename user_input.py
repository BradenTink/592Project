import pandas as pd
import os
import random


def welcome_user():
    """
        Prints welcoming message to the terminal.

        No parameters and return value.
    """
    bongo_cat = """
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⡷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠋⠈⠻⣮⣳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣾⡿⠋⠀⠀⠀⠀⠙⣿⣿⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣿⡿⠟⠛⠉⠀⠀⠀⠀⠀⠀⠀⠈⠛⠛⠿⠿⣿⣷⣶⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣾⡿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠻⠿⣿⣶⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⣀⣠⣤⣤⣀⡀⠀⠀⣀⣴⣿⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠿⣿⣷⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣄⠀⠀
    ⢀⣤⣾⡿⠟⠛⠛⢿⣿⣶⣾⣿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠿⣿⣷⣦⣀⣀⣤⣶⣿⡿⠿⢿⣿⡀⠀
    ⣿⣿⠏⠀⢰⡆⠀⠀⠉⢿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⢿⡿⠟⠋⠁⠀⠀⢸⣿⠇⠀
    ⣿⡟⠀⣀⠈⣀⡀⠒⠃⠀⠙⣿⡆⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠇⠀
    ⣿⡇⠀⠛⢠⡋⢙⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀
    ⣿⣧⠀⠀⠀⠓⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠛⠋⠀⠀⢸⣧⣤⣤⣶⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⡿⠀⠀
    ⣿⣿⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠻⣷⣶⣶⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⠁⠀⠀
    ⠈⠛⠻⠿⢿⣿⣷⣶⣦⣤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⡏⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠻⠿⢿⣿⣷⣶⣦⣤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⡄⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠛⠻⠿⢿⣿⣷⣶⣦⣤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⡄⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠛⠛⠿⠿⣿⣷⣶⣶⣤⣤⣀⡀⠀⠀⠀⢀⣴⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⡿⣄
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠛⠛⠿⠿⣿⣷⣶⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣹
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠀⠀⠀⠀⠀⠀⢸⣧
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣆⠀⠀⠀⠀⠀⠀⢀⣀⣠⣤⣶⣾⣿⣿⣿⣿⣤⣄⣀⡀⠀⠀⠀⣿
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⢿⣻⣷⣶⣾⣿⣿⡿⢯⣛⣛⡋⠁⠀⠀⠉⠙⠛⠛⠿⣿⣿⡷⣶⣿
    """
    print(bongo_cat)
    print("\nWelcome new user!\n\nPlease wait while the dataset loads ☕ ☕ ☕\n")


def goodbye_user():
    """
        Prints goodbye message to the terminal.

        No parameters and return value.
    """
    bongo_cat_goodbye = """
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣶⠶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⣻⣿⢿⡆⠹⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠏⢰⣏⣥⡼⠃⠀⢹⡦⢤⣤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣄⣀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⠀⠀⠀⢀⣠⠶⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠓⠦⣤⣤⠶⠚⢋⣹⡄⠘⣧⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⢀⣼⣿⡟⢿⠈⣉⣻⣦⣤⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡶⠛⠁⠻⡆⢹⡀⠀⠀⠀⠀⠀
    ⣄⡀⠀⠀⣾⣿⢿⣽⠟⠲⡿⠼⠇⠙⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣦⡀⠀⣷⠘⡇⠀⠀⠀⠀⠀
    ⠈⠙⠳⣦⣿⡷⠚⠛⠒⠛⠃⠀⠀⠀⠀⠀⠀⠀⣠⣴⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠶⠿⠀⣿⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠉⠙⠶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠶⣄⣀⠀⠀⠀⠀⠀⠀⠈⠙⠓⢶⣤⡄⠀⠀⠀⢀⣠⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⠟⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠳⢦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠳⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠶⢤⣀⠀⣤⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠂⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠁⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡏⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠴⠛⠳⢦⣄⡀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣄⡀⠀⠀⠀⠀⣀⣠⠔⠊⠁⠀⠀⠀⠀⠈⠙⠳⢦
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠒⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """
    print("\n")
    print(bongo_cat_goodbye)
    print("\nSee you next time!")


def successful_entry():
    """
        Prints successful message to the terminal.

        No parameters and return value.
    """
    bongo_cat_drums = """
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡤⠾⠋⠀⠙⢦⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⣀⣀⡀⠀⣠⡶⠋⠁⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠶⣤⣀⠀⠀⠀⠀⡄⠀⠀⠀
    ⠀⠀⠀⣼⠟⣯⡙⣿⡭⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⡶⠞⠋⣿⠀⠀⠀
    ⡀⠀⠀⣿⠉⠻⠀⠈⠀⠀⠀⢾⠆⢀⡀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⠀⠀⠀
    ⠉⠓⠒⢻⣦⣤⣀⣀⠀⠀⠀⠀⠀⠀⠉⠛⠃⠀⠀⢠⣦⡀⠀⠀⠀⠀⠀⠀⣼⠁⠀⠀⠀
    ⠀⣠⠚⠉⠁⠀⠀⠉⠉⠻⢗⠲⠦⢤⣄⣀⡀⠀⠀⠈⠉⠀⠀⠀⠀⠀⠀⠀⠘⣷⠀⠀⠀
    ⠀⣧⡀⠀⠀⠀⠀⠀⠀⠀⣸⣧⠶⠒⠚⠛⠛⣻⠂⠀⠀⠀⠀⣀⣀⠀⠀⠀⠀⠸⡇⠀⠀
    ⠀⢻⣝⠓⠦⠤⢤⢤⠶⣚⣿⡇⠀⠀⠀⢀⡼⢛⡷⡖⠒⠒⠛⢅⠈⠉⠙⠒⠲⠤⢧⣄⣀
    ⠀⠈⣏⠹⡟⠒⢲⠚⠋⡟⢹⣧⡀⠀⠀⠀⠀⠊⠀⠇⠀⠀⠀⠈⡇⠀⠀⠀⠀⠀⠀⠀⠉
    ⠀⠀⢸⡄⡇⠀⢸⠀⢠⡇⠘⣷⡙⠢⣄⣀⠀⠀⠀⠀⠀⢀⣠⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⢳⣼⣀⣸⣇⣸⡦⣤⡇⡏⠓⠦⣬⣍⣙⣛⣛⡯⣽⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠈⠙⠛⠛⠁⠀⠈⣿⡇⠀⠀⡟⠀⠀⢀⡏⢠⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢷⣤⣰⠁⠀⢀⣞⣠⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠛⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """

    print(bongo_cat_drums)
    print("\nThank you for entering valid inputs. You can now review your statistics.\n")


def angry_cat():
    """
        Prints message to let the user that they have not been entering valid entries.

        No parameters and return value.
    """
    angry_cat = """
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠲⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⣀⣠⣤⣄⣀⣠⠔⠚⠉⠀⠀⠙⠒⠤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⢀⣌⠡⠀⣀⠀⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠲⢤⣀⡤⢴⡀⠀
    ⣀⣀⡠⡖⠁⠀⠀⠀⠀⡸⠁⠀⢰⡆⣀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠁⠀
    ⢀⠊⠑⣦⢀⣀⡀⢔⣾⣀⡀⠀⠀⠀⠈⠉⠓⠂⠀⢠⣄⠀⠀⠀⢀⡀⠀⡎⠀⠀
    ⠻⠠⢀⠈⣶⠒⠒⠉⠀⠀⠈⠉⠑⠒⠲⠤⠤⣀⣀⠀⠀⣀⡤⠞⠁⠀⠀⠙⡄⠀
    ⢃⠀⠰⢃⣷⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡩⠋⠁⠀⢰⠀⠀⠀⡀⠸⡀
    ⢸⡀⢑⡒⢚⡿⠃⠀⠀⢀⠤⠶⠭⠦⠤⢐⣈⠉⠉⠑⣒⠆⠒⠁⠳⠤⣄⣠⠞⠓
    ⠀⠳⢧⣖⡾⠀⠀⠀⠀⢼⡒⠀⠀⠀⠀⠀⠀⠀⠀⠠⠤⢄⣠⣊⡤⠞⠉⠀⠀⠀
    ⠀⠀⠀⠀⢠⠀⠀⠀⠀⠀⠳⣄⣠⠤⠖⠒⠒⠒⠒⠒⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠜⠀⠀⠀⠀⠀⠀⠜⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """
    print(angry_cat)
    print("Only valid entries allowed.\n")


def explain_values(data_to_explain, genre, user_song="", suggested_song=""):
    """
        Explains what the graphs mean for the user.
        
        Parameters
        =======================
        data_to_explain (str) : description of topic to explain for conditional statements
        genre (str) : song genre
        user_song (str) : song name from user
        suggested_song (str) : suggested song name based on closeness of boringness value

        No return value
    """

    # default variables
    bar_graph_explanation = """
    Danceability: Describes how suitable a track is for dancing.

    Energy: Measure of intensity and activity. Typically, energetic tracks feel fast, loud, and noisy.

    Speechiness: The presence of spoken words in a song.

    Acousticness: Describes how acoustic a song is. 

    Instrumentalness: Amount of vocals in the song.

    Liveness: Describes the likelihood the song was recorded with a live audience. 

    Valence: Musical positiveness conveyed by a track.
    """

    explanation_cat = """
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠹⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⢀⡠⠖⠋⠁⠀⠀⠘⠲⠤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⢀⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠲⢤⡀⠀⢀⣠⡄⠀
    ⠀⠀⣠⠴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠉⠀⡇⠀
    ⢀⡴⠋⠀⠀⠀⠀⣀⣿⠂⣆⣠⡀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠃⠀
    ⣾⠀⠀⠀⠀⠀⡀⠀⠁⠀⠀⠈⠙⠁⠀⠀⣴⠄⠀⠀⠀⠀⠀⠀⣾⠀⠀
    ⠻⠦⠤⠴⠖⠋⠉⠓⠒⠶⠤⣄⣀⡀⠀⠐⠺⡂⠀⠀⠀⠀⠀⠀⠘⣆⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠓⡾⠁⠀⠀⠀⠀⢀⠀⠀⠹⡆
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠷⢤⣤⠤⠴⠚⠛⠒⠦⢤⣷
    """

    sad_cat ="""
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡶⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠋⠁⠀⠻⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠏⠀⠀⠀⠀⠘⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⠶⠞⠛⠋⠀⠀⠀⠀⠀⠀⠈⠛⠳⢶⣤⡀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⢠⣤⣤⣤⣤⣤⣀⡀⠀⢀⣠⡶⠟⠉⠀⠀⠀⢀⣀⣠⣤⣤⡶⠄⠀⡀⠀⠀⠀⠈⠻⣶⡀⠒⠒⢲⣿⡹⣷⣄⠀⠀⠀⢠⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⢸⡇⠀⠀⠈⠉⠉⠙⠓⠟⠁⠀⠀⣼⣿⣻⠀⡉⠉⠿⠛⠛⠛⢻⡀⠙⣦⡀⠀⠀⠀⠈⢿⡄⠀⣼⠃⠉⢻⣿⡘⠢⣄⠀⠈⢣⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠈⣷⡀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⡿⠇⣡⣶⣿⠛⠦⠶⠲⢦⣌⡛⢲⡋⠻⣄⠀⠀⠀⠘⣇⣼⠧⣀⣰⠟⠁⠙⢆⠈⠳⣄⠀⢹⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠘⣧⡀⠀⠀⠀⠀⢠⣴⣿⡿⠋⠀⣄⣻⣍⠻⠃⠀⠀⠀⢶⣄⣹⡄⠳⣤⠾⣦⠀⠀⢠⡿⢁⠀⣸⠟⢦⡀⠀⠈⢳⡀⠘⣆⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠘⣷⡄⠀⠀⠀⠀⢹⠊⢸⡆⠀⢧⢨⣿⠦⣀⣦⢤⣿⣿⠆⣩⣦⠀⠀⠳⣼⠀⣀⡾⠁⠉⣹⠟⢦⡀⠙⢦⣠⡾⠻⣦⠘⠀⠦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⣸⠏⠀⠀⠀⠀⠀⠘⡲⠞⢡⠀⠈⢿⡉⢙⡧⡿⠙⠛⠉⠘⠛⠁⠀⠀⠀⠘⠉⠉⢠⡤⣾⠟⠚⠛⢻⡋⠛⢻⡀⢀⣿⡄⠀⠀⠀⠙⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⣿⠀⠀⠀⠀⠀⠀⠘⢧⣀⣸⠀⠀⠀⠉⠛⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠁⠀⠀⢸⣶⠧⢴⣞⡛⠛⠉⠀⠀⠀⠀⠀⠈⠳⣄⣀⣠⣤⠀⠀⠀⠀⠀
    ⠀⠀⢻⣄⠀⠀⠀⠀⠀⠀⠀⡏⠁⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠳⣦⣀⠀⠀⠀⣠⣴⠶⠛⣏⣩⠟⠀⠀⠀⡄⠀
    ⠀⢀⣄⠻⢷⣄⡀⠀⠀⠀⠀⠙⣲⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢷⡼⠿⡍⠀⢦⣠⠞⣇⠈⢳⡀⠀⢸⡀
    ⠀⣟⢿⠛⠷⠾⠛⠓⠚⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⢒⣦⡖⠛⡿⠀⠀⠀⠀⢈⣀⣀⣹⣴⠟⣇⠀⠸⡄⠀⢳⠀⠀⠇
    ⠀⢿⣼⣆⣀⣀⢠⣄⣀⣀⣀⣀⣀⣞⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⠀⠉⣿⣁⠀⢠⡀⠀⠠⠖⠋⠉⢿⠛⢻⠶⣤⣷⠀⠸⠂⠀⠀
    ⠀⠈⠙⢻⡉⠉⠉⢿⠉⢿⡙⢯⡿⠁⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠴⣍⡀⠀⢀⡼⠁⠘⢦⡀⠹⣆⠀⠀⠀⠀⠈⠀⠀⠀⠀⢹⣻⡆⠀⠀⠀
    ⠀⡆⠀⠀⢳⡀⠀⠈⢧⡀⠻⣾⠓⠂⠀⠀⣠⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⠃⠠⠤⣝⣶⣋⡘⢦⡀⢀⣷⡾⠛⣟⠛⠛⠛⠛⠛⠛⠛⠉⢻⠉⠀⠀⠀⠀
    ⠀⢻⡀⠀⠀⠳⣄⠀⠀⠙⣶⣟⠉⠀⢀⣾⠛⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⢀⣤⠞⠋⠈⢯⠉⠛⠻⡿⠦⣽⣄⠘⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠹⣄⡀⠀⠙⢷⣶⡟⠋⠉⠀⣠⡟⠁⠀⠀⠙⠷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠇⠀⢀⣷⣀⣤⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠈⠙⠲⠀⠀⠉⠻⢿⡲⠚⠋⠀⠀⠀⠀⠀⠀⠈⠙⠳⢦⣤⣀⡀⠀⠀⠀⠀⠀⠀⢀⣈⣽⠿⠋⠉⠉⠉⠉⠉⠁⠀⠘⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠓⠦⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠛⠛⠛⠛⠛⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    
    """

    print(explanation_cat)

    if data_to_explain == "bar graph":
        print("\nFor the bar graphs, here is a brief explanation of what values on the x-axis mean:")
        print(bar_graph_explanation)
    elif data_to_explain == "histogram":
        print("\nA histogram shows the count of each taken measurement.\n")
    elif data_to_explain == "distributions":
        print("\nA distribution curve is similar to a histogram but with continuous values.\n")
    elif data_to_explain == "pie chart":
        print(f"\nThis pie chart shows the popularity of the genre, {genre.lower()}.\n")
    elif data_to_explain == "scatter":
        print(f"\nThe scatter plot curve shows the relation between the 'Total Beats' and 'Boringness' for the genre, {genre.lower()}.\n")
    elif data_to_explain == "pivot":
        print("\nOur pivot table takes shows the relation between the tempo and the duration of the song when compared to the entire dataset.\n")
    elif data_to_explain == "suggested song":
        print("People tend to listen to songs with the 'same vibe'.\n")
        os.system("pause")
        if suggested_song == "No song suggestion found.":
            print("We couldn't find a song similar to yours in the dataset. Sorry about that.\n")
            print(sad_cat)
        else:
            print(f"\nTry listening to the song '{suggested_song}' because you liked '{user_song}' from the genre, {genre}.\n")
    os.system("pause")


def get_genre_from_user(genre_list):
    """
        Asks the user for a song genre until a valid input is accepted.

        Raise : ValueError if the song genre is not found.
        
        Return (str) : song genre
    """
    entry_count = 0
    not_valid_input = True
    genre_list_lower = [genre.lower() for genre in genre_list]
    genres_concat = ", ".join(genre_list_lower)
    print(f"From the dataset, the following genres are available: {genres_concat}.\n")

    while(not_valid_input):
        #Ask for genre
        genre = input("Please enter a song genre (type q to quit): ").lower().strip()
        try: 
            if genre == "quit" or genre == "q":
                goodbye_user()
                exit()
            elif genre not in genre_list_lower:
                raise ValueError()
            not_valid_input = False
        except ValueError:  
            #Genre not found
            entry_count += 1
            if entry_count < 3:
                print("Invalid user input.\n")
            else:
                angry_cat()
    
    if genre == "rnb":
        genre = "RnB"
    else:
        genre = genre.title()

    return genre


def get_random_songs(song_list):
    """
        Prints a list of random songs in a list.

        Parameters
        =======================
        song_list (list[str]) : list of song names

        No return value.
    """
    random_songs = set([random.choice(song_list) for _ in range(30)])
    print("\nHere are a couple of song suggestions: \n")
    for song in random_songs:
        print(f"\t{song}")


def get_song_name_from_user(song_list, genre):
    """
        Ask a user for a song name until a valid input is accepted.

        Parameters:
        song_list (list[str]) : list of song names

        Raise: ValueError if the song name is not found
        
        Return (str) : song name
    """
    not_valid_input = True
    entry_count = 0
    

    while(not_valid_input):
        #Ask for song
        song_name = input("\nFrom the genre " + genre.lower() + ", enter a song that came out before 2020 (type q to quit): ")

        try:
            if song_name == "quit" or song_name == "q":
                goodbye_user()
                exit()      
            elif (song_name in song_list):
                print("\nYou entered the song: " + song_name + ".\n")
                successful_entry()
                os.system("pause")
                not_valid_input = False
            else:
                raise ValueError
        except ValueError:
            entry_count += 1
            if entry_count < 3:
                get_random_songs(song_list)
            else:
                angry_cat()
    
    song_name = song_name

    return song_name