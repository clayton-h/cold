#Makefile
.phony: all
all: test
	@echo "All done..."

.PHONY: run
run:
	python cold.py

.PHONY: clean
clean:
	rm -rf __pycache__
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	rm -rf .hypothesis

.phony: test
test:
	pytest -v test_cold.py

.phony: style-check
style-check:
	flake8 .

.phony: type-check
type-check:
	mypy --strict .

.phony: kattis
kattis:
	@kattis -f cold.py
	
# add to all
# .phony: test
# test:
# 	@cat 1.in | python cold.py | diff - 1.ans
# 	@cat 1.in | python cold.py | diff - 1.ans
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
