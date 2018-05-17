sloth
=====

[![Build Status](https://travis-ci.org/cvhciKIT/sloth.svg)](https://travis-ci.org/cvhciKIT/sloth)

sloth is a tool for labeling image and video data for computer vision research.

The documentation can be found at http://sloth.readthedocs.org/ .

Latest Releases
===============

2013/11/29 v1.0: 2e69fdae40f89050fbaeef22491eee2a92e78b4f [.zip](https://github.com/cvhciKIT/sloth/archive/v1.0.zip) [.tar.gz](https://github.com/cvhciKIT/sloth/archive/v1.0.tar.gz)

For a full list, visit https://github.com/cvhciKIT/sloth/releases

---

### Sloth set-up

1. Clone or download 3GIMBALS sloth repo: https://github.com/3GIMBALS/sloth
2. Install conda
3. `cd` to sloth/
4. `conda create -n .env python=2.7 anaconda`
5. Activate the environment `source activate .env`
6. `conda install pyqt=4`
7. `python setup.py install`
8. Check that sloth runs by:
    * Try opening sloth window: `sloth --config sloth_custom_configuration.py`

NOTE: You may need to change default Python environment path and restart computer for this to work. Once restarted, make sure to re-activate conda environment. This may be specifically a Windows OS issue. 

---

### Annotating a site

First enter initials in the `annotations` column of `geojson_check.csv` at the given site you are annotating as a placeholder and indicator to other annotators to reduce overlap of efforts. 
1. Open the corresponding Geojson file for the site in [Geojson.io](http://geojson.io/#map=2/20.0/0.0). Only the areas subsumed by polygons or rectangles need annotations. 
2. Open Sloth using the custom configuration file using the same command in the set-up above. 
3. Open all of the images for a single site (this creates one annotation file per site).
4. Annotate all vessels within AOIs to best of ability. Does not have to be perfect. 
5. Save the file periodically. When finished, upload to the annotations sub-directory in the shared folder using a file name that clearly indicates the site (e.g., <site-name>_annotations.json). 

Finally, replace your first name initial in the `annotations` column of `geojson_check.csv` with a 1. 
