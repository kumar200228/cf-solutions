for s in[*open(0)][1:]:
 a=[];i=0
 while(x:=s[(i:=i-1)])not in a:a+='05'*(x=='0')+'27'*(x=='5')
 print(-i-3)
