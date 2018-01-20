# coding: utf-8 

__author__ = 'Marcelo Rodrigues'
__email__ = 'marcelorodriguesss@gmail.com'
__credits__ = 'Fco Vasconcelos Junior, Marcelo Rodrigues'
__date__ = '07 Nov 2017'
__modified__ = '20 Jan 2018'

from netCDF4 import Dataset

def save_nc_sst_echam46(sst, lat, lon, fname='sst_out.nc', year='1900'):

    foo = Dataset(fname, 'w', format='NETCDF3_CLASSIC')

    foo.createDimension('lat', 64)
    foo.createDimension('lon', 128)
    foo.createDimension('time', 12

    x = foo.createVariable('lon', 'd', ('X'))
    x.units = 'degrees_E'
    x.long_name = 'longitude'
    x.axis = 'X'
    x[:] = lon[:]

    y = foo.createVariable('lat', 'd', ('Y'))
    y.units = 'degrees_N'
    y.long_name = 'latitude'
    y.axis = 'Y'
    y[:] = lat[:]

    l = foo.createVariable('time', 'i', ('time'))
    l.units = 'months since {0}-01-15'.format(year)
    l.calendar = '360_day'
    l.long_name = "time"
    l[:] = range(12)

    # L=12, Y=128, X=128

    v = foo.createVariable('sst', float, ('time','lat', 'lon'))
    v.long_name = 'sea surface temperature'
    v.units = '[K]'
    v.missing_value = -999
    v[:] = sst[:]

    foo.close()

