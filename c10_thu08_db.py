# member list in the file
# 073 ชัยบดินทร์
# 106 ภาคิน
# 108 ภูดิศ
# 109 ยุทธภูมิ
# 117 ศุภฤกษ์

def main():
    members = {}
    while True:
        print()
        ask = input('what do u want (add/read/exit) : ').lower()
        if ask == "add" or ask == "a":
            id, name, lastname = ui_addMember(members)
            members = bl_addMember(members, id, name, lastname)
        if ask == "read" or ask == "r":
            id = ui_readMember()
            print(id)
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

def ui_readMember() -> (int):
    print()
    id = int(input('input ur id: '))
    if 67130500000 > id or id >= 67130501000:
        print('please input id with format (67130500xxx)')
    return id

def bl_addMember(members: dict, id: int, name: str, lastname: str) -> (dict):
    print()
    print('process > bl_addMember')
    members[id] = {'name': name,'lastname': lastname}
    return members

if __name__ == "__main__":
    main()
