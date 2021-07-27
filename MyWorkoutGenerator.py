from ExcerciseLibrary import *



question = input("What is your goal for today's workout? (Build Muscle, Gain Strength, or Lose Weight)\n ")

if question == "Gain Strength".lower():
    muscle_group1 = input("What muscle group would you like to workout today? (Chest, biceps, back, legs, or shoulders)")
    if muscle_group1 == "chest".lower():
        print()
        print("-->Here is the workout you will do today<--")
        print()
        print(chest.barbell, "4-8 reps")
        print(chest.dumbell, "4-8 reps" )
        print(chest.calisthenics, "4-8 reps")
        print()
    elif muscle_group1 == "biceps".lower():
        print()
        print("-->Here is the workout you will do today<--")
        print()
        print(biceps.barbell, "4-8 reps")
        print(biceps.dumbell, "4-8 reps")
        print(biceps.calisthenics, "4-8 reps")
        print()
    elif muscle_group1 == "back".lower():
        print()
        print("-->Here is the workout you will do today<--")
        print()
        print(back.barbell, "4-8 reps")
        print(back.dumbell, "4-8 reps")
        print(back.calisthenics, "4-8 reps")
        print()
    elif muscle_group1 == "legs".lower():
        print()
        print("-->Here is the workout you will do today<--")
        print()
        print(legs.barbell, "4-8 reps")
        print(legs.dumbell, "4-8 reps")
        print(legs.calisthenics, "4-8 reps")
        print()
    elif muscle_group1 == "shoulders".lower():
        print()
        print("-->Here is the workout you will do today<--")
        print()
        print(shoulders.barbell, "4-8 reps")
        print(shoulders.dumbell, "4-8 reps")
        print(shoulders.calisthenics, "4-8 reps")
        print()



elif question == "Build Muscle".lower():
    muscle_group = input("What muscle group would you like to workout today? (Chest, biceps, back, legs, or shoulders)")
    if muscle_group == "chest".lower():
        print()
        print("-->Here is the workout you will do today<--")
        print()
        print(chest.barbell, "10-12 reps")
        print(chest.dumbell, "10-12 reps" )
        print(chest.calisthenics, "10-12 reps")
        print()
    elif muscle_group == "biceps".lower():
        print()
        print("-->Here is the workout you will do today<--")
        print()
        print(biceps.barbell, "10-12 reps")
        print(biceps.dumbell, "10-12 reps")
        print(biceps.calisthenics, "10-12 reps")
        print()
    elif muscle_group == "back".lower():
        print()
        print("-->Here is the workout you will do today<--")
        print()
        print(back.barbell, "10-12 reps")
        print(back.dumbell, "10-12 reps")
        print(back.calisthenics, "10-12 reps")
        print()
    elif muscle_group == "legs".lower():
        print()
        print("-->Here is the workout you will do today<--")
        print()
        print(legs.barbell, "10-12 reps")
        print(legs.dumbell, "10-12 reps")
        print(legs.calisthenics, "10-12 reps")
        print()
    elif muscle_group == "shoulders".lower():
        print()
        print("-->Here is the workout you will do today<--")
        print()
        print(shoulders.barbell, "10-12 reps")
        print(shoulders.dumbell, "10-12 reps")
        print(shoulders.calisthenics, "10-12 reps")
        print()
elif question == "Lose Weight".lower():
    print()
    print("-->Here is the workout you will do today<--")
    print()
    print(lose_weight.tredmill)
    print(lose_weight.run)
    print(lose_weight.jump_rope)
    print()
