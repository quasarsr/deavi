"""
Copyright (C) 2016-2020 Quasar Science Resources, S.L.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
OR OTHER DEALINGS IN THE SOFTWARE.
"""
from pipeline.luigi_tasks import avi_task, parameter, local_target

from avi.task.algorithm_task import algorithm_task
from avi.task.gaia_query_task import gaia_query_task
from avi.task.herschel_query_task import herschel_query_task

from avi.log import logger

class algorithm(avi_task):
    request = parameter()
    alg_name = parameter()
    params = parameter()
    results = parameter()

    def output(self):
        algorithm_task().output()
        return local_target("/data/output/test.text")

    def run(self):
        t = algorithm_task()
        t.task_id = self.request.algorithm_model_model.pk
        t.task_data.data = self.params
        t.run()

class gaia_query(avi_task):
    request = parameter()
    name_coord = parameter()
    name = parameter()
    input_file = parameter()
    ra = parameter()
    dec = parameter()
    shape = parameter()
    radius = parameter()
    width = parameter()
    height = parameter()
    polygon = parameter()
    table = parameter()
    params = parameter()
    file_name = parameter()
    adql = parameter()

    def output(self):
        gaia_query_task().output()

    def run(self):
        t = gaia_query_task()
        data = {'name_coord':self.name_coord,
                'name':self.name,
                'input_file':self.input_file,
                'ra':self.ra,
                'dec':self.dec,
                'shape':self.shape,
                'radius':self.radius,
                'width':self.width,
                'height':self.height,
                'polygon':self.polygon,
                'table':self.table,
                'params':self.params,
                'output_file':self.file_name,
                'adql':self.adql}
        t.task_data.data = data
        t.task_id = self.request.gaia_query_model_model.pk
        t.run()

class herschel_query(avi_task):
    request = parameter()
    name_coord = parameter()
    name = parameter()
    input_file = parameter()
    ra = parameter()
    dec = parameter()
    shape = parameter()
    radius = parameter()
    width = parameter()
    height = parameter()
    polygon = parameter()
    positional_images = parameter()
    table = parameter()
    instrument = parameter()
    level = parameter()
    params = parameter()
    file_name = parameter()
    adql = parameter()
    
    def output(self):
        herschel_query_task().output()
    def run(self):
        log = logger().get_log('risea')
        log.info('deavi_task run...')
        t = herschel_query_task()
        t.task_id = self.request.herschel_query_model_model.pk
        data = {'name_coord':self.name_coord,
                'name':self.name,
                'input_file':self.input_file,
                'ra':self.ra,
                'dec':self.dec,
                'shape':self.shape,
                'radius':self.radius,
                'width':self.width,
                'height':self.height,
                'polygon':self.polygon,
                'positional_images':self.positional_images,
                'table':self.table,
                'instrument':self.instrument,
                'level':self.level,
                'params':self.params,
                'output_file':self.file_name,
                'adql':self.adql}
        t.task_data.data = data
        t.run()
