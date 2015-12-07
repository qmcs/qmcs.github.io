#!/usr/bin/env python3

import json
import requests
import os
import sys
import subprocess
import git

PR_FMT = 'https://{uname}:{token}@api.github.com/repos/qmcs/qmcs.github.io/pulls/{number}'
COMMIT_MSG_FMT = 'Automerged PR {number}'

def check_envs():
    if ('EECS_GITHUB_TOKEN' not in os.environ) or ('GITHUB_USER' not in os.environ):
        if os.path.exists('./github_admin_auth.py'):
            import github_admin_auth
        else:
            raise ValueError('Environment variables EECS_GITHUB_TOKEN and GITHUB_USER not set')


def merge_pr(number):
    global MERGE_FMT
    uname = os.environ['GITHUB_USER']
    token = os.environ['EECS_GITHUB_TOKEN']
    pr_uri = PR_FMT.format(**locals())

    resp = requests.get(pr_uri)
    req_body = {
        'commit_message': COMMIT_MSG_FMT.format(**locals()),
        'sha': resp.json()['head']['sha']
    }

    resp = requests.request('PUT', pr_uri + '/merge', json=req_body)

    if 'merged' not in resp.json():
        print('PR not merged, response below: ')
        print(resp.json())
        sys.exit(1)

def pull():
    repo = git.Repo(os.getcwd())
    repo.remotes.origin.pull()
    return repo

def publish_master():
    subprocess.call(['make', 'github'])

def push_master(repo):
    rgit = repo.git
    rgit.checkout('master')
    rgit.push('origin', 'master')


if __name__ == '__main__':
    pr_number = int(sys.argv[1])
    check_envs()
    merge_pr(pr_number)
    repo = pull()
    publish_master()
    push_master(repo)

