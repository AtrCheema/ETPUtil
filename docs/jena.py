import numpy as np
import pandas as pd
from ETUtil.ETUtil.et_methods import PenmanMonteith

_df = pd.read_csv('../data/jen_obj.txt')
# https://www.bgc-jena.mpg.de/wetter/Weatherstation.pdf
# TODO input df contains 'SWDR (W/m**2)', can that be used?
df = pd.DataFrame()
df[['rel_hum', 'wind_speed', 'temp', 'tdew',
    'rn']] = _df[['rh (%)', 'wv (m/s)', 'T (degC)', 'Tdew (degC)', 'Rn (W/m**2)']]

# rn = df['rn']
# rn = np.where(rn < 0.0, 0.0, rn)
# df['rn'] = rn

df.index = pd.to_datetime(_df['index'])
df.index.freq = pd.infer_freq(df.index)

units = {'temp': 'Centigrade',
         'rel_hum': 'percent',
         'tdew': 'Fahrenheit',
         'wind_speed': 'MilesPerHour'}

constants = dict()
constants['lat_dec_deg'] = 50.9
constants['altitude'] = 155
# These values are not accurate
constants['a_s'] = 0.23
constants['albedo'] = 0.23
constants['b_s'] = 0.5
constants['wind_z'] = 2

eto_model = PenmanMonteith(df, units=units, constants=constants, verbosity=2)
pet = eto_model()
#eto_model.plot_outputs()
