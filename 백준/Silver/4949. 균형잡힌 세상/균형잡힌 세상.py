while True :
    text_list = input()
    check_list = ''
    if text_list == "." : 
        break
    for text in text_list:
        if text not in '()[]': continue
        else : 
            check_list += text
    
    for _ in range(len(check_list)//2 +1):
        check_list =  check_list.replace('()','')
        check_list = check_list.replace('[]','')
    if len(check_list)==0 : print("yes")
    else: print("no")
