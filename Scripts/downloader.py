import re
import repos


def download(args):
    if not len(args) == 3:
        return "ERR_ARG"
    repo,package,version = args
    print("Repo: {}\nPackage:{}\nVersion:{}".format(repo,package,version))

    # Getting Package repo
    status = repos.check_exists(repo,package,version)
    if status == "OK":
        status = repos.download(repo,package,version)
    if not status == "OK":
        print("Error downloading: ",status)
    else:
        return "OK"


def download_url(args):
    if args == []:
        print("No argument supplied")
        return

    URI = re.match('(https?|ftp):\/\/([^\/]+)',args[0])
    if URI == None:
        print("Error URL not parsable")
        return
    repo = repos.get_repo_name(URI.group(2))
    if repo == None:
        print("Error Repository does not exist in codebase")
    else:
        print(repo)
