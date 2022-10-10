"""Configuration file for the ds003825 dataset.

Set the `MNE_BIDS_STUDY_CONFIG` environment variable to
"config_ds003825" to overwrite `config.py` with the values specified
below.

Download ds003825 from OpenNeuro: https://github.com/OpenNeuroDatasets/ds003825
"""

import itertools
from mne_bids import get_entity_vals

study_name = 'ds003825'

bids_root = f'/storage/store2/data/{study_name}'
deriv_root = f'/storage/store2/derivatives/{study_name}/mne-bids-pipeline/'

subjects = sorted(get_entity_vals(bids_root, entity_key='subject'))

task = 'rsvp'
interactive = False
ch_types = ['eeg']
resample_sfreq = 250.0
epochs_tmin = -0.05
epochs_tmax = 0.6
decim = 2
baseline = (None, 0)
reject = None
# reject = {'eeg': 150e-6}
conditions = ["animal", "food", "body part"]
contrasts = list(itertools.combinations(conditions, 2))
decode = True

# event_repeated = "drop"
run_source_estimation = False

N_JOBS = 20
# N_JOBS = 1

on_error = "debug"

# memory_location = False
