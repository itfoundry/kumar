#! /usr/bin/env AFDKOPython
# encoding: UTF-8
from __future__ import division, absolute_import, print_function, unicode_literals
import hindkit as kit

# ---

for tag, family in [
    (
        'Filled', kit.Family(
            client = 'Google Fonts',
            trademark = 'Kumar One',
            script = 'Gujarati',
        ),
    ),
    (
        'Outlined', kit.Family(
            client = 'Google Fonts',
            trademark = 'Kumar One Outline',
            script = 'Gujarati',
        ),
    ),
]:

    family.set_styles(kit.constants.styles.SINGLE)

    family.info.openTypeNameDesigner = "Parimal Parmar"
    family.info.openTypeHheaAscender, family.info.openTypeHheaDescender = (1050, -450)

    family.masters[0].filename = 'Kumar One-' + tag
    family.styles[0].abstract_directory = 'styles/' + tag

    project = kit.Project(
        family,
        fontrevision = '1.000',
        options = {
            # 'prepare_mark_positioning': True,
            'do_style_linking': True,
            'build_ttf': True,
        },
    )
    project.build()
