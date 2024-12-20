# Lethal COVID-19 Single Nuclei RNA Sequencing Analysis

This repository contains a comprehensive analysis of single-nuclei RNA sequencing (snRNA-seq) data from patients who succumbed to COVID-19. The study aims to elucidate the molecular and cellular mechanisms underlying severe outcomes in COVID-19 by leveraging advanced computational techniques.

## Repository Structure

The analysis is organized into several key stages, each documented in individual Jupyter notebooks:

1. **Quality Control**: [1.Quality_Control.ipynb](https://github.com/MikiasHWT/scRNA_Lethal_Covid19_Analysis/blob/main/1.Quality_Control.ipynb)
   - *Overview*: Initial assessment and filtering of raw snRNA-seq data to ensure high-quality inputs for downstream analysis.
   - *Key Steps*:
     - Removal of low-quality nuclei and potential doublets.
     - Outlier detection using Median Absolute Deviation.
     - Assessment of sequencing depth and mitochondrial gene content.

2. **Normalization**: [2.Normalization.ipynb](https://github.com/MikiasHWT/scRNA_Lethal_Covid19_Analysis/blob/main/2.Normalization.ipynb)
   - *Overview*: Standardization of gene expression measurements across nuclei to account for technical variability.
   - *Key Steps*:
     - Comparison of various normalization and transformation methods.
     - Application of scaling factors to normalize counts.
     - Logarithmic transformation to stabilize variance.
     - Scran size factor-based normalization.
     - Pearson's residuals transformation.

3. **Feature Selection**: [3.Feature_Selection.ipynb](https://github.com/MikiasHWT/scRNA_Lethal_Covid19_Analysis/blob/main/3.Feature_Selection.ipynb)
   - *Overview*: Identification of highly variable genes that capture significant biological signals.
   - *Key Steps*:
     - Comparison of various feature selection methods.
     - Scry-based deviant gene determination.
     - Seurat highly variable gene identification.
     - Pearson's residual-based highly variable gene determination.
     - Selection of genes for downstream analyses based on variability thresholds.

4. **Dimensionality Reduction**: [4.Dimensionality_Reduction.ipynb](https://github.com/MikiasHWT/scRNA_Lethal_Covid19_Analysis/blob/main/4.Dimensionality_Reduction.ipynb)
   - *Overview*: Reduction of data complexity to facilitate visualization and clustering.
   - *Key Steps*:
     - Principal Component Analysis (PCA) to identify major axes of variation.
     - Visualization using Uniform Manifold Approximation and Projection (UMAP) and t-Distributed Stochastic Neighbor Embedding (t-SNE).

5. **Integration**: *(In Progress)*
   - *Overview*: Combining data from multiple samples to create a unified dataset.
   - *Key Steps*:
     - Alignment of datasets to correct for batch effects.
     - Merging of datasets for comprehensive analysis.

6. **Quality Assessment**: *(In Progress)*
   - *Overview*: Evaluation of the integrated dataset to ensure data integrity and consistency.
   - *Key Steps*:
     - Assessment of integration success.
     - Identification of any remaining technical artifacts.

7. **Cell Annotation**: *(In Progress)*
   - *Overview*: Classification of nuclei into distinct cell types based on expression profiles.
   - *Key Steps*:
     - Assignment of cell type identities using known marker genes.
     - Experimentation with reference-based cell annotation.

8. **Differential Gene Expression**: *(In Progress)*
   - *Overview*: Identification of genes with varying expression levels between conditions or cell types.
   - *Key Steps*:
     - Statistical testing to detect differentially expressed genes.
     - Functional enrichment analysis to interpret biological significance.

9. **Trajectory Analysis**: *(In Progress)*
   - *Overview*: Reconstruction of dynamic processes and lineage relationships among cells.
   - *Key Steps*:
     - Pseudotime analysis to infer developmental trajectories.
     - RNA velocity analysis.
     - Identification of genes driving temporal changes.
