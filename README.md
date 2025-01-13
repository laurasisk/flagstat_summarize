# flagstat_summarize
 Purpose: For many samtools flagstat output files, this script will concatenate the data in each file and calculate the mean for all files. The output is a .csv file. 


# Directions
1. Clone this repository or download flagstat_summarize.py
2. Move flagstat_summarize.py into the directory with the samtools flagstat output .tsv files. See example_files folder in this repository to see how these files should look.
3. Make the file executable
```
chmod +x flagstat_summarize.py
```
4. Run the file with python3
```
python3 flagstat_summarize.py
```
6. Open the csv file to view!

