import xarray
import gcsfs

gcs = gcsfs.GCSFileSystem(token='anon')

era5_path = 'gs://gcp-public-data-arco-era5/ar/full_37-1h-0p25deg-chunk-1.zarr-v3'
full_era5 = xarray.open_zarr(gcs.get_mapper(era5_path), chunks=None)

demo_start_time = '2023-01-01'
demo_end_time = '2023-01-02'
data_inner_steps = 6

sliced_era5 = (
    full_era5
    [['geopotential', 'specific_humidity', 'temperature', 'u_component_of_wind', 'v_component_of_wind']]
    .sel(
        time=slice(demo_start_time, demo_end_time, data_inner_steps),
        latitude=slice(-35, -22),
        longitude=slice(16, 33),
    )
    .compute()
)

print(sliced_era5)