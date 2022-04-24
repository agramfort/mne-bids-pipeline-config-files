"""
OMEGA Resting State Sample Data
"""

study_name = 'ds000247'
bids_root = f'/storage/store/data/{study_name}'
deriv_root = f'/storage/store2/derivatives/{study_name}/mne-bids-pipeline/'
subjects_dir = f'{bids_root}/derivatives/freesurfer/subjects'

N_JOBS = 10

# subjects = ['0002']
# sessions = ['01']
task = 'rest'

ch_types = ['meg']
spatial_filter = 'ssp'

l_freq = 1.0
h_freq = 40.0

rest_epochs_duration = 10
rest_epochs_overlap = 0
epochs_tmin = 0
baseline = None
