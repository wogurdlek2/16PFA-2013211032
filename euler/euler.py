#-*-coding:cp949
#http://euler.synap.co.kr/prob_detail.php?id=1

#10���� ���� �ڿ��� �߿��� 3 �Ǵ� 5�� ����� 3, 5, 6, 9 �̰�, �̰��� ��� ���ϸ� 23�Դϴ�.
#1000���� ���� �ڿ��� �߿��� 3 �Ǵ� 5�� ����� ��� ���ϸ� ���ϱ��?

sum = 0

for a in range(1, 1000) :
    if a%3 == 0 :
        print "There is %d!!" %a
        sum = sum + a
        print "Now sum is %d" %sum
    elif a%5 == 0 :
        print "There is %d!!" %a
        sum = sum + a
        print "Now sum is %d" %sum

print "Finally, Sum is %d" %sum