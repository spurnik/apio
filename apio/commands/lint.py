# -*- coding: utf-8 -*-
# -- This file is part of the Apio project
# -- (C) 2016-2018 FPGAwars
# -- Author Jesús Arroyo
# -- Licence GPLv2

import click

from apio.managers.scons import SCons

# Python3 compat
import sys
if (sys.version_info > (3, 0)):
    unicode = str


@click.command('lint')
@click.pass_context
@click.option('-p', '--project-dir', type=unicode, metavar='path',
              help='Set the target directory for the project.')
@click.option('-a', '--all', is_flag=True,
              help='Enable all warnings, including code style warnings.')
def cli(ctx, project_dir, all):
    """Lint the verilog code."""
    exit_code = SCons(project_dir).lint({
        'all': all
        })
    ctx.exit(exit_code)
