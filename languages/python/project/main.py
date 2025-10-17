########################################################################################################################################
#! Settings
import random

##! Character Settings
character_name=("")
character_family_name=("")
character_gender=("")
character_age=()
character_age_title=("")
character_race=("")
character_class=("")

##! Character Skills
character_skills = {"strenght": random.randint(1,5),
                   "agility": random.randint(1,5),
                   "luck": random.randint(1,5),
                   "charisma": random.randint(1,5),
                   "health": random.randint(1,5)}

########################################################################################################################################
#! Introduction
print ("Welcome dear adventurer!")
character_name=input("What is thy name adventurer?\n")
character_family_name=input(f"Ah the mighty {character_name}, what a fitting name for a main character!\nFrom which family do you hail?\n")
character_gender=input(f"So its {character_name} {character_family_name} and you are obviously a...(male/female)\n").lower()

if character_gender == ("male"):
    character_gender = "Sir" 
    character_skills["strenght"] += random.randint(0,3)
    character_skills["health"] += random.randint(0,3)
elif character_gender == "female":
    character_gender = "Lady"
    character_skills["charisma"] += random.randint(0,3)
    character_skills["agility"] += random.randint(0,3)

character_age=int(input(f"Ah yes ofcourse, obviously you are {character_gender} {character_name} {character_family_name}!\nAnd how many winters have you experienced? "))
if character_age <= 20:
    character_age_title = ("Young")
    character_skills["agility"] += random.randint(0,4)
    character_skills["health"] += random.randint(0,4)
    print ("You are a young one! Shouldn't you be assisted by a squire?")

elif 20 < character_age <= 50:
    character_age_title = ("Vibrant")
    character_skills["strenght"] += random.randint(0,4)
    character_skills["health"] += random.randint(0,4)
    print ("You are at the peak of your life! Dont you have anything else to do right now?")

elif character_age > 50:
    character_age_title = ("Elder")
    character_skills["luck"] += random.randint(0,4)
    character_skills["charisma"] += random.randint(0,4)
    print (f"My oh my you are one lucky {character_gender} to have survived this long!")

print("You find yourself in the land of the mighty king Atlest in the kingdom of Rurin, surrounded by enemie kingdoms and decieving allies")
character_race=(input("The land of Rurin has many inhabitants, mixed with many races. What is thy race? Are you a mighty Orc? Or a stout Dwarf, maybe you are a Human or an agile Elf....or maybe a shallow gnome")).lower()

if character_race == ("orc"):
    character_skills["strenght"] += random.randint(0,4)
    character_skills["health"] += random.randint(0,4)
    print ("Youa are a mighty orc, direct descendet of the mighty god of strenght and vigor")

elif character_race == ("dwarf"):
    character_skills["luck"] += random.randint(0,4)
    character_skills["strenght"] += random.randint(0,4)
    print ("You are a hard working dwarf, said to be picked out of rock by the dragon god")
    
elif character_race == ("human"):
    character_skills["health"] += random.randint(0,4)
    character_skills["charisma"] += random.randint(0,4)
    print ("You are the most common race in these lands, known as the youngest child of the god of wealth and justice")
    
elif character_race == ("Elf"):
    character_skills["luck"] += random.randint(0,4)
    character_skills["agility"] += random.randint(0,4)
    print ("You are the oldest child of Life and the forgotten child of death")
    
elif character_race == ("Gnome"):
    character_skills["health"] += random.randint(0,4)
    character_skills["agility"] += random.randint(0,4)
    print ("Your origgins")

    

