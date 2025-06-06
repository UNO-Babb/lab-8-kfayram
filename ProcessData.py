#ProcessData.py
#Name: Kyle
#Date:
#Assignment:

import random

def main():

  #Open the files we will be using
  inFile = open("names.dat", 'r')
  outFile = open("StudentList.csv", 'w')

  #Process each line of the input file and output to the CSV file
  
  #line = inFile.readline()
  for line in inFile:
    data = line.split()
    first = data[0]
    last = data[1]
    idNum = data[3]
    year = data[5]
    major = data[6]

    #print(data)

    student_id = makeID(first, last, idNum)
    majAbv = makeMaj(major)
    yearAbv = abvYear(year)
    majYear = majAbv + "-" + yearAbv

    output = last + ", " + first + ", " + student_id + ", " + majYear + "\n"
    outFile.write(output)
    
  #Close files in the end to save and ensure they are not damaged.
  inFile.close()
  outFile.close()

def makeID(first, last, idNum):
  #print(first, last, idNum)
  idLen = len(idNum)

  while len(last) < 5:
    last = last + "X"

  id = first[0] + last + idNum[idLen - 3: ]

  #print(id)
  return(id)

def makeMaj(major):
  #major = data[6]
  abvMajor = major[:3]
  return abvMajor

def abvYear(year):
  #year = data[5]
  if year == "Freshman":
      return "FR"
  elif year == "Sophomore":
      return "SO"
  elif year == "Junior":
      return "JR"
  elif year == "Senior":
      return "SR"
  else:
      return "Unknown"  

if __name__ == '__main__':
  main()
