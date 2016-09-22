import logging
import cmd
import os
import itertools

def main():
    askUser()


def askUser():
    #ask for the path of the file
    pathFile =input("Input your file's path :")
    while(os.path.exists(pathFile) ==False):
        print("wrong input")
        pathFile = input("Input your file's path :")
    print('valid path')
    #ask for the path of the logs's file
    pathLogFile = input("Input your LOG file's path :")
    while (os.path.exists(pathLogFile) == False):
        print("wrong input")
        pathLogFile = input("Input your LOG file's path :")
    print('valid path')
    #ask for the deph of exploration
    wrongInput = True
    while (wrongInput):
        try:
            depthExploration = int(input("Input the depth of exploration :"))
            wrongInput = False
        except ValueError:
            wrongInput = True
        if (depthExploration <= 0):
            wrongInput = True
        if (wrongInput):
            print("wrong input")
    print('valid number')
    # ask for the deph of exploration
    wrongInput = True
    while(wrongInput):
        try:
            frequency = int(input("Input the frequency of verification :"))
            wrongInput = False
        except ValueError:
            wrongInput = True
        if (frequency <= 0):
            wrongInput = True
        if (wrongInput):
            print("wrong input")
    print('valid number')

def yolo():
    wrongInput =True

main()