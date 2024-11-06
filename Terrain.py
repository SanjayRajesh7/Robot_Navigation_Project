from Robot import Robot
class Terrain:
    def __init__(self):
        self.robots = dict()
    
    def create_robot(self, robot_id):
        if robot_id in self.robots:
            return f"Robot with ID {robot_id} already exists."
        else:
            self.robots[robot_id] = Robot(robot_id)
            return f"Robot with ID {robot_id} is created successfully!!!."
    
    def move_robot(self, robot_id, direction_and_steps):
        if robot_id not in self.robots:
            return f"Robot with ID {robot_id} does not exist."
        else:
            if len(direction_and_steps) != 2 or direction_and_steps[0].upper() not in ["N","S","E","W"] and not direction_and_steps[1].isdigit():
                return "Invalid Input Format for Direction and Steps"
            else:
                occupied_positions = {robot_properties.position for r_id, robot_properties in self.robots.items() if r_id != robot_id}
                
                direction = direction_and_steps[0].upper()
                steps = int(direction_and_steps[1])
                robot = self.robots[robot_id]

                return robot.move(direction, steps, occupied_positions)

    def get_robot_position(self, robot_id):
        if robot_id not in self.robots:
            return f"Robot with ID {robot_id} does not exist."
        else:
            return f"The position of {robot_id} is {self.robots[robot_id].position}."
        
    def get_all_robots_id_and_position(self):
        if len(self.robots.items()) == 0:
            print("Robots are not yet created")
        else:
            for robot_id, robot_properties in self.robots.items():
                print(f"The position of {robot_id} is {robot_properties.position}.")