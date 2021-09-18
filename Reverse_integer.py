class Solution:
  def reverse(self, x: int) -> int:
    num=0
    num_dis=abs(x)
    while(num_dis):
      temp = num_dis%10
      num_dis=(num_dis-temp)//10
      if num==0:
        num=temp
      else:
        num=(num*10)+temp
    if x<0:
      num=num*(-1)
    return num if num > -2**31 and num < 2**31-1 else 0
