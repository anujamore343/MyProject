#Write a python function to print the table of given user input
def table(i<=5):
  num=int(input("enter a number :"))
  for i in range(1,11): 
    print(f"{num}*{i}={num*i})
  table()
