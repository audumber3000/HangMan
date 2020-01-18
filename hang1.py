
class c1():
  def __init__(self):

      print('HangMan')
      print("Rules of the Game")
      print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
      print('1.you have to guess the word.')
      print('2.guess the letter by letter.')


  def hang(self):

      num = int(input("Enter your fav number: "))
      print('Now you have 5 chances')
      lst = []

      with open('audu.txt' , mode='r') as f:
          line=f.readlines()

      print (line[num])
      line1 = line[num]
      a = str(line1)
      for i in range(0,5):

          let = input("Enter your guess letter: ")
          print(f'chance no:{i}')
          if(let in line1):
              flag = True
          else:
              flag = False

          if(flag==True):
              print("yeah!! Great")
              lst.append(let)

              print("--------------------------------------")
          else:
              print("Opps!! try again.")

              print("---------------------------------------")

      print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
      print("Your chances has been over..")
      print("your right guessed letters are >>")
      print(f'{lst}')
      final = str(input("Enter you guessed word:"))
      print(a)
      if(final!= a):
          print("better luck next time")
      else:
          print("great")



if __name__=='__main__':
    v = c1()
    v.hang()