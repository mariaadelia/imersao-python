# strip() ira retirar espacos em brancos desnecessarios que possam ter sido adicionados erroneamente
first_name = input("Hey, what's your first name?: ").strip()
last_name = input("And your last name? : ").strip()
whole_name = first_name + " " + last_name

print("Well, pleased to meet you, " + whole_name + ".")