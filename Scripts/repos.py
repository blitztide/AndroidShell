import fdroid

repositories = {
        "fdroid" : fdroid,
}

repo_commands = {
}

def do_repo(args):
    'parse repo command and dispatch'
    command, *subargs = args
    if command in repo_commands:
        repo_commands[command](subargs)
    else:
        return "ERR_NOTIMPL"

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

def repo_update(repo):
    if repo in repositories:
        repositories[repo].update_repo()
    else:
        return "ERR_NO_UPDATE"

def repo_search(args):
    if len(args)== 2:
        repo,package = args
        if repo in repositories:
            repositories[repo].search(package)
        else:
            print(repo,"not found")
            return "ERR_NO_UPDATE"

repo_commands['search']=repo_search
