import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        url = "https://cloud-api.yandex.net:443/v1/disk/resources/upload"
        file_name = path_to_file.split("\\")[-1]
        params = {"path": f'/{file_name}'}
        headers = {"Authorization": "OAuth " + self.token}
        response = requests.get(url, headers=headers, params=params)
        if 200 <= response.status_code < 300:
            data = response.json()
            url = data['href']
            with open(file_path, 'rb') as f:
                response = requests.put(url, files={'file': f})
            print("Файл загружен")
        else:
            print('Возникла ошибка')


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = input('Вставьте ссылку на файл')
    token = input('Вставьте токен')
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)