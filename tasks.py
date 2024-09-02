from invoke import task
import os


@task
def serve(c):
    re_exec("pelican content -l --relative-urls -r -t theme -b 0.0.0.0")


@task
def build(c):
    c.run("pelican content -t theme")

    c.run("rm -rf output/theme/.webassets-cache")
    with open("output/.nojekyll", "w") as f:
        f.write("")
    with open("output/CNAME", "w") as f:
        f.write("nitori.org\n")


def re_exec(cmd):
    args = cmd.split(" ")
    os.execvp(args[0], args)
