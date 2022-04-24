from pathlib import Path
import shutil
import importlib
import os

import coloredlogs, logging
from mako.template import Template

coloredlogs.install()
logger = logging.getLogger(__name__)

reports_folder = Path(__file__).parent / 'reports'
reports_folder.mkdir(exist_ok=True)

datasets = [
    "ds000117",
    "ds000246",
    "ds000247",
    "ds000248",
    # "ds001810",
    # "ds001971",
    "ds003104",
    "ds003392",
    "ds004107",
]


def copy_datasets_reports():
    for dataset in datasets:
        config = importlib.import_module(f"config_{dataset}")
        deriv_root = Path(config.deriv_root)
        print("Processing: ", deriv_root)
        report_fnames = list(deriv_root.rglob("**/*.html"))
        if report_fnames:
            dataset_folder = reports_folder / dataset
            dataset_folder.mkdir(exist_ok=True)
        else:
            continue
        for fname in report_fnames:
            fsize = fname.stat().st_size / 1e6  # size in MB
            fname_relative = fname.relative_to(deriv_root)
            if fsize < 30:
                logger.info(f"Copying: {fname_relative}")
                shutil.copy(fname, dataset_folder / fname.name)
            else:
                logger.error(f"File to big ({fsize:.2f} MB): {fname_relative}")


def build_index():
    """Build index from directory listing."""

    INDEX_TEMPLATE = r"""
    <html>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <body>
    <div class="container">
    <h2 class="text-center"><a href="https://mne.tools/mne-bids-pipeline/">MNE-BIDS-Pipeline</a> reports</h2>
    % for dataset in fnames_per_dataset:
        <h3>Dataset: <a href="https://openneuro.org/datasets/${dataset}">${dataset}</h3>
        <div class="list-group">
        % for name in fnames_per_dataset[dataset]:
            <a href="${name}" class="list-group-item list-group-item-action">${name}</a>
        % endfor
        </div>
    % endfor
    </div>
    </body>
    </html>
    """

    EXCLUDED = ['index.html']

    fnames = [fname for fname in sorted(list(reports_folder.rglob("**/*.html")))
              if fname.name not in EXCLUDED]
    fnames = [fname.relative_to(reports_folder) for fname in fnames]
    fnames_per_dataset = {}
    for dataset in datasets:
        fnames_dataset = [fname for fname in fnames
                          if fname.parts[0] == dataset]
        if fnames_dataset:
            fnames_per_dataset[dataset] = sorted(fnames_dataset)
    html = Template(INDEX_TEMPLATE).render(
        fnames_per_dataset=fnames_per_dataset)
    with open(reports_folder / 'index.html', 'w') as f:
        f.write(html)


if __name__ == '__main__':
    copy_datasets_reports()
    build_index()
