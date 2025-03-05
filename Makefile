share:
	gcc -shared -o includes/compiled/CMethods.o includes/CMethods.h
	gcc -shared -o includes/compiled/CStrings.o includes/CStrings.h

clear:
	rm includes/compiled/CMethods.so
	rm includes/compiled/CStrings.so

pushable:
	rm -rf __pycache__
	rm -rf Pack/__pycache__
	rm -rf SDK/PackImplementations/__pycache__
	rm -rf SDK/SpecificProgramScope/__pycache__
	rm -rf SystemPackMonitor/__pycache__
run:
	python3 Shell.py