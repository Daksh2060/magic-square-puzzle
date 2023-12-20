import systemImages
import createImages

# Constants for board size and value range
BOARD_SIZE_MIN = 1
BOARD_SIZE_MAX = 5
VALUE_MIN = -9
VALUE_MAX = 9

# Function reads board data from a CSV file
def read_board(file_path):
    
    #Load board data into an array and return
    with open(file_path) as file:
        size = int(file.readline().split(',')[0])
        data = [line.split(',') for line in file]
    return size, data


# Function initializes RGB dictionary for color coding based on CSV file
def initialize_rgb_dict(file):
    
    rgb_dict = {}

    # Skip the header line
    next(file)

    for value in file:
        datalist = value.split(",")
        
        # Skip invalid data entries
        if len(datalist) != 4:
            continue

        key = int(datalist[0])
        rgb_dict[key] = [int(datalist[1]), int(datalist[2]), int(datalist[3])]

        # Create inverse colors for non-zero values
        if key != 0:
            rgb_dict[-key] = [255 - int(datalist[1]), 255 - int(datalist[2]), 255 - int(datalist[3])]

    return rgb_dict


# Function creates an initial game board from the provided data
def create_initial_board(board_data):
    
    numbers = []
    for data in board_data:
        datalist = [int(num) for num in data]
        numbers.append(datalist)
    return numbers


# Function displays the current player board in terminal
def display_board(columns, numbers):
    
    #Add a line break to clarity
    print("=" * 100 + "\n")
    print(" " * 8, end="")
    
    #Print labels for both column and row sums
    for column in columns:
        print("{:>13}".format(column), end="")
    print("{:>11}".format("Sum") + "\n"*2)

    # Print out grid based on current game values, columns to be added in main
    for i, row in enumerate(numbers):
        print("Row {}".format(i), end="")
        for value in row:
            print("{:>13}".format(str(value).strip("\n")), end="")
        print("{:>13}".format(sum(row)))
        print("\n")

    print("Sum" + " " * 2, end="")
    for i in range(len(numbers[0])):
        print("{:>13}".format(sum(row[i] for row in numbers)), end="")
    print("\n")


# Function to check is the player has won
def win_check(lst):
    # Check if the sum of a list is zero, indicating a win
    return sum(lst) == 0


# main initiates gameplay 
def main():

    # Get player's name
    name = input("Please enter your name: ").strip("!.,?><")
    print("\n" + f"Welcome to the 'Colourful Zero' game {name}!" + "\n")

    play_again = True
    end_game = False
    games_won = 0
    total_score = 0
    game_number = 1

    while play_again:
        # Choose a game board
        board_choice = input("Please choose a board (1-5): ")
        print("\n")
        while not board_choice.isdigit() or not BOARD_SIZE_MIN <= int(board_choice) <= BOARD_SIZE_MAX:
            board_choice = input("Please enter a board between 1 and 5: ")
            print("\n")

        # Read board data from file
        size, board_data = read_board(f"./boards/board{board_choice}.csv")
        columns = [f"Col {i}" for i in range(size)]

        numbers = create_initial_board(board_data)

        turns = size**2 // 2
        win = False
        score = 0

        while turns > 0:
            # Display the game board and ask for player input
            display_board(columns, numbers)
            print("Turns Remaining: {}\n".format(turns))

            change_row = int(input("(0 - {}) Row?: ".format(size - 1)))
            change_col = int(input("(0 - {}) Column?: ".format(size - 1)))
            change_value = int(input("(-9 - 9) Value?: "))

            # Validate player input
            if change_row not in range(size) or change_col not in range(size) or change_value not in range(VALUE_MIN, VALUE_MAX + 1):
                break

            # Update the game board
            numbers[change_row][change_col] = change_value

            # Check for a win
            if win_check([row[change_col] for row in numbers]) and win_check(numbers[change_row]):
                score += 10
                win = True
                break

            turns -= 1

        print("\nYou've used up all your turns. The final board is:\n")
        display_board(columns, numbers)

        # Check for wins in rows and columns
        for i in range(size):
            if win_check([row[i] for row in numbers]):
                score += 1
            if win_check(numbers[i]):
                score += 1

        total_score += score

        # Display game outcome
        if win:
            print(f"Congratulations {name}! You won! Your score was: {score}")
            games_won += 1
        else:
            print(f"Looks like you lost this game, {name}. You got {score} points.")

        # Create custom images based on the game board
        diagonal = [numbers[i][i] for i in range(size)]
        canvas_board = systemImages.getBlackImage(100 * size, 100 * size)
        canvas_diag = systemImages.getBlackImage(100, 100 * size)

        # Generate and save images to current directory
        createImages.color_board(canvas_board, numbers, initialize_rgb_dict(open("./colorcoding.csv")))
        createImages.color_diag(canvas_diag, diagonal, initialize_rgb_dict(open("./colorcoding.csv")))
        systemImages.saveImage(canvas_board, f"boardimage{board_choice}-{game_number}.jpg")
        systemImages.saveImage(canvas_diag, f"diagimage{board_choice}-{game_number}.jpg")

        print("I saved 2 images based on this board for you!\n")

        # Ask if the player wants to play again
        continue_play = input("\nWould you like to play again? (Y/N)? ").lower().strip("!,.?")

        while continue_play not in {"y", "n"}:
            continue_play = input("Sorry, I don't get it, please enter 'Y' or 'N': ").lower().strip("!,.?")

        if continue_play == "n":
            play_again = False

        game_number += 1

    if not end_game:
        # Display total games won and total score
        print("\nYou won a total of {} games, with a total score of {}".format(games_won, total_score))
        print("\nThank you for playing, {}\n".format(name))

    input("Please press ENTER to exit")

if __name__ == "__main__":
    main()
