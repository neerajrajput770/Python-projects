
account = {
    "type" : "Bussiness account",
    "Account_number" : 7858021820,
    "name" : "Neeraj Singh",
    "blance" : 50000,
    "pin" : 7858
}

print("=====MINI ATM=====")

acc_no = int(input("Enter your account number..:"))

if acc_no == account["Account_number"]:
    pin = int(input("Enter your pin...:"))
    if pin == account["pin"]:
        while True:
            print("=====ATM MENU=====")
            print("1.Chak Blance.:")
            print("2.Deposite Blance.:")
            print("3.Withdrawl Blance.:")
            print("4.Account Details.:")
            print("5.Exit")

            choices = input("enter your choice...:")
            if choices == "1":
                print("Your Blance is",account["blance"])

            elif choices =="2":
                amount = int(input("Enter Deposite Amount..."))

                if amount > 0:
                    account["blance"] = account["blance"] + amount
                    print("Amount deposite Succesful",account["blance"])

                else:
                    print("INVALID BLANCE")

            elif choices == "3":
                amount = int(input("Enter Withdrawl blance..."))

                if amount <= 0:
                    print("Invalid amount")
                
                elif amount > account["blance"]:
                    print("Insuffient amount")
               
                else :
                    account["blance"] = account["Account_number"] - amount
                    print("WITHDRAWL SUCCESFULL...")
                    print("Current blance", account["blance"])

            elif choices == "4":
                print("\nACCOUNT NAME:", account["name"])
                print("\nACCOUNT NUMBER:", account["Account_number"])
                print("\nACCOUNT PIN :", account["pin"])
                print("\nACCOUNT BLANCE:", account["blance"])
                print("\nACCOUUNT TYPE:", account["type"])

            elif choices == "5":
                print("THANK YOU!")
                break
            

    else:
        print("INVALID PIN \n TRY AGAIN")
else:
    print("INVALID ACCOUNT NUMBER")