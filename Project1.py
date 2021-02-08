import doctest
def read_input(path: str):
    """
    Read game board file from path.
    Return list of str.
    """
    list_cows = []
    with open(path) as check:
        for i in check:
            list_cows.append(i)
    return list_cows

def left_to_right_check(input_line: str, pivot: int):
    """
    Check row-wise visibility from left to right.
    Return True if number of building from the left-most hint is visible looking to the right,
    False otherwise.

    input_line - representing board row.
    pivot - number on the left-most hint of the input_line.

    >>> left_to_right_check("412453*", 4)
    True
    >>> left_to_right_check("452453*", 5)
    False
    """
    new_list = []
    for i in range(1, len(input_line)):
        if input_line[i] != '*' and len(new_list) <= 5:
            new_list.append(int(input_line[i]))
    step_number = new_list[0]
    str_numbers = ''
    for i in range(1, len(new_list)):
        if str(step_number) not in str_numbers:
            str_numbers = str_numbers + str(step_number)
        if step_number < new_list[i]:
            str_numbers = str_numbers + str(new_list[i])
            step_number = new_list[i]
    count = len(str_numbers)  
    if count < pivot:
        return False
    return True
def check_not_finished_board(board: list):
    """
    Check if skyscraper board is not finished, i.e., '?' present on the game board.

    Return True if finished, False otherwise.

    >>> check_not_finished_board(['***21**', '4?????*', '4?????*', '*?????5', '*?????*', '*?????*', '*2*1***'])
    False
    >>> check_not_finished_board(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_not_finished_board(['***21**', '412453*', '423145*', '*5?3215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == '?':
                return False
    return True

def check_uniqueness_in_rows(board: list):
    """
    Check buildings of unique height in each row.

    Return True if buildings in a row have unique length, False otherwise.

    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True                         
    >>> check_uniqueness_in_rows(['***21**', '452453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*', '*543215', '*35214*', '441532*', '*22222*'])
    False
    """
    
    for i in range(1, len(board) - 1):
        board[i] = board[i][1:]
        board[i] = board[i][:5]
        for j in range(len(board[i])):
            if board[i][j] != '*' and board[i].count(board[i][j]) > 1:
                return False
    return True
def check_horizontal_visibility(board: list):
    """
    Check row-wise visibility (left-right and vice versa)

    Return True if all horizontal hints are satisfiable,
     i.e., for line 412453* , hint is 4, and 1245 are the four buildings
      that could be observed from the hint looking to the right.

    >>> check_horizontal_visibility(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_horizontal_visibility(['***21**', '452453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    >>> check_horizontal_visibility(['***21**', '452413*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    vers_board = []
    for row in board:
        vers_board.append(row[::-1])
    for row in board:
        if row[0] != '*':
            if left_to_right_check(row, int(row[0])) == False:
                return False
    for row in vers_board:
        if row[0] != '*':
            if left_to_right_check(row, int(row[0])) == False:
                return False
    return True
def check_columns(board: list):
    """
    Check column-wise compliance of the board for uniqueness (buildings of unique height) and visibility (top-bottom and vice versa).

    Same as for horizontal cases, but aggregated in one function for vertical case, i.e. columns.

    >>> check_columns(['***21**', '412453*', '423145*', '*543215',\
    '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_columns(['***21**', '412453*', '423145*', '*543215',\
    '*35214*', '*41232*', '*2*1***'])
    False
    >>> check_columns(['***21**', '412553*', '423145*', '*543215',\
    '*35214*', '*41532*', '*2*1***'])
    False
    """
    top_down_board = []
    for i in range(1, 6):
        new_str = ''
        for j in range(7):
            new_str = new_str + board[j][i]
        top_down_board.append(new_str)
    for row in top_down_board:
        row = row[1:]
        row = row[:5]
        if len(set(row)) != len(row):
            return False
    down_top_board = []
    for row in top_down_board:
        down_top_board.append(row[::-1])
    for row in top_down_board:
        if row[0] != '*':
            if left_to_right_check(row, int(row[0])) == False:
                return False
    for row in down_top_board:
        if row[0] != '*':
            if left_to_right_check(row, int(row[0])) == False:
                return False
    return True, top_down_board
print(check_columns(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***']))
def check_skyscrapers(input_path: str):
    """
    Main function to check the status of skyscraper game board.
    Return True if the board status is compliant with the rules,
    False otherwise.
    """
    if check_not_finished_board(read_input(input_path)) == True:
        if check_uniqueness_in_rows(read_input(input_path)) == True:
            if check_horizontal_visibility(read_input(input_path)) == True:
                if check_columns(read_input(input_path)) == True:
                    return True
    return False
#doctest.testmod()

