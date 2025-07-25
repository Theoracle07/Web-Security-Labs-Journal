print("############The following usernames:############")
for i in range(150):
    if i % 3:
       print("carlos")
    else:
        print("wiener")


print("############The following usernames:############")
with open('password.txt', 'r') as f:
    lines = f.readlines()

    i = 0
    for pwd in lines:
        if i % 2:
            print(pwd.strip('\n'))
        else:
            print('peter')
            print(pwd.strip('\n'))
        i = i + 1


                        
