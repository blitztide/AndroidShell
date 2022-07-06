#!/usr/bin/env python3
import readline
import shlex

import downloader
import repos
import analyser

class AS(object):
    prompt = 'AS> '
    commands = {}
    lists = {}
    should_exit = False

    def do_analyse(args):
        'Starts analysis of a chosen repo package version'
        analyser.do_analysis(args)

    def do_help(args):
        'Prints help commands'
        print("Android shell commands:")
        for x in AS.commands:
            print(x, " - ", AS.commands[x].__doc__)

    def do_echo(args):
        'Returns the arguments supplied'
        print(args)

    def do_exit(args):
        'Exits the application'
        AS.should_exit = True
    
    def do_download(args):
        'download REPO APP_NAME VERSION\n\teg: FDroid fr.ralala.hexviewer 132'
        downloader.download(args)

    def do_list(args):
        'list configured items arg[]'
        if not args == []:
            search = args[0].lower()
            if search in AS.lists:
                for search_item in AS.lists[search]:
                    print(search_item)  
            else:
                print(search, "not listable")
        else:
            AS.do_help(args)

    def do_update(args):
        'Updates a specified repo'
        if len(args) == 1:
            repos.repo_update(args[0])

    def main(self):
        commands = {
                "exit":AS.do_exit,
                "help":AS.do_help,
                "echo":AS.do_echo,
                "download":AS.do_download,
                "list":AS.do_list,
                "analyse":AS.do_analyse,
                "update":AS.do_update
                }
        AS.commands = commands
        AS.lists['repos'] = repos.repositories
        print("Welcome to AndroidShell")
        while True:
            if AS.should_exit:
                exit()
            cmd, *args = shlex.split(input(AS.prompt))
            try:
                if cmd in commands:
                    commands[cmd](args)

                else:
                    print("Unknown command: {}".format(cmd))
                    AS.do_help(args)
            except Exception as e:
                print("Error", e)

if __name__ == '__main__':
    app = AS()
    app.main()
