# File I/O IT Inventory Project - Baasim Ahmed
#This program handles IT equipment inventory by writing to and reading from a plain text file.

#Function that writes to the txt document
def writing_function(file):
    #Open the file using the appropriate mode
    output_file = open(file, "w")
    #Prompt user for name of the equipment
    tool = input("Name of the equipment or type 'quit' to finish: ")
    #Use a sentinel controlled loop until user types quit
    while tool.lower() != "quit":
        #Prompt the user for the number and cost of the tool
        number = input("Number on hand: ")
        price = input("Cost of one piece of this equipment: ")
        #Write the inputs to the file
        output_file.write(f"{tool},{number},{price}\n")
        tool = input("Name of the equipment or type 'quit' to finish: ")
    #Close the file
    output_file.close()
    return

#Function that reads and prints all information
def reading_function(file):
    #Open the file using the appropriate mode
    input_file = open(file, "r")
    #Include Column Headings
    print("IT Inventory")
    print(f"{"Name":<20}{"Number on Hand":>20}{"Cost":>10}")
    #For loop that prints the tool + info, formatted.
    for line in input_file:
        tool, number, price = line.split(",")
        number = int(number)
        price = float(price)
        print(f"{tool:<20}{number:>20}{price:>10.2f}")
    #Close the file
    input_file.close()
    return

#Function that adds the total cost
def summary(file):
    #Open the file using the appropriate mode
    input_file = open(file, "r")
    #Set a variable that is the total value
    total = float(0.0)
    #use a for loop that splits the txt info, then cast the variables and calculate the total.
    for line in input_file:
        tool, number, price = line.split(",")
        number = int(number)
        price = float(price)
        total += number * price
    #Close the file
    input_file.close()
    #Print the total
    print(f"Total value of inventory: {total:.2f}")
    return

#Define main, assign a variable to the file, and call the 2 other functions.
def main():
    file = "homework.txt"
    writing_function(file)
    reading_function(file)
    summary(file)
    return

main()