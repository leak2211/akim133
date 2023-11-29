import requests

def tts():
    iam_token = 'AIM_TOKEN'
    folder_id = 'FOLDER_ID'
    headers = {
        "Authorization": "Bearer " + iam_token
    }
    data = {
        "text": "Порода ездовых собак аборигенного типа, предназначенная для работы в упряжке, одна из древнейших пород собак.",
        "lang": "ru-RU",
        "voice": "filipp",
        "folderId": folder_id
    }
    response = requests.post("https://tts.api.cloud.yandex.net/speech/v1/tts:synthesize", headers=headers, data=data)
    response_bytes = response.content
    with open("speech.ogg", "wb") as file:
        file.write(response_bytes)

if __name__ == "__main__":
    tts()
