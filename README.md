# Bird_Calls
Data processing steps for pre-processing bioacoustic and climatic information for use in a Hyperspheric analysis.

## Directory Structure
```txt
Bird_Calls/
├── 01_data/                           
│   ├── bioacoustic/                     # Raw bioacoustic recordings and trimmed final samples
│   └── covariates/                      # Environmental covariates (e.g., temp, precip)
│
├── 02_train_and_predict/              
│   ├── train.ipynb                      # Train the model on classified samples
│   └── predict.ipynb                    # Run predictions using trained models on out-of-sample recordings
│
└── 03_summarize/                      
    ├── eta_plot.jpeg                    # Visual of model eta coefficients
    ├── plot_etas.R                      # R script to generate eta_plot.jpeg
    ├── spatial_prediction_maps.jpeg     # Visual summary of spatial predictions
    ├── spect_samples.jpg                # Example spectrograms used in modeling
    ├── spect_fig_and_sample_nums.ipynb  # Jupyter notebook creating spectrogram figures
    ├── prediction_map.R                 # R script to generate prediction maps
    └── plot_avg_temp_and_precip_across_years.R  # R script for temp/precip trends

```

