# arm-task

This has been tested using py.test on a Debian system. Install pytest by running

	pip install pytest


Assumptions:

Based on the diagram in the task description, the workers have been assigned to a top and bottom row. If both the top and bottom worker at a spot are in an identical state, the top worker will take priority to perform an action.

A worker won't pick up a component they are already holding.

If a worker is holding a finished product, they won't pick up a component.