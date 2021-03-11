from django.shortcuts import render
from . import models

# Create your views here.
def sendbt(request):
    return render(request, './Models_Assignment/send.html')

def send(request):
    num = int(input("\nEnter The Number of Rows To Insert: "))
    for i in range(num):
        accno = int(input("\nAccount No.: "))
        cust_name = input("\nCustomer Name: ")
        loan_amount = float(input("\nLoan Amount: "))
        installments = int(input("\nInstallments: "))
        int_rate = float(input("\nInterest Rate: "))
        start_date = input("\nStart Date: ")
        interest = float(input("\nInterest: "))
        loanobj = models.Loan_Accounts(Accno=accno, Cust_name=cust_name, Loan_amount=loan_amount, Installments=installments, Int_rate=int_rate, Start_date=start_date, Interest=interest)
        loanobj.save()

    return render(request, './Models_Assignment/save.html')
