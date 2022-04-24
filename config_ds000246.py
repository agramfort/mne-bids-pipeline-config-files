"""
Auditory MEG
"""

study_name = 'ds000246'
bids_root = f'/storage/store2/data/{study_name}'
deriv_root = f'/storage/store2/derivatives/{study_name}/mne-bids-pipeline/'
subjects_dir = f'{bids_root}/derivatives/freesurfer/subjects'

runs = ['01']
l_freq = 0.3
h_freq = 100
decim = 4
subjects = ['0001']
ch_types = ['meg']
reject = dict(mag=4e-12, eog=250e-6)
conditions = ['standard', 'deviant', 'button']
contrasts = [('deviant', 'standard')]
decode = True
on_error = 'abort'
parallel_backend = 'loky'
# dask_worker_memory_limit = '3G'
# dask_temp_dir = "./.dask-worker-space"
# dask_open_dashboard = True
N_JOBS = 10
