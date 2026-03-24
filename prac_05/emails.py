def main():
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = name_from_email(email)
        confirmation = input("Is your name Lindsay Ward? (Y/n)")
        # Anything other than Y or Enter is treated as a "no"
        if confirmation != "Y" and confirmation != "":
            name = input("Name: ")
        email_to_name[email] = name #key->value 保存
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")

def name_from_email(email):
    prefix = email.split("@")[0]
    parts = prefix.split(".")
    name = " ".join(parts).title()#吧parts里的内容用“ ”（空格）链接起来，.title()首字母大写
    return name

main()