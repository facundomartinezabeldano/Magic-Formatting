import os
import platform
import sys
import asyncio
from InquirerPy import inquirer

if platform.system() == 'Windows':
   asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

def main():
    print("\n \n Welcome to magical formatting \n \n")
    filenames = os.listdir()
    filenames.remove('magic_formatting.py')
    l = [
        "format with numbers and spaces",
        "format with numbers and underscores",
        "format with numbers and middle-scores",
        "replace middle scores with underscores",
        "replace underscores with middle-scores",
        "print_files",
        "exit"
    ]

    choices = inquirer.fuzzy(message="Select an action to perfom", choices=l).execute()

    menu = {
        "format with numbers and spaces":format_with_numbers_and_spaces,
        "format with numbers and underscores": format_with_numbers_and_underscores,
        "format with numbers and middle-scores": format_with_numbers_and_middle_scores,
        "replace middle scores with underscores": replace_middle_scores_with_underscores,
        "replace underscores with middle-scores": replace_underscores_with_middle_scores,
        "print_files": print_files,
        "exit": exit_screen
    }
    menu[choices](filenames)
    
    return

def format_with_numbers_and_spaces(l,extension_lenght = 4):
    '''
    Changes the name of all the files with a single name given by the user, using numbers and spaces for separators
    ie: "This is an example 1"
    '''
    name = inquirer.text("Select file name: ").execute()
    if(inquirer.confirm(message=" ATENTION ! Do you want to specify a file extension lenght? ie. lenght of a .jpg file = 4 this includes the . , it's 4 by default").execute()):
        extension_lenght = inquirer.number(message="Select a file extension length: ",float_allowed=False).execute()
    for index , file in enumerate(l):
        os.rename(file,f'{name} {index + 1} {file[-extension_lenght:]}')
    return

def format_with_numbers_and_underscores(l,extension_lenght = 4):
    '''
    Changes the name of all the files with a single name given by the user, using numbers and under scores for separators
    ie: "This_is_an_example_1"
    '''
    name = inquirer.text("Select file name: ").execute()
    name.replace(" ","_")
    if(inquirer.confirm(message=" ATENTION ! Do you want to specify a file extension lenght? ie. lenght of a .jpg file = 4 this includes the . , it's 4 by default").execute()):
        extension_lenght = inquirer.number(message="Select a file extension length: ",float_allowed=False).execute()
    for index , file in enumerate(l):
        os.rename(file,f'{name}_{index + 1}_{file[-extension_lenght:]}')
    return

def format_with_numbers_and_middle_scores(l,extension_lenght = 4):
    '''
    Changes the name of all the files with a single name given by the user, using numbers and middle scores for separators
    ie: "This-is-an-example-1"
    '''
    name = inquirer.text("Select file name: ").execute()
    name.replace(" ","-")
    if(inquirer.confirm(message=" ATENTION ! Do you want to specify a file extension lenght? ie. lenght of a .jpg file = 4 this includes the . , it's 4 by default").execute()):
        extension_lenght = inquirer.number(message="Select a file extension length: ",float_allowed=False).execute()
    for index , file in enumerate(l):
        os.rename(file,f'{name}-{index + 1}-{file[-extension_lenght:]}')
    return

def replace_middle_scores_with_underscores(l):
    '''
    Changes all the middlescores in every file name to "_"
    '''
    for file in l:
        new_name = file.replace("-","_")
        os.rename(file,new_name)
    return

def replace_underscores_with_middle_scores(l):
    for file in l:
        new_name = file.replace("_","-")
        os.rename(file,new_name)
    return

def exit_screen(dummy_argument):
    print("Goodbye")
    return sys.exit()


def print_files(dummy_argument):
    '''
    Prints the name of all the files in the current working directory exept from this file itself
    '''
    filenames = os.listdir()
    filenames.remove('magical_formatting.py')

    print(f' >>> Your path is: {os.getcwd()} \n >>> Your file names are: \n')
    for f in filenames:
            print(f)

    if(inquirer.confirm(message="Exit ?").execute()):
        exit_screen("dummy")
    return

while True:
    main()