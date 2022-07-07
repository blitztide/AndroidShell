import os,requests
import zipfile
from io import BytesIO
import time
import json
import pprint

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
        filetime = os.path.getmtime(repo_path)
        current_time = time.time()
        if filetime < ( current_time - 86400 ):
            print("Repo out of date")
            fetch_repo()
        else:
            print("Repo up to date")
    else:
        print("Repo not on disk")
        fetch_repo()

def fetch_repo():
    print("Updating fdroid repo")
    url = "https://f-droid.org/repo/index-v1.jar"
    response = requests.get(url,stream=True)
    if response.status_code == requests.status_codes.codes.ok:
        zp = zipfile.ZipFile(BytesIO(response.content))
        fp = open(repo_path,"wb")
        fp.write(zp.open("index-v1.json").read())
        fp.close()

def search(package):
    json_data = open(repo_path)
    jdata = json.load(json_data)
    try:
        jdata["packages"][package]
    except:
        print("Unable to locate package")
        return
    for version in jdata["packages"][package]:
        print("{}: Version {} Updated: {}".format(package, version["versionCode"], version["added"]))

    json_data.close()
