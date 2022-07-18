def main():
    user_input = input("Input here Please: ")
    convert(user_input)

def convert(string):
    string = string.replace(":)", "🙂").replace(":(", "🙁")
    
    print(string)

main()