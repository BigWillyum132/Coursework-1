data1 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
dims = 3
def transpose(data,dims):
    biglist = []
    final_list = []
    for i in data:
        for j in i:
            biglist.append(j)
    for i in range(dims):
        print(i)
        final_list[i] = [biglist[i]]
        
    
    
if __name__ == '__main__':
    transpose(data1,dims)