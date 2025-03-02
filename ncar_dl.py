"""
format: NetCDF4
Valid Date Range: Jan 2023-Feb 2023
to Parameter(s):  Geopotential, Relative Humidity, Temperature, U/V component of wind
Vertical Level(s): 500 hpa
Gridded Product:  Analysis
Grid:  0.25° x 0.25° from 0E to 359.75E and 90N to 90S (1440 x 721 Longitude/Latitude)
total size: 221884.17 mb
"""
#! /usr/bin/env python3
#
# python script to download selected files from rda.ucar.edu
# after you save the file, don't forget to make it executable
#   i.e. - "chmod 755 <name_of_script>"
#
import requests
#
files = [
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_129_z.ll025sc.2023010100_2023010123.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_130_t.ll025sc.2023010100_2023010123.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_131_u.ll025uv.2023010100_2023010123.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_132_v.ll025uv.2023010100_2023010123.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_157_r.ll025sc.2023010100_2023010123.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_129_z.ll025sc.2023010200_2023010223.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_130_t.ll025sc.2023010200_2023010223.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_131_u.ll025uv.2023010200_2023010223.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_132_v.ll025uv.2023010200_2023010223.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_157_r.ll025sc.2023010200_2023010223.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_129_z.ll025sc.2023010300_2023010323.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_130_t.ll025sc.2023010300_2023010323.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_131_u.ll025uv.2023010300_2023010323.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_132_v.ll025uv.2023010300_2023010323.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_157_r.ll025sc.2023010300_2023010323.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_129_z.ll025sc.2023010400_2023010423.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_130_t.ll025sc.2023010400_2023010423.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_131_u.ll025uv.2023010400_2023010423.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_132_v.ll025uv.2023010400_2023010423.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_157_r.ll025sc.2023010400_2023010423.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_129_z.ll025sc.2023010500_2023010523.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_130_t.ll025sc.2023010500_2023010523.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_131_u.ll025uv.2023010500_2023010523.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_132_v.ll025uv.2023010500_2023010523.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_157_r.ll025sc.2023010500_2023010523.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_129_z.ll025sc.2023010600_2023010623.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_130_t.ll025sc.2023010600_2023010623.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_131_u.ll025uv.2023010600_2023010623.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_132_v.ll025uv.2023010600_2023010623.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_157_r.ll025sc.2023010600_2023010623.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_129_z.ll025sc.2023010700_2023010723.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_130_t.ll025sc.2023010700_2023010723.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_131_u.ll025uv.2023010700_2023010723.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_132_v.ll025uv.2023010700_2023010723.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_157_r.ll025sc.2023010700_2023010723.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_129_z.ll025sc.2023010800_2023010823.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_130_t.ll025sc.2023010800_2023010823.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_131_u.ll025uv.2023010800_2023010823.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_132_v.ll025uv.2023010800_2023010823.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_157_r.ll025sc.2023010800_2023010823.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_129_z.ll025sc.2023010900_2023010923.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_130_t.ll025sc.2023010900_2023010923.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_131_u.ll025uv.2023010900_2023010923.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_132_v.ll025uv.2023010900_2023010923.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_157_r.ll025sc.2023010900_2023010923.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_129_z.ll025sc.2023011000_2023011023.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_130_t.ll025sc.2023011000_2023011023.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_131_u.ll025uv.2023011000_2023011023.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_132_v.ll025uv.2023011000_2023011023.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_157_r.ll025sc.2023011000_2023011023.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_129_z.ll025sc.2023011100_2023011123.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_130_t.ll025sc.2023011100_2023011123.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_131_u.ll025uv.2023011100_2023011123.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_132_v.ll025uv.2023011100_2023011123.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_157_r.ll025sc.2023011100_2023011123.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_129_z.ll025sc.2023011200_2023011223.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_130_t.ll025sc.2023011200_2023011223.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_131_u.ll025uv.2023011200_2023011223.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_132_v.ll025uv.2023011200_2023011223.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_157_r.ll025sc.2023011200_2023011223.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_129_z.ll025sc.2023011300_2023011323.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_130_t.ll025sc.2023011300_2023011323.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_131_u.ll025uv.2023011300_2023011323.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_132_v.ll025uv.2023011300_2023011323.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_157_r.ll025sc.2023011300_2023011323.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_129_z.ll025sc.2023011400_2023011423.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_130_t.ll025sc.2023011400_2023011423.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_131_u.ll025uv.2023011400_2023011423.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_132_v.ll025uv.2023011400_2023011423.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_157_r.ll025sc.2023011400_2023011423.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_129_z.ll025sc.2023011500_2023011523.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_130_t.ll025sc.2023011500_2023011523.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_131_u.ll025uv.2023011500_2023011523.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_132_v.ll025uv.2023011500_2023011523.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_157_r.ll025sc.2023011500_2023011523.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_129_z.ll025sc.2023011600_2023011623.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_130_t.ll025sc.2023011600_2023011623.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_131_u.ll025uv.2023011600_2023011623.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_132_v.ll025uv.2023011600_2023011623.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_157_r.ll025sc.2023011600_2023011623.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_129_z.ll025sc.2023011700_2023011723.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_130_t.ll025sc.2023011700_2023011723.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_131_u.ll025uv.2023011700_2023011723.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_132_v.ll025uv.2023011700_2023011723.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_157_r.ll025sc.2023011700_2023011723.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_129_z.ll025sc.2023011800_2023011823.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_130_t.ll025sc.2023011800_2023011823.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_131_u.ll025uv.2023011800_2023011823.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_132_v.ll025uv.2023011800_2023011823.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_157_r.ll025sc.2023011800_2023011823.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_129_z.ll025sc.2023011900_2023011923.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_130_t.ll025sc.2023011900_2023011923.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_131_u.ll025uv.2023011900_2023011923.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_132_v.ll025uv.2023011900_2023011923.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_157_r.ll025sc.2023011900_2023011923.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_129_z.ll025sc.2023012000_2023012023.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_130_t.ll025sc.2023012000_2023012023.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_131_u.ll025uv.2023012000_2023012023.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_132_v.ll025uv.2023012000_2023012023.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_157_r.ll025sc.2023012000_2023012023.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_129_z.ll025sc.2023012100_2023012123.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_130_t.ll025sc.2023012100_2023012123.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_131_u.ll025uv.2023012100_2023012123.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_132_v.ll025uv.2023012100_2023012123.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_157_r.ll025sc.2023012100_2023012123.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_129_z.ll025sc.2023012200_2023012223.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_130_t.ll025sc.2023012200_2023012223.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_131_u.ll025uv.2023012200_2023012223.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_132_v.ll025uv.2023012200_2023012223.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_157_r.ll025sc.2023012200_2023012223.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_129_z.ll025sc.2023012300_2023012323.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_130_t.ll025sc.2023012300_2023012323.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_131_u.ll025uv.2023012300_2023012323.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_132_v.ll025uv.2023012300_2023012323.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_157_r.ll025sc.2023012300_2023012323.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_129_z.ll025sc.2023012400_2023012423.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_130_t.ll025sc.2023012400_2023012423.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_131_u.ll025uv.2023012400_2023012423.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_132_v.ll025uv.2023012400_2023012423.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_157_r.ll025sc.2023012400_2023012423.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_129_z.ll025sc.2023012500_2023012523.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_130_t.ll025sc.2023012500_2023012523.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_131_u.ll025uv.2023012500_2023012523.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_132_v.ll025uv.2023012500_2023012523.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_157_r.ll025sc.2023012500_2023012523.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_129_z.ll025sc.2023012600_2023012623.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_130_t.ll025sc.2023012600_2023012623.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_131_u.ll025uv.2023012600_2023012623.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_132_v.ll025uv.2023012600_2023012623.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_157_r.ll025sc.2023012600_2023012623.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_129_z.ll025sc.2023012700_2023012723.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_130_t.ll025sc.2023012700_2023012723.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_131_u.ll025uv.2023012700_2023012723.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_132_v.ll025uv.2023012700_2023012723.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_157_r.ll025sc.2023012700_2023012723.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_129_z.ll025sc.2023012800_2023012823.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_130_t.ll025sc.2023012800_2023012823.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_131_u.ll025uv.2023012800_2023012823.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_132_v.ll025uv.2023012800_2023012823.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_157_r.ll025sc.2023012800_2023012823.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_129_z.ll025sc.2023012900_2023012923.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_130_t.ll025sc.2023012900_2023012923.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_131_u.ll025uv.2023012900_2023012923.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_132_v.ll025uv.2023012900_2023012923.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_157_r.ll025sc.2023012900_2023012923.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_129_z.ll025sc.2023013000_2023013023.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_130_t.ll025sc.2023013000_2023013023.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_131_u.ll025uv.2023013000_2023013023.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_132_v.ll025uv.2023013000_2023013023.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_157_r.ll025sc.2023013000_2023013023.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_129_z.ll025sc.2023013100_2023013123.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_130_t.ll025sc.2023013100_2023013123.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_131_u.ll025uv.2023013100_2023013123.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_132_v.ll025uv.2023013100_2023013123.nc",
    "e5.oper.an.pl/202301/e5.oper.an.pl.128_157_r.ll025sc.2023013100_2023013123.nc",
    "e5.oper.an.pl/202302/e5.oper.an.pl.128_157_r.ll025sc.2023020100_2023020123.nc",
]
#
# download the data file(s)
for file in files:
    idx = file.rfind("/")
    if (idx > 0):
        ofile = file[idx+1:]
    else:
        ofile = file

    response = requests.get("https://data.rda.ucar.edu/d633000/" + file)
    with open(ofile, "wb") as f:
        f.write(response.content)
