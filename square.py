import numpy as np
def check_square(grid_input,sum_to_add):
    data, subgrid_size, grid_size = grid_input
    x = 0
    for x in range(grid_size):

        for y in range(grid_size):

            squarelist = []
            for i in np.arange(subgrid_size):
                
                for j  in np.arange(subgrid_size):

                    datapoint = data[i+x*subgrid_size][j+y*subgrid_size]
                    #print(datapoint)
                    #print(i,j)
                    squarelist.append(datapoint)
            if (sum(squarelist) != sum_to_add) or (len(squarelist) != len(set(squarelist))):
                return False
    return True
            
#used for testing grids.
if __name__ == '__main__':
    grid1 = [
		[1, 2, 3, 4],
		[5, 6, 7, 8],
		[9, 10, 11, 12],
		[13, 14, 15, 16]]
    grid4 = [
		[1, 3, 4, 2],
		[4, 2, 1, 3],
		[2, 1, 3, 4],
		[3, 4, 2, 1]]
    grid_input = (grid1,2,2)
    grid_input = (grid4, 2, 2)
    print(check_square(grid_input,10))