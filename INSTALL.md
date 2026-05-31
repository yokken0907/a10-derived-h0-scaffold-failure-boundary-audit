# Install / Reproduce

This repository is primarily an archive and manuscript package. No real-data likelihood or MCMC pipeline is included.

To inspect the normalized audit summary:

```bash
python scripts/verify_manifest.py
python -m json.tool data/terminal_audit_status.json
```

To rebuild the paper PDF from source, run from the repository root:

```bash
cd paper
latexmk -pdf -interaction=nonstopmode A10_derived_H0_scaffold_failure_boundary_audit_v0_1_0.tex
```

The source audit ZIPs are archived in `audit_logs/source_zips/`. They are included for traceability, not for making observational claims.
