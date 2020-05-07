Scrapes the [Federal Student Aid website](https://studentaid.gov/data-center/student/application-volume/fafsa-school-state) to download all FAFSA volume reports by postsecondary school.

## Setup

 Clone this repository and run `pipenv install`.

 ## Usage

Running `python download-reports.py` will download every file in the [FAFSA by Postsecondary School](https://studentaid.gov/data-center/student/application-volume/fafsa-school-state) dropdown menu into a directory named `raw-files/`.

The `download_reports()` function also returns a dictionary that maps time periods (e.g. 2020-2021 Q2) to their corresponding filenames (e.g. `./raw-files/2020-2021-app-data-by-school-q2.xls`).
