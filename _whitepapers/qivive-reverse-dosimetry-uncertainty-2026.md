---
layout: whitepaper
title: "From micromolar activity to human dose: the uncertainty behind quantitative IVIVE"
summary: "Recent PBK model benchmarks and EFSA's scientific opinion on developmental neurotoxicity illustrate how assay dosimetry, model applicability and exposure assumptions determine the credibility of non-animal quantitative risk assessment."
authors:
  - PharmaToxAI
date: 2026-11-16
published: true
pdf: ""
---

A concentration-response experiment may establish that a chemical perturbs a biological process at a particular concentration. It does not establish the administered dose needed to produce that concentration in a human organ. Quantitative in vitro to in vivo extrapolation (QIVIVE) addresses this gap by combining experimental concentration-response information with toxicokinetic modelling.

Recent work makes the limitations of this translation unusually tangible. In a 2026 benchmark of a generic physiologically based kinetic (PBK) model, Spaenig and colleagues found that predicted peak plasma concentrations were within threefold of observed values for only 31% of the 26 chemicals examined [1]. Meanwhile, a comparison of modelling platforms for developmental neurotoxicity reported considerably better agreement between administered equivalent doses and available in vivo effect levels in its particular study design [2]. These are distinct benchmarks, with different targets and chemical populations. Their results cannot be pooled into a single accuracy estimate for QIVIVE.

The regulatory relevance of this issue is illustrated by EFSA's Scientific Opinion on developmental neurotoxicity, published in December 2025 and amended in January 2026 [3]. It asks how data from an in vitro battery can contribute quantitatively to pesticide assessment. The question is as much about experimental dosimetry and model evaluation as about computational implementation.

## The concentration that belongs in the model

Nominal concentration is the amount introduced into an assay divided by the nominal exposure volume. It is a convenient experimental descriptor, but its relationship to biologically effective concentration depends on the compound and the test system.

Binding to serum proteins, adsorption to plastic, partitioning into lipid-rich cellular compartments, chemical instability and metabolism can alter exposure over time. A compound with substantial nonspecific binding may consequently generate a markedly different unbound concentration in two laboratories using different serum concentrations.

For a simplified system at equilibrium, the unbound concentration in medium can be written as

**C_free = f_u,medium × C_total,medium**

where the fraction unbound is dimensionless. This expression requires a measured or defensibly estimated total medium concentration. Substituting the nominal concentration assumes that losses from the medium are negligible. It also assumes that the relevant binding relationship applies over the tested concentration range.

For intracellular targets, extracellular unbound concentration may be an imperfect surrogate for target-site exposure. Active uptake, efflux, ion trapping and intracellular metabolism can break the implicit equilibrium between extracellular and intracellular compartments. Cell-associated total concentration has its own limitations because it includes material bound to cellular structures.

The exposure metric should therefore be selected in relation to the biology of the assay. For a rapidly reversible receptor interaction, peak unbound concentration may be informative. A response driven by cumulative damage may instead depend on exposure duration or an integrated concentration-time metric. Neither choice is justified merely by availability of an assay EC50.

## Reverse dosimetry and the inverse problem

A PBK model describes the distribution and elimination of a substance using physiological compartments and chemical-specific parameters. In a simple perfusion-limited tissue compartment, the rate of change of chemical amount is represented by blood delivery minus venous removal and local elimination:

**dA_t/dt = Q_t × (C_art − C_t/K_t:b) − R_elimination,t**

Here A_t is tissue amount, Q_t is tissue blood flow, C_art is arterial concentration, C_t is tissue concentration and K_t:b is the tissue-to-blood partition coefficient. All terms must use compatible concentration and amount units. This representation is inadequate for tissues in which membrane transport limits distribution unless additional processes are introduced.

Forward dosimetry starts with an external dose and predicts an internal exposure metric. Reverse dosimetry searches for the external dose that reproduces a selected experimental exposure metric. For linear kinetics under a fixed exposure scenario, a unit-dose simulation can be used to calculate:

**AED = D_ref × C_target / C_model(D_ref)**

The administered equivalent dose (AED) has the same units as D_ref, and the two concentrations must represent equivalent quantities. Nonlinear kinetics require numerical inversion or another appropriate search strategy. A unique solution should not be assumed when the dose-response relationship of the selected kinetic metric is non-monotonic.

Consider a hypothetical oral exposure scenario. An assay benchmark concentration is 10 micromolar total medium concentration, with measured medium fraction unbound of 0.1. A model predicts an unbound plasma peak of 0.2 micromolar after 1 mg/kg. Under linear kinetics and assuming the peak unbound metrics are biologically comparable, the equivalent dose is 5 mg/kg. Matching the nominal 10 micromolar to the unbound plasma concentration would instead yield 50 mg/kg.

These are illustrative calculations, not empirical safety values. They show how an apparently minor distinction in concentration definitions propagates into the estimated dose. Even a perfectly solved PBK model cannot repair a biologically inappropriate choice of target concentration.

## What the recent benchmarks establish

Spaenig et al. compared a generic high-throughput PBK workflow with chemical-specific models and available kinetic observations across 26 organic chemicals [1]. Half of the predictions of peak plasma concentration fell within one order of magnitude of the corresponding in vivo values. The study also identified a directional relationship with lipophilicity: peak levels tended to be underestimated for more lipophilic substances and overestimated for more hydrophilic substances.

This directional bias matters for reverse dosimetry. Under linear kinetics, underprediction of internal exposure per unit dose inflates the predicted external dose required to reach an assay threshold. Such an error may make an exposure margin appear larger than warranted. Conversely, overprediction can lead to conservative prioritisation. The limited size of the benchmark prevents treating the observed lipophilicity relationship as a universal correction rule.

Kreutz et al. investigated a different question: whether a developmental neurotoxicity extrapolation workflow could be implemented across three PBPK platforms [2]. The study used bioactivity data from seven assays within the larger developmental neurotoxicity battery and compared estimated equivalent doses with available in vivo effect levels. Agreement was within a factor of three for 78% of chemicals in that comparison.

The distinction between these studies is important. Agreement with measured peak plasma concentrations assesses one component of toxicokinetic prediction. Agreement with an in vivo effect dose assesses the combined extrapolation procedure against a biological observation, with uncertainties on both sides. Platform agreement can support reproducibility, but shared assumptions and parameter sources can also produce correlated errors. Independent kinetic observations remain valuable.

A further collaborative assessment of computational toxicokinetic predictions, published in the January 2026 issue of Toxicology in Vitro, provides a relevant source for evaluating the reliability of predicted inputs [4]. Its subject is directly pertinent to screening pipelines that use estimated chemical-specific parameters to avoid experimental bottlenecks. The uncertainty of an input prediction should remain visible when that prediction is passed to a kinetic model.

## Intestinal metabolism and the cost of generic assumptions

Generic models are attractive because a consistent structure can be deployed across a chemical inventory. However, chemicals differ in the processes controlling their disposition.

Korol-Bexell and colleagues investigated intestinal toxicokinetics as a refinement to high-throughput IVIVE in 2025 [5]. Their study addresses a limitation of approaches that account for hepatic metabolism but simplify other presystemic processes. An orally administered chemical may be metabolised within the intestine before reaching the systemic circulation. Failing to represent this process can overestimate systemic exposure to the parent compound.

In conventional pharmacokinetic notation, oral bioavailability can be expressed as the product of the absorbed fraction and the fractions escaping intestinal and hepatic first-pass elimination:

**F = F_a × F_g × F_h**

Reducing F_g decreases systemic parent exposure if other factors remain constant. The implications for hazard are conditional: a metabolite formed in the gut may itself be active, and local intestinal toxicity cannot be evaluated simply by examining systemic parent concentrations.

More detailed compartmental models can capture such mechanisms, but additional parameters introduce estimation uncertainty. Refinement is most useful when a process plausibly affects the decision and sufficient data exist to constrain it.

## EFSA's developmental neurotoxicity opinion

The EFSA Panel on Plant Protection Products and their Residues provides a specific application framework for QIVIVE of developmental neurotoxicity battery data for pesticide active substances [3]. This is an EU scientific opinion, not a general authorisation for replacing toxicity testing in other product categories or jurisdictions.

Its practical emphasis is on connecting comparable exposure metrics, evaluating the kinetic model at an appropriate level of complexity and documenting uncertainty. The recommended starting point is a conservative whole-body model, with refinement where supporting evidence warrants it. Plasma unbound exposure and cell-associated exposure are treated differently when establishing correspondence with assay data.

The opinion also places QIVIVE results within an overall weight-of-evidence assessment. This is important because translating a concentration into an external dose does not establish that the observed in vitro response is an adverse developmental outcome. Relevance of the biological endpoint, developmental timing, metabolic competence and coverage of mechanisms remain separate questions.

OECD's 2021 PBK guidance provides a broader foundation for characterising and reporting kinetic models [6]. Model purpose, underlying assumptions, parameter provenance and evaluation need to be documented sufficiently for independent scrutiny. These principles remain useful even when a model is intended only for internal screening rather than a regulatory submission.

## Uncertainty in a decision-oriented workflow

A single equivalent dose obscures several distinct sources of uncertainty:

- Experimental uncertainty in the estimated benchmark concentration and its biological interpretation.
- Assay dosimetry uncertainty, including free concentration, stability and intracellular distribution.
- Chemical-specific kinetic parameter uncertainty, especially binding, clearance and absorption.
- Physiological variability and structural model uncertainty.
- Uncertainty in the correspondence between experimental and in vivo exposure metrics.

The October 2026 paper by Sangion and colleagues presents a framework specifically devoted to uncertainty in dose extrapolation from in vitro bioassays [7]. This recent work is relevant to the development of quantitative reporting practices; its publication should not be mistaken for formal regulatory adoption of a particular uncertainty procedure.

For a simple linear model, log(AED) equals log(C_target) minus log(C_model) plus log(D_ref). Uncertainty in both concentration terms therefore propagates directly into the result. Covariance matters: treating correlated inputs as independent can distort the resulting interval.

In more complicated systems, Monte Carlo sampling can propagate parameter uncertainty and physiological variability through the forward model and subsequent inversion. Sampling distributions must respect physical constraints and known dependence between parameters. Structural uncertainty can be investigated through alternative credible models or exposure metrics. A narrow simulation interval conditional on a poorly chosen model provides little assurance.

Sensitivity analysis can help decide which additional measurements are worth obtaining. If predicted equivalent dose is sensitive to intrinsic clearance but relatively insensitive to tissue partitioning over plausible ranges, a clearance experiment may reduce decision uncertainty more effectively than additional partition coefficient predictions.

## Practical implementation

For early compound assessment, a defensible QIVIVE workflow begins with a clearly specified decision: prioritisation, comparison of exposure margins or development of evidence for a particular hazard assessment. A suggested implementation is:

1. Establish chemical identity, exposure route, regimen and the biological endpoint; retain original assay conditions and concentration units.
2. Estimate a concentration-response reference point with uncertainty and examine cytotoxicity or analytical interference.
3. Characterise the relevant in vitro exposure metric, explicitly distinguishing measured from estimated values.
4. Parameterise the PBK model with documented experimental and computational inputs, and evaluate applicability to the chemical.
5. Simulate internal exposure and perform reverse dosimetry using compatible concentration metrics.
6. Propagate uncertainty and test alternative plausible assumptions. Compare equivalent doses with exposure estimates only within a specified assessment context.

An exposure margin calculated as equivalent dose divided by estimated human exposure is a useful dimensionless screening quantity when both doses share the same route, units and exposure basis. It is not automatically a margin of safety. The biological reference point may represent early cellular bioactivity rather than an adverse outcome, and population variability or susceptible developmental stages may be incompletely represented.

For cosmetic ingredients, an oral equivalent dose cannot simply be substituted into a dermal exposure assessment. Skin absorption, local tissue exposure and route-dependent metabolism require their own treatment. Similarly, extrapolation from a pure ingredient to a finished formulation needs evidence concerning composition and exposure.

## Conclusions

QIVIVE supplies a quantitative connection between a cellular experiment and an external exposure scenario. Recent benchmarks show that this connection is practicable but sensitive to the chemical domain, the selected kinetic endpoint and the assumptions used in constructing the model.

Generic PBK workflows are appropriate starting points for many prioritisation problems. A decision with greater consequences requires stronger evidence that the model predicts the relevant exposure metric and that the assay concentration represents a biologically comparable exposure. Experimental characterisation of binding, stability or clearance can sometimes contribute more to the credibility of the result than a more elaborate computational architecture.

The value of QIVIVE lies in making the exposure assumptions testable and the associated uncertainty explicit. Its output is a conditional estimate that contributes to a larger toxicological assessment.

## References

1. Spaenig M, Ashraf MW, Bouhifd M, Drake C, Sobanski T, Escher SE. Applicability of next-generation risk assessment generic PBK models and their performance within the chemical domain. *Archives of Toxicology*. 2026;100:3893–3906. [doi:10.1007/s00204-026-04443-7](https://doi.org/10.1007/s00204-026-04443-7).
2. Kreutz A, Chang X, Lawless M, Proença S, Schaller S, Kleinstreuer N, Hogberg HT. Comparison of physiologically based pharmacokinetic modeling platforms for developmental neurotoxicity in vitro to in vivo extrapolation. *Toxicological Sciences*. 2026;209(2):kfaf147. [doi:10.1093/toxsci/kfaf147](https://doi.org/10.1093/toxsci/kfaf147).
3. EFSA Panel on Plant Protection Products and their Residues (PPR). Scientific Opinion on the application of physiologically based kinetic (PBK) modelling for the quantitative in vitro to in vivo extrapolation (QIVIVE) of developmental neurotoxicity in vitro battery (DNT IVB) data for pesticide active substances. *EFSA Journal*. 2025;23(12):e9814. Amended 7 January 2026. [doi:10.2903/j.efsa.2025.9814](https://doi.org/10.2903/j.efsa.2025.9814).
4. Wambaugh JF, Sipes NS, Padilla Mercado G, et al. Collaborative evaluation of in silico predictions for high throughput toxicokinetics. *Toxicology in Vitro*. 2026;110:106150. [doi:10.1016/j.tiv.2025.106150](https://doi.org/10.1016/j.tiv.2025.106150).
5. Korol-Bexell E, Jarnagin AS, Brennan A, Ford J, Bounds J, MacMillan DM, Hughes MF, Wetmore BA. Refining high-throughput in vitro–in vivo extrapolation modeling through incorporation of intestinal toxicokinetics. *Toxicological Sciences*. 2025;207(2):348–360. [doi:10.1093/toxsci/kfaf105](https://doi.org/10.1093/toxsci/kfaf105).
6. OECD. Guidance document on the characterisation, validation and reporting of Physiologically Based Kinetic (PBK) models for regulatory purposes. OECD Series on Testing and Assessment No. 331. OECD Publishing, Paris; 2021. [doi:10.1787/d0de241f-en](https://doi.org/10.1787/d0de241f-en).
7. Sangion A, Armitage JM, Nong A, Barton-Maclaren T, Arnot JA. A framework to characterize uncertainty for dose extrapolation from in vitro bioassays. *Regulatory Toxicology and Pharmacology*. 2026;173:106284. Published online 26 October 2026. [doi:10.1016/j.yrtph.2026.106284](https://doi.org/10.1016/j.yrtph.2026.106284).
