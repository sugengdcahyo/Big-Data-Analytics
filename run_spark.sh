#!/bin/bash

# Set environment variables
#export SPARK_HOME=/home/imgbox/BigData/venv
#export PATH=$SPARK_HOME/bin:$PATH
#export PYTHONPATH=$SPARK_HOME/python:$PYTHONPATH
# Tambahkan variabel lingkungan lainnya jika diperlukan

# Log file untuk menyimpan output dari pra-pemrosesan, spark-submit, dan pascapemrosesan
LOG_FILE="/var/log/pyspark/job.err.log"

source /home/imgbox/BigData/venv/bin/activate

# Pra-pemrosesan
echo "Mulai pra-pemrosesan pada $(date)" | tee -a $LOG_FILE
# Tambahkan perintah pra-pemrosesan Anda di sini
# Contoh:
# python /path/to/pre_process_script.py >> $LOG_FILE 2>&1

# Jalankan spark-submit
echo "Mulai spark-submit pada $(date)" | tee -a $LOG_FILE
/home/imgbox/BigData/venv/bin/spark-submit --master spark://imgbox2:7077 \
--conf spark.rpc.message.maxSize=256 \
/home/imgbox/BigData/pyspark/batch/news_ingest.py >> $LOG_FILE 2>&1

# Pascapemrosesan
echo "Mulai pascapemrosesan pada $(date)" | tee -a $LOG_FILE
# Tambahkan perintah pascapemrosesan Anda di sini
# Contoh:
# python /path/to/post_process_script.py >> $LOG_FILE 2>&1

echo "Script selesai pada $(date)" | tee -a $LOG_FILE
