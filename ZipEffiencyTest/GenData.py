import random
import uuid
import hashlib
import os

app_ver = "1.0"
app_bundle = "com.hello.sg"

# https://gist.githubusercontent.com/ruanbekker/a1506f06aa1df06c5a9501cb393626ea/raw/cef847b6402da0fe00977e7349a4dc3fbeb4df54/array-names.py
contacts1 = str([
    "Aaran",
"Aaren",
"Aarez",
"Aarman",
"Aaron",
"Aaron-James",
"Aarron",
"Aaryan",
"Aaryn",
"Aayan",
"Aazaan",
"Abaan",
"Abbas",
"Abdallah",
"Abdalroof",
"Abdihakim",
"Abdirahman",
"Abdisalam",
"Abdul",
"Abdul-Aziz",
"Abdulbasir",
"Abdulkadir",
"Abdulkarem",
"Abdulkhader",
"Abdullah",
"Abdul-Majeed",
"Abdulmalik",
"Abdul-Rehman",
"Abdur",
"Abdurraheem",
"Abdur-Rahman",
"Abdur-Rehmaan",
"Abel",
"Abhinav",
"Abhisumant",
"Abid",
"Abir",
"Abraham",
"Abu",
"Abubakar",
"Ace",
"Adain",
"Adam",
"Adam-James",
"Addison",
"Addisson",
"Adegbola",
"Adegbolahan",
"Aden",
"Adenn",
"Adie",
"Adil",
"Aditya",
"Adnan",
"Adrian"
])
contacts2 = str([
    "Adrien",
"Aedan",
"Aedin",
"Aedyn",
"Aeron",
"Afonso",
"Ahmad",
"Ahmed",
"Ahmed-Aziz",
"Ahoua",
"Ahtasham",
"Aiadan",
"Aidan",
"Aiden",
"Aiden-Jack",
"Aiden-Vee",
"Aidian",
"Aidy",
"Ailin",
"Aiman",
"Ainsley",
"Ainslie",
"Airen",
"Airidas",
"Airlie",
"AJ",
"Ajay",
"A-Jay",
"Ajayraj",
"Akan",
"Akram",
"Al",
"Ala",
"Alan",
"Alanas",
"Alasdair",
"Alastair",
"Alber",
"Albert",
"Albie",
"Aldred",
"Alec",
"Aled",
"Aleem",
"Aleksandar",
"Aleksander",
"Aleksandr",
"Aleksandrs",
"Alekzander",
"Alessandro",
"Alessio",
"Alex",
"Alexander",
"Alexei",
"Alexx",
"Alexzander"
])

dylibs1 = str(["frida", "firebase", "guardian", "crashlytics", "poiuytrewq", "pqowqowopq", "mvnxcvnmxmv", "dfsndkfjk"])
dylibs2 = str(["xrida", "direbase", "guardien", "frashlytics", "lkjhgfdsa", "dsfsfsdfs", "bvcbcvnbcvmb", "sotirjwjf"])

def randomContacts():
    if random.randint(0, 1) == 0:
        return contacts1
    else:
        return contacts2

def randomDylibs():
    if random.randint(0, 1) == 0:
        return dylibs1
    else:
        return dylibs2

N = 10

def generateNormalFile():
    f = open("normal_generated.txt", "w")
    for i in range(N):
        line = {"app_ver": app_ver, "app_bundle": app_bundle, "contacts": randomContacts(), "dylibs": randomDylibs()}
        f.write(str(line) + "\n")
    f.close()

def generateCompactFile():
    f = open("compact_generated.txt", "w")

    lookup = {
        hashlib.md5(contacts1.encode()).hexdigest(): contacts1,
        hashlib.md5(contacts2.encode()).hexdigest(): contacts2,
        hashlib.md5(dylibs1.encode()).hexdigest(): dylibs1,
        hashlib.md5(dylibs2.encode()).hexdigest(): dylibs2,
    }
    f.write(str(lookup) + "\n")

    for i in range(N):
        c = randomContacts()
        d = randomDylibs()
        line = {"app_ver": app_ver, "app_bundle": app_bundle, "contacts": hashlib.md5(c.encode()).hexdigest(), "dylibs": hashlib.md5(d.encode()).hexdigest()}
        f.write(str(line) + "\n")
    f.close()

generateNormalFile()
generateCompactFile()

os.system("rm -f *.gz")
os.system("gzip -k *.txt")