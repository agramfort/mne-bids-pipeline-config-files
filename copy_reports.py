from pathlib import Path
import shutil
import importlib
import os

from mako.template import Template

reports_folder = Path(__file__).parent / 'reports'
reports_folder.mkdir(exist_ok=True)

datasets = [
    "ds000117",
    "ds000246",
    "ds000247",
    "ds000248",
    "ds001810",
    "ds001971",
    # "ds003104",
    # "ds003392",
    "ds004107",
]


def copy_datasets_reports():
    for dataset in datasets:
        config = importlib.import_module(f"config_{dataset}")
        deriv_root = Path(config.deriv_root)
        print(deriv_root)
        report_fnames = list(deriv_root.rglob("**/*.html"))
        if report_fnames:
            dataset_folder = reports_folder / dataset
            dataset_folder.mkdir(exist_ok=True)
        else:
            continue
        for fname in report_fnames:
            print(fname)
            fsize = fname.stat().st_size / 1e6  # size in MB
            print(f"Size: {fsize / fsize:.2f} MB")
            if fsize < 20:
                shutil.copy(fname, dataset_folder / fname.name)


def build_index():
    """Build index from directory listing."""

    INDEX_TEMPLATE = r"""
    <html>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <body>
    <h2>${header}</h2>
    <p>
    % for name in names:
        <li><a href="${name}">${name}</a></li>
    % endfor
    </p>
    </body>
    </html>
    """

    EXCLUDED = ['index.html']

    fnames = [fname for fname in sorted(list(reports_folder.rglob("**/*.html")))
              if fname.name not in EXCLUDED]
    fnames = [fname.relative_to(reports_folder) for fname in fnames]
    header = "MNE-BIDS-Pipeline reports"
    html = Template(INDEX_TEMPLATE).render(names=fnames, header=header)
    with open(reports_folder / 'index.html', 'w') as f:
        f.write(html)


if __name__ == '__main__':
    copy_datasets_reports()
    build_index()
