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

NormalFileName = "normal_generated"
CompactFileName = "compact_generated"

def generateNormalFile():
    f = open(NormalFileName + ".txt", "w")
    for i in range(N):
        line = {"app_ver": app_ver, "app_bundle": app_bundle, "contacts": randomContacts(), "dylibs": randomDylibs()}
        f.write(str(line) + "\n")
    f.close()

def generateCompactFile():
    f = open(CompactFileName + ".txt", "w")

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


def genAndCompare():
    generateNormalFile()
    generateCompactFile()

    os.system("rm -f *.gz")
    os.system("gzip -k *.txt")
    # os.system("ls -l | egrep 'gz|txt' | tr -s ' ' | cut -d ' ' -f 5,9-")

    file_stats1 = os.stat(NormalFileName + ".txt")
    file_stats2 = os.stat(CompactFileName + ".txt")
    reduction_on_text = (1 - file_stats2.st_size / file_stats1.st_size)

    file_stats1 = os.stat(NormalFileName + ".txt.gz")
    file_stats2 = os.stat(CompactFileName + ".txt.gz")

    reduction_on_gz = (1 - file_stats2.st_size / file_stats1.st_size)
    return (reduction_on_text, reduction_on_gz)

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print("Benchmark size reduction of text compaction + gzip")


def showResult(message, reduction):
    if reduction < 0:
        print(f"{message}: " + f"{bcolors.WARNING}{100 * reduction:.2f}{bcolors.ENDC}" + " %")
    else:
        print(f"{message}: " + f"{bcolors.OKGREEN}{100 * reduction:.2f}{bcolors.ENDC}" + " %")

for count in (2, 5, 10, 20, 30, 40, 50,60,70,80,90,100):
    N = count
    print("Number of records N = {}".format(N))

    numRun = 50
    textReduction = 0.0
    gzReduction = 0.0
    for i in range(numRun):
        result = genAndCompare()
        textReduction += result[0]
        gzReduction += result[1]

    showResult("Avg text size reduction", textReduction/numRun)
    showResult("Avg gzip size reduction", gzReduction/numRun)
    print("---------------------------------")