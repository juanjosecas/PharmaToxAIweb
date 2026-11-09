---
layout: whitepaper
title: "Liver microphysiological systems in 2026: from impressive models to cross-platform evidence"
summary: "New FDA-CDER–3Rs Collaborative work places liver microphysiological systems in a defined regulatory context of use. Recent experimental studies reveal what human-relevant models can measure, where their predictive claims remain fragile, and how to evaluate them across platforms."
authors:
  - PharmaToxAI
date: 2026-11-09
published: true
pdf: ""
---

## Why the comparison matters

Drug-induced liver injury (DILI) remains difficult to predict before clinical exposure. Human hepatic metabolism, inflammatory responses, transport processes and interindividual susceptibility interact in ways that neither a single biochemical assay nor a conventional animal study can reproduce completely. Microphysiological systems (MPS) attempt to preserve selected aspects of this biology using human cells, three-dimensional architecture, controlled flow and, sometimes, multiple interacting cell types.

The central problem in 2026 is no longer whether a liver-on-chip can produce plausible hepatic functions. Many platforms can. The harder question is whether a particular system produces reproducible, decision-relevant evidence when its performance is evaluated against clinically meaningful comparators, using blinded compounds and a predefined interpretation strategy.

A study published in July 2026 by LaFollette and colleagues describes a collaboration between the 3Rs Collaborative and FDA's Center for Drug Evaluation and Research (CDER) to evaluate eight commercially available liver MPS platforms [1]. Its most important contribution is methodological: the comparison was designed around a **defined context of use**, retrospective assessment of elevated liver signals observed in early clinical trials, rather than a generic claim that an organ chip predicts all hepatotoxicity.

This distinction has implications for both regulatory science and the design of routine in vitro safety programmes.

## What a liver MPS actually adds

Conventional two-dimensional hepatocyte cultures can be informative for short-term metabolic and cytotoxicity studies. Their limitations include changes in differentiation state, declining enzyme activities, restricted multicellular interactions and exposure conditions that may differ substantially from those in vivo. More complex culture formats may retain hepatic function for longer and permit repeated dosing, dynamic exposure and the measurement of interactions among parenchymal and non-parenchymal cells.

These advantages are not automatic. A three-dimensional format does not guarantee physiological transporter polarity, human-relevant metabolite formation or clinically predictive responses. Perfusion introduces additional variables: compound binding to device materials, adsorption to tubing, flow-dependent transport, residence time and changes in unbound concentrations. Nominal medium concentration may therefore be a poor proxy for the concentration experienced by cells.

The experimental system needs to be characterized in functional terms. Albumin and urea production indicate aspects of hepatocyte activity, but they do not establish metabolic competence on their own. CYP activity, transporter function, morphology, tissue integrity and the stability of baseline measurements over the dosing interval provide complementary information. The appropriate combination depends on the mechanism and decision being studied.

The question is particularly consequential for DILI, where a reduction in ATP, an increase in lactate dehydrogenase release, mitochondrial dysfunction, altered bile-acid handling and inflammatory signalling represent different biological events. Combining them into one unqualified “viability” result discards information that may explain the observed injury.

## The FDA-CDER and 3Rs Collaborative cross-platform evaluation

LaFollette et al. describe the design of a systematic assessment involving **eight commercial liver MPS** [1]. The programme uses a harmonized experimental strategy, blinded test compounds, common endpoints and independent data analysis. Importantly, it aims to establish **category-level performance expectations**, not simply rank vendors or declare one platform superior.

A defined context of use changes the experimental design. Retrospectively evaluating liver signals from early clinical trials requires drug selections, exposure regimens and decision thresholds that resemble the problem being addressed. It also requires negative comparators and a strategy for distinguishing a true predictive signal from a nonspecific response at supraphysiological concentrations.

The publication describes the study design. It should not be cited as proof that all eight platforms met prespecified performance targets, nor as FDA qualification of the systems. The distinction between a prospective evaluation framework and completed analytical validation is fundamental.

FDA's separate regulatory-science project comparing immune-containing Hepatomune with Hepatopac illustrates another important question: whether adding immune components improves the discrimination of clinically hepatotoxic drugs from related drugs without comparable liver liabilities [2]. That programme is explicitly framed around drug pairs, functional endpoints and inflammatory responses. The FDA project description states objectives, not a final demonstration of improved predictive performance.

## Evidence from recent primary studies

### A scalable microfluidic system

Kulkarni and colleagues reported a liver-on-chip model based on the OC-Plex platform, using primary human hepatocytes and monitoring albumin, urea, CYP3A4, cytokeratin-18, mitochondrial function and viability [3]. Their initial evaluation included **17 compounds**, spanning pharmaceuticals and cosmetic ingredients. The authors reported favorable classification metrics in the tested subset.

The result supports technical feasibility and provides a useful example of multiparametric measurement. However, the small and selected compound panel limits the precision of any performance estimate. Apparent sensitivity and specificity are also sensitive to the reference labels, compound prevalence, tested concentrations and the way ambiguous cases are handled. An internally successful pilot is not equivalent to independent external validation across laboratories, donors and chemical classes.

### Organoids combined with perfusion

Chen and colleagues developed a human liver organoid-on-chip system incorporating an endothelial barrier and a dynamic microenvironment [4]. Their study assessed hepatic markers, albumin and urea production, and drug responses using concentration gradients informed by clinical exposure. Seven drugs were examined, including troglitazone and fialuridine.

The study is valuable because it connects organoid function, exposure and injury markers within one experimental platform. Its reported classification performance should nonetheless be interpreted within the small compound panel and the study's own grading scheme. Clinical Hy's Law is a clinical signal involving specific patterns of serum laboratory abnormalities; measuring ALT, AST, ALP or LDH in a chip does not by itself reproduce or validate clinical Hy's Law as a regulatory endpoint.

The authors also measured selected pharmacokinetic quantities by LC-MS/MS. That is a stronger basis for interpreting exposure than relying only on nominal dosing, although the correspondence between microfluidic and human systemic kinetics remains model-dependent.

### Cell-resolved mechanisms in 2D and 3D

A 2026 experimental study used single-cell transcriptomics to examine acetaminophen responses in human two-dimensional and three-dimensional liver microtissues [5]. Cell-resolved approaches can distinguish population shifts from transcriptional changes within a cell type, and can identify whether the cells presumed to mediate a toxic response are actually present and transcriptionally competent.

The important methodological implication is that two cultures with similar bulk viability may have different cellular compositions and response trajectories. Single-cell sequencing is not a routine substitute for functional endpoints, but it can clarify why models disagree and whether a mechanistic claim is supported.

### Species and format comparisons

An October 2025 study compared primary hepatocytes from humans, monkeys, rats and dogs in the PhysioMimix LC12 platform and conventional plate cultures [6]. Such comparisons are useful because they address two separate sources of variation: species biology and culture format. A model's apparent improvement over 2D culture may depend on the tested chemical and endpoint; a species difference observed in one format should not automatically be extrapolated to all hepatic injury mechanisms.

## From assay signal to an interpretable exposure

A common weakness in in vitro DILI studies is the use of nominal concentration as though it were equivalent to a clinically relevant exposure.

At minimum, an exposure-aware study should distinguish total and unbound concentrations, the relevant human comparator (for example, plasma Cmax under the intended dosing regimen), protein binding, accumulation, metabolism and depletion during the experiment. Where practical, time-resolved chemical measurements in the medium and device compartments should accompany biological endpoints.

For repeated-dose MPS experiments, a concentration-time profile is often more informative than a single nominal concentration. The experimental exposure can be described by an area under the concentration-time curve, peak concentration, trough concentration and duration above a mechanistically relevant threshold, while acknowledging that the in vitro compartment is not equivalent to plasma or liver tissue.

PBPK and quantitative in vitro–in vivo extrapolation can help connect these quantities, but only when the assumptions are explicit. A fitted relationship between nominal chip concentration and human plasma exposure is not sufficient to establish a mechanistic translation. Device sorption, protein binding, intracellular partitioning and metabolic clearance may need to be measured or bounded.

This is one reason a cross-platform comparison should harmonize what is feasible without pretending that nominally identical dosing produces identical cellular exposures across devices.

## Reproducibility is more than repeating a well

A technically credible MPS evaluation needs to distinguish variation among independent experiments, cell donors, operators, production lots and laboratories. Technical replicates within a single device or culture batch do not capture those sources of variability.

Relevant documentation includes cell provenance and donor characteristics, culture age, seeding and recovery criteria, flow and oxygen conditions, compound preparation, medium composition, device materials, dosing schedule, endpoint assay calibration and predefined exclusion rules.

For DILI classification, the choice of reference compounds is equally important. Negative compounds should not be selected solely because they are easy to classify; structurally or pharmacologically related comparator pairs can provide a more demanding test. Positive controls should cover different injury mechanisms, and compounds known to interfere with optical or metabolic assays need appropriate analytical controls.

A blinded external evaluation is particularly valuable because assay tuning, compound selection and threshold optimization can otherwise become entangled with the expected answer. A model can look reliable retrospectively while failing on the next chemical series.

The same caution applies to machine-learning analyses of MPS outputs. Data splitting should respect experimental batches, donors and chemical identity. Replicate wells from the same compound and experiment must not be distributed across training and test sets as though they were independent biological examples.

## Regulatory position: engagement is not qualification

FDA announced in September 2024 that an organ-on-chip technology intended to assess relative human DILI risk had been accepted at the **letter-of-intent stage** of the ISTAND pilot programme [7]. The agency explicitly described this as the first stage of a multi-step qualification pathway. Acceptance of the letter does not establish qualification of the tool or general regulatory acceptance of liver chips.

Similarly, the 2026 FDA-CDER–3Rs Collaborative evaluation is evidence of regulatory-science engagement and a structured evaluation effort. It is not a blanket endorsement of a technology category.

Regulatory utility depends on a precise context of use: the decision supported, target population, compound classes, reference standard, acceptable uncertainty and consequences of an incorrect prediction. A system that is useful for investigating an early clinical liver signal may not be adequate for routine quantitative risk assessment of an unrelated industrial chemical or finished cosmetic formulation.

These distinctions are especially important outside the United States. FDA programmes do not automatically determine acceptance by authorities in Argentina or other Latin American jurisdictions. OECD methods, FDA drug-development tools and national requirements have different scopes and legal status.

## A practical evaluation framework

For a research or service laboratory considering a liver MPS, platform selection should begin with the biological and decision problem, not with the most complex device.

For example, a short-term question about direct mitochondrial toxicity may be answerable in a simpler human hepatic system with orthogonal functional assays. A question involving repeated exposure, reactive metabolite formation or immune-mediated amplification may justify a more complex multicellular system. The added biological features should be tested for incremental information rather than assumed to improve prediction.

A defensible evaluation sequence would be:

1. **Define the context of use.** Specify the intended decision and the clinically or toxicologically relevant reference endpoint.
2. **Characterize the model.** Demonstrate baseline stability, relevant metabolic and transporter functions, and the presence and identity of required cell types.
3. **Measure exposure.** Document nominal and, when feasible, actual concentrations over time, including binding and device losses.
4. **Use mechanistically diverse endpoints.** Combine injury and function measurements, with controls for chemical and optical interference.
5. **Challenge the model.** Include blinded positive and negative comparators, related chemical pairs and independent donors or batches.
6. **Quantify uncertainty.** Report performance with confidence intervals and investigate discordant compounds rather than discarding them.
7. **Preserve provenance.** Record compound identity, experimental conditions, raw measurements, processing steps and decision thresholds.

The last step is critical when experimental evidence is integrated with QSAR, read-across or PBPK models. The output should remain traceable to individual observations and assumptions. A single composite score may be convenient for prioritization, but it should not conceal disagreement among methods.

## What can reasonably be concluded in 2026?

Human liver MPS can provide sustained functional measurements, repeated exposure and multicellular information that simpler systems may not capture. Recent primary studies demonstrate technically feasible platforms and promising results in selected chemical panels. These findings support their use in mechanistic investigation and compound prioritization.

The stronger claim—that a particular platform reliably predicts clinically relevant DILI across diverse compounds and laboratories—requires independent, blinded evaluation against a defined reference standard. The 2026 FDA-CDER–3Rs Collaborative programme is important because it places that requirement at the centre of the study design.

For PharmaToxAI, the practical implication is to treat advanced cellular systems as **evidence-generating components** within an integrated assessment, rather than as self-validating replacements for animal or clinical data. Their value depends on the quality of exposure characterization, endpoint interpretation, domain of applicability and the reproducibility of the resulting decision.

## References

1. LaFollette MR, Blinova K, Daniel AB, Dalmas DA, Richardson E, Marsh G, et al. Introduction to the 3RsC's cross-platform microphysiological systems evaluation for drug-induced liver injury in collaboration with FDA-CDER. *Regulatory Toxicology and Pharmacology*. 2026;172:106189. [https://doi.org/10.1016/j.yrtph.2026.106189](https://doi.org/10.1016/j.yrtph.2026.106189).

2. US Food and Drug Administration. Microphysiological Systems for the Evaluation of Drug-induced Liver Injury. Regulatory science project, initiated January 9, 2024. [FDA project page](https://www.fda.gov/science-research/advancing-regulatory-science/microphysiological-systems-evaluation-drug-induced-liver-injury).

3. Kulkarni G, Chen L, Sang J, Seo JH, Grall R, Wang Y, et al. A scalable human liver-on-a-chip platform for predictive safety assessment. *Toxicology*. 2026;521:154378. [https://doi.org/10.1016/j.tox.2025.154378](https://doi.org/10.1016/j.tox.2025.154378).

4. Chen X, Bao F, Liu J, Wang Y, Tao T, Zhang G, Qin J. A human liver organoids-on-chip for the assessment of drug-induced liver injury. *BMC Pharmacology and Toxicology*. 2026;27:30. [https://doi.org/10.1186/s40360-025-01074-z](https://doi.org/10.1186/s40360-025-01074-z).

5. Single-cell transcriptomics of acetaminophen-induced responses in human 2D and 3D liver microtissues. *Archives of Toxicology*. 2026;100:1411–1424. [https://doi.org/10.1007/s00204-025-04296-6](https://doi.org/10.1007/s00204-025-04296-6).

6. Comparative Analysis of Species-Specific Hepatocyte Function and Drug Effects in a Liver Microphysiological System PhysioMimix LC12 and 96-Well Plates. *ACS Pharmacology & Translational Science*. 2025;8:4138–4158. [https://doi.org/10.1021/acsptsci.5c00554](https://doi.org/10.1021/acsptsci.5c00554).

7. US Food and Drug Administration. FDA's ISTAND Pilot Program accepts a submission of first organ-on-a-chip technology designed to predict human drug-induced liver injury. September 24, 2024. [FDA announcement](https://www.fda.gov/drugs/drug-alerts-and-statements/fdas-istand-pilot-program-accepts-submission-first-organ-chip-technology-designed-predict-human-drug).
