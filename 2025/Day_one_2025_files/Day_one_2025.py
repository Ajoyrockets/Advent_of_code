start_vaule = 50
# This opens the input file 
with open(r"C:\Users\ajoyp\OneDrive\Documents\Advent_of_code\2025\Day_one_2025_files\Day_one_2025_input_file.txt", "r") as file:
    List_input_file = [str(line.strip()) for line in file] # This will turn it into a list 
    num_lines = len(List_input_file) # how many rotations there are 

List_input_file_change = []
List_input_file_change = List_input_file 
num_lines_change = num_lines
while num_lines_change > 0 :
    Next_rotation = []
    Next_rotation = List_input_file_change.pop(0) # removes one item in the list at a time 
    num_lines_change = len(List_input_file_change)
    pos_neg = Next_rotation[0]
    if pos_neg == "R" :                           # removes the letter to leave the number 
        number_rotation = Next_rotation.lstrip("R")
        print(number_rotation)
    else :
        number_rotation = Next_rotation.lstrip("L")
        print(number_rotation)
