from forcecalcclass import ForceCalculator

MENU = '''\n:~Net Force Calculator Program
          1) Add force
          2) Remove force
          3) Show forces
          4) Find force components
          5) Compute resultant force
          6) Reset calculator
          7) Stop the program
          Enter option~:'''

def prompt_num(prompt_str: str) -> float:
    """
    Prompts the user for a float.
    :param prompt_str: Prompt to show user.
    :return: float: user input.
    """
    while True:
        user = input(prompt_str)
        try:
            return float(user)
        except ValueError:
            print(f"\nInput '{user}' is not a valid float number! Please try again.")

def get_force_name() -> str:
    """Helper function to get the name of a force."""
    return input("\n:~Enter name of force~:").strip()

def add_force_option(force_calculator: ForceCalculator):
    """Handles the logic for adding a force."""
    name = get_force_name()
    magnitude = prompt_num("\n:~Enter value for Magnitude (N)~: ")
    angle = prompt_num("\n:~Enter value for Angle (degrees)~: ")
    try:
        force_calculator.add_force(name, magnitude, angle)
    except RuntimeError as e:
        print(e)

def remove_force_option(force_calculator: ForceCalculator):
    """Handles the logic for removing a force."""
    name = get_force_name()
    try:
        force_calculator.remove_force(name)
    except RuntimeError as e:
        print(e)

def show_forces_option(force_calculator: ForceCalculator):
    """Handles the logic for showing all forces."""
    forces = force_calculator.get_forces()
    if not forces:
        print("\nThere are no forces in the calculator.")
    else:
        print("\nForces in the calculator:")
        print(force_calculator)

def find_force_components_option(force_calculator: ForceCalculator):
    """Handles the logic for finding force components of a specific force."""
    name = get_force_name()
    try:
        force = force_calculator[name]
        print(f"\nForce components for Force object '{name}':")
        print(force)
    except RuntimeError as e:
        print(e)

def compute_resultant_force_option(force_calculator: ForceCalculator):
    """Handles the logic for computing the resultant force."""
    print("\nComputing the resultant force of all forces in the calculator...")
    print(force_calculator.compute_net_force())

def reset_calculator_option():
    """Handles the logic for resetting the calculator."""
    return ForceCalculator()  # Return a new ForceCalculator object

def stop_program_option():
    """Handles stopping the program."""
    print("\nExiting the program...")
    return False

def main():
    # Initialize the ForceCalculator object
    force_calculator = ForceCalculator()

    # Mapping options to functions for cleaner structure
    options = {
        "1": lambda: add_force_option(force_calculator),
        "2": lambda: remove_force_option(force_calculator),
        "3": lambda: show_forces_option(force_calculator),
        "4": lambda: find_force_components_option(force_calculator),
        "5": lambda: compute_resultant_force_option(force_calculator),
        "6": lambda: reset_calculator_option(),
        "7": lambda: stop_program_option()
    }

    # Main loop
    while True:
        # Show menu and get user input
        option = input(MENU).strip()

        # Check if the option is valid, then call the corresponding function
        if option in options:
            result = options[option]()  # Call the function associated with the option
            if option == "6":
                force_calculator = result  # Reset the force calculator
            elif option == "7" and result is False:
                break  # Stop the program
        else:
            print("\nInvalid option. Please try again.")

if __name__ == "__main__":
    main()
