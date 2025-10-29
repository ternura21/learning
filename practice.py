height=int(input('请输入身高'))
age=int(input(('请输入年龄' )))
student_card=input('请问是否有学生证，有则输入1，无则输入0')
final_price=80
full_price=100
if height<=130 or age<=6 or age>=80:
    print('因为您满足条件，所以免门票')
elif height > 130 and age > 6 and age < 80 and student_card == '1':
 print('您需要支付',final_price)
else:
 print('您需要支付',full_price)