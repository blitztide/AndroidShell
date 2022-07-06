import os,requests
import zipfile

repo_path = "/UNI/db/fdroid/repo.json"
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

def update_repo():
    'updates the local index of the repository'
    if os.path.exists(repo_path):
        print("Last updated:", os.path.getmtime(repo_path))
    else:
        fetch_repo()

def fetch_repo():
    url = "https://f-droid.org/repo/index-v1.jar"
    response = requests.get(url,stream=True)
    if response.status_code == requests.status_codes.codes.ok:
        if zipfile.is_zipfile(response.content):
            fp = open(repo_path,"wb")
            fp.write(zipfile.ZipFile(fp).read("index_v1.json"))
            fp.close()
        else:
            raise("Not zip file")
    
