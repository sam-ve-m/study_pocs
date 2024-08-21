import requests


counter = 0


def add_contact(phones_types: list):
    global counter
    payload = {
      "email": f"{counter}",
      "address": "string",
      "lastName": "string",
      "firstName": "string",
      "phoneList": [
        {
          "type": phone,
          "number": "(11) 1111-1111"
        } for phone in phones_types
      ]
    }
    requests.post("http://localhost:8888/g3/register", json=payload)
    counter += 1
    print(counter)
    return True


add_contact(["mobile", "mobile", "mobile"])
add_contact(["commercial", "commercial", "residential"])
