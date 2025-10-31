#This is what we called Dunder or Magic methods in Python

class Bag:
  def __len__(self):
    return 60
  

  def __str__(self):
    return "This is a Bag"
  

print(len(Bag()))
print(Bag())