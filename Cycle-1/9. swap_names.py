print('\nTo create a single string separated with space from two strings by swapping the character at position 1.')
name1='Hello'
name2='All'
print('\nFirst name: ',name1)
print('\nSecond name: ',name2)
new_name1=name2[0]+name1[1:]
new_name2=name1[0]+name2[1:]
name=new_name1+' '+new_name2
print('\nResultant new string: ',name,'\n')