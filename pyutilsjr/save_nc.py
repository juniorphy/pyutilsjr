# coding: utf-8 

__author__ = 'Marcelo Rodrigues'
__email__ = 'marcelorodriguesss@gmail.com'
__date__ = '07 Nov 2017'

from netCDF4 import Dataset


def save_nc(var, lat, lon, fname='sst_out.nc', year='1900'):

    foo = Dataset(fname, 'w', format='NETCDF4')

    foo.createDimension('Y', 181)
    foo.createDimension('X', 360)
    foo.createDimension('S', 12)
    foo.createDimension('M', 24)
    foo.createDimension('L', 10)

    x = foo.createVariable('X', 'f8', ('X'))
    x.units = 'degrees_E'
    x.long_name = 'longitude'
    x[:] = lon[:]

    y = foo.createVariable('Y', 'f8', ('Y'))
    y.units = 'degrees_N'
    y.long_name = 'latitude'
    y[:] = lat[:]

    s = foo.createVariable('S', 'f8', ('S'))
    s.units = 'months since {0}-01-15'.format(year)
    s.long_name = "forecast start time"
    s[:] = range(12)

    m = foo.createVariable('M', 'f8', ('M'))
    m.long_name = "member"
    m[:] = range(24)

    l = foo.createVariable('L', 'f8', ('L'))
    l.long_name = "lead"
    l[:] = range(10)

    # S=12, L=10. M=24, Y=181, X=360

    v = foo.createVariable('sst', float, ('S', 'L', 'M', 'Y', 'X'))
    v.long_name = 'sea surface temperature'
    v.units = '[C]'
    # v.missing_value = -999
    v[:] = var[:]

    foo.close()

