## Setup

 Clone this repository and run `pipenv install`.

 ## Usage

 Running `python main.py` will download every file in the [FAFSA by Postsecondary School](https://studentaid.gov/data-center/student/application-volume/fafsa-school-state) dropdown menu into a directory named `raw-files/`. The `main()` function returns a dictionary mapping the time period (e.g. 2020-2021 Q2) to the filename (e.g. `./raw-files/2020-2021-app-data-by-school-q2.xls`).
 