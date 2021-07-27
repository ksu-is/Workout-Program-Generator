from ExcerciseLibrary import *



question = input("What is your goal for today's workout? (Build Muscle, Gain Strength, or Lose Weight)\n ")

if question == "Build Muscle".lower():
    
    muscle_group = input("What muscle group would you like to worjout today? (Chest, biceps, back, legs, or shoulders)")
    if muscle_group == "chest".lower():
        print("Here is the workout you will do today")
        print()
        print(chest.barbell, "10-12 reps")
        print(chest.dumbell, "10-12 reps" )
        print(chest.calisthenics, "10-12 reps")
    elif muscle_group == "biceps".lower():
        print("Here is the workout you will do today")
        print()
        print(biceps.barbell, "10-12 reps")
        print(biceps.dumbell, "10-12 reps")
        print(biceps.calisthenics, "10-12 reps")
    elif muscle_group == "back".lower():
        print("Here is the workout you will do today")
        print()
        print(back.barbell, "10-12 reps")
        print(back.dumbell, "10-12 reps")
        print(back.calisthenics, "10-12 reps")
    elif muscle_group == "legs".lower():
        print("Here is the workout you will do today")
        print()
        print(legs.barbell, "10-12 reps")
        print(legs.dumbell, "10-12 reps")
        print(legs.calisthenics, "10-12 reps")
    elif muscle_group == "shoulders".lower():
        print("Here is the workout you will do today")
        print()
        print(shoulders.barbell, "10-12 reps")
        print(shoulders.dumbell, "10-12 reps")
        print(shoulders.calisthenics, "10-12 reps")
