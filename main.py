# Human characteristics

hair_color = {"black": "CCAGCAATCGC", "brown": "GCCAGTGCCG", "blonde": "TTAGCTATCGC"}
facial_shape = {"square": "GCCACGG", "round": "ACCACAA", "oval": "AGGCCTCA"}
eye_color = {"blue": "TTGTGGTGGC", "green": "GGGAGGTGGC", "brown": "AAGTAGTGAC"}
gender = {"male": "TGCAGGAACTTC", "female": "TGAAGGACCTTC"}
race = {"white": "AAAACCTCA", "black": "CGACTACAG", "asian": "CGCGGGCCG"}

suspectprofile = []

print("The criminal has the following characteristics: ")

with open("dna.txt") as suspectdna:
    readable = suspectdna.read()

    if hair_color.get("black") in readable:
        print("Black")
        suspectprofile.append({"hair_color": "black"})
    elif hair_color.get("brown") in readable:
        print("Brown")
        suspectprofile.append({"hair_color": "brown"})
    elif hair_color.get("blonde") in readable:
        print("Blonde")
        suspectprofile.append({"hair_color": "blonde"})
with open("dna.txt") as suspectdna:
    readable = suspectdna.read()

    if facial_shape.get("square") in readable:
        print("Square")
        suspectprofile.append({"facial_shape": "square"})
    elif facial_shape.get("round") in readable:
        print("round")
        suspectprofile.append({"facial_shape": "round"})
    elif facial_shape.get("oval") in readable:
        print("Oval")
        suspectprofile.append({"facial_shape": "oval"})
with open("dna.txt") as suspectdna:
    readable = suspectdna.read()

    if eye_color.get("blue") in readable:
        print("Blue eyes")
        suspectprofile.append({"eye_color": "blue"})
    elif eye_color.get("green") in readable:
        print("Green eyes")
        suspectprofile.append({"eye_color": "green"})
    elif eye_color.get("brown") in readable:
        print("Brown eyes")
        suspectprofile.append({"eye_color": "brown"})
with open("dna.txt") as suspectdna:
    readable = suspectdna.read()

    if gender.get("male") in readable:
        print("Male")
        suspectprofile.append({"gender": "male"})
    if gender.get("female") in readable:
        print("Female")
        suspectprofile.append({"gender": "female"})
with open("dna.txt") as suspectdna:
    readable = suspectdna.read()

    if race.get("white") in readable:
        print("White")
        suspectprofile.append({"race": "white"})
    if race.get("black") in readable:
        print("Black")
        suspectprofile.append({"race": "black"})
    if race.get("asian") in readable:
        print("Asian")
        suspectprofile.append({"race": "asian"})

eva = [{"hair_color": "blonde"}, {"facial_shape": "oval"}, {"eye_color": "blue"}, {"gender": "female"}, {"race": "white"}]
larisa = [{"hair_color": "brown"}, {"facial_shape": "oval"}, {"eye_color": "brown"}, {"gender": "female"}, {"race": "white"}]
matej = [{"hair_color": "black"}, {"facial_shape": "oval"}, {"eye_color": "blue"}, {"gender": "male"}, {"race": "white"}]
miha = [{"hair_color": "brown"}, {"facial_shape": "square"}, {"eye_color": "green"}, {"gender": "male"}, {"race": "white"}]

print("Matching DNA...")

if suspectprofile == eva:
    print("Eva is guilty!")
elif suspectprofile == larisa:
    print("Larisa is guilty!")
elif suspectprofile == matej:
    print("Matej is guilty!")
elif suspectprofile == miha:
    print("Miha is guilty!")
else:
    print("None of the list is guilty")