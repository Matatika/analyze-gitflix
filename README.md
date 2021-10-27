# analyze-gitflix

This analyze bundle is an example of a Matatika Custom Datasource with a spreadsheet extractor and simple charts.

## Deployment

To import data from a spreadsheet / csv file at `https://github.com/Matatika/analyze-gitflix/GitFlixUsers.csv` and
publish the charts into your [Matatika workspace](https://www.matatika.com) -

- create a new workspace (Profile -> New workspace)
- import data from a custom datasource (Profile -> Data Imports -> Custom Datasource)
- Paste the discovery.yml as below
- Run the Import

```
version: 19
extractors:
  - name: tap-gitflix
    namespace: tap_gitflix
    label: Gitflix
    description:
      Example custom extractor.
    docs: https://meltano.com/plugins/extractors/spreadsheets-anywhere.html
    repo: https://github.com/ets/tap-spreadsheets-anywhere
    pip_url: git+https://github.com/ets/tap-spreadsheets-anywhere.git
    executable: tap-spreadsheets-anywhere
    capabilities:
      - catalog
      - discover
      - state
    settings:
      - name: tables
        kind: array
        value: '[{"path":"https://meltano.com/files","name":"gitflixusers","pattern":"GitFlixUsers.csv","start_date":"2021-01-01T00:00:00Z","key_properties":["id"],"format":"csv"}]'
        description:
          An array holding json objects that each describe a set of targeted
          source files. See docs for details.
files:
  - name: analyze-gitflix
    namespace: tap_gitflix
    update:
      analyze/datasets/tap-gitflix/user-ages.yml: true
      analyze/datasets/tap-gitflix/user-genders.yml: true
    pip_url: git+https://github.com/Matatika/analyze-gitflix
```


## Development

pip ignores package_data, during development we need to 

```console
    python3 setup.py sdist
```

put the following into your discovery.yml

```
version: 19
extractors:
  - name: tap-gitflix
    namespace: tap_gitflix
    label: Gitflix
    description:
      Example custom extractor.
    docs: https://meltano.com/plugins/extractors/spreadsheets-anywhere.html
    repo: https://github.com/ets/tap-spreadsheets-anywhere
    pip_url: git+https://github.com/ets/tap-spreadsheets-anywhere.git
    executable: tap-spreadsheets-anywhere
    capabilities:
      - catalog
      - discover
      - state
    settings:
      - name: tables
        kind: array
        value: '[{"path":"https://meltano.com/files","name":"gitflixusers","pattern":"GitFlixUsers.csv","start_date":"2021-01-01T00:00:00Z","key_properties":["id"],"format":"csv"}]'
        description:
          An array holding json objects that each describe a set of targeted
          source files. See docs for details.
files:
  - name: analyze-gitflix
    namespace: tap_gitflix
    update:
      analyze/datasets/tap-gitflix/user-ages.yml: true
      analyze/datasets/tap-gitflix/user-genders.yml: true
    pip_url: [full path]/analyze-gitflix/dist/files-gitflix-datasets-0.1.0.tar.gz
```