#! /usr/bin/env AFDKOPython
# encoding: UTF-8
from __future__ import division, absolute_import, print_function, unicode_literals
import hindkit as kit

# ---

for name, tag in [
    ('Kumar One', 'Filled'),
    ('Kumar One Outline', 'Outlined'),
]:

    family = kit.Family(
        client = 'Google Fonts',
        base_name = name,
        script = 'Gujarati',
    )

    family.set_styles(kit.constants.styles.SINGLE)

    i = family.info
    i.openTypeNameDesigner = "Parimal Parmar"
    i.openTypeHheaAscender, i.openTypeHheaDescender = (1150, -650)

    family.masters[0].filename = 'Kumar One-' + tag
    family.styles[0].abstract_directory = 'styles/' + tag

    project = kit.Project(
        family,
        fontrevision = '1.001',
        options = {
            # 'prepare_mark_positioning': True,
            'do_style_linking': True,
            'build_ttf': True,
        },
    )
    project.build()
