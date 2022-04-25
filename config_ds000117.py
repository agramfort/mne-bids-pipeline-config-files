"""
Faces dataset
"""

study_name = 'ds000117'
bids_root = f'/storage/store2/data/{study_name}'
deriv_root = f'/storage/store2/derivatives/{study_name}/mne-bids-pipeline/'
subjects_dir = f'{bids_root}/derivatives/freesurfer/subjects'

# subjects = "all"

task = 'facerecognition'
# ch_types = ['eeg']
ch_types = ['meg']
data_type = 'meg'

eog_channels = ['EEG062']

# deriv_root = Path('/storage/store2/data/ds000117/derivatives/mne-bids-pipeline-eeg')
# if 'meg' in ch_types:
#     deriv_root = Path('/storage/store2/data/ds000117/derivatives/mne-bids-pipeline')

# ch_types = ['meg']
runs = ['01', '02', '03', '04', '05', '06']
# runs = ['01']
sessions = ['meg']
interactive = False
acq = None
subjects = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
            '11', '12', '13', '14', '15', '16']
# subjects = ['03']
# subjects = ['01']

#######################
# Maxfilter

if 'meg' in ch_types:
    use_maxwell_filter = True
    find_noisy_channels_meg = True
    mf_st_duration = 10.0  # 10 seconds with tSSS
    mf_cal_fname = bids_root + '/derivatives/meg_derivatives/sss_cal.dat'
    mf_ctc_fname = bids_root + '/derivatives/meg_derivatives/ct_sparse.fif'
    # mf_head_origin = 'auto'
    mf_head_origin = [0.003, 0.009, 0.04]

#######################
# Epoching
epochs_tmin = -0.2
epochs_tmax = 2.9
reject_tmax = 0.8
decim = 5
l_freq = None
h_freq = 40

reject = {'grad': 4000e-13, 'mag': 4e-12}
conditions = ['Famous', 'Unfamiliar', 'Scrambled']
contrasts = [('Famous', 'Scrambled'),
             ('Unfamiliar', 'Scrambled'),
             ('Famous', 'Unfamiliar')]
# decode = False
decode = True

spatial_filter = None
if 'meg' in ch_types:
    spatial_filter = 'ssp'
elif 'eeg' in ch_types:
    spatial_filter = 'ica'
    ica_reject = dict(grad=4000e-13, mag=4e-12)
    ica_decim = 11
    ica_n_components = 0.999

random_state = 42

#######################
# Source imaging
# subjects_dir = op.join(bids_root, 'derivatives', 'freesurfer', 'subjects')
# subjects_dir = op.join(bids_root, 'derivatives_fs', 'freesurfer', 'subjects')
# recreate_bem = True

def mri_t1_path_generator(bids_path):
    bids_path.session = 'mri'
    return bids_path

#######################
# Global
on_error = 'debug'
N_JOBS = len(subjects)
N_JOBS = 1
