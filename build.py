#! /usr/bin/env AFDKOPython
# encoding: UTF-8
from __future__ import division, absolute_import, print_function, unicode_literals
import hindkit as kit

family = kit.Family(
    client = 'Google Fonts',
    script = 'Gujarati',
    trademark = 'Kumar One',
    designers = 'Parimal Parmar',
)
family.set_masters(
    [kit.Master(family, _file_name='Kumar One-Filled.ufo')]
)
family.set_styles(kit.constants.styles.SINGLE)

family_outlined = kit.Family(
    client = 'Google Fonts',
    script = 'Gujarati',
    trademark = 'Kumar One Outline',
    designers = 'Parimal Parmar',
)
family_outlined.set_masters(
    [kit.Master(family_outlined, _file_name='Kumar One-Outlined.ufo')]
)
family_outlined.set_styles(kit.constants.styles.SINGLE)

for f in [family, family_outlined]:
    builder = kit.Builder(
        f,
        fontrevision = '0.900',
        vertical_metrics = {
            'Ascender': 750,
            'Descender': -250,
            'LineGap': 200,
        },
        options = {
            # 'prepare_mark_positioning': True,
            'override_GDEF': True,
            'do_style_linking': True,
        },
    )
    builder.build()
