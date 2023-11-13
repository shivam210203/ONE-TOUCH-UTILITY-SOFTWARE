# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 20:47:53 2023

@author: shiva

"""



print()
print()

print("                                                                                     ONE TOUCH- UTILITY APP")
print()
print("                                                                              one stop solution to all you needs")


print()
print()

while(True):
    print("MENU:")
    print()
    
    print("1:COUNT DOWN TIMER        2.CALCULATOR")
    print()
    print("3: TO DO LIST             4.ALARM")
    print()
    print("5: WEATHER                6.WORLD CLOCK")
    print()
    print("7: MUSIC PLAYER           8.STOPWATCH")
    print()
    print("9. exit")
    print()
    print()

    choice = int(input("enter your choice:"))


    if choice==1:
        import ctt
    
    elif choice==2:
        import calc
        
    elif choice==3:
        import td
        
    elif choice==4:
        import almc
        
    elif choice==5:
        import wt2
        
    elif choice==6:
        import clk
        
    elif choice==7:
        import musicprog23
        
    elif choice==8:
        import stw
        
    elif choice==9:
        break
        exit
    else:
        print("INVALID CHOICE")
        
        