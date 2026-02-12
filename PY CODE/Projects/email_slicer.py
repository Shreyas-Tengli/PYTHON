email=input("Ente ryour email: ")

index= email.index("@")

username=email[:index]

doamain=email[index+1:]

print(f"your domain is {doamain} and your user name is {username}")