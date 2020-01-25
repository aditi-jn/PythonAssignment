ls_square = [[4, 9, 2],
             [3, 5, 7],
             [8, 1, 6]]
square = [0, 0, 0], [0, 0, 0], [0, 0, 0]
def inp_square():
    for r in range(0, 3):
        for c in range(0, 3):
            square[r][c] = int(input("Enter row " + str(r) + " column " + str(c)))
    return square
def determine_lo_shu(td_list):
    row_0 = td_list[0][0] + td_list[0][1] + td_list[0][2]
    row_1 = td_list[1][0] + td_list[1][1] + td_list[1][2]
    row_2 = td_list[2][0] + td_list[2][1] + td_list[2][2]
    col_0 = td_list[0][0] + td_list[1][0] + td_list[2][0]
    col_1 = td_list[0][1] + td_list[1][1] + td_list[2][1]
    col_2 = td_list[0][2] + td_list[1][2] + td_list[2][2]
    diag_up = td_list[2][0] + td_list[1][1] + td_list[0][2]
    diag_down = td_list[0][0] + td_list[1][1] + td_list[2][2]
    if row_0 == row_1 and row_0 == row_2 and row_0 == col_0 and row_0 == col_1 and row_0 == col_2 and row_0 == diag_up and row_0 == diag_down:
        print("This is a Lu Shu Magic Square!")
    else:
        print("This is not a Lu Shu Magic Square")
determine_lo_shu(inp_square())