import random
from datetime import datetime 
class Admin:
    User = [] 
    total_balance = []
    total_loan = [] 
    loan_transaction = [] 
    def __init__(self,name,email,account_type) -> None:
        self.name = name
        self.email = email 
        self.account_type = account_type 
        self.Password = 123

    def show_user_list(self):
        for user in self.User:
            print(f'Name: {user.name} Email: {user.email} Account_No.- {user.acc_no} total_balace:{user.deposit}' ) 
    def delete_user_account(self,ac_no):
        x = 0
        for i,user in enumerate(self.User):
            if user.acc_no == ac_no:
                x = 1
                del self.User[i]
        if x == 1:
            return f'\nACCOUNT NO. {ac_no} is deleted.'
        else:
            return f'\n ACCOUNT DOES NOT EXIST.'
  
    def check_total_Bank_balnc(self):
        s = 0
        t = 0
        for user in self.User:
            t+=user.deposit 
        if len(self.total_loan):
           
            for loan in self.total_loan:
                s +=loan
            
        return t-s-s
       
    def take_loan(self):
        ACC = int(input('Type YOUR ACCOUNT NO. '))
        loan = int(input('Type the amount of loan: '))
        if loan > 20000 or loan < 500:
            print(f'\nSORRY. You can not take LOAN more than 20000taka and less than 500taka') 
        else:
            x = True
            if self.check_total_Bank_balnc() > loan:
                for user in self.User:
                    if user.acc_no == ACC:
                        x = False
                        if user.loan_limit !=0:
                            user.deposit = loan 
                            print(f'\n{user.name} with ACC NO. {user.acc_no} have taken {loan}/- taka loan')
                            self.total_loan.append(loan) 
                            user.loan_limit-=1 
                            self.loan_transaction.append(f'Name: {user.name} taken loan {loan}/-taka DateTime: {datetime.now()}') 
                        else:
                            print(f'\nSORRY. You can\'t take loan more than two times.\n')
                if(x):
                    print(f'\nACCOUNT DOES NOT EXIST.\n')

            else:
                print(f'\nTHIS BANK IS BANKRUPT.\n')        
        
    def Loan_transaction(self):
        L = len(self.loan_transaction)
        if L != 0:
            for loan_transaction in self.loan_transaction:
                print(f'\n{loan_transaction}')
        else:
            print(f'\nNo LOAN transaction YET.\n') 
    def total_loan_given (self):
        s = 0
        for loan in self.total_loan:
            s+=loan 
        return s

    
    def Available_balance(self): 
        pass

                

    def __repr__(self) -> str:
        return f'\nAn ADMIN account was created with Password 123.\n'
    
                
       

    
         
 
class User(Admin):
    def __init__(self,name,email,account_type) -> None: 
        self.__balance = 0  
        self.acc_no = random.randint(400, 679) 
        self.transaction = []
        self.User.append(self)
        self.loan_limit = 2
        super().__init__(name,email,account_type)
        

    @property
    def deposit(self):
        return self.__balance 
    
    @deposit.setter
    def deposit(self,amount):
        if amount < 100:
            print(f'Sorry. You can\'t deposit below 100 taka. Thanks.')
        else:
            self.__balance += amount 
            # self.total_balance +=amount
            self.transaction.append(f'DEPOSIT: {amount}/- taka. {datetime.now()}') 
            # print(f'\nYou have DEPOSITED {amount}/- taka')


    @property
    def withdraw(self):
        return self.__balance
    @withdraw.setter
    def withdraw(self,amount):
        if self.check_total_Bank_balnc() == 0:
            print('\nBank is BANKRUPT\n')
        elif amount < 500:
            print(f'\nYou have to withdraw minimum 500taka. Thanks.')
        elif(amount >self.__balance):
            print(f'\nWithdrawal amount exceeded')
        else:
            self.__balance -= amount 
            # self.total_balance -= amount
            self.transaction.append(f'WITHDRAW: {amount}/- taka. {datetime.now()}') 
            #print(f'\nYou have withdrawn {amount}/- taka')

    def check_transaction(self):
        # T = int(input('TYPE ACCOUNT NO. '))
        
        L = len(self.transaction)
        if L!=0:
            for transactions in self.transaction:
                 print(f'\n{transactions}') 
        else:
            print(f'\nNo transaction YET.\n')  
        


        

    def transfer_money(self):  
        my_Acc = int(input('Type Sender ACCOUNT NO. '))
        transfer = int(input('Type how much do you wanna transfer?  ')) 
        if transfer > 500:

            AccNo = int(input('Type the receiver ACCOUNT NO. ')) 
            x = True
            y = 0
            t = 0
            for user in self.User:
                if user.acc_no == my_Acc: 
                    t = 1
                    if user.deposit > transfer:
                        user.withdraw = transfer
                    else:
                        y = 1
                        print(f'\nYou don\'t have sufficient balance.')
            if y == 0:
                for user in self.User:
                    if user.acc_no == AccNo:
                        x = False
                        user.deposit = transfer
                        print(f'{transfer}/- taka has transferred from Account number {my_Acc} to {AccNo}')
            if x == True or t == 0:
                print(f'\nACCOUNT does not exist.')
                for user in self.User:
                    if user.acc_no == my_Acc:
                        user.deposit = transfer 
        else:
            print(f'\nYOU HAVE TO TRANSFER MORE THAN 500/- TAKA ONLY.')
        
    def Check_available_blnc(self):
        test = int(input('Type your ACCOUNT NO. '))
        x = 1
        for user in self.User:
            if user.acc_no == test:
                x = 0
                print(f'\n{user.name} YOUR CURRENT BALALNCE IS {user.deposit}/-TAKA ONLY.') 
        if(x):
            print('\nACCOUNT DOES NOT EXIST.')

                 

    def __repr__(self) -> str:
        return f'\nA USER account was created with ACCOUNT NO.{self.acc_no}\n'
            
        




    
Fahim = User('Fahim','abdulkaderfahim6@gmail.com','savings')
Karim = User('Jarin','Jarin223@gmail.com','savings')
Jamil = User('Ovi','ovi@gmail.com','CUREENT')
Fahim.deposit = 10000
Karim.deposit = 20000
Jamil.deposit = 300 


testUser = User('Abdul Kader','abdulkader15@gmail.com','Savings')
testAdmin = Admin('Fahim','abdulkaderfahim6@gmail.com','Savings')
while True: 
    print(f'\n1. Create an ADMIN and explore ADMIN features\n2. Create a USER and explore USER features\n3. EXIT')
    op = int(input('ENTER option: ')) 
    if op == 1:
        print(testAdmin) 
        while True:
            print(f'\n1. Show all user ACCOUNT\n2. Delete any user account\n3. Check the total BANK balance\n4. Check the total LOAN of the BANK\n5. See Loan Transaction\n6. GO TO THE PREVIOUS MENU')
            take_o = int(input('ENTER AN OPTION '))
            if take_o == 1:
                chk = int(input('TYPE ADMIN PASSWORD '))
                if chk == testAdmin.Password:
                    testAdmin.show_user_list()
            elif take_o == 2:
                chk = int(input('TYPE ADMIN PASSWORD '))
                if chk == testAdmin.Password:
                    DL = int(input('TYPE the USER ACCOUNT NO. '))
                    print(testAdmin.delete_user_account(DL)) 
            elif take_o == 3:
                chk = int(input('TYPE ADMIN PASSWORD '))
                if chk == testAdmin.Password:
                    print(f'\n{testAdmin.check_total_Bank_balnc()}/- taka only.\n') 
            elif take_o == 4: 
                chk = int(input('TYPE ADMIN PASSWORD '))
                if chk == testAdmin.Password:
                    print(f'\n{testAdmin.total_loan_given()}/- taka only.')
            elif take_o == 5:
                chk = int(input('TYPE ADMIN PASSWORD '))
                if chk == testAdmin.Password:
                    testAdmin.Loan_transaction()
            else: 
                break
    elif op == 2:
        print(testUser)
        while True:
            print(f'\n1. Check the available balance\n2. Check transaction history\n3. Transfer money to another account\n4. Take loan from the BANK\n5. Deposit money\n6. Withdraw money\n7. GO TO THE PREVIOUS MENU\n')
            take_op = int(input('ENTER AN OPTION '))
            if take_op == 1:
                testUser.Check_available_blnc()
            elif take_op == 2:
                T = int(input('TYPE YOUR ACCOUNT NUMBER '))
                f = 0
                for user in testAdmin.User:
                     if user.acc_no == T:
                         f = 1
                         user.check_transaction()
                if f == 0:
                    print(f'\nACCOUNT DOES NOT EXIST.')
            elif take_op == 3:
                testUser.transfer_money() 
            elif take_op == 4:
                testUser.take_loan() 
            elif take_op == 5:
                id = int(input('TYPE THE ACCOUNT NUMBER: ')) 
                flag = 0
                for user in testAdmin.User:
                    if id == user.acc_no:
                        flag =1
                        D = int(input('How much money do you want to DEPOSIT: '))
                        user.deposit = D 
                if flag == 0:
                    print(f'\nACCOUNT DOES NOT EXIST.') 
                else:
                    print(f'\nYou have DEPOSITED {D}/- taka.')
            elif take_op == 6:
                id = int(input('TYPE THE ACCOUNT NUMBER: ')) 
                flag = 0
                for user in testAdmin.User:
                    
                    if id == user.acc_no:
                        flag =1
                        W = int(input('How much money do you want to WITHDRAW: '))
                        user.withdraw = W 
                if flag == 0:
                    print(f'\nACCOUNT DOES NOT EXIST.') 
                
            else:
                break


                
    else:
        break 


        
