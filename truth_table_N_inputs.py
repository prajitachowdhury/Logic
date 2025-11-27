# The Objective of this code is to generate a truth table for N inputs. It is designed to first ask the user to enter the value of N, following which the code will return the truth table for it.

# Import the required libraries
import numpy as np
import pandas as pd


#Function for generating truth table for N inputs
def truth_table(N):
  ttable=pd.DataFrame(np.zeros((pow(2,N),N)))
  counter = 0
  col = 0

  while col<N:
    row = 0
    target= pow(2,N-col-1)
    counter = 0
    while row < ttable.shape[0]:
      if int((counter/target)%2)!=0:
        ttable.at[row, col] = 1
      counter=counter+1
      row = row + 1

    col = col + 1
  print("Truth table for ",N," inputs:") 
  return ttable


# Main program calling the function to generate the truth table
try:
  N = int(input("Enter an integer value of N(1 to 10): "))       
except ValueError:
  print("The input is not an integer.")
else:
  if N < 1 or N > 10 :
    print("Invalid value.")
  else:
    print(truth_table(N))
