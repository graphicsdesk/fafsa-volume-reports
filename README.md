## Setup

Clone this repository and run `pipenv install`.

## Usage

Running `python download-reports.py` will download every file in the [FAFSA by Postsecondary School](https://studentaid.gov/data-center/student/application-volume/fafsa-school-state) dropdown menu into a new directory name `raw-files/`.

The `download_reports()` function also returns a dictionary that maps time periods (e.g. 2020-2021 Q2) to their corresponding filenames (e.g. `./raw-files/2020-2021-app-data-by-school-q2.xls`).

When `download_reports.py` is [the main program](https://stackoverflow.com/a/419185/6174302) (i.e. when it's directly run and not imported), this dictionary will be printed. However, `download_reports()` and its return value can be imported and utilized in other scripts.
