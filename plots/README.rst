--------------------------------------------------------------------------------
Buffered DSM/DTM/HAG from an EPT datasource
--------------------------------------------------------------------------------

This example uses a small Python script to generate a PDAL
pipeline from a template.

Requirements
--------------------------------------------------------------------------------

Install PDAL and Shapely in your conda environment:

::

    conda install -c conda-forge pdal shapely -y


Example usage
--------------------------------------------------------------------------------

::

    python make_pipeline plots.json 591007.1061 5283581.8285 id_name > id_name.json


::

    pdal pipeline id_name.json


Help
................................................................................

::

    usage: make_pipeline.py [-h] [--url URL] [--buffer BUFFER] [--resolution RESOLUTION] pipeline x y id

    Create PDAL pipeline for a MNDNR Plot

    positional arguments:
      pipeline              Pipeline template
      x                     Plot X in EPSG:26195
      y                     Plot Y in EPSG:26195
      id                    Plot ID

    optional arguments:
      -h, --help            show this help message and exit
      --url URL             EPT URL for data
      --buffer BUFFER       Plot buffer size
      --resolution RESOLUTION
                            box buffer for query


Template
--------------------------------------------------------------------------------

The template uses Python substitutions to fill in values for stages in the PDAL
pipeline

The following values are available to use for substitution:

    * ``url``: EPT URL
    * ``x``: X coordinate
    * ``y``: Y coordinate
    * ``id``: A name to use for output files
    * ``buffer``: Radius to buffer the point
    * ``gdal_resolution``: Raster output resolution
    * ``ept_resolution``: EPT selection resolution
    * ``ept_bounds``: EPT selection window
    * ``gdal_bounds``: Raster output bounds


The template itself uses the approach defined by Jim's PDAL pipelines in the
directory above this

`Plots.json template <plots.json>`_.
