# 📘 Python match-case Statement (Introduced in Python 3.10+)
# Python does not have switch-case like other languages, so the 'match' statement was introduced in version 3.10
# It allows cleaner handling of multiple conditions (like switch-case in C, Java, etc.)

# 🔔 Note: This only works in Python 3.10 and above

# 🖥️ Taking input from user
x = int(input("Enter a number: "))

# 🧠 match behaves like switch
match x:
    # Case 0
    case 0:
        print("X is 0")
    
    # Case 1
    case 1:
        print("X is 1")
    
    # Case with condition (when x equals 90)
    case _ if x == 90:
        print("X is 90")

    # Another case with condition (when x equals 78)
    case _ if x == 78:
        print("X is 78")

    # Default case if none of the above match
    case _:
        print("Aahh!! Enter again !") 


# 🧠 Important Differences from Other Languages:

# In C or Java switch-case:
# switch(x) {
#    case 0:
#        printf("X is 0");
#        break;         // break needed to stop
#    case 1:
#        printf("X is 1");
#        break;
# }

# ✅ But in Python's match-case:
# No 'break' needed!
# Once a case is matched, Python automatically exits the match block.

# So here, if x == 90:
# Only "X is 90" will be printed, and no other case will run.
