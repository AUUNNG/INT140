validate = {
    67130500109: {
        "firstname": "Yuttapoom",
        "lastname": "Haphanom"
    }
}

try:
    result = validate[1]
except KeyError:
    result = ""


print(result)
