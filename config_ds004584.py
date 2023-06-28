import mne

study_name = 'ds004584'
bids_root = f'/storage/store3/data/{study_name}'
deriv_root = f'/storage/store3/derivatives/{study_name}/mne-bids-pipeline/'

ch_types = ['eeg']
task_is_rest = True
task = 'Rest'

notch_freq = 60
l_freq = 0.1
h_freq = 49
raw_resample_sfreq = 200

eeg_template_montage = mne.channels.make_standard_montage("standard_1005")

epochs_tmin = 0
epochs_tmax = 10 - 1 / raw_resample_sfreq
rest_epochs_duration = 10. - 1 / raw_resample_sfreq
rest_epochs_overlap = 0.
baseline = None

n_jobs = 40
on_error = 'continue'
