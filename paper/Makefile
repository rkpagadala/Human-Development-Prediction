PANDOC = pandoc
ENGINE = --pdf-engine=xelatex

all: education_mediated_security.pdf

education_mediated_security.pdf: education_mediated_security.md fig_lag_comparison.png fig_beta_vs_baseline.png
	$(PANDOC) education_mediated_security.md -o $@ $(ENGINE)

clean:
	rm -f *.pdf
