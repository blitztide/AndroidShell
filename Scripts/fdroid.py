import os,requests

name = "F-Droid"

def download(package,version):
    url = "https://f-droid.org/repo/{}_{}.apk".format(package,version)
    file_path = "/UNI/db/fdroid/{}_{}.apk".format(package,version)
    response = requests.get(url,stream=True)
    with open(file_path,"wb") as fp:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                fp.write(chunk)
    print(file_path, "Downloaded!")
    return "OK"

def check_exists(package,version):
    'Checks the repository list for latest installed version, updates repo if older than 1 day'
    url = "https://f-droid.org/repo/{}_{}.apk".format(package,version)
    response = requests.head(url)
    if response.status_code == requests.status_codes.codes.ok:
        return "OK"
    else:
        return "ERR_NOT_FOUND"
