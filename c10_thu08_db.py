# member list in the file
# 073 ชัยบดินทร์
# 106 ภาคิน
# 108 ภูดิศ
# 109 ยุทธภูมิ
# 117 ศุภฤกษ์

def main():
    members = {
        67130500100:{
            'name': 'a',
            'lastname': 'a'
        }
    }
    while True:
        print()
        ask = input('what do u want (add/read/exit) : ').lower()
        if ask == "add" or ask == "a":
            id, name, lastname = ui_addMember(members)
            bl_addMember(members, id, name, lastname)

def ui_addMember(members: dict) -> (int, str, str):
    while True:
        print()
        id = int(input('input ur id: '))
        if 67130500000 > id or id >= 67130501000:
            print('please input id with format (67130500xxx)')
            continue
        if id in members:
            print(f'{id} already exits')
            continue
        break
    name = input('input ur name: ')
    lastname = input('input ur lastname: ')
    return id, name, lastname

def bl_addMember(members: dict, id: int, name: str, lastname: str) -> (dict):
    members[id] = {'name': name,'lastname': lastname}

if __name__ == "__main__":
    main()
