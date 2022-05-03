# Diego Jui
# Professor Kyle Dencker 
# Final Assignement
# 25 Apr 2022


# My program's purpose is to organize a schedule a new UCF student would like to follow to better know the campus.


tour_list =[]
location = ""

while (location.lower() != "finished"):
    
    location = input("Welcome to the Univeristy of Central Florida! Please list the places you want to visit on campus before the start of your first semester.\n")

    if (location.lower() != "finished"):
        tour_list.append(location)

        for num in range(len(tour_list)):
            print(num+1,"-", tour_list[num])

    else:
        print("Here is the list of locations you will visit for the day:")

        for num in range(len(tour_list)):
            print(num+1,"-", tour_list[num])

def classes_1():
    classes = input("Would you like to visit your classrooms as well?")

    if classes != "No":
        classes_2 = input("Please list the classes/classrooms you would like to visit.")

        tour_list.append(classes_2)

        for num in range(len(tour_list)):
            print(num+1,"-", tour_list[num])
        print("All locations have been added.")

    if classes == "No":
        print("All locations have beed added.")

def lunch():
    lunch_1 = input("Would you like to get lunch on campus during your tour?")

    if lunch_1 != "No":
        lunch_2 = input("Please choose one of the resturants on campus for lunch.")
        print("Here is the list of locations you will visit:")
    
        for num in range(len(tour_list)):
                print(num+1,"-", tour_list[num])

        print("And you will get lunch at",lunch_2)
        print("Have fun!")


    else:
        print("Very well.")
        print("Here is the list of locations you will visit:")
    
        for num in range(len(tour_list)):
                print(num+1,"-", tour_list[num])
        print("Have fun!")

        
classes_1()
lunch()


