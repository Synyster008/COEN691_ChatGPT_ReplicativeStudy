from evaluation.evaluator import evaluate

# select the folder which will be compared with the ground truth
out_dir = "outputs/ChatGPT/10_shot"

datasets = ['HDFS', 'Hadoop', 'Spark', 'Zookeeper', 'BGL', 'HPC',
            'Thunderbird', 'Windows', 'Linux', 'Android',  'HealthApp',
            'Apache', 'Proxifier', 'OpenSSH', 'OpenStack', 'Mac']

if __name__ == '__main__':
    for dataset in datasets:
        evaluate(f"dataset/{dataset}/{dataset}_2k.log_structured_corrected.csv",
                 f"{out_dir}/{dataset}_2k.log_structured_adjusted.csv")
