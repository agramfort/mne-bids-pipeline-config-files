"""
hMT+ Localizer
"""
from mne_bids import get_entity_vals

study_name = 'ds003392'
bids_root = f'/storage/store2/data/{study_name}'
deriv_root = f'/storage/store2/derivatives/{study_name}/mne-bids-pipeline/'
subjects_dir = f'{bids_root}/derivatives/freesurfer/subjects'

# subjects = "all"
subjects = sorted(get_entity_vals(bids_root, entity_key='subject'))
# exclude_subjects = ["06"]  # projs were applied during acquisition...
# subjects = sorted(list(set(subjects) - set(exclude_subjects)))
# subjects = ['01']
N_JOBS = len(subjects)
# N_JOBS = 1

task = 'localizer'
find_flat_channels_meg = True
find_noisy_channels_meg = True
use_maxwell_filter = True
ch_types = ['meg']

l_freq = 1.
h_freq = 40.
resample_sfreq = 250

# Artifact correction.
spatial_filter = 'ica'
ica_max_iterations = 500
ica_l_freq = 1.
ica_n_components = 0.99
ica_reject_components = 'auto'

# Epochs
epochs_tmin = -0.2
epochs_tmax = 1.0
baseline = (None, 0)

# Conditions / events to consider when epoching
conditions = ['coherent', 'incoherent']

# Decoding
decode = True
contrasts = [('incoherent', 'coherent')]

# Noise estimation
process_er = True
noise_cov = 'emptyroom'

on_error = "debug"
