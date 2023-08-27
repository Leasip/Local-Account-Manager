from sys import stderr
from getpass import getpass
import json

class accountManager():
    try:
        open(r"Accounts.txt", "x").close()
    except FileExistsError:
        pass

    try:
        with open(r"Accounts.txt", "r") as file:
            accounts = dict(json.load(file))
    except json.decoder.JSONDecodeError:
        accounts = {}
        
    def dumpJSON(self, data):
        with open(r"Accounts.txt", "w") as file:
            json.dump(data, file, sort_keys=True, indent=4)

    def docslist(self, docs):
        for doc in range(len(docs)):
            print(docs[doc])
            
    def addAccount(self):
        self.platform = input("Please provide a platform. ").lower()

        # Uncomment these lines if you want to disallow multiple accounts for one platform
        
        #if self.platform in self.accounts:
        #    print("An account already exists for this platform.", file=stderr)
        #    return
        
        self.username = input("Please provide a username or email address. ").lower()
        self.password = getpass("Please provide a password. ")
        try:
            self.accounts[self.platform][self.username] = self.password
        except KeyError:
            self.accounts[self.platform] = {self.username: self.password}

        self.dumpJSON(self.accounts)
        print("New account for", self.platform, "successfully added.")
        
    def getAccount(self):
        if self.accounts.keys():
            print("Please select an account to retrieve. Available accounts are shown below.")
            for acc in range(len(self.accounts.keys())):
                print(list(self.accounts.keys())[acc])
            self.platform = input().lower()
            try:
                if self.accounts[self.platform]:
                    pass
                print("Please enter the username or email address of the account for \"" + self.platform + "\". Available usernames are shown below.")
                for usr in range(len(self.accounts[self.platform].keys())):
                    print(list(self.accounts[self.platform].keys())[usr])
                username = input().lower()
                try:
                    password = self.accounts[self.platform][username]
                    print("Your username for \"" + self.platform + "\" is \"" + username + "\", and your password is \"" + password + "\"")
                except:
                    print("That username doesn't have a password associated with it.", file=stderr)
            except:
                print("That platform doesn't have an account associated with it.", file=stderr)
        else:
            print("There are no accounts in the system.", file=stderr)

    def delAccount(self):
        if self.accounts.keys():
            print("Please select an account to delete. Available accounts are shown below.")
            for acc in range(len(self.accounts.keys())):
                print(list(self.accounts.keys())[acc])
            self.platform = input().lower()            
            try:
                if self.accounts[self.platform]:
                    pass
                print("Please enter the username or email address of the account for \"" + self.platform + "\". Available usernames are shown below.")
                for usr in range(len(self.accounts[self.platform].keys())):
                    print(list(self.accounts[self.platform].keys())[usr])
                username = input().lower()
                try:
                    indexOfKey = [idx for idx, key in enumerate(list(self.accounts[self.platform].items())) if key[0] == username][0]
                    password = self.accounts[self.platform][username]
                    if password == self.accounts[self.platform][username]:
                        self.accounts[self.platform].pop(list(self.accounts[self.platform])[indexOfKey])
                        self.dumpJSON(self.accounts)
                        print("Account for", self.platform, "deleted.", file=stderr)
                    else:
                        print("Invalid password. Deletion aborted.", file=stderr)
                except:
                    print("That username doesn't have a password associated with it.", file=stderr)
            except KeyError:
                print("That platform doesn't have an account associated with it.", file=stderr)
        else:
            print("There are no accounts in the system.", file=stderr)



mgr = accountManager()
typeHelp = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Type \"?\" for a list of commands.", "", "Do NOT put your actual login details here! This is, like, the most insecure thing ever because I could just come on here and look at the text file."]
mgr.docslist(typeHelp)
ask = None
while True:
    print()
    ask = input("What do you want to do? ").lower()
    print()
    if ask == "":
        pass
    elif ask == "help" or ask == "?" or ask == "h":
        mgr.docslist(["Display this help menu: help, h, ?", "Add an account to the file: a, add, +, mkfile, touch", "Get a specific account from the file: r, retrieve, g, get", "Remove an account from the file: del, rm, delete, -, remove, d, x", "Read the file with all the accounts: read, r, cat", "Wipe the file clean of all accounts: wipe, rm -rf /, deltree, format", "Exit the account manager: exit, quit, abort, close, esc, q", "Clear the screen: clr, cls, clear", "Display the credits: credits"])
    elif ask == "credits":
        mgr.docslist(["Developer: Leo Assiep", "Information sources: StackOverflow, w3schools, Geeks4Geeks"])
    elif ask == "clr" or ask == "cls" or ask == "clear":
        mgr.docslist(typeHelp)
    elif ask == "add" or ask == "+" or ask == "a" or ask == "touch" or ask == "mkfile":
        mgr.addAccount()
    elif ask == "get" or ask == "g" or ask == "retrieve":
        mgr.getAccount()
    elif ask == "del" or ask == "delete" or ask == "x" or ask == "d" or ask == "-" or ask == "rm" or ask == "remove":
        mgr.delAccount()
    elif ask == "read" or ask == "r" or ask == "cat":
        with open(r"Accounts.txt", "r") as file:
            print("json:")
            print(file.read())
            print()
            print("dict:")
            print(mgr.accounts)
    elif ask == "deltree" or ask == "wipe" or ask == "rm -rf /" or ask == "format":
        if mgr.accounts.keys():
            ask = input("Are you sure you want to clear all accounts? [y/n] ").lower()
            if ask == "y":
                  open(r"Accounts.txt", "w").close()
                  print("File wiped.", file=stderr)
                  mgr.accounts = {}
            else:
                print("Aborted")
        else:
            print("The file has already been wiped.", file=stderr)
    elif ask == "exit" or ask == "quit" or ask == "abort" or ask == "close" or ask == "q" or ask == "esc":
        with open(r"Accounts.txt", "w") as file:
            json.dump(mgr.accounts, file, sort_keys=True, indent=4)
        break
    else:
        print("Input not understood. Please try again.", file=stderr)