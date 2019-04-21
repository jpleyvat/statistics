import sys
import modules.print_data as pd

def main_menu():
  pd.cls()
  print("[R]ecord data")
  print("[E]xit")
  request = input()
  pd.cls()

  return request

def type_of_varible_menu():
  print("[D]iscreet")
  print("[C]ontinuous")
  request = input()
  pd.cls()

  return request

def measures_menu():
  print("____________________________________________")
  print("____________________________________________")
  print("SHOW")
  print("[M]ean")
  print("[G]eometric mean")
  print("[H]armonic mean")
  print("[Me]dian")
  print("[Mo]de")
  print("[A]ll")
  print("--------------------------------------------")
  print("[N]ew entry")
  request = input()
  pd.cls()

  return request

def check_exit(request):
  if(request == 'E' or request == 'e'):
      finish = True
      sys.exit()

  return request

def switch(request):
    if(request == 'C' or request == 'c'):
      pd.print_const()
    if(request == 'M' or request == 'm'):
      pd.print_m()
    elif(request == 'G' or request == 'g'):
      pd.print_mg()
    elif(request == 'H' or request == 'h'):
      pd.print_mh()
    elif(request == 'Me' or request == 'me'):
      pd.print_me()
    elif(request == 'Md' or request == 'md'):
      pd.print_m()
    elif(request == 'A' or request == 'a'):
      pd.printall()

  # if(request_variables == 'D' or request_variables == 'd'):
  # elif(request_variables == 'C' or request_variables == 'c'):
