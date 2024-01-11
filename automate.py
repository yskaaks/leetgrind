import os

def create_folder_and_file(problem_number, problem_name, solution_code):
    # Format folder and file name
    folder_name = f"{str(problem_number).zfill(4)}-{problem_name.replace(' ', '-')}"
    file_name = f"{folder_name}.py"

    # Create folder
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # Create and write to the file
    with open(os.path.join(folder_name, file_name), 'w') as file:
        file.write(solution_code)

    print(f"Solution for '{problem_name}' added successfully.")

# Example usage
problem_number = int(input("Enter the problem number: "))
problem_name = input("Enter the problem name: ")
solution_code = input("Paste your solution code here:\n")

create_folder_and_file(problem_number, problem_name, solution_code)
