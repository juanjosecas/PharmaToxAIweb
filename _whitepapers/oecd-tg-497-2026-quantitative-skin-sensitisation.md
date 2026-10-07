---
layout: whitepaper
title: "OECD TG 497 in 2026: from skin sensitisation hazard to a quantitative point of departure"
summary: "The 2026 OECD TG 497 extends defined approaches for skin sensitisation beyond hazard and potency categories by incorporating quantitative point-of-departure approaches. This brief reviews SARA-ICE, the regression-based DA, their evidence base, limitations and implications for non-animal risk assessment."
authors:
  - PharmaToxAI
date: 2026-10-07
published: true
pdf: ""
---

Skin sensitisation has become one of the clearest examples of how new approach methodologies (NAMs) can move from mechanistic assays to a prescriptive regulatory framework. The 2026 version of **OECD Test Guideline 497 (TG 497), Defined Approaches on Skin Sensitisation**, adopted on 2 July 2026, is an important step in that transition. The guideline still covers defined approaches (DAs) for hazard identification and potency categorisation, but now also includes a third part for deriving a **quantitative point of departure (PoD)**.

That addition matters because hazard classification and quantitative risk assessment answer different questions. Knowing whether a chemical is a sensitiser, or assigning it to a potency category, does not by itself define an exposure level suitable for risk assessment. A quantitative PoD provides a bridge between NAM data and exposure-based decision making.

This white paper summarises what changed, how the new quantitative approaches work, and what should — and should not — be inferred from their inclusion in an OECD Test Guideline.

## What is a Defined Approach?

TG 497 defines a DA as a fixed combination of information sources and a **data interpretation procedure (DIP)**. Inputs may include in chemico, in vitro and, in some DAs, in silico information. The key distinction from an informal weight-of-evidence assessment is that the combination and interpretation of those inputs are specified in advance.

The guideline is organised around three levels of output:

- **Part I — hazard identification:** sensitiser versus non-sensitiser, including the "2 out of 3" DA.
- **Part II — potency categorisation:** integrated testing strategy (ITS) approaches used to support potency classification.
- **Part III — quantitative PoD:** SARA-ICE and a regression-based DA intended to provide quantitative starting points for risk assessment.

The 2026 change therefore does not replace the earlier DAs. It expands the regulatory question that TG 497 can address.

## SARA-ICE: a Bayesian route to a quantitative PoD

The **Skin Allergy Risk Assessment – Integrated Chemical Environment (SARA-ICE)** framework is a Bayesian model developed to integrate mechanistically relevant skin-sensitisation information and estimate an **ED01**, a dermal dose associated with an estimated 1% probability of sensitisation induction in humans.

The underlying model was described by Reinke and colleagues using historical human, murine and in vitro information for hundreds of chemicals. A central methodological advantage is that SARA-ICE is probabilistic: it does not treat the input measurements as error-free observations and can represent uncertainty in the estimated potency.

This is conceptually different from simply converting a positive assay concentration into a safety threshold. The PoD is a model-derived estimate based on the predefined integration of information sources.

The 2026 application study by Reinke and colleagues further evaluated SARA-ICE on a chemically diverse set. Importantly, the authors distinguish the **fixed SARA-ICE DA included in the OECD framework** from **SARA-ICE Extended**, which provides additional outputs such as ED01 distributions, a prediction uncertainty ratio and probabilities for GHS categories. These should not be treated as interchangeable regulatory objects merely because they share the same modelling framework.

## A second route: the regression-based Defined Approach

TG 497 also incorporates a **regression-based DA** for quantitative PoD derivation. This approach is deliberately more transparent and algebraic than SARA-ICE. It combines quantitative outputs from OECD-accepted NAMs through predefined regression models.

The experimental information can include data generated with methods such as:

- kinetic Direct Peptide Reactivity Assay (kDPRA; TG 442C);
- KeratinoSens or related keratinocyte activation assays under TG 442D;
- dendritic-cell activation assays covered by TG 442E.

Natsch evaluated the regression-based workflow using data for 203 chemicals and also examined reproducibility using ring-trial information. One practical feature is that quantitative information generated from assays already used for hazard or potency assessment can be reused rather than requiring an entirely independent testing battery.

Recent work by Lee and colleagues places these regression-derived PoDs within a next-generation risk assessment (NGRA) workflow. Their case studies connect NAM-derived PoDs to quantitative risk assessment after applying additional considerations needed to derive a NAM-based NESIL. This is an application framework, however, and should not be confused with the narrower statement that the OECD DA itself directly defines a universally acceptable safe exposure.

## Why the update is important

The methodological change can be represented as a progression:

**mechanistic assay → integrated hazard call → potency information → quantitative PoD → exposure-based risk assessment**

The first three steps were already well developed in the skin-sensitisation NAM ecosystem. The 2026 TG 497 strengthens the fourth.

This is relevant beyond skin sensitisation because it illustrates a broader requirement for regulatory NAMs: replacing an animal test is not only a matter of matching sensitivity and specificity. For many safety decisions, the method must generate an output that can be connected to **dose and exposure**.

The fragrance-sector analysis by Natsch and colleagues is illustrative. For 110 chemicals, the authors compared PoDs from SARA-ICE, the regression DA and GARDskin dose-response with reference potency values and investigated adjustment factors for moving from NAM-PoDs toward NAM-NESILs. These results support the feasibility of fully non-animal quantitative workflows, but they are empirical evaluations in a particular chemical/use context rather than proof that one adjustment factor or workflow is universally transferable.

## Applicability domain and confidence remain central

Inclusion in TG 497 does not remove the limitations of the underlying assays or models. The guideline explicitly treats applicability domain and confidence as part of the interpretation of defined approaches.

Potential problems remain familiar to computational and experimental toxicology:

- a substance may be outside the applicability domain of one or more component methods;
- solubility, volatility, reactivity or cytotoxicity can compromise assay interpretation;
- mixtures and substances of uncertain or variable composition may not map cleanly onto workflows developed for defined chemicals;
- pro-haptens and chemicals requiring metabolic activation can challenge systems with limited metabolic competence;
- a model-derived PoD carries uncertainty from both its experimental inputs and the model used to integrate them.

For SARA-ICE specifically, a Bayesian formulation provides a natural way to represent prediction uncertainty, but the existence of an uncertainty estimate does not itself establish that uncertainty is sufficiently low for every decision context. For the regression DA, transparency of the mathematical transformation is a strength, but it does not eliminate uncertainty in assay measurements, training/reference data or extrapolation.

A technically defensible assessment therefore needs to retain the identity and quality of each input, check method-specific limitations and document why the DA is applicable to the target substance.

## OECD acceptance is not universal regulatory acceptance

TG 497 is an **OECD Test Guideline**, which gives the included DAs a substantially different status from exploratory NAM models described only in the scientific literature. It provides harmonised procedures and a defined framework for generating and interpreting data.

That status should nevertheless be described precisely.

TG 497 does not mean that every jurisdiction must accept every downstream risk-assessment conclusion based on a NAM-derived PoD. Nor does it validate arbitrary combinations of the component assays. The regulatory object is the **defined approach as specified**, including its inputs, DIP, applicability conditions and reporting requirements.

Likewise, evidence supporting a chemical ingredient cannot automatically be transferred to a complex mixture or finished formulation without addressing composition, exposure and the applicability of the individual methods.

For cosmetics and other topically exposed products, the immediate value of the update is therefore not a generic claim that "animal testing has been replaced." The more defensible statement is that OECD now provides standardised non-animal approaches capable of producing information extending from sensitisation hazard to a quantitative PoD, creating a stronger basis for exposure-led NGRA when the methods are applicable.

## Implications for integrated computational–experimental workflows

The new TG 497 also illustrates where computational toxicology is most useful in a NAM strategy.

In silico information can contribute to defined approaches, analogue selection, mechanistic interpretation and identification of potential domain limitations. But computational similarity or a standalone QSAR prediction is not equivalent to the quantitative PoD produced by the prescribed TG 497 workflow.

A robust workflow should therefore preserve the distinction between:

1. **predictions** generated by computational models;
2. **measurements** from in chemico or in vitro assays;
3. **integrated DA outputs** produced by a fixed DIP;
4. **risk-assessment conclusions** that additionally incorporate exposure, uncertainty and the intended context of use.

This separation is especially important when automated platforms integrate multiple evidence streams. Traceability is more valuable than a single composite "toxicity score": each conclusion should be recoverable to the chemical identity, experimental or computational input, model version, applicability assessment and decision rule that generated it.

## What the 2026 TG 497 changes in practice

The main advance is not another skin-sensitisation assay. It is the formalisation of a route from multiple NAM measurements to a **quantitative regulatory output**.

For developers and safety assessors, this changes the design question. Rather than asking only which non-animal assay can identify a sensitiser, it becomes possible to ask which combination of OECD methods can provide the information needed for a specific decision: hazard identification, potency categorisation or quantitative risk assessment.

The remaining challenge is the same one faced by most mature NAM frameworks: defining where the approach is applicable, characterising uncertainty, and connecting a technically valid output to a clearly stated regulatory or product-safety decision.

TG 497 is therefore a useful model for next-generation toxicology precisely because it does not reduce evidence integration to one assay or one prediction. It specifies how several mechanistic information sources can be combined reproducibly and, in its 2026 form, extends that integration toward quantitative risk assessment.

## References

1. OECD. **Guideline No. 497: Defined Approaches on Skin Sensitisation.** OECD Guidelines for the Testing of Chemicals, Section 4. OECD Publishing, Paris; 2026. DOI: [10.1787/b92879a4-en](https://doi.org/10.1787/b92879a4-en). [OECD publication page](https://www.oecd.org/en/publications/guideline-no-497-defined-approaches-on-skin-sensitisation_b92879a4-en.html).

2. Reinke EN, Reynolds J, Gilmour N, Reynolds G, Strickland J, Germolec D, Allen DG, Maxwell G, Kleinstreuer NC. **The skin allergy risk assessment-integrated chemical environment (SARA-ICE) defined approach to derive points of departure for skin sensitization.** *Current Research in Toxicology.* 2025;8:100205. DOI: [10.1016/j.crtox.2024.100205](https://doi.org/10.1016/j.crtox.2024.100205). [PubMed](https://pubmed.ncbi.nlm.nih.gov/39803375/).

3. Reinke EN, Reynolds J, Gilmour N, Johnson VJ, LaPratt T, Maxwell G, Kleinstreuer NC, Germolec D, Reynolds G. **Deriving a point-of-departure for skin sensitization risk assessments, application of the SARA-ICE tool to a diverse set of chemicals.** *New Approach Methodologies.* 2026;2:100078. DOI: [10.1016/j.namjnl.2026.100078](https://doi.org/10.1016/j.namjnl.2026.100078). [PubMed](https://pubmed.ncbi.nlm.nih.gov/41816003/).

4. Natsch A. **The regression based defined approach for skin sensitization potency assessment based on NAM data from OECD accepted tests.** *Regulatory Toxicology and Pharmacology.* 2026;168:106080. DOI: [10.1016/j.yrtph.2026.106080](https://doi.org/10.1016/j.yrtph.2026.106080). [PubMed](https://pubmed.ncbi.nlm.nih.gov/41794168/).

5. Lee I, Na M, Lavelle M, Schember I, Guttenberg MA, Gerberick GF, Natsch A, Ryan C, Api AM. **Quantitative next generation risk assessment for skin sensitization - application of regression models based on in vitro data to estimate point of departure.** *Regulatory Toxicology and Pharmacology.* 2026;164:105964. DOI: [10.1016/j.yrtph.2025.105964](https://doi.org/10.1016/j.yrtph.2025.105964). [PubMed](https://pubmed.ncbi.nlm.nih.gov/41101518/).

6. Natsch A, Griem P, Irizar A, Bridges J, Vey M, Lee I, Api AM, Kern P, Kimber I. **Derivation of a Point of Departure using NAMs for application in Quantitative Risk Assessment of fragrance materials.** *Regulatory Toxicology and Pharmacology.* 2026;167:106052. DOI: [10.1016/j.yrtph.2026.106052](https://doi.org/10.1016/j.yrtph.2026.106052). [PubMed](https://pubmed.ncbi.nlm.nih.gov/41638464/).

7. Lee I, Forreryd A, Na M, Schember I, Lavelle M, Gradin R, Mattson U, Johansson H, Donthamsetty S, Ladics G, Api AM. **Determining a point of departure for skin sensitization potency and quantitative risk assessment of fragrance ingredients using the GARDskin dose-response assay.** *ALTEX.* 2025;42(2):263-277. DOI: [10.14573/altex.2405131](https://doi.org/10.14573/altex.2405131). [PubMed](https://pubmed.ncbi.nlm.nih.gov/39871732/).

---

*Scope note: this white paper summarises the 2026 OECD TG 497 and selected recent methodological literature. Regulatory applicability depends on jurisdiction, substance type, context of use, study conduct and the specific decision being supported. Inclusion of a method or defined approach in an OECD Test Guideline should not be interpreted as universal acceptance of every downstream risk-assessment use.*
