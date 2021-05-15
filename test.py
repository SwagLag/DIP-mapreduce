def test(test):
    print(test)
    return test

# with open("dutchtext") as infile:
#     stdin = infile.readlines()
outcome = list(map(test,"In de prachtige zeestad Genua, de trotsche bijgenaamd, werd omstreeks het jaar 1435 een knaapje geboren,"))
print(outcome)
