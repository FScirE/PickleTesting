# PickleTesting

This repository utilizes unit tests and GitHub Actions to test the 'pickle' module in Python and present its results.

## How to run

- Run the tests in 'pickle_test.py'.
- Activate the workflows in the Actions tab.
- Run the 'clear_pkl.py' file to clear any old results.
- Push the changes to origin (if there are no changes, just make a comment in some file to have something to push).
- Monitor the results in the 'Pickle tester' workflow in the Actions tab. If any errors occur relating to pushing/pulling from the GitHub repo in any of the jobs in the workflow, re-run the failed jobs until all are done (this is in need of improvement).
- Wait for all jobs to complete.
- Check the results from the 'Result comparison' workflow.

If you need to push any changes to the repository without to running the workflows then disable them in the Actions tab.

## Adding more tests

- In order to add more Python versions (only standard works, i.e. only numbers such as 3.7, 3.8, 3.11) a folder with that versions name with every unit tests folder must be added.

- In order to add more unit tests, on top of adding the code in the 'pickle_test.py' a folder for that unit test must be added in each Python versions folder.

- Adding more operating systems is trivial.

Tip: add an empty text file in a folder for it to be added to the GitHub repository.