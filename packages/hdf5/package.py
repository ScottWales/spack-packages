##############################################################################
# Copyright (c) 2013-2016, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the LICENSE file for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install hdf5
#
# You can edit this file again by typing:
#
#     spack edit hdf5
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *


class Hdf5(AutotoolsPackage):
    """HDF5 is a data model, library, and file format for storing and managing
    data. It supports an unlimited variety of datatypes, and is designed for
    flexible and efficient I/O and for high volume and complex data. HDF5 is
    portable and is extensible, allowing applications to evolve in their use of
    HDF5. The HDF5 Technology suite includes tools and applications for
    managing, manipulating, viewing, and analyzing data in the HDF5 format."""

    homepage = "https://support.hdfgroup.org/HDF5/"
    url      = "https://support.hdfgroup.org/ftp/HDF5/current18/src/hdf5-1.8.18.tar.bz2"

    version('1.8.18', '29117bf488887f89888f9304c8ebea0b')
    depends_on('mpi')

    phases = ['configure', 'build', 'install']

    def configure(self, spec, prefix):
        print('PATH = %s'%env['PATH'])
        env['CC'] = spec['mpi'].mpicc
        env['CXX'] = spec['mpi'].mpicxx
        env['F77'] = spec['mpi'].mpif77
        env['FC'] = spec['mpi'].mpifc
        super(Hdf5,self).configure(spec, prefix)

    def configure_args(self):
        args = ['--enable-fortran',
                '--enable-fortran2003',
                '--enable-cxx',
                '--enable-parallel',
                '--enable-production',
                '--enable-unsupported']
        return args
