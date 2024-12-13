#student name: Weifeng Ke 
#student number: 18879288

def checkColumn(puzzle: list, column: int) -> None:
    """ 
        param puzzle: a list of lists containing the puzzle 
        param column: the column to check (a value between 0 to 8)

        This function checks the indicated column of the puzzle, and 
        prints whether it is valid or not. 
        
        As usual, this function must not mutate puzzle 
    """
    my_col_list=[]
    pass_list=list(range(1,10))
    # Iterate through each row to collect elements of the column range(9)(aka 0-8)
    for i in range(9):
        my_col_list.append(puzzle[i][column])
    
    #check if the sorted my_col_list matches the pass list of 1-9
    if sorted(my_col_list) == pass_list:
        print(f"Column {column} valid")    #if match print valid
    else:                                   #if not match print not valid
        print(f"Column {column} not valid")

def checkRow(puzzle: list, row: int) -> None:
    """ 
        param puzzle: a list of lists containing the puzzle 
        param row: the row to check (a value between 0 to 8)

        This function checks the indicated row of the puzzle, and 
        prints whether it is valid or not. 
        
        As usual, this function must not mutate puzzle 
    """
    my_row_list=[]
    pass_list=list(range(1,10))
    # Iterate through each column to collect elements of the row in range(9)(aka 0-8)
    for i in range(9):
        my_row_list.append(puzzle[row][i])
    
    #check if the sorted my_row_list matches the pass list of 1-9
    if sorted(my_row_list) == pass_list:
        print(f"Row {row} valid")           #if match print valid
    else:                                   #if not match print not valid
        print(f"Row {row} not valid")

def checkSubgrid(puzzle: list, subgrid: int) -> None:
    """ 
        param puzzle: a list of lists containing the puzzle 
        param subgrid: the subgrid to check (a value between 0 to 8)
        Subgrid numbering order:    0 1 2
                                    3 4 5
                                    6 7 8
        where each subgrid itself is a 3x3 portion of the original list
        
        This function checks the indicated subgrid of the puzzle, and 
        prints whether it is valid or not. 
        
        As usual, this function must not mutate puzzle 
    """
    my_subgrid_list=[]
    pass_list=list(range(1,10))
    
    #Determine the top left corner of the subgrid
    row_num=subgrid//3      #calculate which 3 row block the subgrid is on
    col_num=subgrid % 3     #calculate which 3 col block the subgrid is on 
    
    #Iterate through the 3x3 subgrid
    for i in range(row_num*3,row_num*3+3):          #rows for the subgrid range(a,b) = a to b-1
        for j in range(col_num*3, col_num*3+3):     #cols for the subgrid range(a,b) = a to b-1
            my_subgrid_list.append(puzzle[i][j])    #append to my own my_subgrid_list
    
    #check if the sorted my_subgrid_list matches the pass list of 1-9
    if sorted(my_subgrid_list) == pass_list:    #if match print valid
        print(f"Subgrid {subgrid} valid")
    else:                                       #if not match print not valid
        print(f"Subgrid {subgrid} not valid")   
    

if __name__ == "__main__":
    test1 = [ [6, 2, 4, 5, 3, 9, 1, 8, 7],
              [5, 1, 9, 7, 2, 8, 6, 3, 4],
              [8, 3, 7, 6, 1, 4, 2, 9, 5],
              [1, 4, 3, 8, 6, 5, 7, 2, 9],
              [9, 5, 8, 2, 4, 7, 3, 6, 1],
              [7, 6, 2, 3, 9, 1, 4, 5, 8],
              [3, 7, 1, 9, 5, 6, 8, 4, 2],
              [4, 9, 6, 1, 8, 2, 5, 7, 3],
              [2, 8, 5, 4, 7, 3, 9, 1, 6]
            ]
    test2 = [ [6, 2, 4, 5, 3, 9 , 1, 8, 7],
              [5, 1, 9, 7, 2, 8, 6, 3, 4],
              [8, 3, 7, 6, 1, 4, 2, 9, 5 ],
              [6, 2, 4, 5, 3, 9 , 1, 8, 7],
              [5, 1, 9, 7, 2, 8, 6, 3, 4],
              [8, 3, 7, 6, 1, 4, 2, 9, 5 ],
              [6, 2, 4, 5, 3, 9 , 1, 8, 7],
              [5, 1, 9, 7, 2, 8, 6, 3, 4],
              [8, 3, 7, 6, 1, 4, 2, 9, 5 ]
            ]
    
    testcase = test2   #modify here for other testcases
    SIZE = 9

    for col in range(SIZE):  #checking all columns
        checkColumn(testcase, col)
    for row in range(SIZE):  #checking all rows
        checkRow(testcase, row)
    for subgrid in range(SIZE):   #checking all subgrids
        checkSubgrid(testcase, subgrid)