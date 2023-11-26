import requests

folder_id = "Каталог"
iam_token = "IAM-token"
speech_file_path = "audio_2023-10-27_23-14-10.ogg"
result_name_file = f"{speech_file_path.removesuffix('.ogg')}.txt"
url = f"https://stt.api.cloud.yandex.net/speech/v1/stt:recognize?folderId={folder_id}&lang=ru-RU"
headers = {
    "Authorization": f"Bearer {iam_token}"
}

with open(speech_file_path, 'rb') as audio_file:
    response = requests.post(url, headers=headers, files={'file': audio_file})

if response.ok:
    result = response.json()
    with open(result_name_file, "w") as result_file:
        result_file.write(str(result))

    print(result)
else:
    print("Произошла ошибка распознавании речи.")