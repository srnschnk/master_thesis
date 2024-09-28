# Health Outcome Prediction Using Transformer Models
To run the code in this repository, the MIMIC-IV dataset must be downloaded from [PhysioNet](https://physionet.org/content/mimiciv/1.0/). Additionally, preprocessing is required using the pipeline provided by Gupta et al. (2022), available at [MIMIC-IV Data Pipeline](https://github.com/healthylaife/MIMIC-IV-Data-Pipeline?tab=readme-ov-file). The parameters used to execute the pipeline have been hardcoded into the 'PreprocessingPipeline.ipynb' file within this repository.

# Repository Structure

### Preprocessing Pipeline
- **PreprocessingPipeline.ipynb** - Contains the Preprocessing Pipeline of https://github.com/healthylaife/MIMIC-IV-Data-Pipeline?tab=readme-ov-file - The Pipeline has been modfified to group small ethnicity groups together
- **mimic4_preprocess_util.py** - Supplementary file of the Preprocessing Pipeline
- **preprocess_outcomes.py** - Supplementary file of the Preprocessing Pipeline
- utils - Supplementary file of the Preprocessing Pipeline
- preprocessing - Supplementary file of the Preprocessing Pipeline
- notes - Supplementary file of the Preprocessing Pipeline
- model - Supplementary file of the Preprocessing Pipeline

### Data Preparation
- **data_preparation_for_all_models.ipynb** - Loads the csv-files created by the preprocessing pipeline. Performs data preparation and creation of subsets.
- **data_preparation_for_torch_models.ipynb**
- **create_torch_tensors** - Loads the presaved files from data_preparation_for_all_models.ipynb - Performs further data preparation for the PyTorch models - Saves the tensors
- **custom_functions.py** - Defines Data Preparation Functions, used by multiple notebooks

### Traditional Models
- **scikit-learn_models.ipynb** - Contains all traditional models, except the LSTM models
- **scikit-learn_models.ipynb - tuning.ipynb** - Used for finding optimal parameters
- **LSTM_models.ipynb**
- **Hybrid LSTM.ipynb**
- **Hybrid LSTM - tuning.ipynb** - Used for finding optimal parameters

### Med-BERT Models
- **Med_Bert_Models.ipynb**
- **Med_Bert_Models - tuning.ipynb** - used for finding optimal parameters
- **Hybrid_Med-BERT_LSTM.ipynb**

### TFT Model
- **pytorch-tft-models.ipynb**

### Supplementary Notebooks
- **create_plots.ipynb** - Creates Plots for the thesis PDF document
- **read_dimension_table.ipynb** - Used to link item_ids back to dimension tables
- **License.md**
- **.gitignore**
