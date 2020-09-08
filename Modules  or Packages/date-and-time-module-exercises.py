import glob
import datetime

filenames = glob.glob("*.txt")

with open(str(datetime.datetime.now())+".txt", 'w') as file:
  for filename1 in filenames:
    with open(filename1, "r") as f:
      file.write(f.read()+"\n")