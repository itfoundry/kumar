#! /usr/bin/env AFDKOPython
# encoding: UTF-8
from __future__ import division, absolute_import, print_function, unicode_literals
import hindkit as kit

family_filled = kit.Family(
    client = 'Google Fonts',
    trademark = 'Kumar One',
    script = 'Gujarati',
    hide_script_name = True,
)
family_filled.set_masters([kit.Master(family_filled, 'Regular', 0)])
family_filled.set_styles(kit.constants.styles.SINGLE)

family_outlined = kit.Family(
    client = 'Google Fonts',
    trademark = 'Kumar One Outline',
    script = 'Gujarati',
    hide_script_name = True,
)
family_outlined.set_masters([kit.Master(family_outlined, 'Regular', 0)])
family_outlined.set_styles(kit.constants.styles.SINGLE)

for family in [family_filled, family_outlined]:
    builder = kit.Builder(
        family,
        fontrevision = '0.201',
        vertical_metrics = {
            'Ascender': 750,
            'Descender': -250,
            'LineGap': 200,
        },
        options = {
            'prep_mark_positioning': True,
            'override_GDEF': True,
            'do_style_linking': True,
        },
    )
    builder.build()
