"""main file for the project"""

import sqlite3
from sql_module import grubs, seed

with sqlite3.connect("employee.sqlite3") as connection:
    # connects to the database and creates a grub
    my_grub = grubs(database_connection=connection)
    # shares the connection with seed and creates a seed object
    seedling = seed(database_connection=connection)


def create_employee_form(access_table):
    """
    Its a form that gaters the requried user
    input in order to create a new employee
    """
    # Disable all the too-many-branches violations in this function
    # pylint: disable=too-many-branches
    required_inputs = {
        "full_name": None,
        "address": None,
        "work_from_home": None,
        "fun_fact": None,
        "access_level": None,
        "all_done": False
    }
    while not required_inputs["all_done"]:
        if required_inputs["full_name"] is None:
            temp_var = input("\nEnter full name : ")
            if len(temp_var) > 30:
                print("Name is to long")
            else:
                required_inputs["full_name"] = temp_var

        elif required_inputs["address"] is None:
            temp_var = input("\nEnter address : ")
            if len(temp_var) > 70:
                print("Address is to long")
            else:
                required_inputs["address"] = temp_var

        elif required_inputs["work_from_home"] is None:
            temp_var = input("\nY/N Work from home : ").lower()
            if "y" in temp_var:
                required_inputs["work_from_home"] = True
            elif "n" in temp_var:
                required_inputs["work_from_home"] = False
            else:
                print("Invalid input must be yes or no.")

        elif required_inputs["fun_fact"] is None:
            temp_var = input("\nEnter a fun fact : ")
            if len(temp_var) > 30:
                print("Fact is to long")
            else:
                required_inputs["fun_fact"] = temp_var

        elif required_inputs["access_level"] is None:
            for level in access_table:
                print(f"Level ID ({level[0]}) Name {level[-1]}")
            temp_var = input("Enter a access ID : ")
            try:
                if int(temp_var) in list(
                    range(access_table[0][0], access_table[-1][0] + 1)
                ):
                    required_inputs["access_level"] = temp_var
                else:
                    print("Enter a access level thats listed.")
            except ValueError:
                print("Enter a valid number.")

        else:
            print("The folowing are the entered values")
            keys_to_check = list(required_inputs.keys())
            keys_to_check.pop(-1)
            for key in keys_to_check:
                print(f"{key} = {required_inputs[key]}")
            if "y" in input("Yes to continue : ").lower():
                required_inputs["all_done"] = True
            else:
                required_inputs = {
                    "full_name": None,
                    "address": None,
                    "work_from_home": None,
                    "fun_fact": None,
                    "access_level": None,
                    "all_done": False
                }
    return_list = list(required_inputs.values())
    return_list.pop(-1)
    return return_list


def main(my_grub_main, seedling_main):
    """Main function for the program"""

    pick = str(input(
        """
Do you want to either
1) list off all employees
2) create a new employee
> """
    ))
    if "1" in pick:
        for employee in my_grub_main.get_all_of_table("employees_table"):
            print(
                f"employee id number {employee[0]} his name is {employee[1]}"
            )
            print(f"Full info\naddrees: {employee[2]}\nWork From Home: \
{employee[3]}\nFun Fact: {employee[4]}\nAccess Level ID: {employee[5]}")

    if "2" in pick:
        access_table = my_grub_main.get_all_of_table("access_schema")
        seedling_main.insert_to_table(
            "employees_table",
            create_employee_form(access_table=access_table)
        )


if __name__ == "__main__":
    main(my_grub_main=my_grub, seedling_main=seedling)
    while "n" in input("Quit Program (y/n) : ").lower():
        main(my_grub_main=my_grub, seedling_main=seedling)
