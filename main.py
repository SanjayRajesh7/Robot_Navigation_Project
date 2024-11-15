from Terrain import Terrain
import time
terrain = Terrain()

while True:
    print("\nChoose any option from the following:\n1. Create a new robot.\n2. Movie a robot.\n3. Find the position of a robot.\n4. Display the ID and position of all robots.\n5. Exit\n")
    option_chosen = input().strip()
    if option_chosen.isdigit() and int(option_chosen) in [1,2,3,4,5]:
        option_chosen = int(option_chosen)
        if option_chosen == 1:
            robot_id = input("Enter a ID for the new robot : ").strip()
            print(terrain.create_robot(robot_id))
        elif option_chosen == 2:
            robot_id = input("Enter the ID of the robot to be moved : ").strip()
            is_horse_move = input("Do you want move the robot like a horse choin in chess game?\nsay Y(yes)/N(no): ").strip().upper()
            if is_horse_move == "Y" or is_horse_move == "YES":
                direction_and_steps = input("Enter the initial step(s) (either 1 or 2) and direction for the robot to move (eg format:- 2NE,1SE,1NW,2NE): ").strip()
                if len(direction_and_steps) == 3 or direction_and_steps[1:].upper() in ["NE","NW","SE","SW"] and direction_and_steps[0].isdigit():
                    print(terrain.move_robot(robot_id, direction_and_steps, True))
                else:
                    print("Invalid input")
            else:
                direction_and_steps = input("Enter the step(s) (1 to 9) and direction for the robot to move (eg format:- 2N,1S,2E,9W,4NE,9SE): ").strip()
                print(terrain.move_robot(robot_id, direction_and_steps, False))
        elif option_chosen == 3:
            robot_id = input("Enter the ID of the robot to find its position : ").strip()
            print(terrain.get_robot_position(robot_id))
        elif option_chosen == 4:
            terrain.get_all_robots_id_and_position()
        elif option_chosen == 5:
            break
    else:
        print("Invalid Option")
    time.sleep(3)