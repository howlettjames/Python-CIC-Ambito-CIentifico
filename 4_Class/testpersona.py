from persona import Persona

def testPersona():
    per1 = Persona("Tony Starrk", 40)
    per2 = Persona("Allan Poe", 35)

    per1.setEdad(20)

    per1.printInfo()
    per2.printInfo()

    print(per1)

    print(per1 == per2)
    print(per1 != per2)

if __name__ == "__main__":
    testPersona()