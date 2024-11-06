class Robot:
    def __init__(self,robot_id):
        self.robot_id = robot_id
        self.position = (0, 0)

    def move(self, direction, steps, occupied_positions):
        x, y = self.position
        if direction == 'N':
            if x-steps>0:
                while(steps):
                    if (x - steps, y) in occupied_positions:
                        steps -= 1
                    else:
                        x -= steps
                        break
            else:
                return "Robort Could not be moved outside the grid"
        elif direction == 'W':
            if y-steps>0:
                while(steps):
                    if (x, y - steps) in occupied_positions:
                        steps -= 1
                    else:
                        y -= steps
                        break
            else:
                return "Robort Could not be moved outside the grid"
        elif direction == 'S':
            while(steps):
                if (x + steps, y) in occupied_positions:
                    steps -= 1
                else:
                    x += steps
                    break
        elif direction == 'E':
            while(steps):
                if (x, y + steps) in occupied_positions:
                    steps -= 1
                else:
                    y += steps
                    break
        self.position = (x, y)
        return f"Robot with ID {self.robot_id} is moved successfully!!!."