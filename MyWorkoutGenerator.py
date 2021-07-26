from ExcerciseLibrary import *



question = input("What is your goal for today's workout? (Build Muscle, Gain Strength, or Lose Weight)\n ")

if question == "Build Muscle".lower():
    muscle_group = input("What muscle group would you like to worjout today? (Chest, biceps, back, legs, or shoulders)")
    if muscle_group == "chest".lower():
        print(chest.barbell)
