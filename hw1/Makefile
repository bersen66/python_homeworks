# Run demonstration for all script
.PHONY: all
all: nl_file nl_stdin tail_single tail_multiple tail_stdin wc_single wc_multiple wc_stdin

# Run demonstration for nl script
.PHONY: nl_file
nl_file:
	@echo Demonstratibg nl single file
	@echo ===================================
	./nl -f input/nl

.PHONY: nl_stdin 
nl_stdin:
	@echo Demonstratibg nl with stdin 
	@echo ===================================
	cat input/nl_stdin | ./nl

# Run demonstration for tail script
.PHONY: tail_single
tail_single:
	@echo Demonstratibg tail single file 
	@echo ===================================
	./tail -f input/nl

.PHONY: tail_multiple
tail_multiple:
	@echo Demonstratibg tail multiple files
	@echo ===================================
	./tail -f input/tail1 -f input/tail2

.PHONY: tail_stdin
tail_stdin:
	@echo Demonstratibg tail with stdin 
	@echo ===================================
	cat input/tail_stdin | ./tail


# Run demonstration for wc script
.PHONY: wc_single
wc_single:
	@echo Demonstratibg wc single file 
	@echo ===================================
	./wc -f input/wc

.PHONY: wc_multiple
wc_multiple:
	@echo Demonstratibg wc multiple files
	@echo ===================================
	./wc -f input/wc1 -f input/wc2

.PHONY: wc_stdin
wc_stdin:
	@echo Demonstratibg wc with stdin 
	@echo ===================================
	cat input/wc_stdin | ./wc

.PHONY: activate
activate:
	source env/bin/activate


