# Variant 9. Bottles of water
bottles = int(input("Enter the number of bottles:"))
student_val = input("Are you a student? yes/no: ")
pocket = int(input("Enter the money you have:"))



if student_val == "yes" :
    if bottles >= 8 :
        if pocket >= bottles*2:
            print(f"Price per bottle: {2} \n Total cost: {bottles*2}")        
            if pocket - bottles*2 == 0:
                print("Exactly enough money!")
            else :
                print(f"Money left: {pocket - bottles*2}")
        else :
            print(f"Price per bottle: {2} \n Total cost: {bottles*2}")        
            print(f"More monet needed: {bottles*2 - pocket}")
            
    else : 
        if pocket >= bottles*4:
            print(f"Price per bottle: {4} \n Total cost: {bottles*4}")        
            if pocket - bottles*4 == 0:
                print("Exactly enough money!")
            else :
                print(f"Money left: {pocket - bottles*4}")
        else :
            print(f"Price per bottle: {4} \n Total cost: {bottles*4}")        
            print(f"More monet needed: {bottles*4 - pocket}")

elif student_val == "no" :
    if bottles >= 8 :
        if pocket >= bottles*4:
            print(f"Price per bottle: {4} \n Total cost: {bottles*4}")        
            if pocket - bottles*4 == 0:
                print("Exactly enough money!")
            else :
                print(f"Money left: {pocket - bottles*4}")
        else :
            print(f"Price per bottle: {4} \n Total cost: {bottles*4}")        
            print(f"More monet needed: {bottles*4 - pocket}")

    else : 
        if pocket >= bottles*6:
            print(f"Price per bottle: {6} \n Total cost: {bottles*6}")        
            if pocket - bottles*6 == 0:
                print("Exactly enough money!")
            else :
                print(f"Money left: {pocket - bottles*6}")
        else :
            print(f"Price per bottle: {6} \n Total cost: {bottles*6}")        
            print(f"More monet needed: {bottles*6 - pocket}")


