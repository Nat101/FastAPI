import requests

base_url = 'http://127.0.0.1:8000'


def api_greeting():
    response = requests.get(url=f"{base_url}/greeting")
    if response.status_code == 200:
        return response.json()['message']
    else:
        return f"Greeting failed:\nCode:{response.status_code}\nError:{response.json()}"


def api_greeting_personal(username):
    params = {
        'username': username
    }
    response = requests.get(url=f"{base_url}/personal_greeting", params=params)
    if response.status_code == 200:
        return response.json()['message']
    else:
        return f"Personal greeting failed:\nCode:{response.status_code}\nError:{response.json()}"


def api_user_profile(user_id):
    params = {
        'user_id': user_id
    }
    response = requests.get(url=f"{base_url}/user_profile", params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return f"UserProfile failed:\nCode:{response.status_code}\nError:{response.json()}"


def main():

    print(f"\nGreeting:\n {api_greeting()}")
    print(f"\nPersonal Greeting:\n {api_greeting_personal('Natalie Carlson')}")
    print(f"\nUser Profile:\n {api_user_profile(1)}")
    print(f"\nUser Profile:\n {api_user_profile(2)}")
    print(f"\nUser Profile:\n {api_user_profile(3)}")


if __name__ == "__main__":
    main()
