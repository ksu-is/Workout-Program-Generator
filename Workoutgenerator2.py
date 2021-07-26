from random import sample
from exercises import *
from time import sleep
from datetime import date
today = str(date.today())
#log = open("/home/billy/Desktop/Workout " + today + ".txt", "w") #whatever this file is, I don't have it on my PC

#Create the generator class which will actually create the routines according 
#to the desired number of days per week.
class Generator(object):
    def get_goal(self):
        #Get  input from user for goals and store it in a variable called 
        #"goal".
        goal = input("Is your goal to gain strength, endurance, or hypertrophy?\n>>> ")
        goal = goal.lower()
        #This section changes the information and format printed out 
        #according to the goal.
        while True:
            if "strength" in goal:
                self.sets = "5-8"
                self.target_reps = "1-6"
                self.actual_reps = "__/__/__/__/__/__/__/__"
                self.template = '| {:^38} | {:^7} | {:^6} | {:^12} | {:^24} |'
                break
            elif "endurance" in goal:
                self.sets = "1-3"
                self.target_reps = "15-20"
                self.actual_reps = "__/__/__"
                self.template = '| {:^50} | {:^7} | {:^6} | {:^12} | {:^12} |'
                break
            elif "hypertrophy" in goal:
                self.sets = "4"
                self.target_reps = "8-12"
                self.actual_reps = "__/__/__/__"
                self.template = '| {:^50} | {:^7} | {:^6} | {:^12} | {:^12} |'
                break
            else:
                print ("Please enter strength, endurance, or hypertrophy.")
                goal = input("Is your goal to gain strength, endurance, or hypertrophy?\n>>> ")
                goal = goal.lower()
        return self.sets, self.target_reps, self.actual_reps, self.template

    def get_experience(self):
        #Ask the user how much experience they have working out and 
        #store that number in a variable called "experience".
        self.experience = input("How long have you been working out for?\n1. 0-6 months\n2. 6 months - 2 years\n3. 2+ years\n>>> ")
        #Loop through the input request until the user gives a number. 
        #The loop continues until a number is given.
        while True:
            try:
                self.experience = int(self.experience)
            except ValueError:
                print ("Oops, please enter either 1, 2, or 3.")
                self.experience = input("How long have you been working out for?\n1. 0-6 months\n2. 6 months - 2 years\n3. 2+ years\n>>> ")
            else:
                break
        return self.experience

    def check_experience(self, experience):
        #This function verifies that the number given was within the range of
        #options. It can probably be edited out for the mobile versions.
        while self.experience > 3 or self.experience < 1:
            print("Please choose between choice 1, 2, or 3.")
            self.experience = Generator.get_experience(self)
        else:
            pass
        return self.experience

    def get_frequency(self):
        #Ask the user how many days per week they want to work out and store 
        #that number in a variable called "days".
        self.days = input("How many days would you like to workout this week?\n>>> ")
        #Loop through the input request until the user gives a number. 
        #The loop continues until a number is given.
        while True:
            try:
                self.days = int(self.days)
            except ValueError:
                print ("Oops, try entering a number, like 3.")
                self.days = input("How many days would you like to workout this week?\n>>> ")
            else:
                break
        return self.days

    def check_frequency(self, days):
        #This function verifies that the number of days to workout is 
        #between 1 and 6.
        while self.days >= 7 or self.days < 1:
            if self.days == 7:
                print("You need to take at least one rest day per week.")
                self.days = Generator.get_frequency(self)
            elif self.days < 1:
                print("You need to work out at least one day per week.")
                self.days = Generator.get_frequency(self)
            elif self.days > 7:
                print("There are only 7 days per week!")
                self.days = Generator.get_frequency(self)
            else:
                pass
        return self.days

    #This funciton takes the user's preferences for each given category 
    #of exercises and if the user says they do like using a given piece of
    # equipment/style of working out, then the list of those exercises
    #for each muscle group are added to the main list for each muscle group. 
    #If the user says they don't like a certain type of exercise, 
    #then the list of those exercises is just ignored. Only exercises
    #found in the main exercises list are used when generating the workout.
    def user_preference(self, equipment0, equipment1, equipment2, equipment3, equipment4, equipment5, equipment6, equipment7, equipment8, name):
        preference = input("Do you like using and/or have access to {!s}?\n>>> ".format(name))
        while True:
            if "y" in preference:
                for exercise in equipment0:
                    Chest.exercises.append(exercise)
                for exercise in equipment1:
                    Back.exercises.append(exercise)
                for exercise in equipment2:
                    Legs.exercises.append(exercise)
                for exercise in equipment3:
                    Lower_Legs.exercises.append(exercise)
                for exercise in equipment4:
                    Biceps.exercises.append(exercise)
                for exercise in equipment5:
                    Triceps.exercises.append(exercise)
                for exercise in equipment6:
                    Shoulders.exercises.append(exercise)
                for exercise in equipment7:
                    Forearms.exercises.append(exercise)
                for exercise in equipment8:
                    Abs.exercises.append(exercise)
                break
            elif "n" in preference:
                break
            else:
                print ("Sorry, please try inputting yes or no.")
                preference = input("Do you like using and/or have access to {!s}?\n>>> ".format(name))
        return preference

    def get_preferences(self):
        #Here the function is called for each type of exercise to build 
        #the main exercise list which is the only list considered in 
        #generating the workout.
        Generator.user_preference(self, Chest.selectorized, Back.selectorized, Legs.selectorized, Lower_Legs.selectorized, Biceps.selectorized, Triceps.selectorized, Shoulders.selectorized, Forearms.selectorized, Abs.selectorized, "selectorized equipment")
        #In order to remove some repition, and since dumbbells and 
        #barbells are part of the free weights category, the program will 
        #only ask the user if they want to use dumbbells and barbells if 
        #they have already said that they like free weights. Otherwise, 
        #those two options are skipped.
        fwpref = Generator.user_preference(self, Chest.free_weights, Back.free_weights, Legs.free_weights, Lower_Legs.free_weights, Biceps.free_weights, Triceps.free_weights, Shoulders.free_weights, Forearms.free_weights, Abs.free_weights, "free weights")
        if "y" in fwpref:
            Generator.user_preference(self, Chest.dumbbell, Back.dumbbell, Legs.dumbbell, Lower_Legs.dumbbell, Biceps.dumbbell, Triceps.dumbbell, Shoulders.dumbbell, Forearms.dumbbell, Abs.dumbbell, "dumbbell")
            Generator.user_preference(self, Chest.barbell, Back.barbell, Legs.barbell, Lower_Legs.barbell, Biceps.barbell, Triceps.barbell, Shoulders.barbell, Forearms.barbell, Abs.barbell, "barbell")
        else:
            pass
        Generator.user_preference(self, Chest.calisthenics, Back.calisthenics, Legs.calisthenics, Lower_Legs.calisthenics, Biceps.calisthenics, Triceps.calisthenics, Shoulders.calisthenics, Forearms.calisthenics, Abs.calisthenics, "calisthenic exercises")
        Generator.user_preference(self, Chest.cable, Back.cable, Legs.cable, Lower_Legs.cable, Biceps.cable, Triceps.cable, Shoulders.cable, Forearms.cable, Abs.cable, "cable equipment")

    def workout_title(self, days, experience):
        #This function prints out the title of the workout, according to 
        #how many days the user will workout and their experience.
        if experience == 1:
            print("-" * 103,) #file = log) commented out problem file
            print('| {:^99} |'.format("Beginner - " + str(days) + " Day Split")) #, #file = log)
        elif experience == 2:
            print("-" * 103,) #file = log) commented out probelm file
            print('| {:^99} |'.format("Intermediate - " + str(days) + " Day Split")) #, #file = log)
        elif experience == 3:
            print("-" * 103,) #file = log) commented out the probelm file
            print('| {:^99} |'.format("Advanced - " + str(days) + " Day Split")) #, #file = log)

    #The format for the header, taking the name of the workout day as an 
    #argument.
    def header(workout):
        print("|", "-" * 99, "|")#, file = log)
        print('| {:^99} |'.format(workout))#, #file = log)
        print("|", "-" * 99, "|")#, #file = log)

    def section(name):
        #This funciton prints out the format for the workout, according to
        #which section of the workout is being printed out.
        if name == "Warm Ups":
            print('| {:<99} |'.format(name))#, file = log)
            print("|", "-" * 99, "|")#, file = log)
            print('| {:^99} |'.format("Refer to the " + name + " section of the app for the muscles you are training."))#, #file = log)
            print("|", "-" * 99, "|")#, file = log)
        elif name == "Cool Down":
            print("|", "-" * 99, "|")#, file = log)
            print('| {:<99} |'.format(name))#, file = log)
            print("|", "-" * 99, "|")#, file = log)
            print('| {:^99} |'.format("Refer to the " + name + " section of the app for the muscles you are training."))#, #file = log)
        else:
            print('| {:<99} |'.format(name))#, file = log)
            print("|", "-" * 99, "|")#, file = log)

    #This formats the titles of the columns.
    def column_titles(self):
        print (self.template.format("Exercise", "Weight", "Sets", "Target Reps", "Actual Reps"))#, file = log)
        print("|", "-" * 99, "|")#, file = log)

    #This closes up the table at the bottom and adds a little note.
    def footer():
        print("|", "-" * 99, "|")#, file = log)
        print('| {:^99} |'.format("Complete this routine for 2-3 weeks and then come generate a new one!"))#, file = log)
        print("-" * 103)#, file = log)

    #This method prints out all of the exercises for each given muscle group.
    def print_exercises(self, muscle_group):
        for item in muscle_group:
            print (self.template.format(item, '_____', self.sets, self.target_reps, self.actual_reps))#, file = log) 

    #The following functions print out the exercises for the given muscle
    #groups.
    def generate_cardio(self, quantity):
        Generator.header("Cardio Day")
        Generator.section("Warm Ups")
        Generator.section("Workout")
        Generator.column_titles(self)
        cardio_exercises = sample(Cardio.exercises, quantity)
        Generator.print_exercises(self, cardio_exercises)
        Generator.section("Cool Down")

    def generate_full_body(self, large_muscle, small_muscle):
        Generator.header("Full Body Day")
        #The sample method grabs a number of random exercises from the 
        #given list and stores them in a variable according to the exercise.
        Generator.section("Warm Ups")
        #This section prints out the exercises in a list according to the 
        #template above.
        Generator.section("Workout")
        Generator.column_titles(self)
        chest_exercises = sample(Chest.exercises, large_muscle)
        back_exercises = sample(Back.exercises, large_muscle)
        legs_exercises = sample(Legs.exercises, large_muscle)
        lower_legs_exercises = sample(Lower_Legs.exercises, small_muscle)
        biceps_exercises = sample(Biceps.exercises, small_muscle)
        triceps_exercises = sample(Triceps.exercises, small_muscle)
        shoulders_exercises = sample(Shoulders.exercises, small_muscle)
        forearms_exercises = sample(Forearms.exercises, small_muscle)
        abs_exercises = sample(Abs.exercises, small_muscle)
        Generator.print_exercises(self, chest_exercises)
        Generator.print_exercises(self, back_exercises)
        Generator.print_exercises(self, legs_exercises)
        Generator.print_exercises(self, lower_legs_exercises)
        Generator.print_exercises(self, biceps_exercises)
        Generator.print_exercises(self, triceps_exercises)
        Generator.print_exercises(self, shoulders_exercises)
        Generator.print_exercises(self, forearms_exercises)
        Generator.print_exercises(self, abs_exercises)
        Generator.section("Cool Down")

    def generate_upper_body(self, large_muscle, small_muscle):
        Generator.header("Upper Body Day")
        Generator.section("Warm Ups")
        Generator.section("Workout")
        Generator.column_titles(self)
        chest_exercises = sample(Chest.exercises, large_muscle)
        back_exercises = sample(Back.exercises, large_muscle)
        biceps_exercises = sample(Biceps.exercises, small_muscle)
        triceps_exercises = sample(Triceps.exercises, small_muscle)
        shoulders_exercises = sample(Shoulders.exercises, small_muscle)
        forearms_exercises = sample(Forearms.exercises, small_muscle)
        Generator.print_exercises(self, chest_exercises)
        Generator.print_exercises(self, back_exercises)
        Generator.print_exercises(self, biceps_exercises)
        Generator.print_exercises(self, triceps_exercises)
        Generator.print_exercises(self, shoulders_exercises)
        Generator.print_exercises(self, forearms_exercises)
        Generator.section("Cool Down")

    def generate_lower_body(self, large_muscle, small_muscle):
        Generator.header("Lower Body Day")
        legs_exercises = sample(Legs.exercises, large_muscle)
        lower_legs_exercises = sample(Lower_Legs.exercises, small_muscle)
        abs_exercises = sample(Abs.exercises, small_muscle)
        Generator.section("Warm Ups")
        Generator.section("Workout")
        Generator.column_titles(self)
        Generator.print_exercises(self, legs_exercises)
        Generator.print_exercises(self, lower_legs_exercises)
        Generator.print_exercises(self, abs_exercises)
        Generator.section("Cool Down")

    def generate_chest(self, days, large_muscle, small_muscle):
        Generator.header("Chest Day")
        chest_exercises = sample(Chest.exercises, large_muscle)
        triceps_exercises = sample(Triceps.exercises, small_muscle)
        Generator.section("Warm Ups")
        Generator.section("Workout")
        Generator.column_titles(self)
        Generator.print_exercises(self, chest_exercises)
        Generator.print_exercises(self, triceps_exercises)
        if days == 3:
            shoulders_exercises = sample(Shoulders.exercises, small_muscle)
            Generator.print_exercises(self, shoulders_exercises)
        else:
            pass
        Generator.section("Cool Down")

    def generate_back(self, days, large_muscle, small_muscle):
        Generator.header("Back Day")
        back_exercises = sample(Back.exercises, large_muscle)
        biceps_exercises = sample(Biceps.exercises, small_muscle)
        Generator.section("Warm Ups")
        Generator.section("Workout")
        Generator.column_titles(self)
        Generator.print_exercises(self, back_exercises)
        Generator.print_exercises(self, biceps_exercises)
        if days == 3:
            forearms_exercises = sample(Forearms.exercises, small_muscle)
            Generator.print_exercises(self, forearms_exercises)
        else:
            pass
        Generator.section("Cool Down")

    def generate_legs(self, days, large_muscle, small_muscle):
        Generator.header("Leg Day")
        legs_exercises = sample(Legs.exercises, large_muscle)
        lower_legs_exercises = sample(Lower_Legs.exercises, small_muscle)
        Generator.section("Warm Ups")
        Generator.section("Workout")
        Generator.column_titles(self)
        Generator.print_exercises(self, legs_exercises)
        Generator.print_exercises(self, lower_legs_exercises)
        if days == 3:
            abs_exercises = sample(Abs.exercises, small_muscle)
            Generator.print_exercises(self, abs_exercises)
        else:
            pass
        Generator.section("Cool Down")

    def generate_arms(self, small_muscle):
        Generator.header("Arm Day")
        shoulders_exercises = sample(Shoulders.exercises, small_muscle)
        forearms_exercises = sample(Forearms.exercises, small_muscle)
        abs_exercises = sample(Abs.exercises, small_muscle)
        Generator.section("Warm Ups")
        Generator.section("Workout")
        Generator.column_titles(self)
        Generator.print_exercises(self, shoulders_exercises)
        Generator.print_exercises(self, forearms_exercises)
        Generator.print_exercises(self, abs_exercises)
        Generator.section("Cool Down")

    def create_workout(self, experience, days):
        #This function puts all the exercises together according to the format
        #given.
        Generator.workout_title(self, days, experience)
        if experience == 1:
            #Beginners will always have a cardio day if it is an even-numbered
            #day and a weights day if it is an odd-numbered day. This function
            #checks which day it is and provides the workout accordingly.
            for day in range(days):
                if day % 2 == 0:
                    Generator.generate_cardio(self, 1)
                else:
                    Generator.generate_full_body(self, 1, 1)
            Generator.footer()
        elif experience == 2:
            #Intermediate lifters should have cardio on every third day and 
            #weights days on every even pair of days. If only one day is
            #requested, then it will be a cardio day.
            workout = days // 2
            cardio = (days % 2) * workout
            if days == 1:
                Generator.generate_cardio(self, 3)
            elif days < 5:
                for day in range(workout):
                    Generator.generate_upper_body(self, 1, 1)
                    Generator.generate_lower_body(self, 2, 1)
                for day in range(cardio):
                    Generator.generate_cardio(self, 3)
            else:
                for day in range(0, 2):
                    Generator.generate_upper_body(self, 1, 1)
                    Generator.generate_lower_body(self, 2, 1)
                for day in range(0, days - 4):
                    Generator.generate_cardio(self, 3)
            Generator.footer()
        elif experience == 3:
            #Advanced lifters have more specific rules according to how many
            #days per week they can/want to work out. If the user only wants 
            #to work out 1 day of the week, a full body workout will be 
            #generated.
            if days == 1:
                Generator.generate_full_body(self, 1, 1)
            #A 2 day split should consist of an upper body and a lower body day.
            elif days == 2:
                Generator.generate_upper_body(self, 2, 1)
                Generator.generate_lower_body(self, 2, 1)
            #A 3 day split will have a chest day, back day, and leg day.
            elif days == 3:
                Generator.generate_chest(self, days, 3, 2)
                Generator.generate_back(self, days, 3, 2)
                Generator.generate_legs(self, days, 3, 2)
            #A 4 day split should have a Chest Day, Back Day, Leg Day, 
            #and Shoulder/Forearm/Ab Day. Any additional days should just be
            #cardio days.
            elif days >= 4:
                Generator.generate_chest(self, days, 3, 2)
                Generator.generate_back(self, days, 3, 2)
                Generator.generate_legs(self, days, 3, 2)
                Generator.generate_arms(self, 2)
                for day in range(0, days - 4):
                    Generator.generate_cardio(self, 3)
            Generator.footer()


class Engine(object):
    #This function runs all of the functions required to make the program run.
    def start(Generator):
        Generator.get_goal()
        Generator.get_preferences()
        experience = Generator.get_experience()
        experience = Generator.check_experience(experience)
        days = Generator.get_frequency()
        days = Generator.check_frequency(days)
        Generator.create_workout(experience, days)
        #log.close() #commenting out the problem files

gen1 = Generator()
Engine.start(gen1)
