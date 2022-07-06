#!/usr/bin/env python3
import readline
import shlex

import downloader
import repos

class AS(object):
    prompt = 'AS> '
    commands = {}
    lists = {}
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
        exit()
    
    def do_download(args):
        'download REPO APP_NAME VERSION\n\teg: FDroid fr.ralala.hexviewer 132'
        downloader.download(args)

    def do_list(args):
        'list configured items arg[]'
        if not args == []:
            search = args[0].lower()
            if search in AS.lists:
                print("Listing ", search)
                for search_item in AS.lists[search]:
                        print(search_item)

            else:
                print(search_item, "not listable")

    def main(self):
        commands = {
                "exit":AS.do_exit,
                "help":AS.do_help,
                "echo":AS.do_echo,
                "download":AS.do_download,
                "list":AS.do_list
                }
        AS.commands = commands
        AS.lists['repos'] = repos.repositories
        print("Welcome to AndroidShell")
        while True:
            cmd, *args = shlex.split(input(AS.prompt))
            if cmd in commands:
                commands[cmd](args)

            else:
                print("Unknown command: {}".format(cmd))
                AS.do_help(args)

if __name__ == '__main__':
    app = AS()
    app.main()
