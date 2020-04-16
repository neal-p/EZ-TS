#!/bin/bash
for i in input/*log
    do
    file=$(basename ${i%.*})
    ID=$(sbatch --parsable ts_guess/$file-submit.sbatch)
    sbatch --dependency=afterok:$ID conf_search/$file-conf_search.sbatch
    sbatch  --dependency=afternotok:$ID ts_guess/$file-failed.sbatch
done
chmod 777 conf_search/*sh
