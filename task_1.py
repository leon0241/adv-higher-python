#Create a program that will allow the user to enter the number of the month and display a message stating whether it has 28 (or 29), 30 or 31 days. Input should be validated so that only input between 1 and 12 (inclusive)  is accepted.  The program should also display the month in text format, ie Jan, Feb etc.

#The top level design in the diagram below should help you in your parameter passing.,

#You should make use of 2 parallel arrays as shown in the Haggis declarations below:

#DECLARE days INITIALLY [31,28,31,30,31,30,31,31,30,31,30,31]
#DECLARE months INITIALLY ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

def get_month(month):
    score = 13
    while score > 12 or score < 1:
        score = int(input("enter a number for your month"))
        
