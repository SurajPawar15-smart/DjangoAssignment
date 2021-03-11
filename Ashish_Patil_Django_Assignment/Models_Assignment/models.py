from django.db import models

# Create your models here.
class Loan_Accounts(models.Model):
    Accno = models.IntegerField(blank=False, null=False)
    Cust_name = models.CharField(max_length=20, blank=False, null=False)
    Loan_amount = models.FloatField(blank=False, null=False)
    Installments = models.IntegerField(blank=False, null=False)
    Int_rate = models.FloatField(blank=False, null=False)
    Start_date = models.DateField(blank=False, null=False)
    Interest = models.FloatField(blank=False, null=False)




# Output

# In [1]: from Models_Assignment.models import *

# In [2]: loan = Loan_Accounts.objects.all()

# In [3]: loan
# Out[3]: <QuerySet [<Loan_Accounts: Loan_Accounts object (1)>, <Loan_Accounts: Loan_Accounts object (2)>, <Loan_Accounts: Loan_Accounts object (3)>, <Loan_Accounts: Loan_Accounts object (4)>, <Loan_Accounts: Loan_Accounts object (5)>, <Loan_Accounts: Loan_Accounts object (6)>, <Loan_Accounts: Loan_Accounts object (7)>, <Loan_Accounts: Loan_Accounts object (8)>, <Loan_Accounts: Loan_Accounts object (9)>, <Loan_Accounts: Loan_Accounts object (10)>]>

# In [4]: for loan in loans:
#    ...:     print(loan.Accno," ", loan.Cust_name, " ", loan.Loan_amount)

# Accno | Cust_name | Loan_amount
# 1987291882   John   1000000.0
# 19872916732   Roman   200000000.0
# 8798173716   Dean   300000000.0
# 1276187198   Seth   4000000000.0
# 1273892728   Emma   500000.0
# 21673179779   Harry   6000000.0
# 7189739128   Jack   2500000.0
# 1829127878   Will   450000000.0
# 13619219865   Jake   15000000.0
# 184189712   Karen   600000000.0

# In [5]: for loan in loans:
#    ...:     if loan.Installments < 40:
#    ...:         print(f"{loan.Accno} | {loan.Cust_name} | {loan.Loan_amount} | {loan.Installments} | {loan.Int_rate} | {loan.Start_date} | {loan.Interest}")

# Accno | Cust_name | Loan_amount | Installments | Int_rate | Start_date | Interest
# 1987291882 | John | 1000000.0 | 10 | 5.6 | 2020-02-22 | 1000.0
# 19872916732 | Roman | 200000000.0 | 15 | 6.5 | 2020-04-25 | 1200.0
# 8798173716 | Dean | 300000000.0 | 20 | 8.8 | 2020-01-14 | 1300.0
# 1273892728 | Emma | 500000.0 | 5 | 5.5 | 2020-05-15 | 100.0
# 21673179779 | Harry | 6000000.0 | 6 | 6.6 | 2020-06-16 | 160.0
# 7189739128 | Jack | 2500000.0 | 8 | 6.8 | 2020-08-18 | 180.0
# 1829127878 | Will | 450000000.0 | 12 | 5.4 | 2020-10-08 | 180.0

# In [6]: for loan in loans:
#     ...:     if int(str(loan.Start_date)[0:4]) < 2009:
#     ...:         print(loan.Accno, " ", loan.Loan_amount)
#     ...: 
#     ...:     elif int(str(loan.Start_date)[0:4]) < 2009 and int(str(loan.Start_date)[5:7]) < 4:
#     ...:         print(loan.Accno, " ", loan.Loan_amount)
#     ...: 

# Accno | Loan_amount
# 13619219865 | 15000000.0
# 184189712 | 600000000.0

# In [7]: for loan in loans:
#     ...:     if int(str(loan.Start_date)[0:4]) > 2009:
#     ...:         print(loan.Int_rate)
#     ...: 
#     ...:     elif int(str(loan.Start_date)[0:4]) >= 2009 and int(str(loan.Start_date)[5:7]) > 4:
#     ...:         print(loan.Int_rate)

# Int_rate
# 5.6
# 6.5
# 8.8
# 8.6
# 5.5
# 6.6
# 6.8
# 5.4

# In [8]: for loan in loans:
#     ...:     if str(loan.Int_rate).lower() == 'null':
#     ...:         print(f"{loan.Accno} | {loan.Cust_name} | {loan.Loan_amount} | {loan.Installments} | {loan.Int_rate} | {loan.Start_date} | {loan.Interest}")

# No Data 

# In [9]: for loan in loans:
#    ...:     if loan.Installments != 36:
#    ...:         print(f"{loan.Cust_name} | {loan.Loan_amount}")

# Cust_name | Loan_amount
# John | 1000000.0
# Roman | 200000000.0
# Dean | 300000000.0
# Seth | 4000000000.0
# Emma | 500000.0
# Harry | 6000000.0
# Jack | 2500000.0
# Will | 450000000.0
# Jake | 15000000.0
# Karen | 600000000.0 

# In [10]: for loan in loans:
#    ...:     if loan.Loan_amount > 500000 and loan.Int_rate > 8:
#    ...:         print(f"{loan.Cust_name} | {loan.Loan_amount}")

# Cust_name | Loan_amount
# Dean | 300000000.0
# Seth | 4000000000.0
# Karen | 600000000.0

# In [11]: for loan in loans:
#    ...:     if 6 <= loan.Int_rate < 8:
#    ...:         print(f"{loan.Accno} | {loan.Cust_name} | {loan.Loan_amount} | {loan.Installments} | {loan.Int_rate} | {loan.Start_date} | {loan.Interest}")

# Accno | Cust_name | Loan_amount | Installments | Int_rate | Start_date | Interest 
# 19872916732 | Roman | 200000000.0 | 15 | 6.5 | 2020-04-25 | 1200.0
# 21673179779 | Harry | 6000000.0 | 6 | 6.6 | 2020-06-16 | 160.0
# 7189739128 | Jack | 2500000.0 | 8 | 6.8 | 2020-08-18 | 180.0

# In [12]: for loan in loans:
#    ...:     if loan.Installments == 5 or loan.Installments == 6 or loan.Installments == 8:
#    ...:         print(f"{loan.Cust_name} | {loan.Loan_amount}")

# Cust_name | Loan_amount
# Emma | 500000.0
# Harry | 6000000.0
# Jack | 2500000.0

# In [13]: for loan in loans:
#     ...:     if 400000000 <= loan.Loan_amount < 800000000:
#     ...:         print(f"{loan.Accno} | {loan.Cust_name} | {loan.Loan_amount} | {loan.Installments} | {loan.Int_rate} | {loan.Start_date} | {loan.Interest}")

# Accno | Cust_name | Loan_amount | Installments | Int_rate | Start_date | Interest
# 1829127878 | Will | 450000000.0 | 12 | 5.4 | 2020-10-08 | 180.0
# 184189712 | Karen | 600000000.0 | 60 | 8.5 | 2008-12-26 | 600.0

# In [14]: for loan in loans:
#     ...:     if loan.Cust_name == 'Roman':
#     ...:         print(f"{loan.Accno} |  {loan.Cust_name} | {loan.Loan_amount}")

# Accno | Cust_name | Loan_amount
# 19872916732 |  Roman | 200000000.0

# In [15]: for loan in loans:
#     ...:     if loan.Cust_name[-2] == 'a':
#     ...:         print(f"{loan.Accno} |  {loan.Cust_name} | {loan.Loan_amount}")
#     ...: 
# 19872916732 |  Roman | 200000000.0
# 8798173716 |  Dean | 300000000.0

# In [16]: loans = Loan_Accounts.objects.all().order_by('Loan_amount')

# In [17]: for loan in loans:
#     ...:     print(f"{loan.Accno} | {loan.Cust_name} | {loan.Loan_amount} | {loan.Installments} | {loan.Int_rate} | {loan.Start_date} | {loan.Interest}")

# Accno | Cust_name | Loan_amount | Installments | Int_rate | Start_date | Interest 
# 1273892728 | Emma | 500000.0 | 5 | 5.5 | 2020-05-15 | 100.0
# 1987291882 | John | 1000000.0 | 10 | 5.6 | 2020-02-22 | 1000.0
# 7189739128 | Jack | 2500000.0 | 8 | 6.8 | 2020-08-18 | 180.0
# 21673179779 | Harry | 6000000.0 | 6 | 6.6 | 2020-06-16 | 160.0
# 13619219865 | Jake | 15000000.0 | 50 | 4.5 | 2008-04-05 | 140.0
# 19872916732 | Roman | 200000000.0 | 15 | 6.5 | 2020-04-25 | 1200.0
# 8798173716 | Dean | 300000000.0 | 20 | 8.8 | 2020-01-14 | 1300.0
# 1829127878 | Will | 450000000.0 | 12 | 5.4 | 2020-10-08 | 180.0
# 184189712 | Karen | 600000000.0 | 60 | 8.5 | 2008-12-26 | 600.0
# 1276187198 | Seth | 4000000000.0 | 40 | 8.6 | 2020-05-15 | 1100.0

# In [18]: loans = Loan_Accounts.objects.all().order_by('Start_date')[::-1]

# In [19]: for loan in loans:
#     ...:     print(f"{loan.Accno} | {loan.Cust_name} | {loan.Loan_amount} | {loan.Installments} | {loan.Int_rate} | {loan.Start_date} | {loan.Interest}")

# Accno | Cust_name | Loan_amount | Installments | Int_rate | Start_date | Interest 
# 1829127878 | Will | 450000000.0 | 12 | 5.4 | 2020-10-08 | 180.0
# 7189739128 | Jack | 2500000.0 | 8 | 6.8 | 2020-08-18 | 180.0
# 21673179779 | Harry | 6000000.0 | 6 | 6.6 | 2020-06-16 | 160.0
# 1273892728 | Emma | 500000.0 | 5 | 5.5 | 2020-05-15 | 100.0
# 1276187198 | Seth | 4000000000.0 | 40 | 8.6 | 2020-05-15 | 1100.0
# 19872916732 | Roman | 200000000.0 | 15 | 6.5 | 2020-04-25 | 1200.0
# 1987291882 | John | 1000000.0 | 10 | 5.6 | 2020-02-22 | 1000.0
# 8798173716 | Dean | 300000000.0 | 20 | 8.8 | 2020-01-14 | 1300.0
# 184189712 | Karen | 600000000.0 | 60 | 8.5 | 2008-12-26 | 600.0
# 13619219865 | Jake | 15000000.0 | 50 | 4.5 | 2008-04-05 | 140.0


# In [20]: for loan in loans:
#     ...:     if loan.Int_rate < 8:
#     ...:         loan.Loan_amount = F('Loan_amount') - 1000
#     ...:         loan.save()

# In [21]: for loan in loans:
#     ...:     print(loan.Loan_amount)

# Loan_amount
# 999000.0   
# 199999000.0
# 300000000.0
# 4000000000.0
# 499000.0
# 5999000.0
# 2499000.0
# 449999000.0
# 14999000.0
# 600000000.0

# In [22]: for loan in loans:
#     ...:     if int(loan.Loan_amount) < 100000000:
#     ...:         loan.delete()

# In [51]: loans = Loan_Accounts.objects.all()

# In [52]: for loan in loans:
#     ...:     print(loan.Loan_amount)

# Loan_amount
# 199999000.0
# 300000000.0
# 4000000000.0
# 449999000.0
# 600000000.0