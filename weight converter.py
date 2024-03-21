weight = input("Input your weight: ")
cat = input("You want it converted to (K)Gs or (LB)s: ")
if cat.upper() == "K":
    converted = float(weight) * 0.45
    print("Your weight in KGs is: " + str(converted))
elif cat.upper() == "L":
    converted = float(weight) / 0.45
    print("Your weight in LBs is: " + str(converted))
else:
    print("wrong answer")