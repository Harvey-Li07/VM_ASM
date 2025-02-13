share:
	gcc -shared -o includes/compiled/CMethods.o includes/CMethods.h
	gcc -shared -o includes/compiled/CStrings.o includes/CStrings.h

clear:
	rm includes/compiled/CMethods.so
	rm includes/compiled/CStrings.so