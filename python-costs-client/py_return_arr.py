def return_arr():
    sample_arr = ['apple','orange','banana']
    return sample_arr
    
 
 
compare = 'apple'
 
s_arr=return_arr()
 
if compare in s_arr:
    print("you can definitely return an aray from a function in python")
    print(compare)
else:
    print("hang on a second")