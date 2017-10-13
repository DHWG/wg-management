#!/bin/sh

alias dpm="python wgaccounting/manage.py"
dpm migrate
dpm runserver
