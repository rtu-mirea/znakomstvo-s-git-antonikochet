
inputs = input()
mas = inputs.split(' ')


n=int(mas[0])
m=int(mas[1])
s = 0
for j in range(n):
    string_output = ''
    if (j+1)%2==0:
        for i in range(m,0,-1):
            st=''
            if s<10:
                st='  ' + str(s)
            else:
                st=' ' + str(s)
            string_output = st + string_output 
            s=s+1
    else:
        for i in range(m):
            st=''
            if s<10:
                st='  ' + str(s)
            else:
                st=' ' + str(s)
            string_output = string_output + st
            s=s+1
    print(string_output)

            
