#Makefile
.phony: all
all: test
	@echo "All done..."

.PHONY: run
run:
	python hvert.py

.PHONY: clean
clean:
	rm -rf __pycache__
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	rm -rf .hypothesis

# a. Rule for local unit test
.PHONY: local-unit-test
local-unit-test:
	pytest -v test_hvert.py

# b. Rule for local Kattis test on sample input/output files
.PHONY: local-kattis-test
local-kattis-test:
	@cat sample_input.in | python hvert.py | diff - sample_output.ans
	@echo "Local Kattis tests passed..."

# c. Rule for checking styles using flake8
.PHONY: style-check
style-check:
	flake8 .

# d. Rule for fixing styles using autopep8
.PHONY: fix-style
fix-style:
	autopep8 --in-place --recursive --aggressive --aggressive .

# e. Rule for checking types with mypy
.PHONY: type-check
type-check:
	mypy --strict .

# f. Rule to submit problem to Kattis using Kattis CLI
.PHONY: submit-kattis
submit-kattis:
	kattis -f hvert.py

# .phony: test
# test:
# 	pytest -v test_hvert.py

# .phony: style-check
# style-check:
# 	flake8 .

# .phony: type-check
# type-check:
# 	mypy --strict .

# .phony: kattis
# kattis:
# 	@kattis -f hvert.py
	
# add to all
# .phony: test
# test:
# 	@cat 1.in | python hvert.py | diff - 1.ans
# 	@cat 1.in | python hvert.py | diff - 1.ans
# 	@echo "All tests passed..."

# TEST = pytest 
# TEST_ARGS = --verbose --color=yes
# TYPE_CHECK = mypy --strict
# STYLE_CHECK = flake8
# STYLE_FIX = autopep8 --in-place --recursive --aggressive --aggressive

# .PHONY: all
# all: style-check type-check run-test clean

# .PHONY: type-check
# type-check:
# 	$(TYPE_CHECK) .

# .PHONY: style-check
# style-check:
# 	$(STYLE_CHECK) .

# # discover and run all tests
# .PHONY: run-test
# run-test:
# 	$(TEST) $(TEST_ARGS) .

# .PHONY: push
# push: run-test clean
	
# .PHONY: fix-style
# fix-style:
# 	$(STYLE_FIX) .
