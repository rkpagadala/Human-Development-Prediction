PANDOC = pandoc
ENGINE = --pdf-engine=xelatex

all: education_mediated_security.pdf education_mediated_security_energy.pdf

education_mediated_security.pdf: education_mediated_security.md fig_lag_comparison.png
	$(PANDOC) education_mediated_security.md -o $@ $(ENGINE)

education_mediated_security_energy.pdf: education_mediated_security_energy.md fig_lag_comparison.png
	$(PANDOC) education_mediated_security_energy.md -o $@ $(ENGINE)

clean:
	rm -f *.pdf
