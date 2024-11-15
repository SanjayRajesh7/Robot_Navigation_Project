invalid_move_message = "Robort could not be moved outside the grid"
class Robot:
    def __init__(self,robot_id):
        self.robot_id = robot_id
        self.position = (0, 0)

    def move(self, direction, steps, occupied_positions,is_horse_move=False):
        x, y = self.position
        if direction == 'N':
            if x-steps>0:
                while(steps):
                    if (x - steps, y) in occupied_positions:
                        steps -= 1 # to move 1 step towards south
                    else:
                        x -= steps
                        break
            else:
                return invalid_move_message
        elif direction == 'W':
            if y-steps>0:
                while(steps):
                    if (x, y - steps) in occupied_positions:
                        steps -= 1 # to move 1 step towards east
                    else:
                        y -= steps
                        break
            else:
                return invalid_move_message
        elif direction == 'S':
            while(steps):
                if (x + steps, y) in occupied_positions:
                    steps -= 1 # to move 1 step towards north
                else:
                    x += steps
                    break
        elif direction == 'E':
            while(steps):
                if (x, y + steps) in occupied_positions:
                    steps -= 1 # to move 1 step towards west
                else:
                    y += steps
                    break
        elif direction == "SE":
            if is_horse_move: # to mpve like a horse coin in chess game
                initial_move = steps # steps to move towards south
                final_move = 3-steps # steps to move towards east
                while(initial_move):
                    if(x+initial_move,y+final_move) in occupied_positions:
                        if final_move:
                            final_move -= 1 # 1 step towards west
                        else:
                            initial_move -= 1 # 1 step towards north
                    else:
                        x += initial_move
                        y += final_move
                        break
            else: # to move diagonally
                while(steps):
                    if (x+steps,y+steps) in occupied_positions:
                        steps -= 1 # 1 step towards north-west
                    else:
                        x += steps
                        y += steps
                        break
        elif direction == "Sw":
            if is_horse_move: # to mpve like a horse coin in chess game
                initial_move = steps # steps to move towards south
                final_move = 3-steps # steps to move towards west
                if y-final_move > 0 :
                    while(initial_move):
                        if (x+initial_move,y-final_move) in occupied_positions:
                            if final_move:
                                final_move -= 1 # 1 step towards east
                            else:
                                initial_move -= 1 # 1 step towards north
                        else:
                            x += initial_move
                            y -= final_move
                            break
                else: 
                    return invalid_move_message
            else: # to move diagonally
                if (y-steps>0):
                    while(steps):
                        if (x+steps,y-steps) in occupied_positions:
                            steps -= 1 # 1 step towards north-east
                        else:
                            x += steps
                            y -= steps
                            break
                else:
                    return invalid_move_message
        elif direction == "NE":
            if is_horse_move: # to mpve like a horse coin in chess game
                initial_move = steps # steps to move towards south
                final_move = 3-steps # steps to move towards west
                if x-initial_move>0:
                    while(initial_move):
                        if (x-initial_move,y+final_move) in occupied_positions:
                            if final_move:
                                final_move -= 1 # 1 step towards west
                            else:
                                initial_move -= 1 # 1 step towards south
                        else:
                            x += initial_move
                            y -= final_move
                            break
                else: 
                    return invalid_move_message
            else: # to move diagonally
                if (y-steps>0):
                    while(steps):
                        if (x-steps,y+steps) in occupied_positions:
                            steps -= 1 # 1 step towards south-west
                        else:
                            x -= steps
                            y += steps
                            break
                else:
                    return invalid_move_message
        elif direction == "NW":
            if is_horse_move: # to mpve like a horse coin in chess game
                initial_move = steps # steps to move towards south
                final_move = 3-steps # steps to move towards west
                if x-initial_move>0 and y-final_move>0:
                    while(initial_move):
                        if (x-initial_move,y-final_move) in occupied_positions:
                            if final_move:
                                final_move -= 1 # 1 step towards east
                            else:
                                initial_move -= 1 # 1 step towards south
                        else:
                            x -= initial_move
                            y -= final_move
                            break
                else: 
                    return invalid_move_message
            else: # to move diagonally
                if (y-steps>0):
                    while(steps):
                        if (x-steps,y-steps) in occupied_positions:
                            steps -= 1 # 1 step towards south-east
                        else:
                            x -= steps
                            y -= steps
                            break
                else:
                    return invalid_move_message
        self.position = (x, y)
        return f"Robot with ID {self.robot_id} is moved successfully!!!."