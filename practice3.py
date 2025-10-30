admin='abcd'
password='word'
fail=0
success=0
i=1
while i<=3:
    a=input('请输入账户:' )
    print()
    b=input('请输入密码' )
    print()
    if a==admin and b==password:
        success=success+1
        print('输入正常')
    else:
        fail=fail+1
        print('输入错误')
    i=i+1
if success==3:
    print('恭喜您输入正常')
else:
    print('您输入的时候有错误，错误次数为',fail)