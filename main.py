from Terrain import Terrain
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
            direction_and_steps = input("Enter the direction and steps (eg format:- N3,S2,E7,W9) for the robot to move : ").strip()
            print(terrain.move_robot(robot_id, direction_and_steps))
        elif option_chosen == 3:
            robot_id = input("Enter the ID of the robot to find its position : ").strip()
            print(terrain.get_robot_position(robot_id))
        elif option_chosen == 4:
            terrain.get_all_robots_id_and_position()
        elif option_chosen == 5:
            break
    else:
        print("Invalid Option")