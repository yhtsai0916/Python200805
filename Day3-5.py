
def x(add1,add2)

while True:
    print("1.加法")
    print("2.減法")
    print("3.乘法")
    print("4.除法")
    print("5.離開")
    
    sel=int(input("輸入選項:"))
    
    if sel==1:
        add1=int(input("輸入第一個數字:"))
        add2=int(input("輸入第二個數字:"))
        print("答案是",add1+add2)
    elif sel==2:
        add1=int(input("輸入第一個數字:"))
        add2=int(input("輸入第二個數字:"))
        print("答案是",add1-add2)
    elif sel==3:
        add1=int(input("輸入第一個數字:"))
        add2=int(input("輸入第二個數字:"))
        print("答案是",add1*add2)
    elif sel==4:
        add1=int(input("輸入第一個數字:"))
        add2=int(input("輸入第二個數字:"))
        print("答案是",add1/add2)
    else:
        break
    
        

    
        
        
    
    