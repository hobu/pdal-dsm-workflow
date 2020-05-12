for i in ../laz/4342-0{1,2,3,4}-{26,27,28,29,30,31,32,33}_?_?.laz ; do 
	echo Starting $i
	sem -j+0 \
		pdal pipeline pipeline-hag.json \
			--readers.las.filename=$i \
			--writers.gdal.filename=`basename ${i%%.laz}-hag.tif`
done
sem --wait

echo Merging tiles...
gdal_merge.py -tap -o hag.tif *-hag.tif