#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Command: !tips
"""

import random

def _tips():
    return ['man who stand on toilet, get high on pot.',
            'man who run in front of car, get tired.']

def random_tip():
    """Return random tip."""
    tip = random.choice(_tips())
    return tip

def all_tips():
    """Return all tips."""
    return _tips()
