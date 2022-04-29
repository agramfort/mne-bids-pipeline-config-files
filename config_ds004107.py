"""MIND dataset
"""

import os
from mne_bids import get_entity_vals

study_name = 'ds004107'
bids_root = f'/storage/store2/data/{study_name}'
deriv_root = f'/storage/store2/derivatives/{study_name}/mne-bids-pipeline/'
subjects_dir = f'{bids_root}/derivatives/freesurfer/subjects'

subjects = sorted(get_entity_vals(bids_root, entity_key='subject'))
# subjects = subjects[:1]
# subjects = ['mind002']
# subjects = ['mind005']

ch_types = ['meg']
find_flat_channels_meg = False
find_noisy_channels_meg = False
# find_flat_channels_meg = True
# find_noisy_channels_meg = True
use_maxwell_filter = False

baseline = (None, 0)
# reject = dict(grad=3000e-13, mag=3.5e-12, eog=150e-6)
reject = None
reject = "autoreject_global"
spatial_filter = 'ssp'

h_freq = 110
l_freq = None

report_evoked_n_time_points = 3
report_stc_n_time_points = 3

task = "auditory"
if "MNE_BIDS_STUDY_TASK" in os.environ and os.environ['MNE_BIDS_STUDY_TASK']:
    task = os.environ['MNE_BIDS_STUDY_TASK']


def mri_landmarks_kind(bids_path):
    return f"ses-{bids_path.session}"


if task == 'auditory':
    conditions = ['right/noise', 'left/noise',
                  'right/4000', 'left/4000',
                  'right/2500', 'left/2500',
                  'right/500', 'left/500',
                  'right', 'left']
    contrasts = [('right', 'left')]
    tmin, tmax = -0.2, 0.4
    exclude_subjects = ['mind007']  # missing session 1
    exclude_subjects += ['mind010']  # no noise conditions
    exclude_subjects += ['mind006']  # no noise conditions
elif task == 'median':
    conditions = ['right', 'left']
    tmin, tmax = -0.2, 0.5
    contrasts = [('right', 'left')]
    # exclude_subjects = ['mind005', 'mind006', 'mind007', 'mind008',
    #                     'mind009', 'mind010']
    exclude_subjects = []
elif task == 'index':
    conditions = ['right', 'left']
    tmin, tmax = -0.2, 0.5
    exclude_subjects = []
    # exclude_subjects = ['mind009']  # 2 files...
    contrasts = [('right', 'left')]
elif task == 'visual':
    conditions = ['right', 'left']
    tmin, tmax = -0.2, 0.8
    exclude_subjects = ['mind002']  # bad sampling freq
    contrasts = [('right', 'left')]
else:
    raise ValueError()

if task in ['median', 'index']:
    fix_stim_artifact = True
    stim_artifact_tmin = 0.
    stim_artifact_tmax = 0.01

N_JOBS = 30
# parallel_backend = 'dask'
parallel_backend = 'loky'
# dask_open_dashboard = True

# N_JOBS = 1
allow_maxshield = True


def get_t1_from_meeg(bids_path):
    bids_path.session = '01'
    return bids_path


mri_t1_path_generator = get_t1_from_meeg

report_evoked_n_time_points = 3
report_stc_n_time_points = 3

# Exclude for source space analysis as no good MRI
# exclude_subjects = []
# exclude_subjects = ['mind005', 'mind006']

# subjects = list(set(subjects) - set(done_subjects))

on_error = 'continue'
# on_error = 'abort'
# on_error = 'debug'

# log_level = 'debug'
log_level = 'info'

# subjects = sorted(list(set(subjects) - set(exclude_subjects)))

# on_error = 'debug'
# N_JOBS = 1
# subjects = ['mind006']

# recreate_bem = True
exclude_subjects += ['mind005']  # mind005 has no MRI
