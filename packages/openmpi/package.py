#!/usr/bin/env python
"""
Copyright 2017 ARC Centre of Excellence for Climate Systems Science

author: Scott Wales <scott.wales@unimelb.edu.au>

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
from spack import *
import os.path

class Openmpi(Package):
    """
    NCI-specific MPI package

    Needs to load the correct wrappers for NCI's environment
    """
    provides('mpi')

    version('1.4.3')
    version('1.6.5')
    version('1.7.5')
    version('1.8.8')
    version('1.10.3')
    version('2.0.0')

    variant('thread_multiple', default=False,
            description='Enable MPI_THREAD_MULTIPLE support')

    variant('debug', default=False)

    provides('mpi@:2.2', when='@1.6.5')
    provides('mpi@:3.0', when='@1.7.5:')
    provides('mpi@:3.1', when='@2.0.0:')

    def url_for_version(self, version):
        return '/dev/null'

    def setup_dependent_package(self, module, dependent_spec):
        self.spec.mpicc  = os.path.join(env['OPENMPI_ROOT'],'bin','mpicc')
        self.spec.mpicxx = os.path.join(env['OPENMPI_ROOT'],'bin','mpicxx')
        self.spec.mpifc  = '/apps/openmpi/wrapper/fortran/mpif90'
        self.spec.mpif77 = '/apps/openmpi/wrapper/fortran/mpif90'

