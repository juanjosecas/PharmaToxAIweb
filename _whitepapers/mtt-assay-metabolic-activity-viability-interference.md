---
layout: whitepaper
title: "What does the MTT assay actually measure? Metabolic activity, viability and misleading signals"
summary: "MTT is widely used to estimate cell viability, but formazan formation is not a direct cell count. Experimental evidence shows how metabolism, antioxidants, nanoparticles and assay conditions can alter the signal independently of cell survival."
authors:
  - PharmaToxAI
date: 2026-10-13
published: true
pdf: ""
---

The MTT assay remains one of the most frequently used methods in cell-based screening. It is inexpensive, accessible and convenient for comparing experimental treatments. Yet a recurring problem is that the resulting absorbance is routinely described as a direct measurement of “cell viability.”

**MTT measures tetrazolium reduction, not viable-cell number.** The distinction becomes critical when the test material alters metabolism, contains redox-active ingredients or interferes with the optical readout.

## From tetrazolium to formazan: what generates the signal?

MTT is reduced to an insoluble purple formazan product through cellular reducing activity. The amount measured after solubilisation depends on several factors: cell number, metabolic state, MTT uptake and incubation, crystal formation and recovery, and optical measurement conditions. It should not be interpreted as a specific readout of mitochondrial succinate dehydrogenase alone.

A detailed experimental assessment by Ghasemi and colleagues in PC-3 cells varied seeding density, MTT concentration, incubation time, medium composition and serum deprivation. The authors also evaluated extracellular formazan, cell-derived material and PEG-coated gold nanoparticles. Their findings demonstrate that the assay response can shift with conditions unrelated to a proportional change in the number of living cells.

Consequently, a decrease in MTT signal may reflect cell loss, metabolic inhibition or a combination of both. An increase may reflect cell proliferation, higher reduction per cell or non-cellular chemical interference.

## When a compound reacts with the assay

This is particularly relevant to cosmetic ingredients, botanical extracts and antioxidant candidates.

Bruggisser and colleagues showed that kaempferol, resveratrol, selected botanical extracts and antioxidant compounds could reduce MTT in **cell-free systems**. In their experiments, increased formazan production did not necessarily agree with changes in cell number measured by crystal violet staining.

That observation is a direct warning against interpreting an increased MTT signal after treatment with a redox-active ingredient as improved viability or a protective biological effect.

Nanomaterials introduce additional mechanisms of interference. An experimental study on silver nanoparticles found that several particle types directly reduced MTT, while other optical assays were affected differently depending on particle characteristics. Ghasemi and colleagues similarly demonstrated optical interference from PEG-coated gold nanoparticles. Neither the direction nor the magnitude of interference can be assumed across materials.

**A cell-free control containing the complete test matrix at each relevant concentration is therefore essential whenever direct reduction or optical interference is plausible.**

## Why experimental design matters

The interpretation of MTT data should account for:

- **Density and linear range:** establish the relationship between seeded or independently counted cells and the measured signal under the specific culture conditions.
- **Exposure and MTT incubation:** report both durations; treatment-dependent changes in metabolism can occur before detectable cell loss.
- **Matrix interference:** test the sample with MTT but without cells, and evaluate optical background from the sample and medium.
- **Formazan handling:** changes in washing, supernatant removal and solubilisation can alter recovery of the product, including extracellular crystals.
- **Controls and replication:** include vehicle and relevant biological controls, distinguish independent biological experiments from technical wells, and retain individual data before normalization.
- **Orthogonal confirmation:** where the biological conclusion depends on survival, complement MTT with an endpoint based on a different principle, such as direct cell counting or image-based analysis, membrane integrity or another appropriately validated method.

An alternative assay is not automatically interference-free. Resazurin is also a metabolic readout; dye uptake, fluorescence and optical measurements may be affected by test materials. The appropriate choice depends on the question and on the chemistry of the sample.

## A more defensible way to report the result

“Cell viability was 120% of control” is stronger than the experiment may justify when it is based solely on MTT absorbance.

A more accurate formulation is: **“MTT reduction increased to 120% of vehicle control under the tested conditions.”** If an independent assay confirms an increase in viable-cell number, that biological conclusion can then be supported separately.

Likewise, an MTT-derived concentration–response curve may yield a useful operational estimate of the concentration associated with a 50% reduction in signal. It should not automatically be called an LC50 or interpreted as 50% cell death. The endpoint and calculation need to be named explicitly.

This distinction is especially important in studies reporting cytoprotection, anti-ageing activity or recovery after oxidative stress. A higher tetrazolium-reduction signal, by itself, does not establish proliferation, reduced cell death, reversal of senescence or clinical efficacy.

## The practical conclusion

MTT is not an obsolete assay. It remains useful when its signal is understood and its limitations are experimentally controlled. The problem arises when a **metabolic and chemical measurement is presented as an unqualified count of surviving cells**.

For integrated in vitro and computational toxicology, preserving that distinction improves both experimental interpretation and downstream modelling: a machine-learning model trained on MTT-derived labels will learn the properties of the measured endpoint, including any unresolved assay artefacts, rather than a universal notion of cell viability.

## References

1. Ghasemi M, Turnbull T, Sebastian S, Kempson I. The MTT Assay: Utility, Limitations, Pitfalls, and Interpretation in Bulk and Single-Cell Analysis. *International Journal of Molecular Sciences*. 2021;22(23):12827. [https://doi.org/10.3390/ijms222312827](https://doi.org/10.3390/ijms222312827).

2. Bruggisser R, von Daeniken K, Jundt G, Schaffner W, Tullberg-Reinert H. Interference of plant extracts, phytoestrogens and antioxidants with the MTT tetrazolium assay. *Planta Medica*. 2002. [https://pubmed.ncbi.nlm.nih.gov/12058323/](https://pubmed.ncbi.nlm.nih.gov/12058323/).

3. Caveats to the use of MTT, neutral red, Hoechst and Resazurin to measure silver nanoparticle cytotoxicity. *Chemico-Biological Interactions*. 2020;315:108868. [https://doi.org/10.1016/j.cbi.2019.108868](https://doi.org/10.1016/j.cbi.2019.108868).

4. Limitations of the MTT assay when compared to three commonly used cell enumeration assays. *Biochemical and Biophysical Research Communications*. 2015. [https://pmc.ncbi.nlm.nih.gov/articles/PMC4349615/](https://pmc.ncbi.nlm.nih.gov/articles/PMC4349615/).

5. Particle-induced artifacts in the MTT and LDH viability assays. *Journal of Nanoparticle Research*. 2012. [https://pmc.ncbi.nlm.nih.gov/articles/PMC3446248/](https://pmc.ncbi.nlm.nih.gov/articles/PMC3446248/).
