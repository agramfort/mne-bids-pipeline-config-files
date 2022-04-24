"""Somato
"""
study_name = 'ds003104'
bids_root = f'/storage/store2/data/{study_name}'
deriv_root = f'/storage/store2/derivatives/{study_name}/mne-bids-pipeline/'
subjects_dir = f'{bids_root}/derivatives/freesurfer/subjects'

conditions = ['somato_event1']
ch_types = ['meg']
