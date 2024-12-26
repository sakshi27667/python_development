
import numpy as np  # Correct module name

def inp_mat(prompt):
    """
    Function to take a matrix as input from the user.
    """
    print(prompt)
    try:
        rows = int(input("Enter the number of rows: "))
        cols = int(input("Enter the number of columns: "))
        print("Enter the values of the matrix row by row:")
        matrix = []  # Initialize an empty list to store rows

        for i in range(rows):
            row = list(map(float, input(f"Row {i + 1}: ").split()))
            if len(row) != cols:
                print("Error: Number of columns must match the specified size.")
                return None
            matrix.append(row)

        return np.array(matrix)  # Convert list of rows into a NumPy array

    except ValueError:
        print("Error: Invalid input! Please enter numeric values only.")
        return None


def operations():
    """
    Function to perform matrix operations: Addition, Subtraction, or Multiplication.
    """
    while True:
        print("\nMatrix Operations Menu:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Exit")

        choice = input("Enter your operation (1-4): ")

        if choice == "4":
            print("Exiting the program. Goodbye!")
            break  # Exit the program

        if choice not in ["1", "2", "3"]:
            print("Error: Invalid choice! Please select a valid operation.")
            continue  # Restart the loop for a valid choice

        # Take input for two matrices
        mat1 = inp_mat("Matrix 1:")
        if mat1 is None:
            continue
        mat2 = inp_mat("Matrix 2:")
        if mat2 is None:
            continue

        # Perform the chosen operation
        if choice == "1":  # Addition
            if mat1.shape == mat2.shape:
                print("Result of Addition:\n", mat1 + mat2)
            else:
                print("Error: Matrices must have the same dimensions for addition.")

        elif choice == "2":  # Subtraction
            if mat1.shape == mat2.shape:
                print("Result of Subtraction:\n", mat1 - mat2)
            else:
                print("Error: Matrices must have the same dimensions for subtraction.")

        elif choice == "3":  # Multiplication
            if mat1.shape[1] == mat2.shape[0]:
                print("Result of Multiplication:\n", np.dot(mat1, mat2))
            else:
                print("Error: Number of columns in Matrix 1 must equal the number of rows in Matrix 2 for multiplication.")


if __name__ == "__main__":
    operations()
