from invoke import task
import os


@task
def serve(c):
    re_exec("pelican content -l -r -t theme")


def re_exec(cmd):
    args = cmd.split(" ")
    os.execvp(args[0], args)
