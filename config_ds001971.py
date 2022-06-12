"""Configuration file for the ds001971 dataset.

Set the `MNE_BIDS_STUDY_CONFIG` environment variable to
"config_ds001971" to overwrite `config.py` with the values specified
below.

Download ds001971 from OpenNeuro: https://github.com/OpenNeuroDatasets/ds001971
"""

# from mne_bids import get_entity_vals

study_name = 'ds001971'
bids_root = f'/storage/store2/data/{study_name}'
deriv_root = f'/storage/store2/derivatives/{study_name}/mne-bids-pipeline/'

# subjects = sorted(get_entity_vals(bids_root, entity_key='subject'))


task = 'AudioCueWalkingStudy'
interactive = False
ch_types = ['eeg']
reject = None
# reject = {'eeg': 150e-6}
conditions = ['UncuedWalking', 'PreferredCadence', 'AdvanceTempo', 'DelayTempo']
contrasts = [('UncuedWalking', 'AdvanceTempo')]
decode = False

# subjects = ['001']
# subjects = ['008']

# not all runs have the same number of channels
exclude_subjects = ['002', '003', '004', '005', '018', '019']

runs = ['01', '02', '03', '04']

event_repeated = "drop"
run_source_estimation = False

N_JOBS = 10
N_JOBS = 1

on_error = "debug"
