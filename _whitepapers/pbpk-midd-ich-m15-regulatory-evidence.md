---
layout: whitepaper
title: "PBPK after ICH M15: building mechanistic models that can carry regulatory weight"
summary: "ICH M15 turns model-informed drug development into a harmonised evidence framework. For PBPK, the practical consequence is clear: biological plausibility, context of use, model evaluation, uncertainty and documentation matter as much as the simulation itself."
authors: "PharmaToxAI"
date: 2026-09-21
published: true
pdf: ""
---

Physiologically based pharmacokinetic (PBPK) modelling has become one of the most mature forms of model-informed drug development (MIDD). It is routinely used to integrate physicochemical properties, in vitro ADME data, human physiology and clinical pharmacokinetics, and it can support decisions that would otherwise require additional clinical studies. Drug–drug interaction assessment is the obvious example, but the scope now extends to organ impairment, paediatrics, formulation questions and population-specific exposure.

What changed in 2026 is not the mathematics of PBPK. The important development is regulatory: **ICH M15, General Principles for Model-Informed Drug Development, reached Step 4 on 29 January 2026 and was issued by the US FDA as final guidance in June 2026.** M15 provides a harmonised framework for planning, evaluating and documenting MIDD evidence. PBPK therefore sits inside a broader regulatory logic in which the credibility required from a model depends on the question it is being asked to answer and on the consequence of being wrong.

This distinction matters. A PBPK model can reproduce observed concentration–time profiles and still be weak evidence for a proposed extrapolation. Conversely, a model does not need to explain every biological process to be useful if its structure, verification and uncertainty are appropriate for a narrowly defined context of use.

## PBPK is an evidence model, not a simulation exercise

A conventional PBPK model partitions the organism into physiologically meaningful compartments and describes drug movement using mass-balance equations. Organ volumes, blood flows, tissue composition, enzyme and transporter abundance, glomerular filtration and other system parameters are combined with drug-specific information such as lipophilicity, ionisation, plasma protein binding, permeability and intrinsic clearance.

The attraction is mechanistic separation between **drug parameters** and **system parameters**. In principle, the same drug model can be transferred into a population with altered physiology, while the same population model can be used for multiple drugs. This separation is never perfect, but it is the basis for most PBPK extrapolation.

The regulatory problem starts when an apparently mechanistic parameter is poorly identified. Several parameter combinations can produce similar plasma PK. An empirical adjustment may improve the fit while weakening the biological interpretation. A model calibrated against the same data later presented as verification has not undergone independent testing. And an accurate simulation in healthy adults says little by itself about prediction in severe liver disease, pregnancy or a transporter-mediated DDI.

The relevant question is therefore not simply whether the model fits. It is whether the evidence supporting the model is adequate for the proposed decision.

## ICH M15 formalises a risk-based way of thinking about MIDD

ICH M15 is deliberately broader than PBPK. It covers MIDD evidence across model classes and establishes common principles for planning, model evaluation, documentation and regulatory interaction. Its importance for PBPK is that it makes **context of use** central.

A model used internally to select a dose for an exploratory study does not carry the same evidentiary burden as a model used to omit a clinical DDI study or establish labelling recommendations. As regulatory impact increases, the evaluation strategy must become correspondingly stronger.

For a PBPK analysis, that logic can be reduced to a practical sequence:

1. define the question and the regulatory decision the model will inform;
2. specify the model assumptions and the biological processes required to answer that question;
3. identify which parameters are measured, inferred, optimised or borrowed from the platform;
4. evaluate model performance with data relevant to the intended application;
5. characterise uncertainty and test influential assumptions;
6. document the analysis so that an independent reviewer can reconstruct the reasoning.

This is more demanding than reporting predicted/observed ratios. It also makes model development more disciplined: the intended use should shape the verification plan before the final simulation is run.

## EMA was already asking many of the same questions

The European Medicines Agency's current PBPK reporting guideline has been effective since July 2019. It requires sufficient documentation to assess both the qualification of the PBPK platform for the intended use and the predictive performance of the drug model. The guideline explicitly asks for biological plausibility of inputs, uncertainty in parameter values, clarity about model building and optimisation, assumptions and their consequences.

EMA has also recognised that PBPK now belongs to a larger family of mechanistic models. In February 2025 it opened consultation on a concept paper for a new guideline covering mechanistic models used in MIDD, including PBPK, physiologically based biopharmaceutics modelling (PBBM) and quantitative systems pharmacology (QSP). The consultation closed on 31 May 2025.

Taken together with ICH M15, the direction is fairly clear. Regulatory evaluation is moving away from model-specific checklists toward a common question: **is the model credible for this particular use?**

That does not make technical details less important. It makes their relevance easier to judge.

## Verification should challenge the mechanism that will be extrapolated

A frequent weakness in PBPK workflows is verification with data that do not stress the part of the model responsible for the intended extrapolation.

Consider a CYP3A substrate. If the intended application is prediction of a strong-inhibitor DDI, verification should include information that constrains the fraction metabolised through CYP3A and the behaviour of the model under perturbation. Matching single-dose PK in healthy volunteers is useful but insufficient. The model may fit those data with the wrong balance between hepatic metabolism, intestinal metabolism, distribution and absorption.

A recent dordaviprone analysis illustrates a more informative strategy. Jaiswal and colleagues developed a PBPK model using in vitro and clinical data and evaluated dordaviprone both as a victim and perpetrator of CYP-mediated DDIs. Simulated exposures across the clinical studies used for verification were within 1.4-fold of observed values. More importantly, the model reproduced the itraconazole interaction: the simulated increases in AUC and Cmax were 4.6- and 1.7-fold, compared with observed increases of 4.4- and 1.9-fold. That perturbation directly interrogates the CYP3A component needed for subsequent DDI predictions.

The lesson is not that a particular fold-error threshold establishes validity. It does not. The useful feature is that the verification experiment is mechanistically related to the intended prediction.

The same principle applies to transporters. Ujihira and colleagues used genotype, ethnicity and DDI information to verify a PBPK model for coproporphyrin-I, an endogenous biomarker of OATP1B activity. Multiple orthogonal perturbations can be more informative than repeatedly comparing simulated and observed PK under nearly identical conditions.

## Virtual populations are part of the model, not a cosmetic option

PBPK often appears to separate drug and population biology cleanly, but population files contain assumptions that can materially alter predictions. Demography, organ size, blood flow, plasma proteins, renal function, gastrointestinal physiology, enzyme abundance, transporter abundance and genotype frequencies all contribute to simulated variability.

Ezuruike and colleagues recently developed PBPK virtual populations for White, African American, Asian American and Hispanic/Latino North American populations. Their work collated demographic and physiological parameters together with enzyme and transporter abundance and allele frequencies. Across clinical PK and DDI studies, simulations were generally within two-fold of observed data. The analysis also identified population differences in parameters such as CYP3A4, CYP3A5 and OATP1B1 abundance that can alter exposure predictions.

This type of work exposes an important limitation in the phrase “virtual population”. A simulated cohort is not automatically representative because it contains thousands of individuals. Its validity depends on the provenance and adequacy of the distributions used to generate those individuals.

For regulatory use, population assumptions therefore deserve the same traceability as compound parameters.

## Disease models are harder because physiology changes jointly

Organ impairment is a particularly demanding PBPK application. Liver disease does not simply reduce one clearance parameter. Cirrhosis can change liver volume, hepatic blood flow, portosystemic shunting, plasma protein concentrations, enzyme expression, transporter activity, renal function and gastrointestinal physiology. These changes are correlated with disease progression and are not captured perfectly by Child–Pugh class.

Schneider and colleagues published a comprehensive pathophysiology repository for PBPK modelling in liver cirrhosis in 2026. Rather than treating disease as a categorical switch, the work aimed to quantify continuous progression and population variability in relevant physiological parameters. This is a useful direction because it separates two sources of uncertainty that are often conflated: uncertainty about the drug and uncertainty about the disease system.

The distinction has immediate regulatory relevance. FDA issued a new draft guidance in September 2026 on pharmacokinetics in patients with impaired hepatic function. The guidance addresses study design, analysis and the impact of hepatic impairment on dosing and labelling. PBPK does not remove the need to understand the clinical population; it provides a framework in which that knowledge can be integrated and interrogated.

Recent work on bosutinib makes the point well. PBPK was used to investigate atypical exposure changes in patients with hepatic impairment for a drug affected by CYP3A4 and P-glycoprotein. Such analyses are valuable because they can test competing mechanistic explanations—altered absorption, distribution and clearance—rather than treating an observed AUC change as a single empirical effect.

But mechanistic narratives should not be mistaken for identified mechanisms. If several plausible parameter sets explain the available clinical data, additional simulations do not resolve that ambiguity. Sensitivity analysis, alternative model structures and targeted experimental data are needed.

## PBPK can inform labelling when the evidentiary chain is strong enough

The regulatory value of PBPK is easiest to see when modelling changes an actionable recommendation.

A 2026 analysis of cariprazine described PBPK-informed labelling for interactions with CYP3A inhibitors. Cariprazine is challenging because it has active metabolites and a long effective half-life. A short clinical ketoconazole study had informed the original US recommendations, but PBPK enabled assessment over clinically relevant longer coadministration scenarios. This is the type of use for which context of use, verification and transparent assumptions become consequential: the simulation is no longer merely explanatory; it contributes to prescribing information.

Such examples also show why “validated PBPK model” is an imprecise phrase. A model may be sufficiently evaluated for one application and insufficient for another. A CYP3A DDI model is not automatically qualified to predict hepatic impairment, food effects or tissue concentrations. The drug file may be the same, but the extrapolation and the uncertain biological components are different.

## Uncertainty needs to be attached to the decision

PBPK reports often contain sensitivity analyses, but their interpretation can be superficial. Varying parameters by ±20% and showing that plasma AUC changes little is not necessarily informative if the uncertain parameter spans an order of magnitude or if the decision depends on Cmax, tissue exposure or a DDI ratio.

A useful uncertainty analysis starts with the decision threshold. Which uncertain inputs could change the conclusion? Which assumptions are structurally important? What range is scientifically plausible? Are uncertainties correlated? Does a worst-case combination remain consistent with the proposed recommendation?

This creates three distinct layers:

- **parameter uncertainty**: uncertainty in measured or inferred values such as intrinsic clearance, fraction unbound or transporter kinetics;
- **structural uncertainty**: uncertainty about the model itself, such as the need for permeability limitation, enterohepatic recirculation or a transporter process;
- **population uncertainty**: uncertainty in physiological distributions and covariate relationships.

These should not be collapsed into a single confidence interval unless the probabilistic assumptions are defensible.

ICH M15's risk-based framing is useful here. The objective is not to eliminate uncertainty. It is to show that remaining uncertainty is understood well enough for the proposed use.

## New mechanistic resolution does not automatically mean better prediction

PBPK is also expanding in scale. Saini and Gallo introduced single-cell PBPK (scPBPK) models in 2026, linking expression-dependent kinetic processes with distributions inspired by single-cell RNA-sequencing data. Their examples included blood–brain barrier transport for AZD1775 and hepatocyte metabolism of midazolam. The framework can represent cell-to-cell heterogeneity in drug exposure that is invisible in conventional organ-level PBPK.

This is scientifically interesting, particularly for coupling pharmacokinetics to heterogeneous pharmacodynamic responses. It also exposes an old modelling problem in a new form: every increase in resolution introduces parameters and assumptions that require evidence.

Single-cell expression does not map trivially to functional protein abundance or transport capacity. Spatial organisation may matter. Measurement noise and sampling bias in omics datasets propagate into model inputs. A higher-resolution model can therefore be biologically richer while being less identifiable.

For regulatory MIDD, complexity should be justified by the decision. If a standard PBPK model answers the question robustly, cellular resolution is unnecessary. If tissue or cell-specific exposure drives efficacy or toxicity and conventional compartments obscure the mechanism, the additional complexity may be warranted—but then its evaluation must address those new assumptions.

## What a decision-ready PBPK workflow should contain

For PharmaToxAI, the useful abstraction is not “run PBPK”. It is an auditable evidence chain.

A regulatory-oriented workflow should preserve the provenance of each input; distinguish measured, literature-derived, predicted and optimised parameters; version the software platform and population files; predefine the intended application; separate model-development datasets from meaningful verification datasets where possible; record optimisation procedures; perform sensitivity and uncertainty analyses against the decision; and retain both successful and failed model variants when they affect interpretation.

The report should make it possible to answer a few uncomfortable questions quickly:

- Which observation would falsify the proposed mechanism?
- Which parameters were adjusted because the initial model failed?
- Could another parameterisation explain the same clinical PK?
- Has the model been challenged under the biological perturbation it is expected to predict?
- Would plausible uncertainty change the regulatory conclusion?
- Is the virtual population supported for the population being simulated?

If these questions cannot be answered, additional decimal places in the simulated AUC are irrelevant.

## A broader implication for computational ADMET

PBPK offers a useful precedent for predictive toxicology and computational ADMET. It has achieved regulatory utility not because mechanistic models are intrinsically trustworthy, but because the field developed conventions for qualification, verification, reporting, sensitivity analysis and context-specific use.

The same logic applies to QSAR, machine-learning ADMET models and integrated NAM workflows. Prediction accuracy is only one component of credibility. Data provenance, applicability domain, uncertainty, mechanistic consistency and the consequences of model failure determine whether a prediction can support a real decision.

ICH M15 makes that principle explicit at the MIDD level. The regulatory trajectory is toward models that are not merely predictive, but inspectable: their assumptions can be located, their evidence can be traced, and their uncertainty can be related to the decision they support.

For PBPK, that is a more important development than any new simulator feature.

## References

1. International Council for Harmonisation (ICH). **M15: General Principles for Model-Informed Drug Development.** Final version, Step 4, adopted 29 January 2026. https://database.ich.org/sites/default/files/ICH_M15_Step4_Final_Guideline_2026_0129.pdf

2. US Food and Drug Administration. **M15 General Principles for Model-Informed Drug Development.** Final Guidance, June 2026. https://www.fda.gov/regulatory-information/search-fda-guidance-documents/m15-general-principles-model-informed-drug-development

3. European Medicines Agency. **Guideline on the reporting of physiologically based pharmacokinetic (PBPK) modelling and simulation.** EMA/CHMP/458101/2016; effective 1 July 2019. https://www.ema.europa.eu/en/reporting-physiologically-based-pharmacokinetic-pbpk-modelling-simulation-scientific-guideline

4. European Medicines Agency. **Concept paper on the development of a Guideline on assessment and reporting of mechanistic models used in the context of model informed drug development.** EMA/5875/2025, 2025. https://www.ema.europa.eu/en/guideline-assessment-reporting-mechanistic-models-used-context-model-informed-drug-development

5. Jaiswal S, et al. **Assessing Cytochrome P450 Drug Interaction Risk for Dordaviprone Using Physiologically Based Pharmacokinetic Modeling.** *CPT Pharmacometrics Syst Pharmacol.* 2025;14. PMID: 40758244. https://pubmed.ncbi.nlm.nih.gov/40758244/

6. Ujihira Y, Tan SPF, Scotcher D, Galetin A. **Genotype, Ethnicity, and Drug-Drug Interaction Modeling as Means of Verifying Transporter Biomarker PBPK Model: The Coproporphyrin-I Story.** *CPT Pharmacometrics Syst Pharmacol.* 2025;14(5):941–953. doi:10.1002/psp4.70008. https://pubmed.ncbi.nlm.nih.gov/40065524/

7. Ezuruike U, et al. **Development and Verification of Virtual Population Models for Predicting Drug Pharmacokinetics in Ethnic North American Populations.** *CPT Pharmacometrics Syst Pharmacol.* 2025;14(10):1598–1615. doi:10.1002/psp4.70068. https://pubmed.ncbi.nlm.nih.gov/40674384/

8. Schneider ARP, Baier V, Schlender JF, Kuepfer L. **Comprehensive Pathophysiology Repository for PBPK Modeling in Liver Cirrhosis: Quantifying Continuous Disease Progression and Population Variability.** *CPT Pharmacometrics Syst Pharmacol.* 2026;15(3):e70215. doi:10.1002/psp4.70215. https://pubmed.ncbi.nlm.nih.gov/41717827/

9. US Food and Drug Administration. **Pharmacokinetics in Patients with Impaired Hepatic Function: Study Design, Data Analysis, and Impact on Dosing and Labeling.** Draft Guidance, September 2026. https://www.fda.gov/regulatory-information/search-fda-guidance-documents/pharmacokinetics-patients-impaired-hepatic-function-study-design-data-analysis-and-impact-dosing-and

10. **Physiologically Based Pharmacokinetic Modeling in Patients With Hepatic Impairment: Are Changes in Bosutinib Exposure Profiles Driven by Altered Absorption or Distribution?** *CPT Pharmacometrics Syst Pharmacol.* 2026. PMID: 41535725. https://pubmed.ncbi.nlm.nih.gov/41535725/

11. Riad MMH, Marroum P, Shebley M, Xiong H. **Physiologically-Based Pharmacokinetic Model-Informed Labeling for Cariprazine Drug Interactions With CYP3A Inhibitors.** *CPT Pharmacometrics Syst Pharmacol.* 2026;15(4):e70236. doi:10.1002/psp4.70236. https://pubmed.ncbi.nlm.nih.gov/41947022/

12. Saini A, Gallo JM. **Introduction to Single-Cell Physiologically-Based Pharmacokinetic (scPBPK) Models.** *CPT Pharmacometrics Syst Pharmacol.* 2026;15(9):e70320. doi:10.1002/psp4.70320. https://pubmed.ncbi.nlm.nih.gov/42625210/
