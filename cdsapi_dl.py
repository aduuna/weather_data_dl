import cdsapi

client = cdsapi.Client()

dataset = 'reanalysis-era5-pressure-levels'
request = {
    'product_type': ['reanalysis'],
    'variable': ['geopotential'],
    'year': ['2023'],
    'month': ['01'],
    'day': ['01'],
    'time': ['00:00', '06:00', '12:00', '18:00'],
    'pressure_level': ['500'],
    'data_format': 'netcdf4',
}
target = 'download.nc'

client.retrieve(dataset, request, target)
