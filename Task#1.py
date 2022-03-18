#!/usr/bin/env python3

import re

# ukol za 3 body
def camel_to_snake_case(name):
    """Transfer camelCaseNames to snake_case_names.

    >>> camel_to_snake_case('camelCaseNameAllowed')
    'camel_case_name_allowed'
    >>> camel_to_snake_case('longVATNumber')
    'long_vat_number'
    """

    inbetween = re.compile(r'''
                            (
                             (?<!^)[A-Z](?=[a-z])
                             |
                             (?<!^)(?<=[a-z])[A-Z]
                            )
                            ''', re.VERBOSE)
    return inbetween.sub(r'_\1', name).lower()

if __name__ == "__main__":
    import doctest
    doctest.testmod()