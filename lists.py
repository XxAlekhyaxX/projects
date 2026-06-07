Introduction to 2D lists 
"""
board = [[1,2,3],[4,5,6],[7,8,9]] # 2D list 
# print(board[0])
# print(board[1])
# print(board[2])
# print(board[2][2])
# print(board[1][2])
# print(board[0][0])
"""
0,0 0,1 0,2 
1,0 1,1 1,2 
2,0 2,1 2,2 
which ever index changes frequently first it needs to be in the 
inner loop ( column index)
"""
# for row in range(3):
#     for col in range(3):
#         print(board[row][col],end=" ")
#     print()

for row in board:
    for element in row: 
        print(element,end=" ")
    print()
