"""
========================
   가위  바위  보
========================

1. Created by : park hyeon jun
2. 2016 - 10 - 23 - 16:42

========== ========== =======
 computer     user    outcome
========== ========== =======
Rock          Rock      Draw
Rock        Scissors   Lose
Rock        Paper      Win
Scissors      Rock      Win
Scissors   Scissors   Draw
Scissors     Paper      Lose
Paper        Rock      Lose
Paper      Scissors   Win
Paper        Paper      Draw
========== ========== =======

Rock < Paper < Scissor < Rock

"""
import random

def main():
   """rock, cissor, paper"""
   com_finger = random.randrange(3) + 1

   for i in range(10):
      my_finger = int(input("가위(1), 바위(2), 보(3)를 입력하세요. "))
      while not(my_finger == 1 or my_finger == 2 or my_finger ==3):
         my_finger = int(input("가위(1), 바위(2), 보(3)를 입력하세요. "))
   
      if(com_finger == 1):
         if(my_finger == 1):
            print("컴퓨터가 낸 것은 가위입니다. -----> 바겼습니다.")
         elif(my_finger == 2):
            print("컴퓨터가 낸 것은 가위입니다. -----> 이겼습니다.")
         elif(my_finger == 3):
            print("컴퓨터가 낸 것은 가위입니다. -----> 졌습니다.")
      
      elif(com_finger == 2):
         if(my_finger == 1):
            print("컴퓨터가 낸 것은 바위입니다. -----> 졌습니다.!")
         elif(my_finger == 2):
            print("컴퓨터가 낸 것은 가위입니다. -----> 비겼습니다.")
         elif(my_finger == 3):
            print("컴퓨터가 낸 것은 가위입니다. -----> 이겼습니다.")

      elif(com_finger == 3):
         if(my_finger == 1):
            print("컴퓨터가 낸 것은 바위입니다. -----> 이겼습니다.")
         elif(my_finger == 2):
            print("컴퓨터가 낸 것은 가위입니다. -----> 졌습니다.")
         elif(my_finger == 3):
            print("컴퓨터가 낸 것은 가위입니다. -----> 비겼습니다.")

main()