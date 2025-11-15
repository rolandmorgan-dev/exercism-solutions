# Function to find the potential trees to build a tree house
def saddle_points(matrix : list):
    # irregular matrix check
    if any(len(matrix[0]) != len(i) for i in matrix):
        raise ValueError("irregular matrix")
    
    # declaring list variables for tracking the results
    lowest_col, result, = [], []

    # finding the lowest value in each column
    for col_idx, column in enumerate(zip(*matrix)):
        lowest_col.append((col_idx,min(column)))
        
    # finding the largest in row
    for r_idx, row in enumerate(matrix):
        row_max = max(row)
        
        # checking if a column's lowest is also the largest in the row
        for c_idx in range(len(row)):
            if lowest_col[c_idx][1] == row_max:
                result.append({"row": r_idx+1, "column": c_idx+1})
                
    return result
