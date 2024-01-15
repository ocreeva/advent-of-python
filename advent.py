import inspect
import os
import requests

def download(year, day):
    year_str = str(year)
    day_str = str(day)

    root_directory = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

    data_directory = os.path.join(root_directory, year_str)
    if (not os.path.exists(data_directory)):
        os.mkdir(data_directory)

    file_path = os.path.join(data_directory, day_str + ".txt")
    if (not os.path.exists(file_path)):
        session = requests.Session()

        with open(os.path.join(root_directory, ".session"), "r") as cookie_file:
            session.cookies.set("session", cookie_file.read())

        url = "https://adventofcode.com/" + year_str + "/day/" + day_str + "/input"
        response = session.get(url)
        with open(file_path, "wb") as data_file:
            data_file.write(response.content)

    with open(file_path, "r") as data_file:
        return data_file.read().rstrip('\n')
