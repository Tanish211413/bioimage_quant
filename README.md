
# GelQuant

Simple band quantification software for protein and DNA gels/blots. 

## Overview
GelQuant processes gel/blot images for quantification. The software allows users to:  
- **Import and crop** gel images as desired.  
- **Split the image** into user-specified vertical lanes.  
- **Convert lanes to numerical data** using NumPy.  
- **Calculate average RGB intensity** for each row in the lane.  
- **Apply Gaussian weighting** to emphasize the middle of the lane while reducing edge interference.  
- **Baseline correction** based on user-specified regions.  
- **Plot the data** and perform band intensity quantification.  


##  Example Usage
For an example of how GelQuant works, check out:  
 `notebook-example.ipynb`  
 `gel-example.png`  

##  Installation
To install a development version, clone this repository and install it with `pip`:

git clone https://github.com/harmslab/gelquant.git
cd gelquant
pip install -e .

## Dependencies

GelQuant requires the following Python libraries:

matplotlib
,numpy
,pillow (PIL)
,pandas
,os 
,natsort
,scipy

note: for os (built-in, no installation needed)

To Install
pip install matplotlib numpy pillow pandas natsort scipy
