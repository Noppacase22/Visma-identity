from identify import Identifier

def menu():
    choice = 0
    print("What do you want to do?")
    print("1) Run tests")
    print("2) Test your own input")
    while True:
        choice = input("Your input: ")
        if choice in ["1", "2"]:
            return int(choice)
        print("Invalid input. Please choose '1' or '2'.")

def runTests():
# Basic tests to check functionality
# No, I have not done 'real' testing before.
# No, I don't know what 'assert' is.

    I = Identifier()
    
    print("Output tests")
    loginUri = "visma-identity://login?source=severa"
    confirmUri = "visma-identity://confirm?source=netvisor&paymentnumber=102226"
    signUri = "visma-identity://sign?source=vismasign&documentid=105ab44"

    print(I.identify(loginUri))
    print(I.identify(confirmUri))
    print(I.identify(signUri))

    print("\nURI length tests")
    shortUri1 = "visma-identity://sign?source="
    shortUri2 = "://login?source=severa"
    print(I.identify(shortUri1))
    print(I.identify(shortUri2))

    print("\nScheme tests")
    wrongScheme1 = "visma-identity:/login?source=severa"
    wrongScheme2 = "twoday-identify://login?source=severa"
    wrongScheme3 = "://confirm?source=netvisor&paymentnumber=102226"
    print(I.identify(wrongScheme1))
    print(I.identify(wrongScheme2))
    print(I.identify(wrongScheme3))

    print("\nPath tests")
    wrongPath1 = "visma-identity://ngis?source=vismasign&documentid=105ab44"
    wrongPath2 = "visma-identity://sig?source=vismasign&documentid=105ab44"
    wrongPath3 = "visma-identity://consign?source=netvisor&paymentnumber=102226"
    print(I.identify(wrongPath1))
    print(I.identify(wrongPath2))
    print(I.identify(wrongPath3))

    print("\nParameter tests")
    paymentNumberIsString = "visma-identity://confirm?source=netvisor&paymentnumber=23sa26"
    pathHasAnotherPathsParameters = "visma-identity://login?source=netvisor&paymentnumber=102226"
    print(I.identify(paymentNumberIsString))
    print(I.identify(pathHasAnotherPathsParameters))
    return None

def userTests():
    I = Identifier()
    print("\nThis part lets you test the functionality of the identifier")
    while True:
        uri = input("Give URI to test, blank exits:")
        if uri == "":
            break
        print(I.identify(uri))
        print()
    return None

def main():
    print("Welcome to Visma-identify.")
    choise = menu()
    if choise == 1:
        print("\nRunning pre-written tests\n")
        runTests()
    else:
        print("\nTesting your inputs")
        userTests()

    print("\nExiting...")
    print("Have a nice day!")
    return None

main()