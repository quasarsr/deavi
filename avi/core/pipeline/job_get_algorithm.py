"""
Copyright (C) 2016-2018 Quasar Science Resources, S.L.

This file is part of DEAVI.

DEAVI is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

DEAVI is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Foobar.  If not, see <http://www.gnu.org/licenses/>.
"""
from .job import job as parent

from avi.log import logger

class get_algorithm(parent):
    def start(self, data):
        log = logger().get_log('views')
        log.info(data)
        from avi.core.algorithm.algorithm_manager import algorithm_manager
        res = algorithm_manager().get_algorithm(data)
        self.job_data.data = {}
        self.job_data.ok = True
        return self.job_data
