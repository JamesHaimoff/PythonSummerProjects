class bankmachine:
    def __init__(self,name):
        self.name = name
    def newbalance(self,balance):
        self.balance = balance
    def showbalance(self):
        print("%s, your current balance is: %d" % (self.name,self.balance))
    def deposit(self,amount):
        self.balance += amount
        print("Your deposit of %d was successful" % amount)
        print("%s, your new balance is: %d" % (self.name,self.balance))
    def withdrawl(self,amount):
        self.balance -= amount
        print("Your withdrawl of %d was successful" % amount)
        print("%s, your new balance is: %d" % (self.name,self.balance))


def main():
    print("ATM MACHINE")
    name = input("What is your name: ")
    displayname = name
    name = bankmachine(name)
    #setting up each new account with 10000
    name.newbalance(10000)

    while True:
        print("Please select an option %s: " % displayname)
        print("Option 1 - Show Balance")
        print("Option 2 - Deposit")
        print("Option 3 - WithDrawl")
        print("Option 4 - Logout")
        option = int(input("Print Selection Here: "))
        if option == 1:
            print("Option 1 - Show Balance ||||||||||||||||||||||||||||||||||||||||||")
            name.showbalance()
        if option == 2:
            print("Option 2 - Deposit ||||||||||||||||||||||||||||||||||||||||||")
            amount = int(input("Select the amount you would like to deposit: "))
            name.deposit(amount)
        if option == 3:
            print("Option 3 - WithDrawl ||||||||||||||||||||||||||||||||||||||||||")
            amount = int(input("Please select the amount you would like to withdrawl: "))
            name.withdrawl(amount)
            name.showbalance()
        if option == 4:
            print("Exiting the Program...")
            break

if __name__ == "__main__":
    main()