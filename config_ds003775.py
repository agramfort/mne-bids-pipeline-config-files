import pathlib
from mne_bids import get_entity_vals

study_name = 'ds003775'
bids_root = pathlib.Path('/storage/store2/data/ds003775')
deriv_root = pathlib.Path('/storage/store2/derivatives/ds003775/mne-bids-pipeline')
# subjects_dir = None
subjects_dir = str(bids_root / 'derivatives' / 'freesurfer')

N_JOBS = 10
# N_JOBS = 1

subjects = sorted(get_entity_vals(bids_root, entity_key='subject'))
# subjects = subjects[:1]

sessions = ["t1"]

run_source_estimation = False

ch_types = ['eeg']
reader_extra_params = {"units": "uV"}

baseline = None
# reject = dict(grad=3000e-13, mag=3.5e-12, eog=150e-6)
reject = None
# reject = "autoreject_global"
# spatial_filter = 'ssp'
spatial_filter = None

h_freq = 40
l_freq = None

task = "resteyesc"
task_is_rest = True
epochs_tmin = 0.
epochs_tmax = 10.
rest_epochs_overlap = 0.
rest_epochs_duration = 10.
baseline = None

parallel_backend = 'loky'
dask_open_dashboard = True

on_error = 'continue'
# on_error = 'abort'
# on_error = 'debug'

# log_level = 'debug'
log_level = 'info'
