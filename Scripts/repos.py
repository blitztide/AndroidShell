import fdroid

repositories = {
        "fdroid" : fdroid,
}

def get_repo_name(match_object):
    if match_object in repositories:
        return repositories[match_object].name
    else:
        return None


def download(repo, package, version):
    if repo in repositories:
        repositories[repo].download(package,version)
        return "OK"
    else:
        return "ERR_NO_DOWNLOADER"

def check_exists(repo,package,version):
    if repo in repositories:
        return repositories[repo].check_exists(package,version)
    else:
        return "ERR_NO_CHECK_EXISTS"
