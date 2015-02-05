#!/usr/bin/env python
# Copyright (c) 2009-2014 Jonathan M. Lange <jml@mumak.net>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys

from bzrlib import patches
from difftodo import get_comments_from_diff, todos_from_comments


def comments_from_diff():
    phile = sys.stdin
    for comment in get_comments_from_diff(patches.parse_patches(phile)):
        print str(comment)


# XXX: Allow customization of TODO tags.

def todos_from_diff():
    comments = get_comments_from_diff(patches.parse_patches(sys.stdin))
    tags = ('XXX', 'TODO')
    number = -1
    for number, todo in enumerate(todos_from_comments(comments, tags)):
        print todo
    print "Things to do: %s" % (number + 1)
