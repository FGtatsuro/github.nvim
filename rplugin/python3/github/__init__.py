#!/usr/bin/env python
# -*- coding: utf-8 -*-

import neovim

from github.github import GithubHandler


@neovim.plugin
class GithubPlugin():

    def __init__(self, nvim):
        self.handler = GithubHandler(nvim)

    @neovim.command('GithubWebOpen')
    def webopen(self):
        self.handler.open_github_webpage()

# https://wiki.python.org/moin/Vim
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
