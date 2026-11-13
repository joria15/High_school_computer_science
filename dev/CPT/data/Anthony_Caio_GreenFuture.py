"""
author: Anthony Antczak and Caio Gentil Corado
date: 12/16/2024
CPT: Green Future
"""
from InquirerPy import prompt
# function to do prompts without 3 lines of code
def promptinput(message,choices):
    """Creates a prompt of choices"""
    user_input = [
        {
            "type": "list",
            "message": message,
            "choices": choices
        }
    ]
    return prompt(user_input)[0]

# function to input quiz questions
def get_input(prompt, limit):
    """An input that will refuse if any number is higher then the limit"""
    user_input = int(input(prompt))
    while not user_input < limit:
        user_input = int(input("Use a number from *0* to *10*: "))
    return user_input

# function to save data
def data_output(variable, name):
    """Saves a file"""
    variable = str(variable)
    with open("CPT\\data\\"+name, mode="a") as f_out:
        f_out.write(variable)
        f_out.write("\n")

def data_input(name):
    with open(name, mode = "r"):
        pass

# function to say that the user is doing good
def u_good(name, variable):
    if variable <=5:
        print(f"{name}: {variable} is very good, keep it like this or lower to minimize your carbon footprint"+"\n") 

def main():
    namelst = []
    animallst = []
    foodlst = []
    energylst = []
    renewlst = []
    trashlst = []
    housetypelst = []
    matlst = []
    eleclst = []
    housesizlst = []
    peoplelst = []
    #input / output
    #ask the user if company or person
    comp = promptinput("Company or Person?", ["Company", "Person"])
    print(comp)
    if comp == "Person":
        yes_no = str(input("Do you want to do the quiz?(y/n) "))
        while yes_no.lower().startswith("y"):
            name = str(input("What's your name? "))
            #quiz here
            print("==========================================================="+"\n"+"|Answer the following qustions based on a scale of 0 to 10|"+"\n"+"===========================================================")
            animal_based_products = get_input("How often do you use animal-based products? ",11)
            processed_food = get_input("How much of the food that you eat is unprocessed, unpackaged or locally grown? ", 11)
            energy_consumption = get_input("How energy efficient is your home? ",11)
            renewable_energy_usage = get_input("What percentage of your home's electricity comes from renewable sources?(1 = 10% and 10 = 100%) ", 11)
            trash_generation = get_input("Compared to your neighbors, how much trash do you generate? ", 11)
            print("=============================================================================="+"\n"+"|Answer the following questions by chosing the option that most represent you|"+"\n"+"==============================================================================")
            # I GOT THIS IDEA FROM "Thierri - aulasdev" on tiktok
            housetype = promptinput("Which housing type best describes your home",["Freestanding, no running water", "Freestanding, running water", "Multi-storey apartment", "Duplex, row house or building with 2-4 housing units", "Luxury condominium"])
            mat = promptinput("What material is your house constructed with?",["Straw/Bamboo", "Wood", "Brick/Concrete", "Adobe", "Steel/Other"])
            elec = promptinput("Do you have electricity in your home?",["Yes", "No"])
            housesize = promptinput("What is the size of your home?",["Tiny(5m2/50sq ft)","Small(29m2/308sq ft)", "Medium(100m2/1081sq ft)", "Large(378m2/4071sq ft)", "Huge(+474m2/5102sq ft)"])
            print("================================================================================"+"\n"+"Answer the question with precise numbers"+"\n"+"================================================================================")
            people = int(input("How many people live in your household? "))
            namelst.append(name)
            animallst.append(animal_based_products)
            foodlst.append(processed_food)
            energylst.append(energy_consumption)
            renewlst.append(renewable_energy_usage)
            trashlst.append(trash_generation)
            housetypelst.append(housetype)
            matlst.append(mat)
            eleclst.append(elec)
            housesizlst.append(housesize)
            peoplelst.append(people)

            # Saving Data

            data_output(namelst, "name.txt")
            data_output(animallst, "animal.txt")
            data_output(foodlst, "food.txt")
            data_output(energylst, "energy.txt")
            data_output(renewlst, "renew.txt")
            data_output(trashlst, "trash.txt")
            data_output(housetypelst, "housetype.txt")
            data_output(matlst, "mat.txt")
            data_output(eleclst, "elec.txt")
            data_output(housesizlst, "housesize.txt")
            data_output(peoplelst, "people.txt")

            # Giving tips on how to improve carbon emission

            u_good("Animal Based Products",animal_based_products)
            if animal_based_products > 5:
                print(f"Animal based products: {animal_based_products} try to lower this number, animal based products account for 57% of emissions"+"\n")
            u_good("Processed Foods",processed_food)
            if processed_food > 5:
                print(f"processed foods: {processed_food} try to lower this number, food processing accounts for a third of (GHG) greenhouse gasses"+"\n")
            u_good("Energy Consumption",energy_consumption)
            if energy_consumption > 5:
                print(f"energy consumption: {energy_consumption} try to lower this number, using a lot of electricity can create a lot of CO2 emissions"+"\n")
            u_good("Renewable Energy Usage",renewable_energy_usage)
            if renewable_energy_usage > 5:
                print(f"renewable energy usage: {renewable_energy_usage} try to lower this number, the production and consumption of renewable energy causes CO2 emissions"+"\n")
            u_good("Trash Generation", trash_generation)
            if trash_generation > 5:
                print(f"trash generation: {trash_generation} try to lower this number, trash accounts for 10%-15% of (GHG) greenhouse gasses and kills clean drinking water or marine animals"+"\n")

            #empty the list

            namelst = []
            animallst = []
            foodlst = []
            energylst = []
            renewlst = []
            trashlst = []
            housetypelst = []
            matlst = []
            eleclst = []
            housesizlst = []
            peoplelst = []

            #quiz again?
            
            yes_no = str(input("Do you want to do the quiz again? "))
        
    #processing
    #output
    if comp == "Company":
        # Company Questions
        compname = str(input("What is your company name? "))
        specific = str(input("Are you looking for a specific data? "))
        if specific[0].lower() == "y":
            what = promptinput("What specific data are you looking for?",["Food", "Electricity", "Housing", "Population"])



if __name__ == "__main__":
    main()


# if not cmp[0] == p and not cmp[0] == c