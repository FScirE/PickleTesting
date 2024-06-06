# PickleTesting

This repository utilizes unit tests and GitHub Actions to test the 'pickle' module in Python and present its results.

## How to run

- Create your unit tests or run the existing ones in 'pickle_test.py'.
- Activate the workflows in the Actions tab.
- Run the 'clear_pkl.py' file to clear any old results.
- Push the changes to origin (if there are no changes, just make a comment in some file to have something to push).
- Monitor the results in the 'Pickle tester' workflow in the Actions tab. If any error occurs relating to pushing/pulling from the GitHub repo in the workflow, restart the failed processes.
- Wait for all processes to complete.
- Check the results from the 'Result comparison' workflow.

If you need to push any changes to the repository without to running the workflows then disable them in the Actions tab.