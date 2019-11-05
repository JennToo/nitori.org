from invoke import task
import os


@task
def serve(c):
    re_exec("pelican content -l -r -t theme -b 0.0.0.0")


@task
def build(c):
    c.run("pelican content -t theme")
    with open("output/.nojekyll", "w") as f:
        f.write("")


def re_exec(cmd):
    args = cmd.split(" ")
    os.execvp(args[0], args)
