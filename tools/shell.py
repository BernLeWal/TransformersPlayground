#!/bin/python
"""
Utility class to provide a simple interactive shell for the samples
"""
import sys

class SimpleShell:
    def __init__(self, title) -> None:
        self.prompt = "$ "
        self.preprompt = ""
        self.postprompt = ""
        self.shorthelpdisplayed = False
        print("=====", title, "=====")

    def nextLine(self):
        if not self.shorthelpdisplayed:
            print()
            print("Enter prompt here; special commands start with \\; enter \\h for help, \\q to quit.")
            self.shorthelpdisplayed = True

        while True:
            s = input(self.prompt)
            if s.startswith('\\'):
                parts = s.split(' ')
                if parts[0] == "\\q":
                    sys.exit(0)
                if parts[0] == "\\h":
                    print("""
                          Commands help: they start with \\
                          - \\h show help page
                          - \\q quit application
                          
                          """)
            else:
                return s
    
    def print(self, text):
        print(text)