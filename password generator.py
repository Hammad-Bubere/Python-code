#With help of this code you can generate 14 characters password

while True:
    import random
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers ="0123456789"
    symbols ="!#$%^&*()<>?{}[]\/;."
    all =lower+upper+numbers+symbols
    length = 14
    password ="".join (random.sample(all,length))
    print ("Your generated password is:\t",password)
    print("\nFor exit press '0' ,To contunie press '1'")
    option=(input("\nSelect option:\t"))
    if option=="0":
        print("\nprogramme Ended\nThans! for using our code")
        break
    elif option=="1":
        print("\nprogramme continued\n")
        continue
    else:
        print("You entered wrong option!!!\nProgramme continued\n")
        continue
    
        
