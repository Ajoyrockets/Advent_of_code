start_vaule = 50
# This opens the input file 
# with open(r"C:\Users\ajoyp\OneDrive\Documents\Advent_of_code\2025\Day_one_2025_files\Day_one_2025_input_file.txt", "r") as file:
#     List_input_file = [str(line.strip()) for line in file] # This will turn it into a list 
#     num_lines = len(List_input_file) # how many rotations there are 

with open(r"C:\Users\ajoyp\OneDrive\Documents\Advent_of_code\2025\Day_one_2025_files\Day_one_2025_test_file", "r") as file:
    List_input_file = [str(line.strip()) for line in file] # This will turn it into a list 
    num_lines = len(List_input_file) # how many rotations there are 


List_input_file_change = []
List_input_file_change = List_input_file 
num_lines_change = num_lines
print(List_input_file_change)
print(start_vaule)
while num_lines_change > 0 :
    current_rotation = start_vaule
    Next_rotation = []
    Next_rotation = List_input_file_change.pop(0) # removes one item in the list at a time 
    num_lines_change = len(List_input_file_change)
    pos_neg = Next_rotation[0]
    if pos_neg == "R" :                           # removes the letter to leave the number 
        print(f"Current rotation is: {current_rotation}")
        next_rotation = Next_rotation.lstrip("R")
        current_rotation = current_rotation + int(next_rotation)
        if current_rotation > 100 :
            print(f"Current rotation is: {current_rotation}")
            current_rotation = current_rotation - 100
            print(current_rotation)
        else:
            print(current_rotation)

    else :
        next_rotation = Next_rotation.lstrip("L")
        current_rotation = current_rotation + int(next_rotation)
        if current_rotation < 0 :
            current_rotation = 100 + current_rotation 
            print(current_rotation)            
        else:
            print(current_rotation)