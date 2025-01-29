import pickle

import neuralgcm
import xarray
import gcsfs
from dinosaur import xarray_utils

gcs = gcsfs.GCSFileSystem(token='anon')

era5_path = 'gs://gcp-public-data-arco-era5/ar/full_37-1h-0p25deg-chunk-1.zarr-v3'
weatherbench2_source = 'gs://weatherbench2/datasets/era5/1959-2023_01_10-wb13-6h-1440x721_with_derived_variables.zarr'
full_era5 = xarray.open_zarr(gcs.get_mapper(era5_path), chunks={'time': 10})

# model_name = 'v1/deterministic_2_8_deg.pkl'  #@param ['v1/deterministic_0_7_deg.pkl', 'v1/deterministic_1_4_deg.pkl', 'v1/deterministic_2_8_deg.pkl', 'v1/stochastic_1_4_deg.pkl', 'v1_precip/stochastic_precip_2_8_deg.pkl', 'v1_precip/stochastic_evap_2_8_deg'] {type: "string"}
# with gcs.open(f'gs://neuralgcm/models/{model_name}', 'rb') as f:
#   ckpt = pickle.load(f)
# model = neuralgcm.PressureLevelModel.from_checkpoint(ckpt)

print(full_era5.attrs)

demo_start_time = '2023-01-01'
demo_end_time = '2023-01-31'
data_inner_steps = 24  # process every 24th hour

sliced_era5 = (
    full_era5
    [['geopotential', 'specific_humidity', 'temperature', 'u_component_of_wind', 'v_component_of_wind']]
    # .pipe(
    #     xarray_utils.selective_temporal_shift,
    #     variables=model.forcing_variables,
    #     time_shift='24 hours',
    # )
    .sel(time=slice(demo_start_time, demo_end_time, data_inner_steps))
    .compute()
)

print(sliced_era5)
