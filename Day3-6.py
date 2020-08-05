d={}
print("歡迎進入系統")

while True:
    print("1.建立詞彙")
    print("2.列出所有單字")
    print("3.英翻中")
    print("4.中翻英")
    print("5.測驗")
    print("6.離開")
    
    sel=int(input("輸入選項:"))
    
    if sel==1:
        e1=input("輸入英文:")
        c1=input("輸入中文:")
        d[e1]=c1
    elif sel==2:
        print(d)
    elif sel==3:
        e1=input("輸入英文:")
        if e1 in d:
            print(d[e1])
    elif sel==4:
        c1=("輸入中文:")
        for e,c in d.items():
            if c==c1:
                print(e)
    else:
        break
     
      
 
        
        
        
        
    
