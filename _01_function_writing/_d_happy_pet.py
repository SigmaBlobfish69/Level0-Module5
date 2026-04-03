"""
Write methods to represent the activities that will make the user's pet happy.
"""
from tkinter import messagebox, simpledialog, Tk
root = Tk()
root.withdraw()

global happiness_level
happiness_level = 50

def walkPet(pet):
    global happiness_level
    if pet in ["dog", "cat", "guinea pig", "horse", "donkey"]:
        messagebox.showinfo(title="user", message=f"Your {pet} is very happy about taking a walk!")
        happiness_level += 20
    if pet == "fish":
        messagebox.showinfo(title="user", message=f"Your {pet} is not happy about taking a walk!")
        happiness_level -= 20
def feedPet(pet):
    global happiness_level
    messagebox.showinfo(title="user", message=f"Your {pet} is very happy about getting fed!")
    happiness_level += 20
def killPet(pet):
    global happiness_level
    method = simpledialog.askstring(title="user", prompt=f"What method to kill your {pet}? Nuke, pistol, or knife?")
    if method == "nuke":
        messagebox.showinfo(title="user", message=f"Your {pet} has been disintegrated into nothing but ash! Also your house has been blown to bits and you died, too. BAD CHOICE, BUDDY!")
    if method == "pistol":
        messagebox.showinfo(title="user", message=f"The impact of the bullet from your pistol was so forceful that if blew off your {pet}'s head!")
    if method == "knife":
        messagebox.showinfo(title="user", message=f"You have slit your dog's throat, and now it is gurgling on the floor like a pathetic weakling!")
    happiness_level -=100
if __name__== '__main__' :
    # TODO)
    #   1. Ask the user to enter the type of pet they want (give them a few
    #      choices).
    pet = simpledialog.askstring(title="user", prompt="What pet do you want? Dog, cat, fish, guinea pig, horse, donkey?")

    while True:
        activity = simpledialog.askstring(title="user", prompt=f"What activity would you like your {pet} to do? Currently your pet is {happiness_level}/100")
        if activity == None or activity == '':
            exit()
        if activity == "walk":
            walkPet(pet)

        if activity == "feed":
            feedPet(pet)

        if activity == "kill":
            killPet(pet)


    #   2. Use a loop (maybe a while loop?) to keep offering interactions with
    #      their pet until the desired pet happiness level has been reached.
    #      Examples of activities are: Feed, Walk, Play
    #   3. Write a method for each of the pet activities offered.
    #      Each activity should increase (or decrease) the pet's happiness
    #      level by a different amount, depending on the kind of pet they
    #      have. For example, a fish might not enjoy a walk!
        if happiness_level >= 100:
            messagebox.showinfo(title="user", message=f"Your {pet} has reached the max happiness level! Good job!")
            exit()
        if happiness_level <= 0:
            messagebox.showinfo(title="user", message=f"Your {pet} is dead because you did not make it happy (also because you killed it). Go jump off a cliff, loser.")
            exit()
