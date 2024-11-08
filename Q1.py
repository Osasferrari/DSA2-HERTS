import matplotlib.pyplot as plt
import numpy as np
import random
from PIL import Image

# initialize maze image then convert it to a binary grid
def load_maze_image(filepath):
    image = Image.open(filepath).convert("L")  # Change image to black and white
    binary_maze = np.array(image) < 128        # convert to binary where True means path & False means wall
    return binary_maze.astype(int)             # Convert to int: 1 = path, 0 = wall

# Create solution algorithms
class MazeSolver:
    def __init__(self, maze):
        self.maze = maze
        self.start = (0, maze[0].argmax())  # Assuming the entrance is at the top
        self.end = (len(maze) - 1, maze[-1].argmax())  # Assuming the exit is at the bottom
        self.visited = set()  # Track all visited cells for visualization

    # creating loops (backtracking approach)
    def solve_backtracking(self):
        stack = [self.start]
        self.visited = set()  # Track all visited cells for visualization

        while stack:
            position = stack.pop()
            if position == self.end:
                return True  # Solution found

            x, y = position
            self.visited.add(position)  # Mark this cell as visited

            # Explore paths in directions- up,down,left,right
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx, ny = x + dx, y + dy
                # Check its a deadend, if it's a path, and if it hasn't been visited
                if (0 <= nx < self.maze.shape[0] and 0 <= ny < self.maze.shape[1]
                    and self.maze[nx, ny] == 1 and (nx, ny) not in self.visited):
                    stack.append((nx, ny))
        return False  # if no path is found

    # Las Vegas algorithm: randomly tries paths until it finds a solution or reaches a step limit
    def solve_las_vegas(self, max_steps=400):
        position = self.start
        self.visited = set()  # Track all visited cells for visualization

        for _ in range(max_steps):  # Limit steps to prevent infinite loops
            if position == self.end:
                return True  # Solution found
            self.visited.add(position)

            # Get all possible valid directions
            x, y = position
            directions = [(x + dx, y + dy) for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]
                          if 0 <= x + dx < self.maze.shape[0]
                          and 0 <= y + dy < self.maze.shape[1]
                          and self.maze[x + dx, y + dy] == 1
                          and (x + dx, y + dy) not in self.visited]
            
            if directions:
                # Pick a random valid direction
                position = random.choice(directions)
            else:
                break  # No valid moves left, end this run
        return False  # Failed to reach the end within max_steps

# Run simulations for each algorithm
def run_simulations(maze, runs=10000):
    backtracking_success = 0
    las_vegas_success = 0
    solver = MazeSolver(maze)
    
    # Run backtracking algorithm
    for _ in range(runs):
        if solver.solve_backtracking():
            backtracking_success += 1

    # Run Las Vegas algorithm
    for _ in range(runs):
        if solver.solve_las_vegas():
            las_vegas_success += 1

    # Calculate success rates
    backtracking_rate = (backtracking_success / runs) * 100
    las_vegas_rate = (las_vegas_success / runs) * 100

    print("Backtracking Success Rate:", backtracking_rate, "%")
    print("Las Vegas Success Rate:", las_vegas_rate, "%")



# Visualize the solution path
def visualize_path(maze, visited_positions):
    maze_image = np.copy(maze)
    for x, y in visited_positions:
        maze_image[x, y] = 2  # Mark visited squares
    plt.imshow(maze_image, cmap='grey')
    plt.show()

# Main logic to run the selected algorithm
def main():
    maze_filepath = "/Users/osasferrari/Downloads/maze-2.png"  
    maze = load_maze_image(maze_filepath)

    print("Choose the algorithm: \n1. Backtracking\n2. Las Vegas")
    choice = input("Enter 1 or 2: ")

    solver = MazeSolver(maze)

    if choice == '1':
        success = solver.solve_backtracking()
        print("Backtracking Result:", "Success" if success else "Failed")
    elif choice == '2':
        success = solver.solve_las_vegas()
        print("Las Vegas Result:", "Success" if success else "Failed")
    else:
        print("Invalid choice.")
        return

    # Visualize all visited squares
    visualize_path(maze, solver.visited)

if __name__ == "__main__":
    main()
