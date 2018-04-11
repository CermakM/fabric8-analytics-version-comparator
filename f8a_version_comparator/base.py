#!/usr/bin/env python

# Copyright © 2018 Red Hat Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Base class for maven version comparator tasks."""


from abc import ABCMeta, abstractmethod


class Base(metaclass=ABCMeta):
    """Base class for maven version comparator tasks."""

    @abstractmethod
    def compare_to(self):
        """Compare two maven versions."""
        raise NotImplementedError()

    @abstractmethod
    def is_none(self):
        """Check if none."""
        raise NotImplementedError()
