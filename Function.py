# Create workflow pipeline function
def Process_and_integrate(csv_dir):
    for file in os.listdir(csv_dir):
        file_path = os.path.join(csv_dir, file)
        if file.endswith('.csv'): 
            adata = sc.read_csv(file_path).T
            sample_name = file.split("_")[1]  
            adata.obs["Sample"] = sample_name
            print(f"{sample_name} has {adata.X.shape[0]} cells and {adata.X.shape[1]} transcripts")

            adata.var["mt"] = adata.var_names.str.startswith("MT-")
            adata.var["ribo"] = adata.var_names.str.startwith(("RPS", "RPL"))
            adata.var["hb"] = adata.var_names.str.contains(("^HB[^(P)]"))

            sc.pp.calculate_qc_metrics(adata, qc_vars=["mt", "ribo", "hb"], inplace=True, percent_top=[20], log1p=True)

            adata.obs["outlier"] = (
                    is_outlier(adata, "log1p_total_counts", 5)
                    | is_outlier(adata, "log1p_n_genes_by_counts", 5)
            )

            print(f"{sample_name} \n{adata.obs.outlier.value_counts()}")
            adata = adata[(~adata.obs.outlier)].copy()

            print(f"{sample_name} Zero-variance genes:", np.sum(adata.X.var(axis=0) == 0))
            sc.pp.filter_genes(adata, min_cells=1)

            analytic_pearson = sc.experimental.pp.normalize_pearson_residuals(adata, inplace=False)
            adata.layers["pearson_residuals"] = csr_matrix(analytic_pearson["X"])

            sc.pp.highly_variable_genes(adata, n_top_genes=2000, flavor='seurat_v3')
            
            return adata

















def pp(csv_path):
    adata = sc.read_csv(csv_path).T
    sc.pp.filter_genes(adata, min_cells = 10)

    adata = sc.read_csv(csv_path).T
    adata.obs['Sample'] = csv_path.split('_')[2] #'raw_counts/GSM5226574_C51ctr_raw_counts.csv'
    
    
    sc.pp.filter_cells(adata, min_genes=200) 
    sc.pp.filter_genes(adata, min_cells=3) 
    adata.var['mt'] = adata.var_names.str.startswith('mt-')  
    adata.var['ribo'] = adata.var_names.isin(ribo_genes[0].values)
    sc.pp.calculate_qc_metrics(adata, qc_vars=['mt', 'ribo'], percent_top=None, log1p=False, inplace=True)

    upper_lim = np.quantile(adata.obs.n_genes_by_counts.values, .98)
    adata = adata[adata.obs.n_genes_by_counts < upper_lim]
    adata = adata[adata.obs.pct_counts_mt < 20]
    adata = adata[adata.obs.pct_counts_ribo < 2]

    return adata