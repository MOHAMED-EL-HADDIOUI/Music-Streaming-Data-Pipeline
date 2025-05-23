import os
import shutil

def rename_images():
    # Define the image directory
    image_dir = "images"
    
    # Define the new names for each file
    new_names = {
        "Streamify-Architecture.jpg": "music_streaming_architecture.jpg",
        "airflow.jpg": "airflow_workflow.jpg",
        "dashboard.png": "analytics_dashboard.png",
        "dbt.png": "dbt_models.png",
        "kafka.jpg": "kafka_topics.jpg",
        "songs_dag.png": "songs_processing_dag.png",
        "spark.jpg": "spark_streaming.jpg",
        "streamify_dag.png": "main_workflow_dag.png",
        "topics.png": "kafka_topics_overview.png"
    }
    
    # Create backup directory
    backup_dir = os.path.join(image_dir, "backup")
    os.makedirs(backup_dir, exist_ok=True)
    
    # Rename files
    for old_name, new_name in new_names.items():
        old_path = os.path.join(image_dir, old_name)
        new_path = os.path.join(image_dir, new_name)
        
        # Backup original file
        if os.path.exists(old_path):
            backup_path = os.path.join(backup_dir, old_name)
            shutil.copy2(old_path, backup_path)
            
            # Rename file
            os.rename(old_path, new_path)
            print(f"Renamed: {old_name} -> {new_name}")

if __name__ == "__main__":
    rename_images() 