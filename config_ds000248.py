"""
MNE Sample Data
"""
import mne

study_name = 'ds000248'
bids_root = f'/storage/store/data/{study_name}'
deriv_root = f'/storage/store2/derivatives/{study_name}/mne-bids-pipeline/'
subjects_dir = f'{bids_root}/derivatives/freesurfer/subjects'
N_JOBS = 1

subjects = ['01']
rename_events = {'Smiley': 'Emoji',
                 'Button': 'Switch'}
conditions = ['Auditory', 'Visual', 'Auditory/Left', 'Auditory/Right']
epochs_metadata_query = 'index > 0'  # Just for testing!
contrasts = [('Visual', 'Auditory'),
             ('Auditory/Right', 'Auditory/Left')]

time_frequency_conditions = ['Auditory', 'Visual']

ch_types = ['meg']
mf_reference_run = '01'
find_flat_channels_meg = True
find_noisy_channels_meg = True
use_maxwell_filter = True
process_er = False


def noise_cov(bp):
    # Use pre-stimulus period as noise source
    bp = bp.copy().update(processing='clean', suffix='epo')
    epo = mne.read_epochs(bp)
    cov = mne.compute_covariance(epo, rank='info', tmax=0)
    return cov


spatial_filter = 'ssp'
n_proj_eog = dict(n_mag=1, n_grad=1, n_eeg=1)
n_proj_ecg = dict(n_mag=1, n_grad=1, n_eeg=0)
ecg_proj_from_average = True
eog_proj_from_average = False

# bem_mri_images = 'FLASH'
# recreate_bem = True
# recreate_scalp_surface = True

def mri_t1_path_generator(bids_path):
    # don't really do any modifications – just for testing!
    return bids_path

on_error = "debug"
