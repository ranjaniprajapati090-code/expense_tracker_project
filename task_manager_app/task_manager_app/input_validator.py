def get_valid_string(prompt):
    """Ensure input is not empty."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty. Please try again.")


def get_valid_priority(prompt):
    """Ensure priority is Low, Medium, or High."""
    valid_priorities = ["Low", "Medium", "High"]
    while True:
        value = input(prompt).strip().capitalize()
        if value in valid_priorities:
            return value
        print("Invalid priority. Choose Low, Medium, or High.")