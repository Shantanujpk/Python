# Lets learn Dic methods

#1 Update: 

emp_details_infosys = {1:45,2:89,3:96,4:56}
emp_details_tcs = {5:45,6:68,7:98}

# i want to update tcs details to infosys how ? 

emp_details_infosys.update(emp_details_tcs)
print(emp_details_infosys)

emp_details_techM = {1:45,2:89,3:96,4:56,7:899}  # if both have same values it will update with new value , in this case it will update it 7 with 98 and will loose 899
emp_details_Del = {5:45,6:68,7:98}
emp_details_techM.update(emp_details_Del)
print(emp_details_techM)

# 2 clear (): will removes all the items from the list 
emp_details_techM.clear()
print(emp_details_techM)

# 3 pop : removes / pop key value pair whos key is passed 
emp_details_Del.pop(5) # it should pop 45
print(emp_details_Del) #{6: 68, 7: 98}

# 4 popitem , will remove the last key-value pair from the dic
emp_details_infosys.popitem()
print(emp_details_infosys) #7: 98 is popped 

# 5 Del : can also use del keyword to remove the item

del emp_details_infosys[1] # this will remove 1 entry
print (emp_details_infosys)