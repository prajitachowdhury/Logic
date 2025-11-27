# Objective: The objective of this code is to generate a truth table for N inputs. 
# Design: It is designed to first ask the user to enter the value of N, following which the code will return the truth table for it.
# Approach: The approach taken in this code is by first initiating an empty array, generating the binary format of numbers from 0 to N-1, followed by appending the binary format to the original array and further transforming/saving it into a clean DataFrame. 

# Import the required libraries
import pandas as pd
import numpy as np

#Function for generating truth table for N inputs
def tr_table(N):
  table = []
  i = 0
  while i <pow(2,N):
    val = bin(i)[2:]
    val = ((N)-len(val))*'0' + val
    table.append(list(val))
    i = i + 1

  table = pd.DataFrame(table)
  return(table)

# Main program calling the function to generate the truth table
try:
  N = int(input(print("Enter value of N (1<=N<=10):")))      
except ValueError:
  print("The input is not an integer.")
else:
  if N >= 1 and N <= 10 :
    print(tr_table(N))
  elif N < 1 or N > 10 :
    print("Invalid value.")
