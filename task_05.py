#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Using *args and **kwargs"""


def mass_multiplier(*args):
    """Runs the mass multiplier function
       Args: *args, unlimited arguments"""
    retval = 1
    for arg in args:
        retval *= arg
    return retval


def student_report(name, age, school_id, **kwargs):
    """Compiles a student report as a dictionary"""
    kwargs['name'] = name
    kwargs['age'] = age
    kwargs['school_id'] = school_id
    return kwargs
