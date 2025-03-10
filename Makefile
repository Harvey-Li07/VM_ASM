clean:
	@rm -rf __pycache__
	@rm -rf Pack/__pycache__
	@rm -rf SDK/PackImplementations/__pycache__
	@rm -rf SDK/SpecificProgramScope/__pycache__
	@rm -rf SystemPackMonitor/__pycache__
	@echo "Clean up done"
run:
	@echo "Starting... \n"
	@python3 Shell.py
